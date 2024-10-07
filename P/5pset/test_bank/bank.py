# Home Federal Savings Bank

def main():
	given_greeting = input("Greeting: ")
	print(f"{value(given_greeting)}$")

def value(greeting):
	
	if type(greeting) != type(str()):
		raise ValueError("expecting a str()")
	
	greeting = greeting.lower()
	if greeting.startswith("hello"):
		return 0
	elif greeting.startswith("h"):
		return 20
	else:
		return 100

if __name__ == "__main__":
	main()