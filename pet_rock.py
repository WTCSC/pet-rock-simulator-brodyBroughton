# Pet name entry
def get_pet_name():
    while True:
        try:
            pet_name = str(input("What would you like to call your pet rock? "))
            # Pet name max 16 characters
            if len(pet_name) > 16:
                print("Name too long, try again")
            # Prevention for empty strings and strings with spaces in them
            elif pet_name == "" or pet_name.isspace():
                print("You must enter a name!")
            else:
                return pet_name
        except ValueError:
            print("error: get_pet_name")

# Main game loop
def main_loop(stats):
    while True:

        # End condition check
        if stats["anger"] >= 10:
            print(f"{stats["name"]} got too angry and spontaneously combusted. (ノಠ益ಠ)ノ彡┻━┻")
            break
        if stats["hunger"] >= 10:
            print(f"{stats["name"]} died of hunger (Don't ask me how 乁( ⁰͡ Ĺ̯ ⁰͡ ) ㄏ )")
            break

        # Energy
        if stats["energy"] >= 10:
            print(f"{stats["name"]} had so much energy it turned itself into a neutron star and exploded. (ಠ ∩ಠ)")
            break
        if stats["energy"] <= 0:
            print(f"{stats["name"]} died. (;´༎ຶД༎ຶ`)")
            break

        # Print current stats
        print(f"~~~ {stats['name']}'s stats ~~~\n"
                f"Anger: {stats['anger']}\n"
                f"Hunger: {stats['hunger']}\n"
                f"Energy: {stats['energy']}")
        
        # Action choices loop
        while True:
            try:

                print("")
                action_choice = int(input(
                f"1. Pet {stats["name"]}.\n"
                f"2. Feed {stats["name"]}.\n"
                f"3. Give {stats["name"]} an energy drink.\n"
                f"4. Do nothing.\n"
                "Enter: "
                ))

                if action_choice not in (0, 1, 2, 3, 4):
                    print("Invalid selection.")
                    continue
                else:
                    # If we got here then we good
                    break

            except ValueError:
                print("Invalid selection.")

        # Pet the rock
        if action_choice == 1:
            stats["anger"] -= 2

        # Feed the rock
        if action_choice == 2:
            stats["hunger"] -= 2

        # Give the rock copious amounts of caffeine
        if action_choice == 3:
            stats["energy"] += 5

        if action_choice == 0:
            print("https://tinyurl.com/S3CR3TL1NK")
            break

        # Natural depletion from the passage of time
        stats["hunger"] += 1
        stats["anger"] += 1
        stats["energy"] -= 1



def main():

    stats = {
        "name": "",
        "anger" : 5,
        "hunger" : 5,
        "energy" : 5
    }

    pet_name = get_pet_name()

    stats["name"] = pet_name

    main_loop(stats)
    

if __name__ == "__main__":
    main()
    