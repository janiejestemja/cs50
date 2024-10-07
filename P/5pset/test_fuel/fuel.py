# Fuel Gauge

def main():
	while True:
		fraction = input("Fraction: ").strip()

		try:
			percentage = convert(fraction)
		except (ValueError, ZeroDivisionError):
			pass
		else:
			print(gauge(percentage))

def convert(fraction):
	nominator, denominator = fraction.split("/")
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
			return round(result)

def gauge(percentage):
    
	if percentage > 99:
		return "F"

	elif percentage < 1:
		return "E"

	else:
		return f"{percentage}%"


if __name__ == "__main__":
	main()