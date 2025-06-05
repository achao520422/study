import requests
import json


class PveApi:
    def __init__(self, username, password, service_ip, verify=False):
        try:
            assert self.__checkLength(username, password, service_ip), '参数不合法'
        except AssertionError as e:
            print(e)
        self.__private_username = username
        self.___private_password = password
        self.__private_service_ip = service_ip
        self.___private_verify = verify
        self.__private_header_default = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def geTickets(self):
        with open('tickets.json', 'r', encoding='utf-8') as f:
            tickets = json.load(f)
            self.headers = {
                tickets['data']['ticket'].replace('=', ''): '='
            }
            self.cookies = {

                'CSRFPreventionToken': tickets['data']['CSRFPreventionToken'],
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            print(requests.get(f'https://{self.__private_service_ip}/api2/json', headers=self.headers,
                               cookies=self.cookies, verify=self.___private_verify).content)
            return tickets

        data = f'username={self.__private_username}@pam&password={self.___private_password}'
        res = requests.post(f'https://{self.__private_service_ip}/api2/json/access/ticket', data=data,
                            headers=self.__private_header_default,
                            verify=self.___private_verify).json()
        with open('tickets.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(res, ensure_ascii=False))
        return res

    def __checkLength(self, *args):
        for arg in args:
            if len(arg) != 0:
                return True
            else:
                return False


#
# data = 'username=root@pam' + '&password=147258369'
#
# response = requests.post('https://192.168.34.8:8006/api2/json/access/ticket', headers=headers, data=data, verify=False)
# print(response.text)
#
# pve = PveApi('root', '147258369', '192.168.34.8:8006').geTickets()
# print(pve)
# cookies = {
#     'PVE:root@pam:61B2EC05::Y1uRp+iFUpcSTEQsE0M8FB3aQi7lpNO3gIxr/g7rJX6GOLSOshKv9WHsGTUD3huFS3C3kIt/S3tFpg34xqHWFpF5cRjyqyG66ca3h+9ag/wSGuKPt+SkagVJOFZ2nlroSy5pY8sCZu+q5XhwLhElGSJOG43dMUod4Fhc5U2jdRn52FV15dY9aC9ym3FNpxRuNPRorSQASDFASDFZXCZduhEpDMKsTiSYxE0Owwme5g+sNZ1LKbkX5mpM2QdlN183jLU/AVgXPAw5hLdEeZorojC7HcO8f7A4SvmBxRzMl4GbXJYvwc+IyqTM+mZ9oPJPBTgQb+MAEafisW5Vbg': '=',
# }


import requests

cookies = {
    'PVE:root@pam:61B2EC05::Y1uRp+iFUpcSTEQsE0M8FB3aQi7lpNO3gIxr/g7rJX6GOLSOshKv9WHsGTUD3huFS3C3kIt/S3tFpg34xqHWFpF5cRjyqyG66ca3h+9ag/wSGuKPt+SkagVJOFZ2nlroSy5pY8sCZu+q5XhwLhElGSJOG43dMUod4Fhc5U2jdRn52FV15dY9aC9ym3FNpxRuNPRorSQASDFASDFZXCZduhEpDMKsTiSYxE0Owwme5g+sNZ1LKbkX5mpM2QdlN183jLU/AVgXPAw5hLdEeZorojC7HcO8f7A4SvmBxRzMl4GbXJYvwc+IyqTM+mZ9oPJPBTgQb+MAEafisW5Vbg': '=',
}

headers = {
     "Authorization": 'PVEAPIToken=',
    # 'Cookie': 'PVE:root@pam:61B2EC05::Y1uRp+iFUpcSTEQsE0M8FB3aQi7lpNO3gIxr/g7rJX6GOLSOshKv9WHsGTUD3huFS3C3kIt/S3tFpg34xqHWFpF5cRjyqyG66ca3h+9ag/wSGuKPt+SkagVJOFZ2nlroSy5pY8sCZu+q5XhwLhElGSJOG43dMUod4Fhc5U2jdRn52FV15dY9aC9ym3FNpxRuNPRorSQASDFASDFZXCZduhEpDMKsTiSYxE0Owwme5g+sNZ1LKbkX5mpM2QdlN183jLU/AVgXPAw5hLdEeZorojC7HcO8f7A4SvmBxRzMl4GbXJYvwc+IyqTM+mZ9oPJPBTgQb+MAEafisW5Vbg==',
    'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.get(
    'https://192.168.34.8:8006/api2/json/nodes/testpve/qemu/102/status/current',
    cookies=cookies,
    headers=headers,
    verify=False,
).text


print(response)