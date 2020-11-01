dict_a = {
    "name" : "seaweed",
    "type" : "seaweed type",
    "ingredient" : ["Domestic", "carora", "Sesame oil", "Perilla oil"],
    "origin" : "Korea",
}

name_value = dict_a.get("name")
if name_value != None:
    print(name_value)
else:
    print("키가 존재하지 않습니다.")