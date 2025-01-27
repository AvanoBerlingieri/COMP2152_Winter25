import random

diceOptions = list(range(1, 7))

weapons = ["Sword", "Axe", "Bow", "Dagger", "Mace", "Spear"]

print("Available Weapons:")
for weapon in weapons:
    print(f"- {weapon}")

def get_combat_strength(player):
    while True:
        try:
            value = int(input(f"Enter {player}'s combat strength (1-6): "))
            if value in diceOptions:
                return value
            else:
                print("Invalid input. Please enter an number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter an number between 1 and 6.")

heroCombatStrength = get_combat_strength("Hero")
monsterCombatStrength = get_combat_strength("Monster")

print("\nStarting Battle!")
for j in range(1, 20, 2):
    if j == 11:
        print("\nRound 11: Battle Truce declared! The battle ends in a draw.")
        break

    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    hero_strength = heroCombatStrength + hero_roll
    monster_strength = monsterCombatStrength + monster_roll

    selected_weapon = weapons[(j - 1) % len(weapons)]

    print(f"\nRound {j}")
    print(f"Selected Weapon: {selected_weapon}")
    print(f"Hero rolls {hero_roll} (Total Strength: {hero_strength})")
    print(f"Monster rolls {monster_roll} (Total Strength: {monster_strength})")

    if hero_strength > monster_strength:
        print("Hero wins this round!")
    elif monster_strength > hero_strength:
        print("Monster wins this round!")
    else:
        print("This round is a draw!")
