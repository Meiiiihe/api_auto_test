import sys
sys.path.append(".")

import pytest
from api.user_api import UserApi
from common.yaml_util import read_yaml

# 读取YAML数据
test_data = read_yaml("data/user_login.yaml")

class TestUserLogin:
    @pytest.mark.parametrize("data", test_data)
    def test_login(self, data):
        # 调用接口
        res = UserApi().login(data["username"], data["password"])

        # 断言一定成功
        assert res is not None
        assert res["code"] == 200
        print("✅ 用例执行成功：", res)