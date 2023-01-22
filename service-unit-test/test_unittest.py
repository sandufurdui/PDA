import unittest
import profanity
import wall
import gateway.gateway as gateway
import cache
from test__data import *

class Test_Lab(unittest.TestCase):
    def test_censore(self):
        self.assertEqual(profanity.censore("dsasdgdsfgdfs fuck"), "dsasdgdsfgdfs ****")
        self.assertEqual(profanity.censore("dsasd fuck gdsfgdfs"), "dsasd **** gdsfgdfs")

    def test_profanity(self):
        self.assertEqual(profanity.profanity(to_test_profanity), resp_profanity)

    def test_cache(self):
        self.assertEqual(cache.cache(to_test_cache), resp_cache)
    
    def test_wall(self):
        self.assertEqual(wall.wall_root(to_test_wall), resp_wall)
    
    def test_gateway(self):
        self.assertEqual(gateway.gateway(to_test_gateway), resp_gateway)
        self.assertEqual(gateway.gateway(to_test_gateway), resp_gateway1)
    
    def test_gateway_prof(self):
        self.assertEqual(gateway.prof_port(to_test_gateway_prof), resp_gateway_prof)
    
    def test_gateway_wall(self):
        self.assertEqual(gateway.wall_port(to_test_gateway_wall), resp_gateway_wall)

if __name__ == '__main__':
    unittest.main()
