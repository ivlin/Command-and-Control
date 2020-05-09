from flask import Flask
from cryptography.fernet import Fernet
import subprocess
app = Flask(__name__)

symmetric_key=None
crypt=None
email="ivlin@gmail.com"

def generate_keys():
    with open("keys/symmetric_key", "wb") as symmetric_key_f:
        symmetric_key_f.write(Fernet.generate_key())
    subprocess.run(["bash","generate_public.sh",email])

def decrypt(cipher):
    with open("keys/symmetric_key", "rb") as symmetric_key_f:
        symmetric_key = symmetric_key_f.read()
        crypt=Fernet(symmetric_key)
        print(crypt.decrypt(cipher.encode()).decode("utf-8"))

@app.route('/')
def hello():
    return "Test website"

@app.route('/id_rsa.pub')
def get_public():
    with open("keys/id_rsa.pub","r") as public_key_f:
        public_key = public_key_f.read()
        public_key_crypt = crypt.encrypt(public_key.encode())
        return public_key_crypt.decode("utf-8")
    return "Failed to load"

@app.route('/id_rsa')
def get_private():
    with open("keys/id_rsa","r") as private_key_f:
        private_key = private_key_f.read()
        private_key_crypt = crypt.encrypt(private_key.encode())
        return private_key_crypt.decode("utf-8")
    return "Failed to load"

@app.route('/repo')
def repo():
	return "git@github.com:ivlin/commtest"

try:
    with open("keys/symmetric_key", "rb") as symmetric_key_f:
        symmetric_key = symmetric_key_f.read()
        crypt=Fernet(symmetric_key)
except:
	print("Generating new keys")
	generate_keys()
	with open("keys/symmetric_key", "rb") as symmetric_key_f:
		symmetric_key = symmetric_key_f.read()
		crypt=Fernet(symmetric_key)

if __name__ == '__main__':
    app.run()

