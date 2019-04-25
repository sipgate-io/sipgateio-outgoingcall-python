import requests


def outgoing_call():
	base_url = 'https://api.sipgate.com/v2'

	username = 'YOUR_EMAIL'
	password = 'YOUR_PASSWORD'

	device_id = 'YOUR_SIPGATE_DEVICE_EXTENSION'
	caller = 'DIALING_DEVICE'

	callee = 'YOUR_RECIPIENT_PHONE_NUMBER'
	caller_id = 'DISPLAYED_CALLER_NUMBER'

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
		auth=requests.auth.HTTPBasicAuth(username, password),
		headers=headers
	)

	print('Status:', response.status_code)
	print('Body:', response.content.decode("utf-8"))


if __name__ == "__main__":
	outgoing_call()
