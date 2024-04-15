import json
# dictionaries
bond = {
    "identity": {
        "first_name": "James",
        "last_name": "Bond",
    },
    "codename": "007",
}
forty_seven = {
    "identity": {
        "barcode": 640509040147,
        "origin": "romania",
        "experiment": "Ortmeyer"
    },
    "codename": "forty_seven",
}

agents = list()
agents.append(bond)
agents.append(forty_seven)

json_obj = json.dumps(bond, indent=2, sort_keys=True, ensure_ascii=False)
json_objs = json.dumps(agents, indent=2, sort_keys=True)
# print(json_obj) # string
# print(json_objs) # list
# like json.dump
with open('out.json', "w") as f:
    # f.write(json_obj)
    f.write(json_objs)

with open('out.json', "r") as f:
    # return dict or list[dict]
    from_file = json.load(f)
    print(from_file[1])

from_string = json.loads(json_obj)
print(from_string)
