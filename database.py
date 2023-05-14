import os
import json

with open(os.path.join(os.getcwd(), "fullDB.json"), "r") as f:
    data = json.loads(f.read())

    for item in data:
        if item["model"] == "wine_tasting.experiences":
            print(item)
