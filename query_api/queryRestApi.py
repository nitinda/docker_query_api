import requests

def query_api_func(url, paramPayload):
    headers = {'content-type': 'application/json'}
    try:
        response = requests.get(url, params=paramPayload, headers=headers)
        if response.status_code != 200:
            return "Error: " + str(requests.exceptions.HTTPError)
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)
    json_response = response.json()
    return json_response