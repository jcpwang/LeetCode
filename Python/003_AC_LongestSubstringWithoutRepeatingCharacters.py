# Author:   Jerry C. Wang <jcpwang@gmail.com>
# File:     003_AC_LongestSubstringWithoutRepeatingCharacters.py

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        words = {}
        substr = ""
        max_len = 0
        h = 0
        i = 0
        s_len = len(s)
        while i < s_len:
            if(words.get(s[i]) == None):
                words[s[i]] = i
            else:
                #update dictionary if words is obsolete
                if(words[s[i]] < h):
                    words[s[i]] = i
                    i += 1
                    continue
                m = i - h
                if i - h > max_len:
                    max_len = m
                h = words[s[i]] + 1
                words[s[i]] = i
            i += 1

        m = i - h
        if m > max_len:
            max_len = m

        return max_len
