import os
from flask import Flask, render_template, request, redirect, send_file, flash, url_for
from werkzeug.utils import secure_filename
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
import hashlib
from dotenv import load_dotenv

# Load env variables
load_dotenv()
PASSPHRASE = os.getenv("AES_PASSPHRASE", "defaultpass")

# Key derivation
SALT = b"fileshare_salt"
KEY = PBKDF2(PASSPHRASE, SALT, dkLen=32, count=1000000)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB limit

def encrypt_file(filepath):
    with open(filepath, "rb") as f:
        data = f.read()
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)
    encrypted_data = iv + cipher.encrypt(data)
    enc_path = filepath + ".enc"
    with open(enc_path, "wb") as f:
        f.write(encrypted_data)
    return enc_path

def decrypt_file(filepath):
    with open(filepath, "rb") as f:
        encrypted_data = f.read()
    iv = encrypted_data[:16]
    cipher = AES.new(KEY, AES.MODE_CFB, iv=iv)
    data = cipher.decrypt(encrypted_data[16:])
    dec_path = filepath.replace(".enc", ".dec")
    with open(dec_path, "wb") as f:
        f.write(data)
    return dec_path

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file selected!")
        return redirect("/")
    file = request.files["file"]
    if file.filename == "":
        flash("No file selected!")
        return redirect("/")
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    enc_path = encrypt_file(filepath)
    os.remove(filepath)
    flash("File uploaded and encrypted successfully!")
    return redirect(url_for("files"))

@app.route("/files")
def files():
    all_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".enc")]
    return render_template("files.html", files=all_files)

@app.route("/security")
def security():
    return render_template("security.html")

@app.route("/download/<filename>")
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    dec_path = decrypt_file(filepath)
    return send_file(dec_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)