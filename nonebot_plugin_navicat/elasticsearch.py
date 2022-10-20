# -*- coding: utf-8 -*-
import nonebot

try:
    from elasticsearch import AsyncElasticsearch
except ImportError:
    AsyncElasticsearch = None

driver: nonebot.Driver = nonebot.get_driver()
config: nonebot.config.Config = driver.config

elasticsearch_opened: bool = False

if AsyncElasticsearch and getattr(config, "elasticsearch_hosts", None):
    elasticsearch_params = getattr(config, "elasticsearch_params", None) or {}
    elasticsearch_params.update(hosts=getattr(config, "elasticsearch_hosts", None))
    elasticsearch = AsyncElasticsearch(**elasticsearch_params)
    # nonebot.export().elasticsearch = elasticsearch
    elasticsearch_opened = True


@driver.on_startup
async def connect_to_elasticsearch():
    if getattr(config, "elasticsearch_hosts", None):
        if await elasticsearch.ping():
            nonebot.logger.opt(colors=True).info("<y>Connect to Elasticsearch</y>")


@driver.on_shutdown
async def free_elasticsearch():
    global elasticsearch_opened
    if elasticsearch_opened:
        await elasticsearch.close()
        elasticsearch_opened = False
        nonebot.logger.opt(colors=True).info("<y>Disconnect to Elasticsearch</y>")
