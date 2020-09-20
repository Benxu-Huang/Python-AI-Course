# 作業1 判斷分數
c,e,m = map(int,input("請輸入國文,英文,數學分數:").split())
total = c+e+m
avg = total/3

if avg >= 90:
    comment = "優等"
elif avg >= 80:
    comment = "甲等"
elif avg >= 70:
    comment = "乙等"
elif avg >= 60:
    comment = "丙等"
elif avg >= 50:
    comment = "補考"
else: 
    comment = "明年再來"
    
print("國文={}\n英文={}\n數學={}\n總分={}\n平均={}\n評語{}".format(c,e,m,total,avg,comment))
