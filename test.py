from fastapi import FastAPI
import requests

url = "http://127.0.0.1:8000"

req = requests.get(url + "/api/start_session")

session_id = req.json()["session_id"]

req2 = requests.get(url + f"/api/join_session?session_id={session_id}&username=jack")
req3 = requests.get(url + f"/api/join_session?session_id={session_id}&username=jackson")
req4 = requests.get(url + f"/api/session_info?session_id={session_id}")


print(req4.json())
