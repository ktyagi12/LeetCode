# Problem available at: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/543/week-5-june-29th-june-30th/3376/

# Question:
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

'''

from functools import reduce
from collections import defaultdict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # create trie
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        
        for word in words:
            reduce(dict.__getitem__,word,trie)[END] = word
        
        res = set()
        def findstr(i,j,t):
            if END in t:
                res.add(t[END])
                # return
            letter = board[i][j]
            board[i][j] = ""
            if i > 0 and board[i-1][j] in t:
                findstr(i-1,j,t[board[i-1][j]])
            if j>0 and board[i][j-1] in t:
                findstr(i,j-1,t[board[i][j-1]])
            if i < len(board)-1 and board[i+1][j] in t:
                findstr(i+1,j,t[board[i+1][j]])
            if j < len(board[0])-1 and board[i][j+1] in t:
                findstr(i,j+1,t[board[i][j+1]])
            board[i][j] = letter
            
            return 
        
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if board[i][j] in trie:
                    findstr(i,j,trie[board[i][j]])
        return res
        