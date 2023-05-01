data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
	    data.append(line)
	    count += 1
	    if count % 10000 == 0:#%
	        print('已讀取',len(data),'則留言')
print('---------------------')
print('總共有', len(data) , '則留言')#印出總行數
total = 0
for i in range(len(data)):
    total += len(data[i])

average = total/len(data)

print("平均留言長度為:", average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有',len(new),'筆留言長度小於100')
print(new[0])