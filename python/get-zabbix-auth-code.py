mport requests, json


def getZabbixAuthCode(user='', password=''):
    url = 'http://has/zabbix/api_jsonrpc.php'
    post_data = {
        'jsonrpc': '2.0',
        'method': 'user.login',
        'params': {
            'user': user,
            'password': password
        },
        'id': '1'
    }
    post_header = {'Content-Type': 'application/json'}

    with requests.Session() as s:
        sessionResonpse = s.post(url, data=json.dumps(post_data), headers=post_header)
        return json.loads(sessionResonpse.text).get('result', None)


print(getZabbixAuthCode())
