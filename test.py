from fastapi import FastAPI
import requests

url = "http://127.0.0.1:8000"

req = requests.get(url + "/api/start_session")

session_id = req.json()["session_id"]

req1 = requests.get(url + f"/api/join_session?session_id={session_id}&username=jack")
req2 = requests.get(url + f"/api/join_session?session_id={session_id}&username=jack")
req3 = requests.get(url + f"/api/join_session?session_id={session_id}&username=jackson")
req4 = requests.get(url + f"/api/join_session?session_id={session_id}&username=json")
req5 = requests.get(url + f"/api/session_info?session_id={session_id}")
req6 = requests.get(url + f"/api/session_info?session_id={1232334}")

print(req1.json(), req2.json(), req3.json(), req4.json(), req5.json(), req6.json())
