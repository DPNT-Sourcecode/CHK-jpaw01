import unittest

# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}

offers = {
    "A": {
        3: 130
    },
    "B": {
        2: 45
    }
}


def checkout(skus):
    items = []
    if "," in skus:
        items = skus.split(",")
    else:
        items = list(skus)

    items = [c for c in items]


class TestSolution(unittest.TestCase):

    def test_1(self):
        test_cases = [
            {"input": "AAB", "expected_output": -1},
        ]
        for test_case in test_cases:
            inp = test_case["input"]
            expected = test_case["expected_output"]
            err_msg = f"Output should be {expected}, for input {inp}"
            out = checkout(inp)
            self.assertEqual(expected, out, err_msg)


if __name__ == '__main__':
    unittest.main()

