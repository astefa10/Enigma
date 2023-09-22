import utils
from typing import List, Optional
from rotors import Rotor
from reflectors import Reflector
from plugboard import Plugboard

class Enigma:
    def __init__(self, reflector: Reflector, rotors: List[Rotor], plugboard: Plugboard) -> None:
        self.reflector = reflector
        self.rotors = rotors
        self.plugboard = plugboard

    # Rotate rotors before encrypting each letter.
    def rotate_rotors(self):
        turnover = True
        for rotor in self.rotors[::-1]:
            if rotor:
                if turnover:
                    turnover = rotor.rotate()

    # Pass a letter through the rotors in either forward or backward direction.
    def pass_through_rotors(self, letter: str, is_forward: bool) -> str:
        for rotor in self.rotors[::-1] if is_forward else self.rotors:
            if rotor:
                letter = rotor.forward_map(letter) if is_forward else rotor.backward_map(letter)
        return letter

    # Encrypt a message using the Enigma machine.
    def encrypt(self, message: str) -> str:
        message = utils.parse_message(message).upper()
        encrypted_message = ''

        for letter in message:
            # Rotate the rotors
            self.rotate_rotors()

            # Encrypt letter through plugboard, rotors, and reflector
            encrypted_letter = self.plugboard.pairings[letter]
            encrypted_letter = self.pass_through_rotors(encrypted_letter, True)
            encrypted_letter = self.reflector.pairings[encrypted_letter]
            encrypted_letter = self.pass_through_rotors(encrypted_letter, False)
            encrypted_letter = self.plugboard.pairings[encrypted_letter]

            encrypted_message += encrypted_letter

        return encrypted_message
