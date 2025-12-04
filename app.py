import joblib

with open("Frequency_maps.joblib", "rb") as f:
    maps = joblib.load(f)

print("Keys in frequency_maps:")
for k in maps.keys():
    print(k)