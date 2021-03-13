# -*- coding: utf-8 -*-
"""
对外导出mysql连接
"""
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

mysql_opened: bool = False

if config.mysql_host:
    mysql_pool = Database(
        f"mysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}")
    nonebot.export().mysql_pool = mysql_pool


@driver.on_startup
async def connect_to_mysql():
    global mysql_opened
    if config.mysql_host:
        await mysql_pool.connect()
        mysql_opened = True
        nonebot.logger.info("connect to mysql")


@driver.on_shutdown
async def free_db():
    global mysql_opened
    if mysql_opened:
        await mysql_pool.disconnect()
        mysql_opened = False
        nonebot.logger.info("disconnect to mysql")
