from flask import Flask, request, jsonify
from cipher.playfair import PlayFairCipher

app = Flask(__name__) 

# Khởi tạo Playfair Cipher
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'encrypted_text': playfair_cipher.playfair_encrypt(text, playfair_matrix)})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'decrypted_text': playfair_cipher.playfair_decrypt(text, playfair_matrix)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)