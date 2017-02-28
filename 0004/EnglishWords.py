with open("words.txt", "r") as f:
	content = f.read()
	words = content.split()
	wordDict = {}
	for word in words:
		word = word.replace(",","")
		word = word.replace(".","")
		word = word.replace(":","")
		word = word.replace("!","")
		word = word.replace("\"","")
		if word in wordDict:
			wordDict[word] += 1
		else:
			wordDict[word] = 1
	result = sorted(wordDict.items(), key = lambda k: k[1], reverse = True)
	for (k, v) in result: 
		print (k, v)
		# pass

