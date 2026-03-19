
# 图书管理系统

这是一个基于 Django 的简单图书管理系统，用于课程作业。

## 功能特性

- 用户注册、登录、登出
- 图书浏览、搜索、分类筛选
- 图书借阅与归还（AJAX 异步操作）
- 个人借阅历史查看
- 管理员可添加、编辑、删除图书

## 安装与运行

1. 进入项目目录：
cd D:\chengxu\IT

text

2. 创建虚拟环境（可选）：
python -m venv venv
venv\Scripts\activate

text

3. 安装依赖：
pip install -r requirements.txt

text

4. 数据库迁移：
python manage.py makemigrations books
python manage.py migrate

text

5. 创建超级管理员：
python manage.py createsuperuser

text

6. 运行开发服务器：
python manage.py runserver

text

7. 访问 http://127.0.0.1:8000/ 使用系统。

## 项目结构

见项目目录。

## 单元测试

运行测试：
python manage.py test books