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
- 要使用mongodb
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[mongodb]
```
- 要使用redis
``` {.sourceCode .bash}
pip install nonebot-plugin-navicat[redis]
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
MYSQL_HOST
MYSQL_PORT
MYSQL_USER
MYSQL_PASSWORD

# mongodb 如果有MONGODB_HOST则表示要进行mongodb连接
MONGODB_HOST
MONGODB_PORT
MONGODB_USER
MONGODB_PASSWORD

# redis 如果有REDIS_HOST则表示要进行redis连接
REDIS_HOST
REDIS_PORT
REDIS_PASSWORD
REDIS_DB

# 以后会加入更多数据库支持
```
## 导出给其他插件

```{.sourceCode .python}
export = nonebot.require("nonebot_plugin_navicat")
export.mysql_pool # mysql的
export.mongodb_client # mongodb的
export.redis_client # redis的
```

## 直接查询数据库
- 危险功能! 在配置中启用```NAVICAT_EXECUTE_SQL=true```来开启
- 使用方法:发送```super sql + sql```来查询
```
super sql
show databases
```

## 特别感谢

- [Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
- [nonebot / nonebot2](https://github.com/nonebot/nonebot2)

## 优化建议

- 来个postgresql支持?
![](https://i.pixiv.cat/img-original/img/2018/08/29/00/16/10/70434240_p0.png "bug哪里跑 看姐姐给你们全抓起来~")