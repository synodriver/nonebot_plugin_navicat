# -*- coding: utf-8 -*-
"""
对外导出redis连接
"""
import nonebot

try:
    import redis
    from redis.sentinel import Sentinel
except ImportError:
    redis = None

try:
    import rediscluster
except ImportError:
    rediscluster = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

redis_opened: bool = False

if redis and getattr(config, "redis_host", None):
    redis_params = getattr(config, "redis_params", None) or {}
    redis_params.update(host=config.redis_host,
                        port=getattr(config, "redis_port", 6379),
                        db=getattr(config, "redis_db", 0),
                        password=getattr(config, "redis_password", None))
    redis_client = redis.Redis(**redis_params)
    nonebot.export().redis_client = redis_client
    redis_opened = True


@driver.on_startup
async def connect_to_redis():
    if getattr(config, "redis_host", None):
        ret = redis_client.ping()
        if ret:
            nonebot.logger.opt(colors=True).info("<y>Connect to Redis</y>")


@driver.on_shutdown
async def free_db():
    global redis_opened
    if redis_opened:
        redis_client.close()
        redis_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Redis</y>")


# ----------------sentinel-----------------

redis_sentinel_opened: bool = False

if redis and getattr(config, "redis_sentinel_params", None):
    redis_sentinel_params = config.redis_sentinel_params
    sentinel = Sentinel(**redis_sentinel_params)
    nonebot.export().redis_sentinel = sentinel
    redis_sentinel_opened = True


@driver.on_startup
async def connect_to_redis_sentinel():
    if getattr(config, "redis_sentinel_params", None):
        master = sentinel.master_for(config.redis_sentinel_service_name)
        slave = sentinel.slave_for(config.redis_sentinel_service_name)
        if master.ping() and slave.ping():
            nonebot.logger.opt(colors=True).info("<y>Connect to Redis Sentinel</y>")


@driver.on_shutdown
async def free_redis_sentinel():
    global redis_sentinel_opened
    if redis_sentinel_opened:
        master = sentinel.master_for(config.redis_sentinel_service_name)
        slave = sentinel.slave_for(config.redis_sentinel_service_name)
        master.close()
        slave.close()
        redis_sentinel_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Redis Sentinel</y>")


# -----------------------cluster----------------

redis_cluster_opened: bool = False

if rediscluster and getattr(config, "redis_cluster_params", None):
    redis_cluster_params = config.redis_cluster_params
    cluster = rediscluster.RedisCluster(**redis_cluster_params)
    nonebot.export().redis_cluster = cluster
    redis_cluster_opened = True


@driver.on_startup
async def connect_to_redis_cluster():
    if getattr(config, "redis_cluster_params", None):
        if cluster.ping():
            nonebot.logger.opt(colors=True).opt(colors=True).info("<y>Connect to Redis Cluster</y>")


@driver.on_shutdown
async def free_redis_cluster():
    global redis_cluster_opened
    if redis_cluster_opened:
        cluster.close()
        redis_cluster_opened = False
        nonebot.logger.opt(colors=True).opt(colors=True).info("<y>Disconnect to Redis Cluster</y>")
