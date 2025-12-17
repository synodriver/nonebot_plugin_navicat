# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

packages = find_packages(exclude=("test", "tests.*", "test*"))


def get_dis():
    with open("README.markdown", "r", encoding="utf-8") as f:
        return f.read()


def main():
    dis = get_dis()
    setup(
        name="nonebot-plugin-navicat",
        version="0.4.0",
        url="https://github.com/synodriver/nonebot_plugin_navicat",
        packages=packages,
        keywords=["nonebot"],
        description="A batabase manager plugin for nonebot2,provide capability of connection to all kinds of databases",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="synodriver",
        author_email="diguohuangjiajinweijun@gmail.com",
        python_requires=">=3.7",
        install_requires=["nonebot2", "databases>=0.9.0"],
        extras_require={
            "all": [
                "redis>=5.0",
                "pymongo>=4.15.5",
                "aiomysql",
                "asyncpg",
                "aiosqlite",
                "elasticsearch",
                "aiohttp",
            ],
            "mysql": ["aiomysql"],
            "postgresql": ["asyncpg"],
            "sqlite": ["aiosqlite"],
            "mongodb": ["pymongo>=4.15.5"],
            "redis": ["redis>=5.0"],
            "elasticsearch": ["elasticsearch", "aiohttp"],
        },
        license="GPLv3",
        classifiers=[
            "Framework :: AsyncIO",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
        include_package_data=True,
    )


if __name__ == "__main__":
    main()
