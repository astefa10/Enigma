import utils

class Plugboard:
    # Initialize an empty plugboard.
    def __init__(self):
        self.pairings = {letter: letter for letter in utils.ALPHABET}

    # Add a new plug pairing.
    def add_pairing(self, plug_a: str, plug_b: str) -> None:
        plug_a, plug_b = plug_a.upper(), plug_b.upper()
        self.pairings[plug_a] = plug_b
        self.pairings[plug_b] = plug_a

    # Remove an exisiting plug pairing.
    def remove_pairing(self, plug: str) -> None:
        plug = plug.upper()
        if plug in self.pairings:
            connected_plug = self.pairings[plug]
            self.pairings[plug] = plug
            self.pairings[connected_plug] = connected_plug
        else:
            raise ValueError('Invalid plug character')

    # Process a plug through the plugboard.
    def process_input(self, plug: str) -> str:
        return self.pairings.get(plug, plug)
