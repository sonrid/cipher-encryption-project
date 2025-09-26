from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet

# Step 3.1 - Generate RSA Keypair
def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Step 3.2 - Save key
def save_key(key, filename: str, private: bool = False):
    if private:
        pem = key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    else:
        pem = key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    with open(filename, 'wb') as f:
        f.write(pem)

# Step 3.2 - Load key from file
def load_private_key(filename: str):
    with open(filename, 'rb') as f:
        pem = f.read()
    return serialization.load_pem_private_key(pem, password=None)

def load_public_key(filename: str):
    with open(filename, 'rb') as f:
        pem = f.read()
    return serialization.load_pem_public_key(pem)

# Step 3.3 - Hybrid encrypt file
def hybrid_encrypt(input_path: str, output_path: str, public_key):
    # Generate Fernet key
    fernet_key = Fernet.generate_key()
    f = Fernet(fernet_key)

    # Encrypt file data with Fernet
    with open(input_path, 'rb') as fin:
        data = fin.read()
    encrypted_data = f.encrypt(data)

    # Encrypt Fernet key with RSA public key
    encrypted_fernet_key = public_key.encrypt(
        fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        )
    )

    # Save encrypted Fernet key + encrypted data to output file
    with open(output_path, 'wb') as fout:
        # Store key length for proper extraction during decrypt
        fout.write(len(encrypted_fernet_key).to_bytes(4, byteorder='big'))
        fout.write(encrypted_fernet_key)
        fout.write(encrypted_data)


# Step 3.4 - Hybrid decrypt file
def hybrid_decrypt(input_path: str, output_path: str, private_key):
    with open(input_path, 'rb') as fin:
        key_len_bytes = fin.read(4)
        key_len = int.from_bytes(key_len_bytes, byteorder='big')
        encrypted_fernet_key = fin.read(key_len)
        encrypted_data = fin.read()

    # Decrypt Fernet key with RSA private key
    fernet_key = private_key.decrypt(
        encrypted_fernet_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        )
    )
    f = Fernet(fernet_key)

    # Decrypt data with Fernet
    decrypted_data = f.decrypt(encrypted_data)

    # Write decrypted data to output file
    with open(output_path, 'wb') as fout:
        fout.write(decrypted_data)

