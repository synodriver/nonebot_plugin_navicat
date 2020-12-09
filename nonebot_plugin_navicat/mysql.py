# -*- coding: utf-8 -*-
"""
对外导出mysql连接
"""
import nonebot

try:
    import aiomysql
except ImportError:
    aiomysql = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

mysql_opened: bool = False


@driver.on_startup
async def connect_to_mysql():
    global mysql_opened
    if config.mysql_host is not None:
        nonebot.require("nonebot_plugin_navicat").mysql_pool = await aiomysql.create_pool(
            host=config.mysql_host,
            port=config.mysql_port,
            user=config.mysql_user,
            password=config.mysql_password,
            charset="utf8",
            autocommit=True)
        mysql_opened = True
        nonebot.logger.info("connect to mysql")


@driver.on_shutdown
async def free_db():
    global mysql_opened
    if mysql_opened:
        pool: aiomysql.Pool = nonebot.require("nonebot_plugin_navicat").mysql_pool
        pool.close()
        await pool.wait_closed()
        mysql_opened = False
        nonebot.logger.info("disconnect to mysql")
