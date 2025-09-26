from hybridcrypto import generate_rsa_keypair, save_key

def main():
    private_key, public_key = generate_rsa_keypair()
    save_key(private_key, "private.pem", private=True)
    save_key(public_key, "public.pem", private=False)
    print("RSA key pair generated and saved as 'private.pem' and 'public.pem'.")

if __name__ == "__main__":
    main()

