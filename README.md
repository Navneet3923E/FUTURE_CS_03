# FUTURE_CS_03 Given by FUTURE INTERNS

# 🔐 Secure File Share (Flask + AES)

A secure file sharing system built with **Python Flask** where all uploaded files are **AES-encrypted at rest** and automatically **decrypted on download**.  
This project demonstrates secure file handling, encryption, and basic web security practices.

---

## 🚀 Features
- ✅ Secure **file upload & download**
- ✅ **AES encryption (AES-CFB mode)** for confidentiality
- ✅ Files stored **encrypted on disk**
- ✅ Clean **Bootstrap + Tailwind UI**
- ✅ File list page with download option
- ✅ Configurable encryption key using `.env`

---

## 🛠️ Tech Stack
- **Backend:** Python Flask  
- **Encryption:** PyCryptodome (AES)  
- **Frontend:** HTML, CSS, Bootstrap, Tailwind  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
```
secure-file-share/
│-- app.py               # Flask backend
│-- requirements.txt     # Dependencies
│-- .env.example         # Example environment file
│-- templates/           # HTML templates
│   │-- index.html       # Upload page
│   │-- files.html       # File list page
│-- uploads/             # Encrypted files folder
```

---

## ⚡ Setup & Run (Windows/Linux/Mac)

### 1️⃣ Clone Repo
```sh
git clone https://github.com/your-username/secure-file-share.git
cd secure-file-share
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Configure Environment
Create a `.env` file in the root:
```
AES_PASSPHRASE=MyStrongSecurePassphrase123!
```

### 4️⃣ Run the App
```sh
python app.py
```

Open in browser → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔑 Security Overview
- **AES-CFB Encryption** → Encrypts all files with a unique IV.  
- **Key Management** → Secret key stored in `.env`, not in code.  
- **Confidentiality** → Files remain encrypted until explicitly downloaded.  
- **Integrity** → IV and ciphertext handled securely; no plaintext storage.  
- **Threat Model Considered**:
  - Prevents **data exposure if server storage is leaked**.  
  - Mitigates **insider risk** by not storing plaintext.  
  - Protects against **replay attacks** with random IVs.  

---

## 📜 License
MIT License © 2025 Navneet Bhatt
