from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API Key Anda
API_KEY = "F9pJe0lFkaKjkcMRnXn03n84UCk46jYI"

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/test', methods=['POST'])
def test_api():
    try:
        data = request.json.get('input')
        
        # Contoh penggunaan API Key (sesuaikan dengan API yang Anda gunakan)
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Ganti URL ini dengan endpoint API yang sebenarnya
        response = requests.post(
            'https://api.example.com/endpoint',
            headers=headers,
            json={'data': data}
        )
        
        if response.status_code == 200:
            return jsonify({'result': response.json()})
        else:
            return jsonify({'error': f'API Error: {response.status_code}'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
