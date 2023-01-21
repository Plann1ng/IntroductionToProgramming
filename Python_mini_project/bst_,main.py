# from dataclasses import dataclass
import BstMap as bst

# Program starts
# Add pairs
d = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41, "Adam": 27, "Ceve": 37}
map = bst.BstMap()
for k, v in d.items():
    map.put(k, v)
print(map.to_string())        # { (Adam,27) (Ceve,37) (Ella,39) (Fred,44) (Owen,40) (Zoe,41) }
print("Size:", map.size())    # 6

# Override existing values
print("\nOverride existing values")
map.put("Zoe", 99)
map.put("Ceve", 100)
print(map.to_string())       # { (Adam,27) (Ceve,100) (Ella,39) (Fred,44) (Owen,40) (Zoe,99) }

