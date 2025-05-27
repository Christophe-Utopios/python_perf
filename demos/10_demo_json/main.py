import json, os

path = "./demos/10_demo_json/file.json"

# JSON -> JavaScript Object Notation
mon_dict = [{"Prénom" : "Toto", "Nom" : "Tata", "Age" : 18}]

if os.path.exists(path):
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        print(data[0]["Prénom"])
else:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(mon_dict, file, indent=4)

# with open(path, "w", encoding="utf-8") as file:
#         json.dump(mon_dict, file, indent=4)