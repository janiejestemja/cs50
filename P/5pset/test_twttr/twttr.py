# Just setting up my twttr

def main():
	user_input = input("Input: ")
	print(shorten(user_input))

def shorten(word):
	vowels = ["a", "e", "i", "o", "u"]

	output = ""
	for character in word:
		if character.lower() not in vowels:
			output = output + character
		else:
			continue
	
	return output

if __name__ == "__main__":
	main()