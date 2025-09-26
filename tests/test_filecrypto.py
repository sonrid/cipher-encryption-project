import os
import tempfile
from filecrypto import generate_fernet_key, save_key_to_file, load_key_from_file, encrypt_file_fernet, decrypt_file_fernet

def test_fernet_file_crypto():
    key = generate_fernet_key()
    with tempfile.TemporaryDirectory() as tmpdir:
        plain_text = b"Test data for Fernet encryption"
        infile = os.path.join(tmpdir, 'input.txt')
        encfile = os.path.join(tmpdir, 'encrypted.bin')
        decfile = os.path.join(tmpdir, 'decrypted.txt')

        with open(infile, 'wb') as f:
            f.write(plain_text)

        save_key_to_file(key, os.path.join(tmpdir, 'key.key'))
        loaded_key = load_key_from_file(os.path.join(tmpdir, 'key.key'))

        encrypt_file_fernet(infile, encfile, loaded_key)
        decrypt_file_fernet(encfile, decfile, loaded_key)

        with open(decfile, 'rb') as f:
            decrypted_data = f.read()

        assert decrypted_data == plain_text

