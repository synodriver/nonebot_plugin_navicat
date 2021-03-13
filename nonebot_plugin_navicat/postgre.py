# -*- coding: utf-8 -*-
"""
对外导出postgresql连接
"""
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

pgsql_opened: bool = False

if config.pgsql_host:
    pgsql_pool = Database(
        f"postgresql://{config.pgsql_user}:{config.pgsql_password}@{config.pgsql_host}:{config.pgsql_port}")
    nonebot.export().pgsql_pool = pgsql_pool


@driver.on_startup
async def connect_to_pgsql():
    global pgsql_opened
    if config.pgsql_host:
        await pgsql_pool.connect()
        pgsql_opened = True
        nonebot.logger.info("connect to postgresql")


@driver.on_shutdown
async def free_db():
    global pgsql_opened
    if pgsql_opened:
        await pgsql_pool.disconnect()
        pgsql_opened = False
        nonebot.logger.info("disconnect to postgresql")
