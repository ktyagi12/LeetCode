#Problem available at: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/
class Solution:
    def sumZero(self, n: int) -> List[int]:
        L = []
        if not n or n == 0:
            return []
        
        elif n == 1:
            return [0]
        
        else:
            if n%2 == 0:
                for i in range(1,n):
                    L.append(i)
                    L.append(int('-'+ str(i)))

                    l = len(L)
                    if l >= n:
                        break
                print(L)
            else:
                L.append(0)
                for i in range(1,n):
                    L.append(i)
                    L.append(int('-'+ str(i)))

                    l = len(L)
                    if l >= n:
                        break
                print(L)

        return L