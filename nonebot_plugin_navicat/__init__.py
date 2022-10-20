# -*- coding: utf-8 -*-
from . import elasticsearch, mongodb, mysql, postgre, redis, sqlite

if hasattr(elasticsearch, "elasticsearch"):
    elasticsearch = elasticsearch.elasticsearch
if hasattr(mongodb, "mongodb_client"):
    mongodb_client = mongodb.mongodb_client
if hasattr(mysql, "mysql_pool"):
    mysql_pool = mysql.mysql_pool
if hasattr(postgre, "pgsql_pool"):
    pgsql_pool = postgre.pgsql_pool
if hasattr(redis, "redis_client"):
    redis_client = redis.redis_client
if hasattr(redis, "redis_sentinel"):
    redis_sentinel = redis.redis_sentinel
if hasattr(redis, "redis_cluster"):
    redis_cluster = redis.redis_cluster
if hasattr(sqlite, "sqlite_pool"):
    sqlite_pool = sqlite.sqlite_pool
