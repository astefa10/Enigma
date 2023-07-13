class Reflector:
    def __init__(self, reflector_type):
        self.reflector_type = reflector_type.upper()

        if self.reflector_type == "A":
            self.pairings = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EJMZALYXVBWFCRQUONTSPIKHGD'))
        elif self.reflector_type == "B":
            self.pairings = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'YRUHQSLDPXNGOKMIEBFZCWVJAT'))
        elif self.reflector_type == "C":
            self.pairings = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FVPJIAOYEDRZXWGCTKUQSBNMHL'))
        elif self.reflector_type == "B THIN":
            self.pairings = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ENKQAUYWJICOPBLMDXZVFTHRGS'))
        elif self.reflector_type == "C THIN":
            self.pairings = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'))
        else:
            raise ValueError("Invalid reflector type")
