import json
import os

JSON_FILE = "articles.json"

def load_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(data):
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_article_news(title, link):
    data = load_data()
    if not any(article["link"] == link for article in data):
        data.append({"title": title, "link": link})
        save_data(data)
        return True
    else:
        return False
