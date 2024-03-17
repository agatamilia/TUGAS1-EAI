import requests

url = "https://whin2.p.rapidapi.com/send"

payload = { "text": "Halo Guys Welcome" }
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "425a1ac206msh67e41569554d810p1c1c3ejsn081bffa0efa1",
    "X-RapidAPI-Host": "whin2.p.rapidapi.com"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as e:
    print(f"An error occurred: {e}")

print("Response Content:")
print(response.text)
