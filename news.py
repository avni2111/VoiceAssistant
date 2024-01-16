import requests
from ss import key

api_address = f"https://newsapi.org/v2/everything?q=keyword&apiKey={key}"

json_data = requests.get(api_address).json()

if 'articles' in json_data:
    ar = []

    def news():
        for i in range(3):
            ar.append(f"Number {i + 1}: {json_data['articles'][i]['title']}.")

        return ar

    arr = news()
    print(arr)
else:
    print("Error in API response:", json_data)
