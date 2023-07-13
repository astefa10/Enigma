import utils
class Enigma:
    def __init__(self, reflector, rotors, plugboard):
        self.reflector = reflector
        self.rotors = rotors
        self.plugboard = plugboard

    def encrypt(self, message):
        message = utils.parse_message(message)
        message = message.upper()
        encrypted_message = ''
        for letter in message:

            # rotate third rotor
            turnover = True
            for rotor in self.rotors[::-1]:
                if rotor is not None:
                    if turnover:
                        turnover = rotor.rotate()

            encrypted_letter = letter
            # through plugboard
            encrypted_letter = self.plugboard.pairings[encrypted_letter]

            # through rotors, right to left
            for rotor in self.rotors[::-1]:
                if rotor is not None:
                    encrypted_letter = rotor.forward_map(encrypted_letter)

            # through reflector
            encrypted_letter = self.reflector.pairings[encrypted_letter]

            # through rotors, left to right
            for rotor in self.rotors:
                if rotor is not None:
                    encrypted_letter = rotor.backward_map(encrypted_letter)

            # through plugboard
            encrypted_letter = self.plugboard.pairings[encrypted_letter]
        
            encrypted_message += encrypted_letter
        
        return encrypted_message
    

