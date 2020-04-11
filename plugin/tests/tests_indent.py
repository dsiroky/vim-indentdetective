import unittest
import indentdetective as idet

#==========================================================================

class TestIndentDetection(unittest.TestCase):
    def test_unknown_indent(self):
        self.assertEqual(idet.decide((0, 0)), idet.USE_UNKNOWN)
        self.assertEqual(idet.decide((9, 0)), idet.USE_UNKNOWN)
        self.assertEqual(idet.decide((0, 9)), idet.USE_UNKNOWN)
        self.assertEqual(idet.decide((9, 2)), idet.USE_UNKNOWN)
        self.assertEqual(idet.decide((2, 9)), idet.USE_UNKNOWN)

        self.assertEqual(idet.decide((300, 500)), idet.USE_UNKNOWN)
        self.assertEqual(idet.decide((600, 400)), idet.USE_UNKNOWN)

    def test_known_indent(self):
        self.assertEqual(idet.decide((60, 0)), idet.USE_TABS)
        self.assertEqual(idet.decide((60, 4)), idet.USE_TABS)
        self.assertEqual(idet.decide((0, 40)), idet.USE_SPACES)
        self.assertEqual(idet.decide((5, 40)), idet.USE_SPACES)
