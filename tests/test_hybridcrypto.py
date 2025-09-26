import os
import tempfile
from hybridcrypto import (
    generate_rsa_keypair,
    save_key,
    load_private_key,
    load_public_key,
    hybrid_encrypt,
    hybrid_decrypt
)

def test_rsa_hybrid_encryption():
    priv_key, pub_key = generate_rsa_keypair()
    with tempfile.TemporaryDirectory() as tmpdir:
        # Paths for keys
        priv_file = os.path.join(tmpdir, 'private.pem')
        pub_file = os.path.join(tmpdir, 'public.pem')

        save_key(priv_key, priv_file, private=True)
        save_key(pub_key, pub_file)

        priv_loaded = load_private_key(priv_file)
        pub_loaded = load_public_key(pub_file)

        # Prepare files
        plain_text = b"Top secret data for hybrid crypto testing"
        input_file = os.path.join(tmpdir, 'input.txt')
        encrypted_file = os.path.join(tmpdir, 'encrypted.bin')
        decrypted_file = os.path.join(tmpdir, 'decrypted.txt')

        with open(input_file, 'wb') as f:
            f.write(plain_text)

        # Encrypt + Decrypt
        hybrid_encrypt(input_file, encrypted_file, pub_loaded)
        hybrid_decrypt(encrypted_file, decrypted_file, priv_loaded)

        with open(decrypted_file, 'rb') as f:
            decrypted = f.read()

        assert decrypted == plain_text

