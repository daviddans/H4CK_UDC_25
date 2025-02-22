import requests
import os
import json

def ask_deepseek(prompt, base_url, api_key):
    response = requests.post(
        url=base_url,
        headers={
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-chat:free",
            "messages": [
                {"role": "user", "content": prompt}
            ],
        })
    )
    return response
