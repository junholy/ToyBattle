#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis import *

initialStat = {'attack': 50, 'defence': 50}

def createUser(redisObj):
	try:
		userCount = redisObj.incr('userCount', 1)
		userId = 'user{idx}'.format(idx=userCount)
		redisObj.hmset(userId, initialStat)
	except ResponseError:
		return None
	return not None

def incStat(redisObj, userId):
	try:
		stat = redisObj.hgetall(userId)
		stat['attack'] = int(stat['attack']) + 1
		stat['defence'] = int(stat['defence']) + 1
		redisObj.hmset(userId, stat)
	except ResponseError:
		return None
	except:
		return None
	return not None