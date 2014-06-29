#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Now for test multiprocess logging

concurrency = 100

from requests import Request, Session
from multiprocessing import Process, Event

def sendRequest(session, preppedRequest, event):
	event.wait()
	resp = s.send(preppedRequest,
		timeout=1
		)
	print resp.status_code

if __name__ == '__main__':
	url = 'http://127.0.0.1:9090/register'
	req = Request('GET', url)

	prepped = req.prepare()

	processes = []
	event = Event()
	for i in xrange(0, concurrency):
		s = Session()
		p = Process(target=sendRequest, args=(s, prepped, event))
		processes.append(p)
		p.start()

	event.set()
	for p in processes:
		p.join()
