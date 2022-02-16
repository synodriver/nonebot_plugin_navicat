# -*- coding: utf-8 -*-
"""
对外导出mysql连接
"""
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

mysql_opened: bool = False

if getattr(config, "mysql_host", None):
    mysql_pool = Database(
        f"mysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}/{config.mysql_db}")
    nonebot.export().mysql_pool = mysql_pool


@driver.on_startup
async def connect_to_mysql():
    global mysql_opened
    if getattr(config, "mysql_host", None):
        await mysql_pool.connect()
        mysql_opened = True
        nonebot.logger.opt(colors=True).info("<y>Connect to Mysql</y>")


@driver.on_shutdown
async def free_db():
    global mysql_opened
    if mysql_opened:
        await mysql_pool.disconnect()
        mysql_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Mysql</y>")
