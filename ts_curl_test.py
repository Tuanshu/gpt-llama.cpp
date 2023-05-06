import json

import requests

port = 443
path = '../llama.cpp/models/gpt4all-lora-quantized-ggml.bin'


url = "http://localhost:{}/v1/chat/completions".format(port)
headers = {
    "Authorization": "Bearer {}".format(path),
    "Content-Type": "application/json",
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "system",
            "content": "You are ChatGPT, a helpful assistant developed by OpenAI.",
        },
        {
            "role": "user",
            "content": "How are you doing today?",
        },
    ],
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# If you want to print the response, you can use the following line
print(response.json())
