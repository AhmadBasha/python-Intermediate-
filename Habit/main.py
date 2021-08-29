import requests
from datetime import datetime

USERNAME = "ahmed123"
TOKEN = "any token from 8 to 28 chars"
GRAPH_ID = "graph1"

# creating a user
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# my header for the key
headers = {
    "X-USER-TOKEN": TOKEN
}
############
# create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Gym Graph 🏋️‍️",
    "unit": "Km",
    "type": "float",
    "color": "kuro"
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
############
# post a pixe
today = datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    #year month day
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you walk today? ")
    # "quantity": "3.6"

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)

############
# update and delete a pixel

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    "quantity": "3.7"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

#delete

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)
