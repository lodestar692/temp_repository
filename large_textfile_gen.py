
for i in range(20):
	with open('large_text' + str(i) + '.txt', 'w') as f:
		for j in range(165000):
			f.write('Poweerof Looooong Text!!!\n')
			f.write(str(j))