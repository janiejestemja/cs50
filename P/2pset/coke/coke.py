# Choke Machine

def main():
	valid_denominations = [5, 10, 25]

	amount_due = 50

	while amount_due > 0:
		print(f"Amount due: {amount_due}")
		inserted_coin = int(input("Insert coin: "))

		if inserted_coin in valid_denominations:
			amount_due = amount_due - inserted_coin

	if amount_due <= 0:
		print(f"Change owed: {-1 * amount_due}")

if __name__ == "__main__":
	main()