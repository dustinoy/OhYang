def QS(list):
	left=[]
	mid=[]
	right=[]
	if len(list)<=1:
		return list
	else:
		k=list[1]
		for i in list:
			if i <k:
				left.append(i)
			elif i >k:
				right.append(i)
			else:
				mid.append(i)
	left = QS(left)
	right = QS(right)
	return left+mid+right
