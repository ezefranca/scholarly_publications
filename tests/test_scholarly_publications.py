import unittest
from scholarly_publications.fetcher import fetch_all_publications

class TestScholarlyPublications(unittest.TestCase):
    
    def test_fetch_publications_limit(self):
        """Test fetching a limited number of publications."""
        author_id = '6nOPl94AAAAJ'  # Example Google Scholar ID
        max_publications = 1
        publications = fetch_all_publications(author_id, max_publications)
        
        # Assert that the number of publications returned matches the limit
        self.assertEqual(len(publications), max_publications)

if __name__ == '__main__':
    unittest.main()