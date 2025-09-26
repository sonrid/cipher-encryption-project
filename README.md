# Cipher Encryption-Decryption Project

## Project Overview
This project provides a desktop application with a graphical user interface (GUI) to perform encryption and decryption operations using text and file ciphers. It implements classic text ciphers (Caesar and Vigenere), symmetric file encryption (Fernet), and hybrid asymmetric encryption (RSA + Fernet). The goal is to allow users to securely encrypt and decrypt messages and files seamlessly using an easy-to-use interface.

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Git (optional) to clone repo

### Installation

1. Clone or download the project repository.
    git clone <repo-url>
    cd cipher-project

2. Create and activate Python virtual environment:
      python3 -m venv venv
      source venv/bin/activate

3. Install dependencies:
      pip install -r requirements.txt

4. Generate RSA keypair (required for hybrid encryption):
      python generate_rsa_keys.py

5. Run the application:
      python app.py

## Usage Guide

- On launching, the GUI displays tabs for:
  - **Caesar Cipher:** Enter text and shift key to encrypt/decrypt.
  - **Vigenere Cipher:** Enter text and key phrase to encrypt/decrypt.
  - **Fernet File Encrypt:** Select a file, then encrypt/decrypt with symmetric key.
  - **Hybrid RSA + Fernet:** Select files and encrypt/decrypt using RSA asymmetric key exchange combined with Fernet for data encryption.

- File encryption tabs allow selecting input files and automatically handle key storage and retrieval.

- Encrypted files and keys are saved alongside original files with appropriate extensions (`.encrypted`, `.decrypted`).

## Technical Details

- **Caesar Cipher:** Shifts each letter by a user-supplied integer.
- **Vigenere Cipher:** Uses a repeated keyword to shift letters poly-alphabetically.
- **Fernet Encryption:** Symmetric key encryption based on AES in CBC mode with HMAC.
- **Hybrid Encryption:** Generates a random Fernet key to encrypt file data, encrypts that key with RSA public key for secure transfer, and decrypts accordingly using RSA private key.

## Running Tests

- Activate the virtual environment.
- Execute `pytest` from the project root directory to run all unit tests.
- All tests cover encryption/decryption correctness and fault tolerance.
- Test files include:
  - `test_ciphers.py` - Text ciphers
  - `test_filecrypto.py` - Fernet file encryption
  - `test_hybridcrypto.py` - RSA hybrid encryption

## Screenshots

*(Add screenshots here for key GUI tabs, encryption steps, and output messages)*

Example:
![Caesar Cipher Tab](images/caesar_tab.png)
![Hybrid Encryption Tab](images/hybrid_tab.png)

## Known Issues & Future Work

- Current file encryption only supports local file paths; network or cloud storage is a future enhancement.
- Error messages could be more descriptive and detailed.
- Add support for additional cipher algorithms like AES, ChaCha20, or RSA direct encryption.
- Implement a configuration panel for advanced key management.

## Credits & References

- Built with Python `cryptography` library.
- GUI developed using Tkinter standard library.
- Inspired by classical cipher techniques and modern cryptographic protocols.
- Reference: https://cryptography.io, Python docs, various cryptography tutorials.

---

# Demo Script (Optional)

1. Run `python app.py` to start GUI.
2. Encrypt text with Caesar tab (enter text and shift, then encrypt).
3. Decrypt text with Vigenere tab using known key.
4. Use Fernet tab to encrypt a file and decrypt it.
5. Use Hybrid tab to encrypt a file with RSA public key and decrypt with RSA private key.
6. Observe output status and saved encrypted/decrypted files.
7. Close the application with window close button.



