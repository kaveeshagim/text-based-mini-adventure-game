def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You can go left or right.")
    choice1()

def choice1():
    choice = input("Do you want to go left or right? (left/right): ").lower()
    
    if choice == "left":
        encounter_wolf()
    elif choice == "right":
        find_treasure()
    else:
        print("Invalid choice! Please choose left or right.")
        choice1()

def encounter_wolf():
    print("You encounter a fierce wolf! It growls at you.")
    choice = input("Do you want to run away or try to tame the wolf? (run/tame): ").lower()
    
    if choice == "run":
        print("You ran back to safety. You live to explore another day!")
    elif choice == "tame":
        print("The wolf surprisingly allows you to pet it. You've made a new friend!")
    else:
        print("Invalid choice! Please choose run or tame.")
        encounter_wolf()

def find_treasure():
    print("You find a hidden treasure chest!")
    choice = input("Do you want to open it or leave it? (open/leave): ").lower()
    
    if choice == "open":
        print("You opened the chest and found gold! You're rich!")
    elif choice == "leave":
        print("You chose to leave the treasure. Sometimes it's good to walk away!")
    else:
        print("Invalid choice! Please choose open or leave.")
        find_treasure()

if __name__ == "__main__":
    start_game()
