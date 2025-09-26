from cryptography.fernet import Fernet

def generate_fernet_key() -> bytes:
    return Fernet.generate_key()

def save_key_to_file(key: bytes, path: str):
    with open(path, 'wb') as f:
        f.write(key)

def load_key_from_file(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()

def encrypt_file_fernet(input_path: str, output_path: str, key: bytes):
    f = Fernet(key)
    with open(input_path, 'rb') as fin:
        data = fin.read()
    encrypted_data = f.encrypt(data)
    with open(output_path, 'wb') as fout:
        fout.write(encrypted_data)

def decrypt_file_fernet(input_path: str, output_path: str, key: bytes):
    f = Fernet(key)
    with open(input_path, 'rb') as fin:
        data = fin.read()
    decrypted_data = f.decrypt(data)
    with open(output_path, 'wb') as fout:
        fout.write(decrypted_data)

