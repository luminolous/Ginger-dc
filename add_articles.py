import json
import os

# Nama file untuk menyimpan data
JSON_FILE = "articles.json"

# Fungsi untuk memuat data dari file JSON
def load_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan data ke file JSON
def save_data(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk menambahkan berita baru (menghindari duplikasi)
def add_article(title, link):
    data = load_data()
    if not any(article["link"] == link for article in data):
        data.append({"title": title, "link": link})
        save_data(data)
        print("Berita ditambahkan!")
    else:
        print("Berita sudah ada!")

# Contoh penggunaan
add_article("Berita AI Terbaru", "https://techcrunch.com/sample-article")
add_article("Berita AI Terbaru", "https://techcrunch.com/sample-article")
add_article("Berita AI baru", "https://techcrunch.com/sampl-article")
add_article("Berita AI baru", "https://techcrunch.com/sampl-article")
