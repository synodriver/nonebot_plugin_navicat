# -*- coding: utf-8 -*-
"""
以命令行执行sql查询


import json
import traceback

import nonebot
from nonebot import on_command, require
from nonebot.adapters.onebot.v11 import Bot, Event, Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.rule import Rule

config: nonebot.config.Config = nonebot.get_driver().config
require("nonebot_plugin_navicat")
import nonebot_plugin_navicat as export


@Rule
async def config_checker() -> bool:
    return getattr(config, "navicat_execute_sql", False)


sql = on_command("super", rule=config_checker)


@sql.handle()
async def handle_sql(bot: Bot, event: MessageEvent, data: Message = CommandArg()):
    if event.user_id not in config.superusers:
        return
    if event.message:
        db_type, sql_ = str(data[0]).strip().split("\r\n")  # mysql   show databases
        pool_name = db_type + "_pool"  # mysql_pool pgsql_pool
        try:
            rows = await getattr(export, pool_name).fetch_all(sql_)
            rows = list(map(list, rows))
            await bot.send(event, json.dumps(rows, ensure_ascii=False))
        except Exception:
            await bot.send(event, traceback.format_exc())
"""