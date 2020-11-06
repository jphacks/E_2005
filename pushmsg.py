def send_push_message():
    import requests
    import json
    url = 'https://fraud-checker-test.herokuapp.com/raspi'
    headers =  {'Content-Type': 'application/json'}
    payload = {'raspi_id': 'jphacks-e2005-kokokatu', 'content': 'a text about fraud-conversation'}

    res = requests.post(url, data=json.dumps(payload), headers=headers)
    print(res)

if __name__ == '__main__':
    send_push_message()

