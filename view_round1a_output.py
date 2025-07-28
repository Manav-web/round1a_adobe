import json
import os

# Use the correct filename
output_file = os.path.join("output", "valid_japanese_sample.json")

with open(output_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print("\n📘 Round 1A Outline Output:\n")
for entry in data["outline"]:
    print(f"{entry['level']}: {entry['text']} (Page {entry['page']})")
