# 项目名称：joycastle
本系统旨在将样例中的event 数据存入SQLLite
并构建如下看板：
• 每日活跃用户数（DAU）
• 平均会话时长（分钟）
• 来自应用内购买的总收入
• 每次会话的社交互动次数

## 软件架构(可选)
数据库：SQLite
看板   ：Superset

## 快速开始
————————————superset 安装————————————
## --虚拟环境安装
    pip3 install virtualenv
    python3 -m venv venv-superset
    pip3 install --upgrade setuptools pip
        
## --安装superset
    pip3 install superset
## --创建用户
    superset fab create-admin
## --更新superset db
    superset db upgrade
## -- 加载样例
    superset load_examples
## -- superset初始化
    superset init
## -- 启动服务
    superset run -p 8088

### 依赖检查

## -- Python相关依赖
   wtforms_json、flask_compress、celery、flask_migrate、flask_talisman、flask_caching、sqlparse、bleach、markdown、numpy、pandas、parsedatetime、pathlib2、simplejson，humanize，python-geohash，polyline，geopy，cryptography，backoff，msgpack，pyarrow，contextlib2，croniter，retry，selenium，isodate

### 运行
   访问地址：http://127.0.0.1:8088


