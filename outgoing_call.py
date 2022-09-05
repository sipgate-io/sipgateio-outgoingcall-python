import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("token")
token_id = os.environ.get("tokenId")

callee = os.environ.get("callee")
caller = os.environ.get("caller")
device_id = os.environ.get("device_id")
caller_id = os.environ.get("caller_id")


def outgoing_call():
	base_url = 'https://api.sipgate.com/v2'

	headers = {
		'Content-Type': 'application/json'
	}

	request_body = {
		"deviceId": device_id,
		"callee": callee,
		"caller": caller,
		"callerId": caller_id
	}

	response = requests.post(
		base_url + '/sessions/calls',
		json=request_body,
		auth=requests.auth.HTTPBasicAuth(token_id, token),
		headers=headers
	)

	print('Status:', response.status_code)
	print('Body:', response.content.decode("utf-8"))


if __name__ == "__main__":
	outgoing_call()
