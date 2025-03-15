import requests

# Kode API
API_KEY = '37e69887-7cd7-4c46-8300-e3a6f5805dc5'

# URL endpoint API (ganti dengan URL API yang sesuai)
API_URL = 'https://api.contoh.com/data'

# Fungsi untuk mengakses API
def get_data_from_api():
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Data dari API:", data)
    else:
        print("Gagal mengakses API. Kode status:", response.status_code)

# Panggil fungsi untuk mengakses API
if __name__ == "__main__":
    get_data_from_api()
