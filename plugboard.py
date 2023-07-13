import string
import utils

class Plugboard:
    def __init__(self):
        self.pairings = {letter: letter for letter in utils.ALPHABET}

    def add_pairing(self, plug_a, plug_b):
        plug_a, plug_b = plug_a.upper(), plug_b.upper()
        self.pairings[plug_a] = plug_b
        self.pairings[plug_b] = plug_a

    def remove_pairing(self, plug):
        plug = plug.upper()
        connected_plug = self.pairings[plug]
        self.pairings[plug] = plug
        self.pairings[connected_plug] = connected_plug

    def process_input(self, plug):
        return self.pairings.get(plug, plug)
