REFLECTOR_CONFIGS: dict[str,dict] = {
        'A': {'pairings': dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'EJMZALYXVBWFCRQUONTSPIKHGD'))},
        'B': {'pairings': dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'YRUHQSLDPXNGOKMIEBFZCWVJAT'))},
        'C': {'pairings': dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FVPJIAOYEDRZXWGCTKUQSBNMHL'))},
        'B THIN': {'pairings': dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ENKQAUYWJICOPBLMDXZVFTHRGS'))},
        'C THIN': {'pairings': dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'))},
}

class Reflector:
    
    # Initialize a reflector with the given type
    def __init__(self, reflector_type):
        self.reflector_type = reflector_type.upper()

        if self.reflector_type in REFLECTOR_CONFIGS:
            self.pairings = REFLECTOR_CONFIGS[self.reflector_type]['pairings']
        else:
            raise ValueError("Invalid reflector type")
