import json
import os
import requests


def get_headers(pat_token):
    headers = {"Authorization": f'Snowflake Token="{pat_token}"'}
    return headers


pat_token = os.getenv("PAT_TOKEN")
if not pat_token:
    raise ValueError("PAT_TOKEN environment variable is not set")

headers = get_headers(pat_token)

URL = "https://bfc46pfe-sfsenorthamerica-cromano.snowflakecomputing.app/predict-proba"

data = {
    "data": [
        [
            0,
            615,
            8,
            240,
            3,
            0,
            615000,
            114000,
            0.18536585365853658,
            149375.90308231063,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
        ]
    ]
}


def send_request(data: dict):
    output = requests.post(URL, json=data, headers=headers)
    if output.status_code != 200:
        print(f"Response: {output.text}")
    assert output.status_code == 200, (
        f"Failed to get response from the service. Status code: {output.status_code}"
    )
    return output.content


results = send_request(data=data)
print(json.loads(results))
