# API Auto Test

基于 Python + pytest 的 API 自动化测试框架。

## 项目结构

```
api_auto_test/
├── api/              # API 接口层
│   └── user_api.py
├── common/           # 通用工具类
│   ├── request_util.py
│   └── yaml_util.py
├── testcase/         # 测试用例
│   └── test_user_login.py
├── data/             # 测试数据 (YAML)
│   └── user_login.yaml
├── report/           # 测试报告
│   └── allure-result/
├── config.py         # 全局配置
├── pytest.ini        # pytest 配置
└── requirements.txt  # 依赖列表
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试

```bash
pytest
```

### 3. 查看测试报告

```bash
allure serve report/allure-result
```

## 功能特性

- **YAML 数据驱动**：测试数据与代码分离
- **参数化测试**：支持多组测试数据
- **失败自动重试**：默认重试 2 次
- **Allure 报告**：生成可视化测试报告

## 依赖

- requests
- pytest
- pyyaml
- allure-pytest
- pytest-rerunfailures
- python-dotenv
