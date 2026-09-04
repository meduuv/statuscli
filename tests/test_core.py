import unittest
from statuscli import summarize
class Tests(unittest.TestCase):
 def test_summary(self): self.assertEqual(summarize([{"status":"ok"},{"status":"ok"},{"status":"down"}]),{"down":1,"ok":2})
if __name__=="__main__":unittest.main()
