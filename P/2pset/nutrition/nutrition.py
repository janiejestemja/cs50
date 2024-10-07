# Nutrition Facts

def main():
	fruit_name = input("Item: ").strip().lower()

	if calories_of_fruit(fruit_name):
		print(f"Calories: {calories_of_fruit(fruit_name)}")

def calories_of_fruit(fruit_name):
	fruit_calories_per_portion = {
	"apple": 130,
	"avocado": 50, 
	"banana": 110,
	"cantaloupe": 50,
	"grapefruit": 60,
	"grapes": 90,
	"honeydow melon": 50,
	"kiwifruit": 90,
	"lemon": 15,
	"lime": 20,
	"nectarine": 60,
	"orange": 80,
	"peach": 60,
	"pear": 100,
	"pineapple": 50,
	"pums": 70,
	"strawberries": 50,
	"sweet cherries": 100,
	"tangerine": 50,
	"watermelon": 80,
	}

	if fruit_name in fruit_calories_per_portion:
		return fruit_calories_per_portion[fruit_name]
	else:
		return None

if __name__ == "__main__":
	main()