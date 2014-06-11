#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crud import *

def register(redisObj, *args):
	done = createUser(redisObj)
	if done is None:
		return "FAIL"
	return "SUCCESS"