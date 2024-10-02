import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('setup....')
        super().setUp()

    def tearDown(self) -> None:
        print('teardown...')
        super().tearDown()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class MyTestCase2(unittest.TestCase):

    def setUp(self) -> None:
        print('setup....')
        super().setUp()

    def tearDown(self) -> None:
        print('teardown...')
        super().tearDown()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(MyTestCase))
    suite.addTest(loader.loadTestsFromTestCase(MyTestCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)
