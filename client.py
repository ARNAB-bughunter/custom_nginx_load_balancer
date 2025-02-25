import requests
import json

json_data = json.dumps( { "number": 15 } )

response = requests.post("http://0.0.0.0:7000/",json_data)
print(response.text)


# response = requests.get("http://0.0.0.0:8990/")
# print(response.text)


# url = "/factorial"

