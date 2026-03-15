from collections import deque

substances = list(map(int, input().split(", ")))
crystals = deque(list(map(int, input().split(", "))))

potions_checklist = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

crafted_potions = []

while True:
    if len(crafted_potions) == 5:
        break
    if not substances:
        break
    if not crystals:
        break

    curr_substance = substances[-1]
    curr_crystal = crystals[0]
    combined = curr_substance + curr_crystal

    for key, value in potions_checklist.items():
        if value == combined:
            crafted_potions.append(key)
            substances.pop()
            crystals.popleft()
            del potions_checklist[key]
            break
    else:
        for key, value in potions_checklist.items():
            if value < combined:
                crafted_potions.append(key)
                del potions_checklist[key]
                substances.pop()
                curr_crystal = crystals.popleft() - 20
                if curr_crystal > 0:
                    crystals.append(curr_crystal)
                break
        else:
            substances.pop()
            curr_crystal = crystals.popleft() - 5
            if curr_crystal > 0:
                crystals.append(curr_crystal)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(map(str, crafted_potions))}")

if substances:
    print(f"Substances: {', '.join([str(substances[i]) for i in range(len(substances) - 1, -1, -1)])}")
if crystals:
    print(f"Crystals: {', '.join([str(crystals[c]) for c in range(len(crystals))])}")
