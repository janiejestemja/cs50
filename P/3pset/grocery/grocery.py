# Grocery List

def main():

	grocery_dict = dict()
	while True:
		try:
			item = input("Item: ")
		except EOFError:
			print(f"\n")
			for key in sorted(grocery_dict):
				print(grocery_dict[key], key.upper())
			break
		else:
			if item not in grocery_dict:
				grocery_dict[item] = 1
			else:
				grocery_dict[item] += 1

if __name__ == "__main__":
	main()