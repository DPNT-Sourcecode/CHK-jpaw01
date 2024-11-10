import unittest
from typing import List

# noinspection PyUnusedLocal
# skus = unicode string


prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 70,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 20,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 17,
    "Y": 20,
    "Z": 21,
}

offers = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(10, 80), (5, 45)],
    "K": [(2, 120)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(3, 130), (2, 90)],
}

free_items_offer = {
    "E": [(2, "B")],
    "F": [(3, "F")],
    "N": [(3, "M")],
    "R": [(3, "Q")],
    "U": [(4, "U")],
}

group_discount = ["Z", "S", "T", "Y", "X"]


def apply_special_offer(skus: List[str]) -> List[str]:
    spl_offer_count = 0
    spl_items = []
    for i in group_discount:
        if i in skus:
            spl_items.extend([i] * skus.count(i))
            


def remove_free_items(skus: List[str]) -> List[str]:
    free_items = []
    for free_item in free_items_offer.keys():
        if free_item in skus:
            c = skus.count(free_item)
            free_item_threshold = free_items_offer[free_item][0][0]
            free_item_qty = c // free_item_threshold
            free_items.extend([free_items_offer[free_item][0][1]] * free_item_qty)

    free_items = sorted(free_items)
    for fi in free_items:
        if fi in skus:
            i = skus.index(fi)
            skus[i] = ""

    return sorted([x for x in skus if x != ""])


def checkout(skus):
    items = []
    if "," in skus:
        items = skus.split(",")
    else:
        items = list(skus)

    items = sorted(items)
    if len(items) == 0:
        return 0

    items = remove_free_items(items)

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
                offer_counts = offers[last_item]
                for oc in offer_counts:
                    offer_count = oc[0]
                    offer_price = oc[1]
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
        offer_counts = offers[last_item]
        for oc in offer_counts:
            offer_count = oc[0]
            offer_price = oc[1]
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
            {"input": "HHHHHHHHHH", "expected_output": 80},
            {"input": "HHHHHHHHHHH", "expected_output": 90},
            {"input": "HHHHHHHHHHHH", "expected_output": 100},
            {"input": "FF", "expected_output": 20},
            {"input": "FFFAAA", "expected_output": 150},
            {"input": "FFF", "expected_output": 20},
            {"input": "EEBEEB", "expected_output": 160},
            {"input": "BEEAAA", "expected_output": 210},
            {"input": "AAAAAAAA", "expected_output": 330},
            {"input": "EEB", "expected_output": 80},
            {"input": "AAAAAAA", "expected_output": 300},
            {"input": "AAABB", "expected_output": 175},
            {"input": "AAA", "expected_output": 130},
            {"input": "ABCa", "expected_output": -1},
        ]
        for test_case in test_cases:
            inp = test_case["input"]
            expected = test_case["expected_output"]
            err_msg = f"Output should be {expected}, for input {inp}"
            out = checkout(inp)
            self.assertEqual(expected, out, err_msg)


if __name__ == '__main__':
    unittest.main()

