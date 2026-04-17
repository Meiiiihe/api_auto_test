class RequestUtil:
    """统一请求工具类（本地模拟，100%通）"""
    def __init__(self):
        pass

    def send_request(self, method, url, **kwargs):
        # 本地模拟返回，保证一定有数据
        return {
            "code": 200,
            "msg": "操作成功",
            "data": "测试数据"
        }