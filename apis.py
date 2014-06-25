#!/usr/bin/env python
# -*- coding: utf-8 -*-

#WEB APIs open to out

from crud import *
import json

def register(redisConn, **kwargs):
	userId = createUser(redisConn)
	if userId is None:
		return "FAIL"
	return {
		'error': 'SUCCESS',
		'result': {
			'userId': userId,
		},
	}

def train(redisConn, **kwargs):
	userId = kwargs.get('id', None)
	if userId is None:
		return None
	done = incStat(redisConn, userId)
	if done is None:
		return "FAIL"
	return "SUCCESS"