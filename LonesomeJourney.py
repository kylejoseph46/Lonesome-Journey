#Kyle Joseph
#Purpose: Lonesome Journey is a game about a boy lost in the wilderness trying to make his way home. 
#On his way home he has to get across many obstacles from fighting dragons to crossing a river.


import colorama
from colorama import Fore, Style
from random import randint


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

	def lower_hp(self, incoming_damage, monster):
		random_num = randint(1,5)
		if random_num == 1:
			print(Fore.RED + "Attack missed")
			print(Style.RESET_ALL)
		else:
			print(Fore.RED + f'{monster.get_name()} hit {self.name} for {monster.get_dmg()} dmg!{Style.RESET_ALL}')
			self.hp = self.hp - incoming_damage
			if self.hp <= 0:
				print(f'You have been defeated by the {monster.get_name()}')
				self.death()

	def gain_money(self, money):
		self.money += money

	def lose_money(self, money):
		self.money -= money

	def get_money(self):
		return self.money

	def death(self):
		print(f'{self.name} has died')
		print("Game Over!")
		exit()

	def restore_hp(self):
		print(f'{self.name}s HP has been restored')
		self.hp = 20

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

	def lower_hp(self, incoming_damage, player):
		random_num = randint(1,5)
		if random_num == 1:
			print(Fore.RED + f'{self.name}s Attack missed {Style.RESET_ALL}')
		else:
			print(Fore.RED + f'{player.get_name()} hit the {self.get_name()} for {player.search_weapon("Battered Sword").get_dmg()} dmg!{Style.RESET_ALL}')
			self.hp = self.hp - incoming_damage
			if self.hp <= 0:
				self.death()

	def death(self):
		print(f'{self.name} has been defeated')

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
	def directions(self, dir1, dir2):
			print("Here are the directions from your current location:")
			print(Fore.BLUE)
			print("1| North")
			print("2| South")
			print(Style.RESET_ALL)
			try:
				direction_choice1 = int(input("Which direction would you like to go?: "))
				if direction_choice1 > 2 or direction_choice1 < 1:
					raise Exception
			except Exception:
				print(Fore.RED + f'WRONG INPUT! {Style.RESET_ALL}')
				print("Instructions: Enter '1' for North, Enter '2' for South")
				direction_choice1 = int(input("Which direction would you like to go?: "))
			if direction_choice1 == 1:
				print(f'You have entered the {dir1}')
			elif direction_choice1 == 2:
				print(f'You are approaching the {dir2}')
			return direction_choice1


	def battle(self, player, monster, battle_value):
		print("Battle begin:")
		run = 'no'
		while(player.get_hp() > 0 and monster.get_hp() > 0 and run == 'no'):
			print(Fore.RED + f'1| Attack {monster.get_name()}')	
			print(f'2| Run Away {Style.RESET_ALL}')
			first_fight_option = int(input("What would you like to do?: "))
			if first_fight_option == 1:
				monster.lower_hp(player.search_weapon("Battered Sword").get_dmg(), player)
				if monster.get_hp() > 0:
					player.lower_hp(monster.get_dmg(), monster)
				print("Battle stats:")
				print(Fore.GREEN, monster)
				print(f' {player} {Style.RESET_ALL}')
				print('')
				if monster.get_hp() <= 0:
					print(f'You have gained ${battle_value}')
					player.gain_money(battle_value)
					player.restore_hp()
			
			if first_fight_option == 2:
				run = 'yes'
				print(Fore.RED, "You have escaped!, but you are a coward for avoiding your first battle!" + Style.RESET_ALL)

def main():
	main_menu = Menu()
	player_name = input("What is your name?: ")
	new_player = Player(player_name)
	print(f'Hello {new_player.get_name()}, welcome to your lonesome journey!')
	print(f'{new_player.get_name()} has obtained the battered sword and $100!')
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
		main_menu.battle(new_player, weak_goblin, 5)
	
	
	cont = input("Type 'enter' to continue: ")
	print("You have now begun your lonesome journey!")


	direction_choice = main_menu.directions("Forbidden Forest", "Mystical Lake")
	if direction_choice == 1:
		large_toad = Monster("Large Toad", 8, 3)
		print("Kyle: WHOAAAAH")
		print(f'You have encountered a {large_toad.get_name()}')
		main_menu.battle(new_player, large_toad, 8)
		print(f'{new_player.get_name()}: "What is this?')
		print(f'{new_player.get_name()} has obtained a{Fore.GREEN} grass sword {Style.RESET_ALL}')
		grass_sword = Weaponry("Grass Sword", 5)	
		new_player.set_weapon(grass_sword)
		print("Take a look at your new sword:")
		print(Fore.GREEN, new_player.search_weapon("Grass Sword"))
		print(Style.RESET_ALL) 
		#Leads to village where you can buy items.
	elif direction_choice == 2:
		piranha = Monster("Piranha", 8, 3)
		print("Kyle: WHOAAAAH")
		print(f'You have encountered a {piranha.get_name()}')
		main_menu.battle(new_player, piranha, 8)
		print(f'{new_player.get_name()}: "What is this?')
		print(f'{new_player.get_name()} has obtained a{Fore.BLUE} water sword {Style.RESET_ALL}')
		water_sword = Weaponry("Water Sword", 5)	
		new_player.set_weapon(water_sword)
		print("Take a look at your new sword:")
		print(Fore.BLUE, new_player.search_weapon("Water Sword"))
		print(Style.RESET_ALL) 
		#Take boat on river that leads to mountain village.


if __name__ == "__main__":
	main()
