# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

packages = find_packages(exclude=('test', 'tests.*', "test*"))


def get_dis():
    with open("README.markdown", "r", encoding="utf-8") as f:
        return f.read()


def main():
    dis = get_dis()
    setup(
        name="nonebot-plugin-navicat",
        version="0.2.3",
        url="https://github.com/synodriver/nonebot_plugin_navicat",
        packages=packages,
        keywords=["nonebot"],
        description="A batabase manager plugin for nonebot2,provide capability of connection to all kinds of databases",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="synodriver",
        author_email="diguohuangjiajinweijun@gmail.com",
        python_requires=">=3.7",
        install_requires=["nonebot2", "databases"],
        extras_require={
            "all": ["redis", "redis-py-cluster",
                    "motor",
                    "aiomysql", "asyncpg", "aiosqlite",
                    "elasticsearch", "aiohttp"],
            "mysql": ["aiomysql"],
            "postgresql": ["asyncpg"],
            "sqlite": ["aiosqlite"],
            "mongodb": ["motor"],
            "redis": ["redis", "redis-py-cluster"],
            "elasticsearch": ["elasticsearch", "aiohttp"]
        },
        license="GPLv3",
        classifiers=[
            "Framework :: AsyncIO",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        include_package_data=True
    )


if __name__ == "__main__":
    main()
