# nonebot_plugin_navicat
[![pypi](https://img.shields.io/pypi/v/nonebot-plugin-navicat.svg)](https://pypi.org/project/nonebot_plugin_navicat/) 
![implementation](https://img.shields.io/pypi/implementation/nonebot-plugin-navicat)
![wheel](https://img.shields.io/pypi/wheel/nonebot-plugin-navicat)
![python](https://img.shields.io/pypi/pyversions/nonebot-plugin-navicat)
[![license](https://img.shields.io/github/license/synodriver/nonebot_plugin_navicat.svg)](https://raw.githubusercontent.com/synodriver/nonebot_plugin_navicat/main/LICENSE)

- 基于[nonebot2](https://github.com/nonebot/nonebot2)

## 功能

- 对外暴露出数据库连接 支持mysql mongodb redis

## 开始使用

必须使用 pip

- 通过 pip 从 [PyPI](https://pypi.org/project/nonebot_plugin_navicat/) 安装

``` {.sourceCode .bash}
pip install nonebot-plugin-navicat
```
- 我全都要
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[all]
```
- 要使用mysql
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[mysql]
```
- 要使用postgresql
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[postgresql]
```
- 要使用sqlite
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[sqlite]
```
- 要使用mongodb
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[mongodb]
```
- 要使用redis
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[redis]
```
- 要使用elasticsearch
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[elasticsearch]
```

- 在 nonebot2 项目中设置 load_plugin()

``` {.sourceCode .python}
nonebot.load_plugin('nonebot_plugin_navicat')
```

- 参照下文在 nonebot2 项目的环境文件 .env.\* 中添加配置项

## 配置项
配置数据库连接
```
# mysql 如果有MYSQL_HOST则表示要进行mysql连接
MYSQL_HOST=
MYSQL_PORT=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DB=

# postgresql 如果有PGSQL_HOST则表示要进行postgresql连接
PGSQL_HOST=
PGSQL_PORT=
PGSQL_USER=
PGSQL_PASSWORD=
PGSQL_DB=

# sqlite 如果有SQLITE_HOST则表示要进行sqlite连接 这里是路径
SQLITE_HOST=

# mongodb 如果有MONGODB_HOST则表示要进行mongodb连接
MONGODB_HOST=
MONGODB_PORT=
MONGODB_USER=
MONGODB_PASSWORD=

# redis 如果有REDIS_HOST则表示要进行redis连接
REDIS_PARAMS={"decode_responses":true}
REDIS_HOST=
REDIS_PORT=
REDIS_PASSWORD=
REDIS_DB=

# redis sentinel 如果有REDIS_SENTINEL_PARAMS则表示要进行redis sentinel连接
REDIS_SENTINEL_PARAMS=
REDIS_SENTINEL_SERVICE_NAME=    # 必填

# redis cluster 如果有REDIS_CLUSTER_PARAMS则表示要进行redis cluster连接
REDIS_CLUSTER_PARAMS=
REDIS_CLUSTER_NODES=
# 集群没有db选项

# elasticsearch 如果有ELASTICSEARCH_PARAMS则表示要进行elasticsearch连接
ELASTICSEARCH_PARAMS=
ELASTICSEARCH_HOSTS=


# 以后会加入更多数据库支持
```
## 导出给其他插件

```{.sourceCode .python}
from nonebot import require

require("nonebot_plugin_navicat")
import nonebot_plugin_navicat as export # 兼容老写法，不至于大改

export.mysql_pool # mysql的

export.pgsql_pool # postgresql的

export.sqlite_pool # sqlite的

export.mongodb_client # mongodb的

export.redis_client # redis的
export.redis_sentinel
export.redis_cluster

export.elasticsearch # elasticsearch的
```

## 直接查询数据库 (0.2.0中已删除)
- 危险功能! 在配置中启用```NAVICAT_EXECUTE_SQL=true```来开启
- 使用方法:发送```super ${dbname} + sql```来查询
```
super mysql
show databases
```
## 更新记录
- v0.3.0rc1 适配nonebot rc版本

- v0.2.3 修复beta2的bug


- v0.2.1 加入了对redis哨兵和集群的支持，对```elasticsearch```的支持



- v0.2.0 使用 [databases](https://github.com/encode/databases/) 代替直接连接,有了广泛的通用性
- 移除了直接命令行查询数据库的功能,迁移到了单独的一个插件里面 *[nonebot-plugin-super](https://github.com/synodriver/nonebot_plugin_super)*
## 特别感谢

- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)

## 优化建议

- bug report
- more databases support
![](https://i.pixiv.cat/img-original/img/2018/08/29/00/16/10/70434240_p0.png "bug哪里跑 看姐姐给你们全抓起来~")