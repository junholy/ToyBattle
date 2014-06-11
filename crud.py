#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis import *

def createUser(redisObj):
	rtn = redisObj.hmset('user1', {'attack': 90, 'defence': 85})
	if not rtn:
		return None
	return not None
