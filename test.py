import unittest
import Validation


class test(unittest.TestCase):
    def test1(self):
        result = Validation.validInputs("x+2", "10", "20")
        self.assertEqual(result, "true")

    def test2(self):
        result = Validation.validInputs("not function", "10", "20")
        self.assertNotEqual(result, "true")

    def test3(self):
        result = Validation.validInputs("x+2+4x^2", "", "20")
        self.assertNotEqual(result, "true")

    def test4(self):
        result = Validation.validInputs("x+2+4x^2", "", "")
        self.assertNotEqual(result, "true")

    def test5(self):
        result = Validation.validInputs("x+2+4x^2", "21", "5")
        self.assertNotEqual(result, "true")

    def test6(self):
        result = Validation.validInputs("x+2+4x^2", "21", "200")
        self.assertEqual(result, "true")

    def test7(self):
        result = Validation.validInputs("", "21", "200")
        self.assertNotEqual(result, "true")

    def test8(self):
        result = Validation.validInputs("", "201", "200")
        self.assertNotEqual(result, "true")

    def test9(self):
        result = Validation.validInputs("2*x+x^2", "-201", "-3")
        self.assertEqual(result, "true")

    def test10(self):
        result = Validation.validInputs("2*x+x^2", "-201", "-202")
        self.assertNotEqual(result, "true")

    def test11(self):
        result = Validation.validInputs("2*X+x^2+", "-203", "-202")
        self.assertNotEqual(result, "true")


if __name__ == '__main__':
    unittest.main()
