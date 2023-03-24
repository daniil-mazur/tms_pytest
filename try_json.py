import json

data = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

def json_to_string():
    print(data)
    print(type(data))
    new_str = json.dumps(data, indent=4)
    print(new_str)
    print(type(new_str))

def json_to_file():
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file, indent=4)

def str_to_dict():
    new_str = json.dumps(data, indent=4)
    new_dict = json.loads(new_str)
    print(new_dict)
    print(type(new_dict))

def file_to_dict():
    with open("data_file.json", "r") as write_file:
        new_dict = json.load(write_file)
    print(new_dict)
    print(type(new_dict))


# json_to_string()
# json_to_file()
# str_to_dict()
file_to_dict()