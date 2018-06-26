urls = ["http://www.google.com/a.txt",
		"http://www.google.com.tw/a.txt",
		"http://www.google.com/download/c.jpg",
		"http://www.google.co.jp/a.txt",
		"http://www.google.com/b.txt",
		"https://facebook.com/movie/b.txt",
		"http://yahoo.com/123/000/c.jpg",
		"http://gliacloud.com/haha.png"	]

files = {}
for i in urls:
	f = i.split('/').pop();
	if(f in files):
		files[f] += 1
	else:
		files[f] = 1

for j in range(0,3):
	top = max(files.items(), key=lambda x: x[1])
	del files[top[0]]
	print(top)