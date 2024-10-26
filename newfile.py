from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_ip', methods=['POST'])
def get_ip():
    data = request.get_json()
    domain = data.get('domain')
    try:
        ip_address = socket.gethostbyname(domain)
        return jsonify({'ip': ip_address})
    except socket.gaierror:
        return jsonify({'error': 'Invalid domain name'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
