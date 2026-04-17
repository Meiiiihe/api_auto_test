from common.request_util import RequestUtil

class UserApi:
    def __init__(self):
        self.request = RequestUtil()

    def login(self, username, password):
        # 本地模拟，不请求网络
        return self.request.send_request("POST", "/user/login")