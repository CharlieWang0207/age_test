drive = input('請問你有沒有開過車?')
if drive != '有' and drive != '沒有': # 設置於此可以優先判定是否填入有/無
	print('只能輸入 有/沒有')
	raise SystemExit # raise代表觸發錯誤 # SystemExit是終止程式
age = input('請問你的年齡?')
age = int(age)
if drive == '有':
    if age >= 18:
        print('你通過測驗了')
    else:
        print('你怎麼會開過車')
elif drive == '沒有':
	if age >= 18:
		print('你可以去考駕照啦')
	else:
		print('你還不能開車')