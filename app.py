from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAP7QzwEAAAAA2w%2BL1BRc5%2F%2B7qldCS8I%2FJ9aEjWg%3D0rSdtjlz6yATY9JWAaUdU1YVx73KjZ29aUYu14oEn3PQFdcNlH"  # Ganti dengan Bearer Token baru setelah regenerasi

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/twitter', methods=['GET'])
def get_twitter_data():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    api_url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10"
    
    try:
        response = requests.get(api_url, headers={'Authorization': f'Bearer {BEARER_TOKEN}'})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
