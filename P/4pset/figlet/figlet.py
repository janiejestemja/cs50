# Frank, Ian and Glens's letters

import sys
from random import choice
from pyfiglet import Figlet

def main():
	figlet = Figlet()

	if len(sys.argv) != 1 and len(sys.argv) != 3:
		sys.exit("Error: Unexpected number of commandlinearguments (expects none or two)")
	
	if len(sys.argv) == 1:
		font = choice(figlet.getFonts())

	if len(sys.argv) == 3:
		if sys.argv[1] != "-f" and sys.argv[1] != "--font":
			sys.exit("Error: first commandlineargument should be either '-f' or '--font'.")

		elif sys.argv[2] not in figlet.getFonts():
			sys.exit("Error: chosen font not found.")

		else:
			font = sys.argv[2]

	user_input = input("Input: ")
	
	figlet.setFont(font=font)
	print(figlet.renderText(user_input))

if __name__ == "__main__":
	main()