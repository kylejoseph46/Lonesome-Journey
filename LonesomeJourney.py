#Kyle Joseph
#Purpose: Lonesome Journey is a game about a boy lost in the wilderness trying to make his way home. 
#On his way home he has to get across many obstacles from fighting dragons to crossing a river.


import colorama
from colorama import Fore, Style


class Player:
	def __init__(self, name):
		self.name = name
		self.weapons = []
		self.armory = []
		self.items = []
		self.hp = 20
		self.money = 0

	def get_name(self):
		return self.name

	def get_hp(self):
		return self.hp
	
	def set_weapon(self, new_weapon):
		self.weapons.append(new_weapon)

	def set_armory(self, new_armor):
		self.armory.append(new_armor)

	def search_weapon(self, weapon_match):
		for index in self.weapons:
			if index.get_name() == weapon_match:
				return index

	def lower_hp(self, incoming_damage):
		self.hp = self.hp - incoming_damage

	def gain_money(self, money):
		self.money += money

	def lose_money(self, money):
		self.money -= money

	def get_money(self):
		return self.money

	def __str__(self):
		return f'{self.name}s HP: {self.hp}'


class Monster:
	def __init__(self, name, hp, dmg):
		self.name = name
		self.hp = hp
		self.dmg = dmg

	def get_name(self):
		return self.name

	def get_hp(self):
		return self.hp

	def get_dmg(self):
		return self.dmg

	def lower_hp(self, incoming_damage):
		self.hp = self.hp - incoming_damage

	def __str__(self):
		return f'{self.name}s HP: {self.hp}'


class Weaponry:
	def __init__(self, name, dmg):
		self.name = name
		self.dmg = dmg
	
	def get_name(self):
		return self.name

	def get_dmg(self):
		return self.dmg

	def __str__(self):
		return f' + {self.name}: {self.dmg} dmg'


class Menu:
	def welcome_screen(self):
		pass

	def directions(self, dir1, dir2):
			print("Here are the directions from your current location:")
			print("1| North")
			print("2| South")
			try:
				direction_choice1 = int(input("Which direction would you like to go?: "))
				if direction_choice1 > 2 or direction_choice1 < 1:
					raise Exception
			except Exception:
				print(Fore.RED + "WRONG INPUT!")
				print(Style.RESET_ALL)
				print("Instructions: Enter '1' for North, Enter '2' for South")
				direction_choice1 = int(input("Which direction would you like to go?: "))
			if direction_choice1 == 1:
				print(f'You have entered the {dir1}')
			elif direction_choice1 == 2:
				print(f'You are approaching the {dir2}')
			return direction_choice1


def main():
	main_menu = Menu()
	player_name = input("What is your name?: ")
	new_player = Player(player_name)
	print(f'Hello {new_player.get_name()}, welcome to your lonesome journey!')
	print(f'You have obtained the battered sword and $100!')
	battered_sword = Weaponry("Battered Sword", 2)	
	new_player.set_weapon(battered_sword)
	new_player.gain_money(100)
	print("Take a look at your starting weapon:")
	print(Fore.BLUE, new_player.search_weapon("Battered Sword"))
	print(Style.RESET_ALL) 
	print('')

	#Exception handling for 'ready' input to ensure the player enters it correctly.
	first_fight_flag = 0
	while first_fight_flag == 0:
		try:
			first_fight = input("Type 'ready' to enter your first battle: ")
			if first_fight != 'ready':
				raise Exception
			first_fight_flag = 1
		except Exception:
			first_fight = input("Type 'ready' to enter your first battle: ")
			if first_fight == 1:
				first_fight_flag = 1

	if first_fight == 'ready':
		weak_goblin = Monster("Weak Goblin", 6, 2)
		print(f'{weak_goblin.get_name()} approaches')
		print('')
		print("Battle begin:")
		run = 'no'
		while(new_player.get_hp() > 0 and weak_goblin.get_hp() > 0 and run == 'no'):
			print(Fore.RED + f'1| Attack {weak_goblin.get_name()}')	
			print(f'2| Run Away')
			print(Style.RESET_ALL)
			first_fight_option = int(input("What would you like to do?: "))
			if first_fight_option == 1:
				print(f'You hit the {weak_goblin.get_name()} for {new_player.search_weapon("Battered Sword").get_dmg()} dmg!')
				weak_goblin.lower_hp(new_player.search_weapon("Battered Sword").get_dmg())
				new_player.lower_hp(weak_goblin.get_dmg())
				print('')
				print("Battle stats:")
				print(Fore.GREEN, weak_goblin)
				print('', new_player)
				print(Style.RESET_ALL)
				print('')
				if weak_goblin.get_hp() <= 0:
					print(Fore.RED, f'You have defeated the {weak_goblin.get_name()}')
					print("", "You have gained $5")
					new_player.gain_money(5)
					print(Style.RESET_ALL)

				elif new_player.get_hp() <= 0:
					print(Fore.RED, f'You have been defeated by the {weak_goblin.get_name()}')
					print("", "You lost $5")
					new_player.lose_money(5)
					print("", "You have been respawned!")
					print(Style.RESET_ALL)
			
			if first_fight_option == 2:
				run = 'yes'
				print(Fore.RED, "You have escaped!, but you are a coward for avoiding your first battle!")
				print(Style.RESET_ALL)
		cont = input("Type 'enter' to continue: ")
		print("You have now begun your lonesome journey!")


	direction_choice = main_menu.directions("Forbidden Forest", "Mystical Lake")
	if direction_choice == 1:
		pass	
	elif direction_choice == 2:
		pass



if __name__ == "__main__":
	main()
