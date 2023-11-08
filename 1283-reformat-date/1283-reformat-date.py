class Solution:
    def reformatDate(self, date: str) -> str:
        val = date.split(" ")
        month_dic = {"Jan": "1" , "Feb":"2" , "Mar":"3", "Apr":"4", "May":"5", "Jun":"6", "Jul":"7", "Aug":"8", "Sep":"9", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        day = val[0][:-2] 
        if len(day)==2:
            day = val[0][:-2] 
        else:
            day = "0"+val[0][:-2]
        print(day)
        year = val[2]
        month = month_dic[val[1]]
        if len(month)==2:
            month = month_dic[val[1]]
        else:
            month = "0"+ month_dic[val[1]]
        print(month)
        return year+"-"+month+"-"+day
        