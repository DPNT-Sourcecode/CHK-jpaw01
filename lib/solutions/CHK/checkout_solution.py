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
    "A": [(3, 130)],
    "B": [(2, 45)]
}


def checkout(skus):
    items = []
    if "," in skus:
        items = skus.split(",")
    else:
        items = list(skus)

    items = sorted([c.capitalize() for c in items])
    if len(items) == 0:
        return 0

    total = 0
    last_item = items[0]
    item_count = 0
    idx = 0

    while idx < len(items):
        item = items[idx]
        if item not in prices:
            return -1

        if last_item == item:
            item_count += 1
        else:
            if last_item in offers:
                offer_count = offers[last_item][0][0]
                offer_price = offers[last_item][0][1]

                while item_count >= offer_count:
                    total += offer_price
                    item_count -= offer_count
                total += item_count * prices[last_item]
            else:
                total += item_count * prices[last_item]
                item_count = 0

            item_count = 1
            last_item = item
        idx += 1

    if last_item in offers:
        offer_count = offers[last_item][0][0]
        offer_price = offers[last_item][0][1]

        while item_count >= offer_count:
            total += offer_price
            item_count -= offer_count
        total += item_count * prices[last_item]
    else:
        total += item_count * prices[last_item]

    return total


class TestSolution(unittest.TestCase):

    def test_1(self):
        test_cases = [
            {"input": "AAAAAAA", "expected_output": 310},
            {"input": "AAABB", "expected_output": 175},
            {"input": "AAA", "expected_output": 130},
            {"input": "A,a,B", "expected_output": 130},
            {"input": "A,a,x", "expected_output": -1},
        ]
        for test_case in test_cases:
            inp = test_case["input"]
            expected = test_case["expected_output"]
            err_msg = f"Output should be {expected}, for input {inp}"
            out = checkout(inp)
            self.assertEqual(expected, out, err_msg)


if __name__ == '__main__':
    unittest.main()

