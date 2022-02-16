# -*- coding: utf-8 -*-
"""
对外导出postgresql连接
"""
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

pgsql_opened: bool = False

if getattr(config, "pgsql_host", None):
    pgsql_pool = Database(
        f"postgresql://{config.pgsql_user}:{config.pgsql_password}@{config.pgsql_host}:{config.pgsql_port}/{config.pgsql_db}")
    nonebot.export().pgsql_pool = pgsql_pool


@driver.on_startup
async def connect_to_pgsql():
    global pgsql_opened
    if getattr(config, "pgsql_host", None):
        await pgsql_pool.connect()
        pgsql_opened = True
        nonebot.logger.opt(colors=True).info("<y>Connect to Postgresql</y>")


@driver.on_shutdown
async def free_db():
    global pgsql_opened
    if pgsql_opened:
        await pgsql_pool.disconnect()
        pgsql_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Postgresql</y>")
