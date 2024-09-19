class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def compute(left, right, operator):
            results = []
            for l in left:
                for r in right:
                    if operator == '+':
                        results.append(l + r)
                    elif operator == '-':
                        results.append(l - r)
                    elif operator == '*':
                        results.append(l * r)
            return results

        def ways(expr):
            # If it's a number, return it as a single-element list
            if expr.isdigit():
                return [int(expr)]
            
            res = []
            # Traverse through the expression
            for i in range(len(expr)):
                if expr[i] in "+-*":
                    # Split the expression at operator
                    left = ways(expr[:i])
                    right = ways(expr[i + 1:])
                    # Combine the results from left and right using the current operator
                    res.extend(compute(left, right, expr[i]))
            
            return res
        
        return ways(expression)