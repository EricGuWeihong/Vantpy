#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from test.common.BrowserDriver import BrowserDriver
from utils.config import Config
class model(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c = Config()
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)


    def setUp(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()