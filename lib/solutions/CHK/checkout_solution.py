

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()


class TestSolution(unittest.TestCase):
    obj = Solution()

    def test_1(self):
        test_cases = [
            {"input": ([1], 9), "expected_output": -1},
        ]
        for test_case in test_cases:
            inp = test_case["input"]
            expected = test_case["expected_output"]
            err_msg = f"Output should be {expected}, for input {inp}"
            out = self.obj.minimumSubarrayLength(*inp)
            self.assertEqual(expected, out, err_msg)


if __name__ == '__main__':
    unittest.main()
