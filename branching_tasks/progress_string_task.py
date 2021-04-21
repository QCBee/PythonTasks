str1, str2, str3 = len(input()), len(input()), len(input())
mini_l = int(min(str1, str2, str3))
maxi_l = int(max(str1, str2, str3))
aver_l = int(str1) + int(str2) + int(str3) - maxi_l - mini_l
if maxi_l - aver_l == aver_l - mini_l:
    print('YES')
else:
    print('NO')

