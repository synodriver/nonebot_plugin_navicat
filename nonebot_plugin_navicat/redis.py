# -*- coding: utf-8 -*-
"""
对外导出mongodb连接
"""
import nonebot

try:
    import redis
except ImportError:
    redis = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

redis_opened = False


@driver.on_startup
async def connect_to_redis():
    global redis_opened
    if config.redis_host is not None:
        nonebot.require("nonebot_plugin_navicat").redis_client = redis.Redis(host=config.redis_host,
                                                                             port=config.redis_port,
                                                                             db=config.redis_db,
                                                                             password=config.redis_password)
        redis_opened = True
        nonebot.logger.info("connect to redis")


@driver.on_shutdown
async def free_db():
    global redis_opened
    if redis_opened:
        redis_client: redis.Redis = nonebot.require("nonebot_plugin_navicat").redis_client
        redis_client.close()
        redis_opened = False
        nonebot.logger.info("disconnect to redis")
