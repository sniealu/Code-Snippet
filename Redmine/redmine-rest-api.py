import requests

class redmineAPI:
    def __init__(self):
        self.__api_key = '1a4403521aaf9f816c4a1370670fa0496d06df67'
        self.__url = 'http://localhost:8081/users.json'
    @property
    def api_key(self):
        return self.__api_key
    @property
    def url(self):
        return self.__url

    def getUser(self):
        rsp = requests.get(self.url, headers={'X-Redmine-API-Key':self.api_key})
        print(rsp.text)


if __name__ == '__main__':
    t = redmineAPI()
    t.getUser()

