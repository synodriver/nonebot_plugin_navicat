# -*- coding: utf-8 -*-
import asyncio

import nonebot
from nonebot.adapters.cqhttp import Bot

nonebot.init(_env_file=r".env")
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", Bot)
nonebot.load_plugin("nonebot_plugin_navicat")

app = nonebot.get_app()

if __name__ == "__main__":
    try:
        nonebot.run()
    finally:
        print("over")
    #
# netstat -aon|findstr "8080"
