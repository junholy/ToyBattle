#!/usr/bin/env python
# -*- coding: utf-8 -*-

#CRUD operations to DB.

from redis import *

initialStat = {
	'attack': 50, 
	'defence': 50, 
	'stamina': 50,
	'power': 50,
	'speed': 50,
	'technique': 50,
}

def createUser(redisConn):
	try:
		userCount = redisConn.incr('userCount', 1)
		userId = 'user{idx}'.format(idx=userCount)
		redisConn.hmset(userId, initialStat)
	except ResponseError:
		return None
	return userId

def incStat(redisConn, userId):
	try:
		stat = redisConn.hgetall(userId)
		stat['attack'] = int(stat['attack']) + 1
		stat['defence'] = int(stat['defence']) + 1
		stat['stamina'] = int(stat['stamina']) + 1
		stat['power'] = int(stat['power']) + 1
		stat['speed'] = int(stat['speed']) + 1
		stat['technique'] = int(stat['technique']) + 1
		redisConn.hmset(userId, stat)
	except ResponseError:
		return None
	except:
		return None
	return not None