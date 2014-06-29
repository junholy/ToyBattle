from apis import *
import unittest
from server import getRedisConn
from crud import initialStat

class TestApiFunctions(unittest.TestCase):
	
	def setUp(self):
		self.redisConn = getRedisConn()
		if self.redisConn is None:
			self.fail("Redis-server is not running.")

	def test_api_register(self):
		stat = {
			'attack': '50', 
			'defence': '50', 
			'stamina': '50',
			'power': '50',
			'speed': '50',
			'technique': '50',
		}
		rtn = register(self.redisConn)
		self.assertEqual(rtn['error'], 0)
		self.assertIn('userId', rtn['result'].keys())
		userId = rtn['result']['userId']
		self.assertEqual(self.redisConn.hgetall(userId), stat)

	def test_api_train(self):
		stat = {
			'attack': '51', 
			'defence': '51', 
			'stamina': '51',
			'power': '51',
			'speed': '51',
			'technique': '51',
		}
		userId = register(self.redisConn)['result']['userId']
		rtn = train(self.redisConn, id=userId)
		self.assertEqual(rtn['error'], 0)
		self.assertEqual(rtn['result']['stat'], stat)

if __name__ == '__main__':
	unittest.main()