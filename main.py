import requests

query = input("Enter the news you want to see : ")

api = "Enter the API Key"

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

print(r)

data = r.json()

print(data)   # helpful for debugging

if data["status"] == "ok":

    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index + 1, article["title"])
        print(article["url"])
        print("\n----------------------------------------------------\n")

else:
    print("Error:", data["message"])