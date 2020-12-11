# -*- coding: utf-8 -*-
import nonebot
from databases import Database

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

sqlite_opened: bool = False


@driver.on_startup
async def connect_to_sqlite():
    global sqlite_opened
    if config.sqlite_host is not None:
        sqlite_pool = Database(f"sqlite://{config.sqlite_host}")
        await sqlite_pool.connect()
        nonebot.require("nonebot_plugin_navicat").sqlite_pool = sqlite_pool
        sqlite_opened = True
        nonebot.logger.info("connect to sqlite")


@driver.on_shutdown
async def free_db():
    global sqlite_opened
    if sqlite_opened:
        sqlite_pool = nonebot.require("nonebot_plugin_navicat").sqlite_pool
        await sqlite_pool.disconnect()
        sqlite_opened = False
        nonebot.logger.info("disconnect to sqlite")
