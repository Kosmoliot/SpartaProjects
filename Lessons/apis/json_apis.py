import json
import requests

# GET method
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/sw96nn")

# print(post_codes_req.status_code)
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(post_codes_req.json()) # Gives a dict


# POST method
json_postcode = json.dumps({"postcodes": ["sw96nn", "OX49 5NU"]})
headers = {'content-type': 'application/json'}

multi_request = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_postcode)
# print(multi_request.json())

post_req = multi_request.json()

print(post_req['result'][0])
