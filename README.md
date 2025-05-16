```markdown
# 🔐 Kyber-768 Python Implementation – PRT558 Project

This repository contains a Python implementation of the **Kyber-768** Key Encapsulation Mechanism (KEM), a **post-quantum cryptographic algorithm** selected by **NIST** for standardization. This project was developed as part of the **PRT558 – Information Security** unit.

---

## 📌 Overview

**Kyber** is a lattice-based public-key encryption and key encapsulation algorithm that offers strong resistance to quantum attacks. This implementation focuses on:

- **Kyber-768** variant (medium security level)
- Key generation
- Encapsulation and decapsulation
- Shared secret verification

> ✅ Note: This is a simplified Python-based version for learning purposes.

---

## 🗂️ Project Structure


kyber_768_impl_prt558/
├── kyber_impl.py          # Main Kyber-768 algorithm implementation
├── kyber_impl_test.py     # Unit tests for functionality
├── report.html            # Project report with explanation and results
├── requirements.txt       # Python dependencies
└── assets                 # Supporting files (images, diagrams, etc.)

````

---

## ⚙️ Getting Started

### 🔁 1. Clone the Repository

```bash
git clone https://github.com/Anilmgr/kyber_768_impl_prt558.git
cd kyber_768_impl_prt558
````

### 🧪 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run the Test Script

```bash
python kyber_impl_test.py
```

This will run key generation, encapsulation, and decapsulation with shared secret verification.

---

## 📘 Report

The `report.html` file contains:

* Background on Kyber and lattice cryptography
* Algorithm explanation
* Output screenshots
* Implementation results

📂 Open `report.html` in a browser to read.

---

## ✅ Sample Output

```text
[+] Public Key Generated
[+] Secret Key Generated
[+] Ciphertext Encapsulated
[+] Shared Secret (Sender) and (Receiver) Match: ✅
```

---

## ⚠️ Disclaimer

> This project is for **educational purposes only**.
> It is **not intended for production** use or secure communication.


