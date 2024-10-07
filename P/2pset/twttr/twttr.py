# Just setting up my twttr

def main():
	vowels = ["a", "e", "i", "o", "u"]

	user_input = input("Input: ")

	output = ""
	for character in user_input:
		if character.lower() not in vowels:
			output = output + character
		else:
			continue
	
	print("Output: ", output)

if __name__ == "__main__":
	main()