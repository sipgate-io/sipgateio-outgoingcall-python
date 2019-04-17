import requests


def main():
	baseURL = 'https://api.sipgate.com/v2'
	username = 'YOUR_EMAIL'
	password = 'YOUR_PASSWORD'

	deviceId = 'YOUR_SIPGATE_DEVICE_EXTENSION'
	callee = 'YOUR_RECIPIENT_PHONE_NUMBER'
	caller = 'DIALING_DEVICE'
	callerId = 'DISPLAYED_CALLER_NUMBER'

	headers = {
		'Content-Type': 'application/json'
	}

	requestBody = {
		"deviceId": deviceId,
		"callee": callee,
		"caller" : caller,
		"callerId" : callerId
	}

	response = requests.post(
		f'{baseURL}/sessions/calls',
		json=requestBody,
		auth=requests.auth.HTTPBasicAuth(username, password),
		headers=headers
	)

	print(f'Status: {response.status_code}')
	print(f'Body: {response.content.decode("utf-8")}')


if __name__ == "__main__":
	main()
