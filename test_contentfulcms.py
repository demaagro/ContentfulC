# test_contentfulcms.py
"""
Tests for ContentfulCMS module.
"""

import unittest
from contentfulcms import ContentfulCMS

class TestContentfulCMS(unittest.TestCase):
    """Test cases for ContentfulCMS class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ContentfulCMS()
        self.assertIsInstance(instance, ContentfulCMS)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ContentfulCMS()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
