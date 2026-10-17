from collections import defaultdict

# def add_employee(departments: defaultdict[str, list[str]], name: str, department:str) -> None:
#     departments[department].append(name)

# departments = defaultdict(list)

# add_employee(departments, "Hunter", "IT")
# add_employee(departments, "Alice", "HR")
# add_employee(departments, "Bob", "IT")
# add_employee(departments, "Sara", "Marketing")

# print(departments)



# def add_skill(skills: defaultdict[str, list[str]], name: str, skill: str) -> None:
#     skills[skill].append(name)

# skills = defaultdict(list)

# add_skill(skills, "Hunter", "Python")
# add_skill(skills, "Alice", "Python")
# add_skill(skills, "Bob", "JavaScript")
# add_skill(skills, "Hunter", "SQL")
# add_skill(skills, "Alice", "Git")
# add_skill(skills, "Bob", "Python")

# print(skills)



# def count_language(languages: defaultdict[str, int], language: str) ->None:
#     languages[language] += 1

# languages = defaultdict(int)

# count_language(languages, "Python")
# count_language(languages, "javascript")
# count_language(languages, "Python")
# count_language(languages, "java")
# count_language(languages, "javascript")
# count_language(languages, "Python")

# print(languages)



# def record_language(
#     data: defaultdict[str, defaultdict[str, int]],
#     name: str,
#     language: str
# ) -> None:
#     data[name][language] += 1


# data = defaultdict(lambda: defaultdict(int))

# record_language(data, "Hunter", "Python")
# record_language(data, "Hunter", "Python")
# record_language(data, "Hunter", "SQL")
# record_language(data, "Alice", "Python")
# record_language(data, "Alice", "JavaScript")

# print(data)



# def add_item(inventory: defaultdict[str, defaultdict[str, int]], player: str, item: str) ->None:
#     inventory[player][item] += 1


# inventory = defaultdict(lambda: defaultdict(int))

# add_item(inventory, "Hunter", "Potion")
# add_item(inventory, "Hunter", "Potion")
# add_item(inventory, "Hunter", "Potion")
# add_item(inventory, "Hunter", "Sword")

# add_item(inventory, "Alice", "Potion")
# add_item(inventory, "Alice", "Potion")
# add_item(inventory, "Alice", "Potion")
# add_item(inventory, "Alice", "Potion")
# add_item(inventory, "Alice", "Potion")
# add_item(inventory, "Alice", "Shield")


# print(inventory)

