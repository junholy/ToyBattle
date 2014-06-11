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
	kwargs = {}
	#ex) env['REQUEST_URI'] = '/train?id=user1'
	parsedURIs = env['REQUEST_URI'].split('?')
	apiName = parsedURIs[0][1:]
	if len(parsedURIs) > 1:
		argsString = parsedURIs[1]
		#ex) argsString = 'id=user1'
		argKey, argValue = argsString.split('=')
		kwargs[argKey] = argValue
	apiFnName = apiName
	return eval(apiFnName)(redisObj=redisObj, **kwargs)
