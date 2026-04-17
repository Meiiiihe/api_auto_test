import yaml
import os

def read_yaml(yaml_path):
    """读取yaml测试数据"""
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data