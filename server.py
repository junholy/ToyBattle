#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apis import *

def getRedisConn():
	try:
		redisObj = StrictRedis()
		redisObj.ping()
	except:
		return None
	else:
		return redisObj	

redisObj = getRedisConn()
if redisObj is None:
	raise

def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	# try:
	return eval(env['REQUEST_URI'][1:])(redisObj=redisObj)
	# except:
	# 	return ["Hello World"]