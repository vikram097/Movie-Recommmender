import pickle, gzip

# apni badi pickle file load karo
with open("similarity.pkl", "rb") as f:
    data = pickle.load(f)

# compressed version save karo
with gzip.open("similarity_compressed.pkl.gz", "wb") as f:
    pickle.dump(data, f)

print("✅ similarity.pkl compressed and saved as similarity_compressed.pkl.gz")
