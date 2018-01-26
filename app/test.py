#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ZXM'

import orm
from models import User, Blog, Comment
import asyncio

loop = asyncio.get_event_loop()


async def test():
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='myblog')

    u = User(name='Test', email='tessts@example.com', password='1234567890s', image='about:blank')

    await u.save()


loop.run_until_complete(test())
