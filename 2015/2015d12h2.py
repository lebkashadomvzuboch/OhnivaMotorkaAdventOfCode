import json

udaj = None

with open("input.txt", "r") as subor:
    udaj = subor.readline().strip()


def hladac(vec):
    if isinstance(vec, int):
        return vec

    elif isinstance(vec, list):
        return sum([hladac(v) for v in vec])

    elif not isinstance(vec, dict):
        return 0

    elif "red" in vec.values():
        return 0

    return hladac(list(vec.values()))


print(hladac(json.loads(udaj)))

# vysledok je 65402
# inspiracia a zistil som ze existuje json
