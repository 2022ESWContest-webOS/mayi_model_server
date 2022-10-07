from flask import Flask
from detect import detect
from process import process
import ssl
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello May I!"

@app.route("/predict")
def predict():
    detect()
    return "Hello May I! Predicting..."

@app.route("/process")
def process_img():
    process()

if __name__ == "__main__":
    # gunicorn flask_server:app -b 0.0.0.0:2431 -w 4
    # python3
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem', password='secret')
    app.run(host="0.0.0.0", port=443, ssl_context=ssl_context)