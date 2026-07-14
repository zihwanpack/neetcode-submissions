class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]

        for s in strs[1:]:
            temp = ''
            for index, alphabet in enumerate(s):
                if index < len(answer) and answer[index] == alphabet:
                    temp += alphabet
                else:
                    break
            
            answer = temp
        return answer
                    
                    
                