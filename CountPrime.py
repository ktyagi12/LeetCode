#Problem available at: https://leetcode.com/problems/count-primes/submissions/
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True]*n
        if n<2:
            return 0
        else:
            prime[1] = prime[0] = False
            
            for i in range(2,n):
                
                if prime[i] is not False:
                    prime[i] = True
                
                for j in range(i*i,n,i):
                    prime[j] = False
        
        return sum(prime)



#=================================================


class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n<3:
            return 0
        
        prime = [1] * n
        prime[1] = prime[0] = 0

        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                prime[i*i:n:i] = [0]* len(prime[i*i:n:i])

        return sum(prime)        