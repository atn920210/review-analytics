data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		#print(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %求餘數 (除以 1000 餘數為 0)
			print(len(data))
print('檔案讀取完了, 總共有',len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於 100')
print(new[0])
print(new[1])

good =[]
for d in data:
	if 'good' in d:
		good.append(d)

# List comprehension #
good = [d for d in data if 'good' in d] # 等同於上面程式碼
print('一共有', len(good), '筆留言包含 good')
#print(good[0])
#print(good[1])

good =[]
for d in data:
	if 'good' in d:
		good.append(1) # 裝進一堆 1

good = [1 for d in data if 'good' in d] # 等同於上面程式碼

bad = ['bad' in d for d in data]
print(bad)

bad =[]
for d in data:
	bad.append('bad' in d) # 等同於上面程式碼


#文字記數#

wc = {} #word_count
for d in data:
	words = d.split() #split 預設值是空白鍵
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] =1 #新增新字進入 wc 字典
# for word in wc:
# 	if wc[word] > 1000:
# 		print(word, wc[word])

print(len(wc))
print(wc['Austin'])

while True:
	word = input('請問你想查什麼字: ')
	if word =='q':
		break
	if word in wc:
		print(word, '出現過的是數為:', wc[word])
	else:
		print('這個字沒有出現過喔!')
print('感謝使用本功能')