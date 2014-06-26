#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Process requests and send their responses.

from apis import *
import json
import logging
import os

loglevel = logging.DEBUG

def getRedisConn():
	try:
		redisConn = StrictRedis()
		redisConn.ping()
	except:
		return None
	else:
		return redisConn	

def configureLogging():
	try:
		os.mkdir('log')
	except:
		pass
	logging.basicConfig(filename='log/server.log', format='%(asctime)s | %(message)s', level=loglevel)

redisConn = getRedisConn()
if redisConn is None:
	raise

configureLogging()

def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	kwargs = {}
	try:
	#ex) env['REQUEST_URI'] = '/train?id=user1'
		parsedURIs = env['REQUEST_URI'].split('?')
		apiName = parsedURIs[0][1:]
		if len(parsedURIs) > 1:
			argsString = parsedURIs[1]
			#ex) argsString = 'id=user1'
			argKey, argValue = argsString.split('=')
			kwargs[argKey] = argValue
			print 'S1'
			logging.info('Success to parse a request. api: {apiName}, args: \
				{args}').format(apiName=apiName, args=kwargs)
		else:
			logging.info('Success to parse a request. api: {apiName}'.format(
				apiName=apiName))
		apiFnName = apiName
		rtn = eval(apiFnName)(redisConn=redisConn, **kwargs)
	except:
		return "Wrong API"
	return json.dumps(rtn)
