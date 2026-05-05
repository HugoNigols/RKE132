from character import Hero, Villain
from file_utils import get_random_from_file

hero_name = get_random_from_file(r"data\heroes (1).txt")
hero_weapon = get_random_from_file(r"data\weapons (1).txt")
villain_name = get_random_from_file(r"data\villains (1).txt")
villain_weapon = get_random_from_file(r"data\weapons (1).txt")

hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)

print("=== BATTLE BEGINS ===")

print(f"Hero: {hero.name} | HP: {hero.hp} | Weapon: {hero.weapon}")
print(f" Villain: {villain.name} | HP: {villain.hp} | Weapon: {villain.weapon}")

round_number = 1

while hero.is_alive() and villain.is_alive():
    print(f"--- ROUND {round_number} ---")

    hero.attack(villain)

    if not villain.is_alive():
        break

    villain.attack(hero)

    round_number = round_number + 1

print("=== BATTLE ENDS ===")

if hero.is_alive():
    print("HERO WINS!")
else:
    print("Dark side wins...")
