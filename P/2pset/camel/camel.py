# camelCase

def main():
	camel_cased_variable = input("camelCase: ").strip()
	
	for character in camel_cased_variable:
		if character.islower():
			print(character, end="")
		elif character.isupper():
			print("_" + character.lower(), end="")
		else:
			print(character, end="")
	print("")

if __name__ == "__main__":
	main()