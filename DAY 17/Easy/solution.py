class Solution:
    def generate_binary_string(self, s):
        result = []

        def backtrack(index, current):
            if index == len(s):
                result.append(current)
                return
            if s[index] == '?':
                backtrack(index + 1, current + '0')
                backtrack(index + 1, current + '1')
            else:
                backtrack(index + 1, current + s[index])

        backtrack(0, "")
        return sorted(result)

