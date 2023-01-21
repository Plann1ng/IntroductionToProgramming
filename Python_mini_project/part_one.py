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

def main(path):
    trial = count_unique(path)
    print(f'{trial}\n')
    check = count_occurencies(path)
    sortd_dct = sorted(check.items(), key=lambda tpl: -tpl[1])
    print("10 most frequent used words:\n")
    for i in range(10):
        print(f'{sortd_dct[i][0]}\t{sortd_dct[i][1]}')

print("100k sentences")
main(os.getcwd() + "/Outpath_100k_sentences.txt")
print("\nholy grail")
main(os.getcwd() + "/Outpath_holy_grail.txt")
