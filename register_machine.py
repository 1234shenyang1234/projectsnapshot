#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目随手拍 - 注册机
用于生成软件注册码
"""

import hashlib

def generate_register_code(machine_code):
    """
    根据机器码生成注册码
    :param machine_code: 机器码
    :return: 注册码
    """
    # 移除机器码中的分隔符
    clean_machine = machine_code.replace('-', '')
    
    # 生成注册码
    # 注意：这里的密钥必须与软件中的密钥一致
    register_code = hashlib.sha256((clean_machine + 'your-secret-key').encode()).hexdigest().upper()
    
    # 格式化注册码，每5位一组，用-分隔
    formatted_register = '-'.join([register_code[i:i+5] for i in range(0, len(register_code), 5)])
    
    return formatted_register

def main():
    """
    注册机主函数
    """
    print("=== 项目随手拍 - 注册机 ===")
    print("请输入机器码：")
    machine_code = input().strip()
    
    if not machine_code:
        print("错误：机器码不能为空")
        return
    
    try:
        register_code = generate_register_code(machine_code)
        print(f"\n注册码：{register_code}")
        print("\n请将此注册码复制到软件中进行激活")
    except Exception as e:
        print(f"生成注册码失败：{str(e)}")

if __name__ == "__main__":
    main()