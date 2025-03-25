#!/bin/bash

# 使用方法说明:
# 1. 设置GitHub访问令牌环境变量
#    export GITHUB_ACCESS_TOKEN="your_github_token"
# 2. 执行脚本
#    ./Tools/git_push.sh

# 确保在AgentProject目录执行
cd "$(dirname "$0")/.." || exit 1

# 从环境变量获取GitHub access token
if [ -z "$GITHUB_ACCESS_TOKEN" ]; then
    echo "Error: GITHUB_ACCESS_TOKEN environment variable is not set"
    echo "Usage: export GITHUB_ACCESS_TOKEN=\"your_github_token\" && ./Tools/git_push.sh"
    exit 1
fi

# 解决Windows Git仓库所有权问题
git config --global --add safe.directory "$(pwd)"

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit"

# 添加远程仓库
git remote add origin "https://${GITHUB_ACCESS_TOKEN}@github.com/StellarFlash/AgentProject.git"

# 推送到远程仓库
git push -u origin main

echo "Git push completed successfully"