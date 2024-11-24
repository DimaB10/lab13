import json
elements = {
    "Гідроген": 1.008,
    "Гелій": 4.0026,
    "Літіій": 6.94,
    "Берилій": 9.0122,
    "Бор": 10.81,
    "Вуглець": 12.011,
}
with open("elements.json", mode="w", encoding="utf-8") as file:
    json.dump(elements, file, ensure_ascii=False, indent=4)

with open("elements.json", mode="r", encoding="utf-8") as file:
    elements = json.load(file)

sorted_elements = dict(sorted(elements.items(), key=lambda x: x[1], reverse=True))

print("Список елементів за відносною атомною масою за спаданням:")
for element, mass in sorted_elements.items():
    print(f"{element}: {mass}")
