#!/bin/bash
echo "启动神经网络研究数据展示网站..."
echo "========================================"

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo "错误：未找到 Python3，请先安装 Python3"
    exit 1
fi

echo "使用 Python 版本:"
python3 --version

echo ""
echo "正在启动本地服务器..."
python3 server.py 