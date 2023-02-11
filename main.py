import requests

print("\nHello and welcome to my News Headline Aggregator.")
print("It shows all of the major news headlines currently appearing in the United States.")

response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=e21aa0bd35ff43979b780a63369c86c3")
data = response.json()
headline_amount = len(data['articles'])
for item in range(headline_amount):
    headline = data['articles'][item]['title']
    print(f"Headline {item+1}: {headline}")