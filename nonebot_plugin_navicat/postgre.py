# -*- coding: utf-8 -*-
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

pgsql_opened: bool = False


@driver.on_startup
async def connect_to_pgsql():
    global pgsql_opened
    if config.pgsql_host is not None:
        pgsql_pool = Database(
            f"postgresql://{config.pgsql_user}:{config.pgsql_password}@{config.pgsql_host}:{config.pgsql_port}")
        await pgsql_pool.connect()
        nonebot.require("nonebot_plugin_navicat").pgsql_pool = pgsql_pool
        pgsql_opened = True
        nonebot.logger.info("connect to postgresql")


@driver.on_shutdown
async def free_db():
    global pgsql_opened
    if pgsql_opened:
        pgsql_pool = nonebot.require("nonebot_plugin_navicat").pgsql_pool
        await pgsql_pool.disconnect()
        pgsql_opened = False
        nonebot.logger.info("disconnect to postgresql")
