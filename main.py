from flask import Flask
from encoder import encryption as e, decryption as d

app = Flask(__name__)

@app.route('/e/<encrypt>')
def yes(encrypt):
        return e(encrypt)
@app.route('/d/<decrypt>')
def no(decrypt):
        return d(decrypt)
@app.route('/')
def index():
        return "this is the encoder/decoder page - welcome!"

if __name__ == "__main__":
    app.run(debug=True)
