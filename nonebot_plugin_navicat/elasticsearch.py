# -*- coding: utf-8 -*-
import nonebot

try:
    from elasticsearch import AsyncElasticsearch
except ImportError:
    AsyncElasticsearch = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

elasticsearch_opened: bool = False

if AsyncElasticsearch and config.elasticsearch_hosts:
    elasticsearch_params = config.elasticsearch_params or {}
    elasticsearch_params.update(hosts=config.elasticsearch_hosts)
    elasticsearch = AsyncElasticsearch(**elasticsearch_params)
    nonebot.export().elasticsearch = elasticsearch
    elasticsearch_opened = True


@driver.on_startup
async def connect_to_elasticsearch():
    if config.elasticsearch_hosts:
        if await elasticsearch.ping():
            nonebot.logger.opt(colors=True).info("<y>Connect to Elasticsearch</y>")


@driver.on_shutdown
async def free_elasticsearch():
    global elasticsearch_opened
    if elasticsearch_opened:
        await elasticsearch.close()
        elasticsearch_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Elasticsearch</y>")
