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

if redis and config.redis_host:
    redis_params = config.redis_params or {}
    redis_params.update(host=config.redis_host,
                        port=config.redis_port,
                        db=config.redis_db,
                        password=config.redis_password)
    redis_client = redis.Redis(**redis_params)
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


# ----------------sentinel-----------------

redis_sentinel_opened: bool = False

if redis and config.redis_sentinel_sentinels:
    redis_sentinel_params = config.redis_sentinel_params or {}
    redis_sentinel_params.update(sentinels=config.redis_sentinel_sentinels)
    sentinel = Sentinel(**redis_sentinel_params)
    nonebot.export().redis_sentinel = sentinel
    redis_sentinel_opened = True


@driver.on_startup
async def connect_to_redis_sentinel():
    if config.redis_sentinel_sentinels:
        master = sentinel.master_for(config.redis_sentinel_service_name)
        slave = sentinel.slave_for(config.redis_sentinel_service_name)
        if master.ping() and slave.ping():
            nonebot.logger.info("connect to redis sentinel")


@driver.on_shutdown
async def free_redis_sentinel():
    global redis_sentinel_opened
    if redis_sentinel_opened:
        master = sentinel.master_for(config.redis_sentinel_service_name)
        slave = sentinel.slave_for(config.redis_sentinel_service_name)
        master.close()
        slave.close()
        redis_sentinel_opened = False
        nonebot.logger.info("disconnect to redis sentinel")


# -----------------------cluster----------------

redis_cluster_opened: bool = False

if rediscluster and config.redis_cluster_nodes:
    redis_cluster_params = config.redis_cluster_params or {}
    redis_cluster_params.update(
        startup_nodes=config.redis_cluster_nodes
    )
    cluster = rediscluster.RedisCluster(**redis_cluster_params)
    nonebot.export().redis_cluster = cluster
    redis_cluster_opened = True


@driver.on_startup
async def connect_to_redis_cluster():
    if config.redis_cluster_nodes:
        if cluster.ping():
            nonebot.logger.info("connect to redis cluster")


@driver.on_shutdown
async def free_redis_cluster():
    global redis_cluster_opened
    if redis_cluster_opened:
        cluster.close()
        redis_cluster_opened = False
        nonebot.logger.info("disconnect to redis cluster")
