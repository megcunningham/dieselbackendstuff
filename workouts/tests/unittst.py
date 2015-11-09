import unittest


class TestBasic(unittest.TestCase):
    "Basic Test"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


class TestBasic2(unittest.TestCase):
    "Show setup and Teardown"

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"
        self.assertNotEqual(self.a, 2)

    def testP_basic2(self):
        "Basic2 with setup"
        assert self.a !=2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2