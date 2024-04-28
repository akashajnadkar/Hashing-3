'''
Time Complexity - O(n). as we are iterating over the entire string
Space Complexity - O(n). To store the hashValues

Works on Leetcode
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #Brute force
        #Generate substrings of length 10, add to hashSet. if substring already in hashSet, add to result O(n)
        # hashSet = set()
        # result = []
        # for i in range(len(s)-9):
        #     substr = s[i:(i+10)]
        #     if substr in hashSet and substr not in result:
        #         result.append(substr)
        #     hashSet.add(substr)
        # return result

        #Using RobinCarp:
        hashMap = {}
        #Store the value of used characters in hashMap
        hashMap[ord('A')] = 1
        hashMap[ord('C')] = 2
        hashMap[ord('G')] = 3
        hashMap[ord('T')] = 4
        hashSet = set()
        result = set()
        hashVal = 0
        outgoing = 4**9
        for i in range(len(s)):
            #when i is at least 10, remove the 1st character to accomodate incoming character
            #adjust hash value accordingly
            if i>=10:
                hashVal= hashVal- (hashMap[ord(s[i-10])]*(outgoing))
            hashVal =  hashVal*4 + hashMap[ord(s[i])]
            #when a hashValue repeats, add the generating to the result
            if hashVal in hashSet:
                result.add(s[i-9:i+1])
            hashSet.add(hashVal)
        return result

        