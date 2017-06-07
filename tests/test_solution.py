from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        thelist = [10, 20, 30]
        res = solution(thelist)
        ans = [[], [10], [20], [30], [10, 30], [10, 20], [20, 30], [10, 20, 30]]
        self.assertEqual(8, len(res))
        self.assertItemsEqual(res, ans)
