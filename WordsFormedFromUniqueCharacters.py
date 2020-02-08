#Problem available at: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/submissions/
import copy
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        if not words or not chars:
            return
        
        chars_dict = {}
        chars_dict_orig = {}
        sum_ = 0
        flag = 'Bad'
        
        for i in chars:
            if chars_dict_orig.__contains__(i):
                chars_dict_orig[i] += 1
            else:
                chars_dict_orig[i] = 1
        
        for j in range(len(words)):
            curr_word = words[j]
            chars_dict = copy.copy(chars_dict_orig)
            
            for k in range(len(curr_word)):
                if not chars_dict.__contains__(curr_word[k]):
                    flag = 'Bad'
                    break
                elif chars_dict.__contains__(curr_word[k]) and chars_dict[curr_word[k]] == 0:
                    flag = 'Bad'
                    break
                
                else:
                    chars_dict[curr_word[k]] -= 1
                    flag = 'Good'
            if flag == 'Good':
                sum_ += len(curr_word)
                
        return sum_        