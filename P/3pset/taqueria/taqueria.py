# Felipes Taqueria

def main():
	total = 0

	while True:
		try:
			item = input("Item: ").title()

		except EOFError:
			print("")
			break

		else:
			total = total + helper_func(item)
			print(f"Total: {total}")

def helper_func(item):

	menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

	if item in menu:
		return menu[item]

	else:
		return 0


if __name__ == "__main__":
	main()