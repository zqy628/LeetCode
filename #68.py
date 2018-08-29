#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        width = 0
        lines = [[]]
        for word in words:
            if lines[-1] == []:
                width += len(word)
            else:
                width += len(word)+1
            if width <= maxWidth:
                lines[-1].append(word)
            else:
                lines.append([word])
                width = len(word)
        sentenses = []
        for line in lines[:-1]:
            if len(line) == 1:
                sentenses.append(line[0]+' '*(maxWidth-len(line[0])))
            else:
                width = sum([len(l) for l in line])
                width_ = maxWidth - width
                a = width_//(len(line)-1)
                b = width_%(len(line)-1)
                blank = [' '*a for i in range(len(line)-1)]
                for i in range(b):
                    blank[i] += ' '
                sentense = line[0]
                for i,blank_ in enumerate(blank):
                    sentense += blank_ + line[i+1]
                sentenses.append(sentense)
        sentenses.append(' '.join(lines[-1]))
        sentenses[-1] = sentenses[-1] + ' '*(maxWidth-len(sentenses[-1]))
        return sentenses