#Problem available at: https://leetcode.com/problems/add-two-numbers-ii/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_list = []
        l2_list = []
        
        while(l1):
            l1_list.append(l1.val)
            l1 = l1.next
        
        while(l2):
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_list = l1_list[::-1]
        l2_list = l2_list[::-1]
        
        min_len = len(l1_list) if len(l1_list)<len(l2_list) else len(l2_list)
        carry = 0
        l3_list = []
        i,j =0,0
        while(min_len):
            if((l1_list[i] + l2_list[j] + carry) > 9):
                
                l3_list.append((l1_list[i]+ l2_list[j] + carry) % 10)
                carry = (l1_list[i]+ l2_list[j] + carry) // 10
            
            else:
                l3_list.append(l1_list[i]+ l2_list[j]+carry)
                carry = 0
            i+=1
            j+=1
            min_len -= 1
        
        while(l1_list[i:]):
            
            if (l1_list[i] + carry ) > 9:
                l3_list.append((l1_list[i] + carry) % 10)
                carry = (l1_list[i] + carry ) //10
                i += 1
            
            else:
                l3_list.append(l1_list[i] + carry)
                carry = (l1_list[i] + carry ) //10
                i += 1
                
        while(l2_list[j:]):
            
            if (l2_list[j] + carry ) > 9:
                l3_list.append((l2_list[j] + carry) % 10)
                carry = (l2_list[j] + carry ) //10
                j += 1
            else:
                l3_list.append(l2_list[j] + carry)
                carry = (l2_list[j] + carry)//10
                j += 1
        
        if carry != 0:
            l3_list.append(carry)
        
        l3_list = l3_list[::-1]
        head = ListNode(int(l3_list[0]))
        res = head
        for i in range(1,len(l3_list)):
            head.next = ListNode( int( l3_list[i] ) )
            head = head.next
            
        
        return res