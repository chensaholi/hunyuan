# -*- coding: utf-8 -*-
import os
import configparser


def get_config(section, key):
    config = configparser.ConfigParser()
    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'hunyuan.txt')
    if os.path.exists(config_path):
        config.read(config_path)
        return config.get(section, key)
    else:
        print("读取配置文件失败: %s" % config_path)
        return ''
