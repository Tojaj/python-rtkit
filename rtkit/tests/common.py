from multiprocessing import Process
from bottle import run
import time
from rtkit.utils import unittest


class TestCaseWithBottle(unittest.TestCase):
    application = NotImplemented

    @classmethod
    def setUpClass(cls):
        cls.server = Process(target=run, args=(cls.application,), kwargs={'port': 5000})
        cls.server.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.join()
