#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crud import *

def register(redisObj, **kwargs):
	done = createUser(redisObj)
	if done is None:
		return "FAIL"
	return "SUCCESS"

def train(redisObj, **kwargs):
	userId = kwargs.get('id', None)
	if userId is None:
		return None
	done = incStat(redisObj, userId)
	if done is None:
		return "FAIL"
	return "SUCCESS"