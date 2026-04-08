import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://bookish-spork-v7prw96v64pfjpv-8000.app.github.dev"

SESSION_FILE = ".session.json"

def save_session(token):
    with open(SESSION_FILE, "w") as f:
        json.dump({"token": token}, f)

def load_session():
    try:
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Replace SESSION = {} with:
SESSION = load_session()

def login(username, password):
    logging.info("🔥 LOGIN FUNCTION CALLED")
    try:
        res = requests.post(
            f"{BASE_URL}/users/login",
            data={"username": username, "password": password},
            timeout=5
        )
        res.raise_for_status()
        token = res.json().get("access_token")
        if token:
            SESSION['token'] = token
            save_session(token)
            logging.info("✅ LOGIN SUCCESSFUL")
        return res.json()
    except Exception as e:
        logging.error("❌ LOGIN ERROR: %s", e)
        return {"error": str(e)}

def get_balance(_=None):
    logging.info("🔥 GET BALANCE FUNCTION CALLED")
    logging.info("🔑 TOKEN: %s", SESSION.get('token', 'NO TOKEN FOUND'))
    headers = {"Authorization": f"Bearer {SESSION.get('token', '')}"}
    try:
        res = requests.get(f"{BASE_URL}/wallet/", headers=headers, timeout=5)
        res.raise_for_status()
        logging.info("✅ BALANCE RESPONSE: %s", res.text)
        return f"Your balance is ₱{res.json()['balance']}"
    except Exception as e:
        logging.error("❌ BALANCE ERROR: %s", e)
        return {"error": str(e)}

def send_money(amount: float, recipient: str):
    logging.info("🔥 SEND MONEY FUNCTION CALLED")
    headers = {"Authorization": f"Bearer {SESSION.get('token', '')}"}
    payload = {"receiver_username": recipient, "amount": amount}
    try:
        res = requests.post(f"{BASE_URL}/transactions/send", json=payload, headers=headers, timeout=5)
        res.raise_for_status()
        logging.info("✅ MONEY SENT: %s", res.text)
        return f"Successfully sent ₱{amount} to {recipient}"
    except Exception as e:
        logging.error("❌ SEND MONEY ERROR: %s", e)
        return {"error": str(e)}