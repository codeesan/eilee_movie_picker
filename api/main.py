from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    eilee_list = ["Box Trolls",
                    "Onward",
                    "Dark Crystal",
                    "Back to the Outback",
                    "Wizard of Oz",
                    "Finding Nemo",
                    "Monsters Inc",
                    "BFG",
                    "Jurassic Park",
                    "Princess Bride"]
    random_number = random.randint(0,len(eilee_list)-1)
    return {"Movie": eilee_list[random_number]}
