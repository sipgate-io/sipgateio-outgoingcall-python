import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
token_id = os.environ.get("TOKEN_ID")

callee = os.environ.get("CALLEE")
caller = os.environ.get("CALLER")
device_id = os.environ.get("DEVICE_ID")
caller_id = os.environ.get("CALLER_ID")


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
