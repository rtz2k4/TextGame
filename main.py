import time
import random

class Player:
    def __init__(self, name, level, experience, max_health, attack, defense, coins):
        self.name = name
        self.level = level
        self.experience = experience
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defense = defense
        self.coins = coins

    def display_stats(self):
        print(f"\n----- {self.name}'s Stats -----")
        print(f"Level: {self.level}")
        print(f"Experience: {self.experience}/{self.level * 100}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Coins: {self.coins}")
        print("-----------------------------")

class Enemy:
    def __init__(self, name, health, attack, defense, coins):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.coins = coins

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def battle(player, enemy):
    print_slow(f"A wild {enemy.name} appears!")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}'s HP: {player.health}")
        print(f"{enemy.name}'s HP: {enemy.health}\n")

        print("1. Attack")
        print("2. Defend")
        choice = input("Choose your action: ")

        if choice == "1":
            damage = player.attack - enemy.defense
            enemy.health -= max(0, damage)
            print_slow(f"{player.name} attacks {enemy.name} and deals {max(0, damage)} damage!")

            enemy_damage = enemy.attack - player.defense
            player.health -= max(0, enemy_damage)
            print_slow(f"{enemy.name} counterattacks and deals {max(0, enemy_damage)} damage to {player.name}!")

        elif choice == "2":
            print_slow(f"{player.name} defends and reduces incoming damage.")

            enemy_damage = (enemy.attack - player.defense) // 2
            player.health -= max(0, enemy_damage)
            print_slow(f"{enemy.name} attacks, but {player.name} defends and takes only {max(0, enemy_damage)} damage.")

        else:
            print_slow("Invalid choice! Try again.")

    if player.health <= 0:
        print_slow(f"\n{player.name} has been defeated. Game over.")
    else:
        player.experience += 20
        player.coins += enemy.coins
        print_slow(f"\nCongratulations! You defeated {enemy.name} and gained 20 experience and {enemy.coins} coins.")
        check_level_up(player)

def check_level_up(player):
    if player.experience >= player.level * 100:
        player.level += 1
        player.max_health += 10
        player.attack += 5
        player.defense += 2
        player.health = player.max_health
        print_slow(f"\nLevel Up! {player.name} is now level {player.level}.")

def visit_shop(player):
    print_slow("\nWelcome to the Shop!")
    print("1. Health Potion (20 coins) - Restore 20 health")
    print("2. Attack Boost (30 coins) - Increase attack by 5")
    print("3. Defense Boost (25 coins) - Increase defense by 3")
    print("4. Exit Shop")

    choice = input("Choose an option: ")

    if choice == "1":
        if player.coins >= 20:
            player.coins -= 20
            player.health = min(player.max_health, player.health + 20)
            print_slow("You bought a Health Potion and restored 20 health.")
        else:
            print_slow("Not enough coins!")

    elif choice == "2":
        if player.coins >= 30:
            player.coins -= 30
            player.attack += 5
            print_slow("You bought an Attack Boost and increased your attack by 5.")
        else:
            print_slow("Not enough coins!")

    elif choice == "3":
        if player.coins >= 25:
            player.coins -= 25
            player.defense += 3
            print_slow("You bought a Defense Boost and increased your defense by 3.")
        else:
            print_slow("Not enough coins!")

    elif choice == "4":
        print_slow("Thanks for visiting the Shop!")

    else:
        print_slow("Invalid choice! Try again.")

def main():
    print_slow("Welcome to the Text RPG Game!\n")

    player_name = input("Enter your name: ")
    player = Player(name=player_name, level=1, experience=0, max_health=50, attack=15, defense=5, coins=50)

    enemies = [Enemy("Goblin", health=30, attack=10, defense=5, coins=10),
               Enemy("Dragon", health=50, attack=20, defense=15, coins=20),
               Enemy("Troll", health=40, attack=15, defense=10, coins=15)]

    while player.health > 0:
        player.display_stats()
        print("\n1. Battle")
        print("2. Visit Shop")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            enemy = random.choice(enemies)
            battle(player, enemy)

        elif choice == "2":
            visit_shop(player)

        elif choice == "3":
            print_slow("Thanks for playing! Goodbye.")
            break

        else:
            print_slow("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
