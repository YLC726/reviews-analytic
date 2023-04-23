data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
	    data.append(line)
	    count += 1
	    if count % 10000 == 0:#%為除以後求於數
	        print('已讀取',len(data),'則留言')
print('---------------------')
print('總共有',len(data),'則留言')#印出總行數
print('---------------------')
print(data[0])#印出第0行
print('---------------------')
print(data[2])
