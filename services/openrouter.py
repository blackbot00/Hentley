import requests
from config import OPENROUTER_API_KEY

def ask_ai(message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a romantic, warm dating companion."},
            {"role": "user", "content": message}
        ]
    }

    r = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )
    return r.json()["choices"][0]["message"]["content"]
