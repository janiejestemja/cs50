# Home Federal Savings Bank

def main():
	given_greeting = input("Greeting: ").lower()
	if given_greeting.startswith("hello"):
		print("0$")
	elif given_greeting.startswith("h"):
		print("20$")
	else:
		print("100$")

if __name__ == "__main__":
	main()