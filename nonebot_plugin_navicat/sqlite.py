# -*- coding: utf-8 -*-
"""
对外导出sqlite连接
"""
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

sqlite_opened: bool = False

if config.sqlite_host:
    sqlite_pool = Database(f"sqlite://{config.sqlite_host}")
    nonebot.export().sqlite_pool = sqlite_pool


@driver.on_startup
async def connect_to_sqlite():
    global sqlite_opened
    if config.sqlite_host:
        await sqlite_pool.connect()
        sqlite_opened = True
        nonebot.logger.info("connect to sqlite")


@driver.on_shutdown
async def free_db():
    global sqlite_opened
    if sqlite_opened:
        await sqlite_pool.disconnect()
        sqlite_opened = False
        nonebot.logger.info("disconnect to sqlite")
