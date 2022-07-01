class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = []
        for i in s:
            if i.isalnum(): #해당 문자가 숫자인지, 문자인지 판별해주는 함수
                i = i.lower()
                alpha.append(i)
        if alpha[::] == alpha[::-1]:
            return True
        else:
            return False

s = "A man , a plan, a canal: Panama"
a = Solution()
print(a.isPalindrome(s))