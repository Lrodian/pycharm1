#!/usr/bin/python
# -*- coding: <encoding name> -*-
import redis

redis_store = redis.StrictRedis(host='127.0.0.1',port=6379)

redis_store.set("name","naruto")

name = redis_store.get("name")

name = str(name,'utf-8')

print(name)