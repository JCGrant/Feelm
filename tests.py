import os
import unittest
import tempfile
from app import app


class FeelmTestCase(unittest.TestCase):
    
    def set_up(self):
        app.config['TESTING'] = True
        self.app = app.test_client()


if __name__ == '__main__':
    unittest.main()
