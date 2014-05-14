#!/usr/bin/python
# Test the replace   (usage:  tests.py)

from replace import *
import unittest

class TestReplacer(unittest.TestCase):

    def test_replacement (self):
        write_file ('f1', [ 'this is some sample text' ])
        replace_text('f1', 'f2', 'this','that')
        self.assertEqual(read_file ('f2'), ['that is some sample text'])
        
    def test_no_replacement (self):
        write_file ('f1', [ 'this is some sample text' ])
        replace_text('f1', 'f2', 'this','that')
        self.assertNotEqual(read_file ('f2'), ['this is some sample text'])
    

if __name__ == '__main__':
    unittest.main()
