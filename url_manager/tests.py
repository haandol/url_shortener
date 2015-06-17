#coding: utf-8

import unittest
from BeautifulSoup import BeautifulSoup as Soup
from django.test.client import Client
from urlparse import urljoin
from views import *

class ShortURLTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.long_url = 'http://north.santa.org'

    def test_get_short_url(self):
        longUrl = LongURL.objects.create(url=self.long_url)
        short_url = get_short_url(longUrl)
        self.assertEquals(urljoin(BASEURL, '1'), short_url) 

    def test_get_long_url(self):
        pass

    def test_encode_basen(self):
       encoded = encode_basen(18)
       self.assertEquals('h', encoded)

       encoded = encode_basen(1024)
       self.assertEquals('ff', encoded)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
