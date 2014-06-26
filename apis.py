#!/usr/bin/env python
# -*- coding: utf-8 -*-

#WEB APIs open to out

from crud import *
import json
import logging

class ErrorCode(object):
	success = 0
	fail = 1

e = ErrorCode()


def register(redisConn, **kwargs):
	userId = createUser(redisConn)
	logging.debug('user created. userId: {userId}'.format(userId=userId))
	if userId is None:
		return e.fail
	return {
		'error': e.success,
		'result': {
			'userId': userId,
		},
	}

def train(redisConn, **kwargs):
	userId = kwargs.get('id', None)
	if userId is None:
		return None
	stat = incStat(redisConn, userId)
	logging.debug('trained. userId: {userId}, stat: {stat}'.format(
		userId=userId, stat=stat))
	if stat is None:
		return e.fail
	return dict(
		error=e.success,
		result=dict(
			stat=stat
		)
	)