import yaml

with open("./data/gatt.yaml", 'r') as stream:
    try:
        data = yaml.safe_load(stream)
        keys = list(data.keys())
        keys.sort()
        print(keys)

        for key in keys:
            print(data[key])
    except yaml.YAMLError as exc:
        print(exc)

if __name__ == "__main__":
    pass
