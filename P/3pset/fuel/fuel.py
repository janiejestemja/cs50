# Fuel Gauge

def main():
	while True:
		nominator, denominator = input("Fraction: ").strip().split("/")

		try:
			result = helper_fuc(nominator, denominator)

		except (ValueError, ZeroDivisionError):
			pass

		else:
			if type(result) == str():
				print(result)
			else:
				print(f"{result}%")


def helper_fuc(nominator, denominator):

	if nominator is None or denominator is None:
		raise ValueError("given fraction is incomplete.")

	try:
		nominator = int(nominator)
		denominator = int(denominator)

	except ValueError:
		raise ValueError("given variables are not recognized as integers.")

	else:
		try:
			result = nominator / denominator

		except ZeroDivisionError:
			raise ZeroDivisionError("we do not divide through zero.")

		else:
			result = result * 100

			if result > 99:
				return "F"

			elif result < 1:
				return "E"

			else:
				return round(result)


if __name__ == "__main__":
	main()