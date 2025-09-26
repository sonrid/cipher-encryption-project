import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from ciphers import caesar_encrypt, caesar_decrypt, vigenere_encrypt, vigenere_decrypt
from filecrypto import encrypt_file_fernet, decrypt_file_fernet, generate_fernet_key, save_key_to_file, load_key_from_file
from hybridcrypto import generate_rsa_keypair, save_key, load_private_key, load_public_key, hybrid_encrypt, hybrid_decrypt

root = tk.Tk()
root.title("Cipher Encryption Decryption Tool")
root.geometry("850x650")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Tabs setup
tab_caesar = ttk.Frame(notebook)
tab_vigenere = ttk.Frame(notebook)
tab_fernet = ttk.Frame(notebook)
tab_hybrid = ttk.Frame(notebook)

notebook.add(tab_caesar, text='Caesar Cipher')
notebook.add(tab_vigenere, text='Vigenere Cipher')
notebook.add(tab_fernet, text='Fernet File Encrypt')
notebook.add(tab_hybrid, text='Hybrid RSA + Fernet')

# ===== Caesar Tab =====
tk.Label(tab_caesar, text="Enter text:").pack(pady=5)
txt_caesar_input = tk.Text(tab_caesar, height=6)
txt_caesar_input.pack()
tk.Label(tab_caesar, text="Enter shift key (number):").pack(pady=5)
entry_caesar_key = tk.Entry(tab_caesar)
entry_caesar_key.pack()
btn_caesar_encrypt = tk.Button(tab_caesar, text="Encrypt")
btn_caesar_encrypt.pack(pady=5)
btn_caesar_decrypt = tk.Button(tab_caesar, text="Decrypt")
btn_caesar_decrypt.pack()
lbl_caesar_output = tk.Label(tab_caesar, text="Output:", anchor='w')
lbl_caesar_output.pack(fill='x', pady=(10, 0))
txt_caesar_output = tk.Text(tab_caesar, height=6)
txt_caesar_output.pack()
status_caesar = tk.Label(tab_caesar, text="", fg="green")
status_caesar.pack(pady=5)

# ===== Vigenere Tab =====
tk.Label(tab_vigenere, text="Enter text:").pack(pady=5)
txt_vig_input = tk.Text(tab_vigenere, height=6)
txt_vig_input.pack()
tk.Label(tab_vigenere, text="Enter key (letters):").pack(pady=5)
entry_vig_key = tk.Entry(tab_vigenere)
entry_vig_key.pack()
btn_vig_encrypt = tk.Button(tab_vigenere, text="Encrypt")
btn_vig_encrypt.pack(pady=5)
btn_vig_decrypt = tk.Button(tab_vigenere, text="Decrypt")
btn_vig_decrypt.pack()
lbl_vig_output = tk.Label(tab_vigenere, text="Output:", anchor='w')
lbl_vig_output.pack(fill='x', pady=(10, 0))
txt_vig_output = tk.Text(tab_vigenere, height=6)
txt_vig_output.pack()
status_vig = tk.Label(tab_vigenere, text="", fg="green")
status_vig.pack(pady=5)

# ===== Fernet Tab =====
tk.Label(tab_fernet, text="File Encryption and Decryption using Fernet").pack(pady=5)
btn_fernet_open = tk.Button(tab_fernet, text="Select File to Encrypt/Decrypt")
btn_fernet_open.pack(pady=5)
btn_fernet_encrypt = tk.Button(tab_fernet, text="Encrypt File")
btn_fernet_encrypt.pack(pady=5)
btn_fernet_decrypt = tk.Button(tab_fernet, text="Decrypt File")
btn_fernet_decrypt.pack()
status_fernet = tk.Label(tab_fernet, text="", fg="green")
status_fernet.pack(pady=5)

# ===== Hybrid Tab =====
tk.Label(tab_hybrid, text="Hybrid RSA + Fernet File Encryption").pack(pady=5)
btn_hybrid_open = tk.Button(tab_hybrid, text="Select File to Encrypt/Decrypt")
btn_hybrid_open.pack(pady=5)
btn_hybrid_encrypt = tk.Button(tab_hybrid, text="Encrypt File")
btn_hybrid_encrypt.pack(pady=5)
btn_hybrid_decrypt = tk.Button(tab_hybrid, text="Decrypt File")
btn_hybrid_decrypt.pack()
status_hybrid = tk.Label(tab_hybrid, text="", fg="green")
status_hybrid.pack(pady=5)

# Global variables to store file paths for file encryption tabs
fernet_file_path = ""
hybrid_file_path = ""

# --- Caesar Handlers ---
def caesar_encrypt_handler():
    try:
        text = txt_caesar_input.get("1.0", tk.END).strip()
        shift = int(entry_caesar_key.get())
        encrypted = caesar_encrypt(text, shift)
        txt_caesar_output.delete("1.0", tk.END)
        txt_caesar_output.insert(tk.END, encrypted)
        status_caesar.config(text="Encrypted successfully", fg="green")
    except Exception as e:
        status_caesar.config(text=f"Error: {e}", fg="red")

def caesar_decrypt_handler():
    try:
        text = txt_caesar_input.get("1.0", tk.END).strip()
        shift = int(entry_caesar_key.get())
        decrypted = caesar_decrypt(text, shift)
        txt_caesar_output.delete("1.0", tk.END)
        txt_caesar_output.insert(tk.END, decrypted)
        status_caesar.config(text="Decrypted successfully", fg="green")
    except Exception as e:
        status_caesar.config(text=f"Error: {e}", fg="red")

btn_caesar_encrypt.config(command=caesar_encrypt_handler)
btn_caesar_decrypt.config(command=caesar_decrypt_handler)

# --- Vigenere Handlers ---
def vig_encrypt_handler():
    try:
        text = txt_vig_input.get("1.0", tk.END).strip()
        key = entry_vig_key.get().strip()
        encrypted = vigenere_encrypt(text, key)
        txt_vig_output.delete("1.0", tk.END)
        txt_vig_output.insert(tk.END, encrypted)
        status_vig.config(text="Encrypted successfully", fg="green")
    except Exception as e:
        status_vig.config(text=f"Error: {e}", fg="red")

def vig_decrypt_handler():
    try:
        text = txt_vig_input.get("1.0", tk.END).strip()
        key = entry_vig_key.get().strip()
        decrypted = vigenere_decrypt(text, key)
        txt_vig_output.delete("1.0", tk.END)
        txt_vig_output.insert(tk.END, decrypted)
        status_vig.config(text="Decrypted successfully", fg="green")
    except Exception as e:
        status_vig.config(text=f"Error: {e}", fg="red")

btn_vig_encrypt.config(command=vig_encrypt_handler)
btn_vig_decrypt.config(command=vig_decrypt_handler)

# --- Fernet Handlers ---
def fernet_open_file():
    global fernet_file_path
    fernet_file_path = filedialog.askopenfilename()
    if fernet_file_path:
        status_fernet.config(text=f"Selected: {fernet_file_path}", fg="blue")

def fernet_encrypt_handler():
    try:
        if not fernet_file_path:
            raise Exception("No file selected")
        key = generate_fernet_key()
        save_key_to_file(key, "fernet_key.key")
        output_file = fernet_file_path + ".encrypted"
        encrypt_file_fernet(fernet_file_path, output_file, key)
        status_fernet.config(text=f"File encrypted as {output_file} and key saved as fernet_key.key", fg="green")
    except Exception as e:
        status_fernet.config(text=f"Error: {e}", fg="red")

def fernet_decrypt_handler():
    try:
        if not fernet_file_path:
            raise Exception("No file selected")
        key = load_key_from_file("fernet_key.key")
        output_file = fernet_file_path + ".decrypted"
        decrypt_file_fernet(fernet_file_path, output_file, key)
        status_fernet.config(text=f"File decrypted as {output_file}", fg="green")
    except Exception as e:
        status_fernet.config(text=f"Error: {e}", fg="red")

btn_fernet_open.config(command=fernet_open_file)
btn_fernet_encrypt.config(command=fernet_encrypt_handler)
btn_fernet_decrypt.config(command=fernet_decrypt_handler)

# --- Hybrid Handlers ---
def hybrid_open_file():
    global hybrid_file_path
    hybrid_file_path = filedialog.askopenfilename()
    if hybrid_file_path:
        status_hybrid.config(text=f"Selected: {hybrid_file_path}", fg="blue")

def hybrid_encrypt_handler():
    try:
        if not hybrid_file_path:
            raise Exception("No file selected")
        pub_key = load_public_key("public.pem")
        output_file = hybrid_file_path + ".encrypted"
        hybrid_encrypt(hybrid_file_path, output_file, pub_key)
        status_hybrid.config(text=f"File encrypted as {output_file}", fg="green")
    except Exception as e:
        status_hybrid.config(text=f"Error: {e}", fg="red")

def hybrid_decrypt_handler():
    try:
        if not hybrid_file_path:
            raise Exception("No file selected")
        priv_key = load_private_key("private.pem")
        output_file = hybrid_file_path + ".decrypted"
        hybrid_decrypt(hybrid_file_path, output_file, priv_key)
        status_hybrid.config(text=f"File decrypted as {output_file}", fg="green")
    except Exception as e:
        status_hybrid.config(text=f"Error: {e}", fg="red")

btn_hybrid_open.config(command=hybrid_open_file)
btn_hybrid_encrypt.config(command=hybrid_encrypt_handler)
btn_hybrid_decrypt.config(command=hybrid_decrypt_handler)

# Start event loop
root.mainloop()

