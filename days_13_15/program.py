from days_13_15.actors import Creature, Wizard, Dragon
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('--------------------')
    print('----WIZARD_GAME-----')
    print('--------------------')
    print()

def game_loop():
    creatures = [
        # TODO: add some creatures
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f"A of {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...")
        print()

        cmd = input("Do you [a]ttack, [r]un or [l]ook around?")
        if cmd == 'a':
            # the hero.attack method returns a bool if the hero outrolls the creature
            # if the hero wins the fight, the creature is removed from the collection
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f"{hero.name}, our hero, defeated {active_creature.name}")
            else:
                print(f"{hero.name} was defeated by {active_creature.name}")
        elif cmd == 'r':
            print(f"The hero, {hero.name} is unsure of his powers and flees")
        elif cmd == 'l':
            print(f"The wizard {hero.name} takes in his surroundings and sees:")
            for c in creatures:
                print(f" * {c.name} of level {c.level}")

        else:
            print("exiting game, goodbye")
            break

        if not creatures:
            print("you have defeated all of the creatures, well done!")
            break

if __name__ == '__main__':
    main()