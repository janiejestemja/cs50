# Outdated

def main():

	months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]	
	months_dict = {month: str(number + 1) for number, month in enumerate(months)}

	while True:
		user_input = input("Date: ").strip().title()

		try:
			month, day, year = user_input.split("/")

		except ValueError:
			try:
				month_and_day, year = user_input.split(",")

			except ValueError:
				pass

			else:
				try:
					month, day = month_and_day.split(" ")

				except ValueError:
					pass

				else:
					if month in months_dict:
						month = months_dict[month]
						
						if date_validation(year, month, day):
							print(f"{year.strip()}-{month}-{day.strip()}")
							break

					else:
						continue

		else:
			if date_validation(year, month, day):
				print(f"{year}-{month}-{day}")
				break

			else:
				continue


def date_validation(year, month, day):
	try:
		day = int(day)
		month = int(month)
		year = int(year)

	except ValueError:
		return False

	else:
		if month in range(1, 13) and day in range(1, 32):
			return True
		else:
			return False

if __name__ == "__main__":
	main()