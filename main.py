text = input('input text:').split()

print('text_size = ',len(text))

def create_gen(text):
	for word in text:
		yield len(word)
  

gen = create_gen(text)

for length in gen:
	print('word_size = ', length)
