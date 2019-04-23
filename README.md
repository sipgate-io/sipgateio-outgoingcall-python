<img src="https://www.sipgatedesign.com/wp-content/uploads/wort-bildmarke_positiv_2x.jpg" alt="sipgate logo" title="sipgate" align="right" height="112" width="200"/>

# sipgate.io python outgoing call example

In order to demonstrate how to initiate an outgoing call, we queried the `/sessions/calls` endpoint of the sipgate REST API.

For further information regarding the sipgate REST API please visit https://api.sipgate.com/v2/doc

### Prerequisites

- python3.6
- pip3
- VoIP client

### How To Use

Navigate to the project's root directory.

Install dependencies:

```bash
$ pip3 install -r requirements.txt
```

In order to run the code you must set the following variables in [main.py](./main.py):

```python
username = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

deviceId = 'YOUR_SIPGATE_DEVICE_EXTENSION'
caller = 'DIALING_DEVICE';

callee = 'YOUR_RECIPIENT_PHONE_NUMBER'
callerId = 'DISPLAYED_CALLER_NUMBER'
```

The `deviceId` uniquely identifies the phone extension which establishes the phone connection,
this variable is needed only when the `caller` is a phone number and not a device extension. Further explanation is given in the section [Web Phone Extensions](#web-phone-extensions). Nevertheless you can still use both as device extension, but in this case the `deviceId` will be ignored.

Use `callee` and `callerId` to set the recipient phone number and the displayed caller number respectively.

Run the application:

```bash
$ python3 main.py
```

##### How It Works

The following explanations lay out how the code example works. There is no need for you to change anything unless you want to do something different.

The sipgate REST API is available under the following base URL:

```python
baseURL = 'https://api.sipgate.com/v2'
```

The API expects request data in JSON format. Thus the `Content-Type` header is set to:

```python
headers = {
	'Content-Type': 'application/json'
}
```

The request body contains the fields: `deviceId`, `caller`, `callee` and `callerId` as specified above.

```python
requestBody = {
		"deviceId": deviceId,
		"callee": callee,
		"caller" : caller,
		"callerId" : callerId
	}
```

We use the python package 'requests' for request generation and execution. The `post` function takes the following arguments:

- request URL
- headers
- authorization header
- request body

The request URL consists of the base URL defined above and the endpoint `/sessions/calls`. The function `HTTPBasicAuth` from the 'requests' package takes the credentials and generates the required Basic Auth header as authorization header (for more information on Basic Auth see our [code example](https://github.com/sipgate/sipgateio-basicauth-python)).

```python
response = requests.post(
	f'{baseURL}/sessions/calls',
	headers=headers,
	auth=requests.auth.HTTPBasicAuth(username, password),
	json=requestBody
)
```

### Web Phone Extensions

A Web Phone extension consists of one letter followed by a number (e.g. 'e0'). The sipgate API uses the concept of Web Phone extensions to identify devices within your account that are enabled to initiate calls.

Depending on your needs you can choose between the following phone types:

| phone type     | letter |
| -------------- | ------ |
| voip phone     | e      |
| external phone | x      |
| mobile phone   | y      |

You can find out what your extension is as follows:

1. Log into your [sipgate account](https://app.sipgate.com/login)
2. Use the sidebar to navigate to the **Phones** (_Telefone_) tab
3. Click on the device from which you want the Web Phone extension (`deviceId`)
4. The URL of the page this takes you to should have the form `https://app.sipgate.com/{...}/devices/{deviceId}` where `{deviceId}` is your Web Phone extension

### Common Issues

#### API returns 200 OK but no call gets initiated

Possible reasons are:

- your phone is not connected
- `caller` does not match your phones Web Phone extension

#### HTTP Errors

| reason                                                                                                                            | errorcode |
| --------------------------------------------------------------------------------------------------------------------------------- | :-------: |
| bad request (e.g. request body fields are empty or only contain spaces, timestamp is invalid etc.)                                |    400    |
| username and/or password are wrong                                                                                                |    401    |
| insufficient account balance                                                                                                                        |    402    |
| no permission to use specified Web Phone extension (e.g. user password must be reset in [web app](https://app.sipgate.com/login)) |    403    |
| wrong REST API endpoint                                                                                                           |    404    |
| wrong request method                                                                                                              |    405    |
| wrong or missing `Content-Type` header with `application/json`                                                                    |    415    |

### Related

- [requests documentation](http://docs.python-requests.org/en/master/)

### Contact Us

Please let us know how we can improve this example.
If you have a specific feature request or found a bug, please use **Issues** or fork this repository and send a **pull request** with your improvements.

### License

This project is licensed under **The Unlicense** (see [LICENSE file](./LICENSE)).

### External Libraries

This code uses the following external libraries

- requests:
  Licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
  Website: http://docs.python-requests.org/en/master/

---

[sipgate.io](https://www.sipgate.io) | [@sipgateio](https://twitter.com/sipgateio) | [API-doc](https://api.sipgate.com/v2/doc)
