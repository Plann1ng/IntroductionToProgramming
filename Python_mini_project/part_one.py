import os

def count_unique(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.split()
        return len(set(text))


def count_occurencies(path):
    empty = {}
    with open(path, "r", encoding='utf-8') as f:
        text = f.read()
        text = text.split()
        for keys in text:
            if len(keys) > 4:
                if keys not in empty:
                    empty[keys] = 0
                empty[keys] += 1
    return empty

