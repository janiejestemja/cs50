# Meal Time

def main():
	number_of_hours = convert(input("Time:").strip())

	if 8 >= number_of_hours >= 7: 
		print("breakfast time")

	elif 13 >= number_of_hours >= 12:
		print("lunch time")

	elif 19 >= number_of_hours >= 18:
		print("dimmer time")

	else:
		return 0


def convert(time):
	hours, minutes = time.split(":")

	return float(int(hours) + int(minutes) / 60)


if __name__ == "__main__":
	main()