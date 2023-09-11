class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        dic2 = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1_ans = 0
        num2_ans = 0

        count = 1
        for i in range(max(len(num2), len(num1))):
            if i < len(num1):
                num1_ans += dic[num1[i]] * count
            if i < len(num2):
                num2_ans += dic[num2[i]] * count
            count *= 10
        num = num1_ans * num2_ans
        ans=""
        if num == 0:
            return "0"
        while num:
            temp = num%10
            num = num//10
            ans+= dic2[temp] 
        return ans[::-1]