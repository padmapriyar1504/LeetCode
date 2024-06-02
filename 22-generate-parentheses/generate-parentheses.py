from collections import deque

class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []

        queue = deque([("", 0, 0)])  
        result = []

        while queue:
            string, open_count, closed_count = queue.popleft()

            if open_count == closed_count == n:
                result.append(string)
                continue

            if open_count < n:
                queue.append((string + "(", open_count + 1, closed_count))

            if closed_count < open_count:
                queue.append((string + ")", open_count, closed_count + 1))

        return result


