from apis import *
import unittest
from server import getRedisConn
from crud import initialStat

class TestApiFunctions(unittest.TestCase):
	
	def setUp(self):
		self.redisConn = getRedisConn()
		if self.redisConn is None:
			self.fail("Redis-server is not running.")

	def test_register(self):
		stat = {
			'attack': '50', 
			'defence': '50', 
			'stamina': '50',
			'power': '50',
			'speed': '50',
			'technique': '50',
		}
		rtn = register(self.redisConn)
		self.assertEqual(rtn['error'], 'SUCCESS')
		self.assertIn('userId', rtn['result'].keys())
		userId = rtn['result']['userId']
		self.assertEqual(self.redisConn.hgetall(userId), stat)

	def test_train(self):
		#TODO
		pass

if __name__ == '__main__':
	unittest.main()