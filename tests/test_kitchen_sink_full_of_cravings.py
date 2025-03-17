from unittest import TestCase
from kitchen_sink_full_of_cravings import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello from kitchen_sink_full_of_cravings!", hello())
