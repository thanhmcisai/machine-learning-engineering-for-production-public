import pickle
import numpy as np
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, conlist

# Change comment

app = FastAPI(title="Predicting Wine Class with batching")

# Open classifier in global scope

# Old model with accuracy 91%
# with open("models/wine.pkl", "rb") as file:
#     clf = pickle.load(file)

# Fail model with accuracy 33,33%
# with open("models/wine-95.pkl", "rb") as file:
#     clf = pickle.load(file)

# New model with accuracy 95%
with open("models/wine-95-fixed.pkl", "rb") as file:
    clf = pickle.load(file)
    
class Wine(BaseModel):
    batches: List[conlist(item_type=float, min_items=13, max_items=13)]


@app.post("/predict")
def predict(wine: Wine):
    batches = wine.batches
    np_batches = np.array(batches)
    pred = clf.predict(np_batches).tolist()
    return {"Prediction": pred}
