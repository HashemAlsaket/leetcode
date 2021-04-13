# Link to video: https://youtu.be/eV9AHqXULoE

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N in [1, 2]:
            return 1
        
        two = [1, 1]
        
        def rec(N):
            if N == 2:
                return
            
            two.append(sum(two))
            two.pop(0)
            rec(N - 1)
        
        rec(N)
        
        return two[-1]