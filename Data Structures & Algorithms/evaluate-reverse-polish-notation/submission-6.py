class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for char in tokens:
            try:
                int(char)
                stack.append(char)
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == "+":
                    res = int(num1) + int(num2)
                if char == "-":
                    res = int(num1) - int(num2)
                if char == "*":
                    res = int(num1) * int(num2)
                if char == "/":
                    res = int(num1) / int(num2)
                stack.append(int(res))

        
        return int(str(stack.pop()))

        