from src.prop import Prop 

class Lightsaber(Prop):
    
    def __init__(self):
        super().__init__("Lightsaber")

    def make_sound(self):
        return "bzzzzz"

