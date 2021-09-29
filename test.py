#chars = sorted('hi mum')
#words = 'this is a test'.split()
#print(words)

text = "This is a sentence"
long_word = [word for word in text.split()if len(text) > 3]
print(long_word)
