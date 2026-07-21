class Solution:
    def addOperators(self, num: str, target: int):
        
        ans = []
        n = len(num)
        
        def backtrack(index, expr, value, prev):
            
            # Reached end of string
            if index == n:
                if value == target:
                    ans.append(expr)
                return
            
            for i in range(index, n):
                
                # Avoid numbers with leading zeros
                if i > index and num[index] == '0':
                    break
                
                # Current number
                curr_str = num[index:i+1]
                curr = int(curr_str)
                
                # First number (no operator before it)
                if index == 0:
                    backtrack(
                        i + 1,
                        curr_str,
                        curr,
                        curr
                    )
                
                else:
                    # Addition
                    backtrack(
                        i + 1,
                        expr + "+" + curr_str,
                        value + curr,
                        curr
                    )
                    
                    # Subtraction
                    backtrack(
                        i + 1,
                        expr + "-" + curr_str,
                        value - curr,
                        -curr
                    )
                    
                    # Multiplication
                    backtrack(
                        i + 1,
                        expr + "*" + curr_str,
                        value - prev + prev * curr,
                        prev * curr
                    )
        
        backtrack(0, "", 0, 0)
        
        return ans