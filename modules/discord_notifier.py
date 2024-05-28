import requests
from config import WEBHOOK_URL

def send_discord_message(message):
    if not WEBHOOK_URL:
        print("Discord webhook URL not provided. Skipping notification.")
        return
    
    data = {"content": message}
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f"Failed to send message to Discord: {response.status_code}")
