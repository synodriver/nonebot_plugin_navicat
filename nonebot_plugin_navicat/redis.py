# -*- coding: utf-8 -*-
"""
对外导出redis连接
"""
import nonebot

try:
    import redis
except ImportError:
    redis = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

redis_opened: bool = False

if redis and config.redis_host:
    redis_client = redis.Redis(host=config.redis_host,
                               port=config.redis_port,
                               db=config.redis_db,
                               password=config.redis_password,
                               decode_responses=True)
    nonebot.export().redis_client = redis_client
    redis_opened = True


@driver.on_startup
async def connect_to_redis():
    if config.redis_host:
        ret = redis_client.ping()
        if ret:
            nonebot.logger.info("connect to redis")


@driver.on_shutdown
async def free_db():
    global redis_opened
    if redis_opened:
        redis_client.close()
        redis_opened = False
        nonebot.logger.info("disconnect to redis")
