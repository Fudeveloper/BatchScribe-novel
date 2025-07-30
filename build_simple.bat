@echo off
chcp 65001 >nul
title AI小说生成器 - 简化打包工具 v4.1.2

echo ====================================
echo   AI小说生成器 - 简化打包工具
echo   版本 4.1.2 - 修复bug + 媒体生成
echo ====================================
echo.

echo 正在启动简化打包脚本...
echo.

python build_simple.py

echo.
echo 打包完成！按任意键退出...
pause >nul 