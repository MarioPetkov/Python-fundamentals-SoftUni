command = input().split("||")
cities = {}
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold

    command = input().split("||")

action = input().split("=>")
while action[0] != "End":
    if action[0] == "Plunder":
        town, people, gold = action[1], int(action[2]), int(action[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")

    elif action[0] == "Prosper":
        town, gold = action[1], int(action[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    action = input().split("=>")
if cities: 
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f"{town} -> Population: {town_information['population']} citizens, Gold: {town_information['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")