class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                stack.append(int(i))
            else: 
                n = stack.pop()
                m = stack.pop()
                if i == '+':
                    result = m + n
                elif i == '-':
                    result = m - n
                elif i == '*':
                    result = m * n
                elif i == '/':
                    result = int(m / n)
                stack.append(result)
        return stack[-1]
