# Math Interpreter

def main():
	x, y, z = input("Expression: ").strip().split(" ", maxsplit=2)
	print(f"{interpreter(x, y, z):2}")

def interpreter(x, y, z):
	x = int(x)
	z = int(z)

	match y:
		case "*":
			return round(float(x * z), 1)
		case "/":
			return round(float(x / z), 1)
		case "+":
			return round(float(x + z), 1)
		case "-":
			return round(float(x - z), 1)

if __name__ == "__main__":
	main()