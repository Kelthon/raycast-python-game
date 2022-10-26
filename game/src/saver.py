from datetime import datetime
from typing import Dict

class Saver():

    def __init__(self) -> None:
        pass

    def save(self, name: str, state: Dict):
        date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        text = f"date={date}\n"

        for i, j in state.items():
            text += i + f"={j}\n"

        save = open(name, "w")
        save.write(text)
        save.close()

    def load(self, name: str) -> Dict:
        save = open(name, "r")
        state = {}
        for line in save:
            key, value = line.split("=")
            value = value.replace("\n", "")
            state[key] = value
        save.close()

        return state
        
    def delete(self, name: str) -> Dict:
        save = open(name, "w")
        save.close()
