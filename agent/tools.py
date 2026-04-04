import requests
import os

BASE_URL = "https://ubiquitous-happiness-jwr79v5x6p9cqggx-8000.app.github.dev"

def login(username, password):
    res = requests.post(
        f"{BASE_URL}/users/login",
        json={"username": username, "password": password}
    )
    return res.json()

def get_balance():
    try:
        res = requests.get(f"{BASE_URL}/wallet/")
        return f"Your balance is ₱{res.json()['balance']}"
    except Exception as e:
        return {"error": str(e)}

def send_money(amount: float, recipient: str):
    payload = {
        "receiver_username": recipient,
        "amount": amount
    }
    res = requests.post(f"{BASE_URL}/transactions/send", json=payload)
    if res.status_code == 200:
        return f"Successfully sent ₱{amount} to {recipient}"
    else:
        return f"Failed to send money: {res.json().get('detail', 'Unknown error')}"
    