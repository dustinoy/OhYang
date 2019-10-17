list=[5,7,3,8,27,9,6,100,1,55]

def QS(list): #定義Quicksort
	left=[] #建立三個list
	mid=[]
	right=[]
	if len(list)<=1: #假如list長度小於等於1就可以直接回傳
		return list
	else:
		k=list[1] #取list第2個數字當基準值
		for i in list:
			if i <k: #假如變數i小於基準值則放到左邊的list
				left.append(i)
			elif i >k: #大於基準值則放到右邊的list
				right.append(i)
			else: #其餘等於基準值的則都集合在同一個list
				mid.append(i)
	left = QS(left) #再把左右的list Quicksort直到不能再跑
	right = QS(right)
	return left+mid+right #最後總結三個部分list就整理好了

QS(list)
