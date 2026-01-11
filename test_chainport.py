# test_chainport.py
"""
Tests for ChainPort module.
"""

import unittest
from chainport import ChainPort

class TestChainPort(unittest.TestCase):
    """Test cases for ChainPort class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainPort()
        self.assertIsInstance(instance, ChainPort)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainPort()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
