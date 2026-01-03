import requests

url = "http://127.0.0.1:65432/send"

print("Connected to REST server")

while True:
    msg = input("Enter message for sending (q/exit to quit): ")
    
    payload = {"message": msg}
    
    try:
        response = requests.post(url, json=payload)
        data = response.json()
        
        print("Server response:", data.get("server_response") or data.get("response"))
        
        if msg in ("exit", "q"):
            break
    except Exception as e:
        print(f"Error: {e}")
        break

print("Connection closed")