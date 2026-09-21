class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, target, current):
            if target == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue

                current.append(candidates[i])

                # Use i again because the same number can be reused
                backtrack(i, target - candidates[i], current)

                current.pop()

        backtrack(0, target, [])
        return result
        