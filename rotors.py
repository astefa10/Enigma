from typing import Any
import utils
import string

ALPHABET = list(string.ascii_uppercase)
ALPHABET_NUM = [x for x in range(26)]
ROTOR_CONFIGS: dict[str,dict] = {
    'I': {'notch':{ALPHABET.index('Q')}, 'pairings':dict(zip(ALPHABET_NUM, 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'))},
    'II': {'notch':{ALPHABET.index('E')}, 'pairings':dict(zip(ALPHABET_NUM, 'AJDKSIRUXBLHWTMCQGZNPYFVOE'))},
    'III': {'notch':{ALPHABET.index('V')}, 'pairings':dict(zip(ALPHABET_NUM, 'BDFHJLCPRTXVZNYEIWGAKMUSQO'))},
    'IV': {'notch':{ALPHABET.index('J')}, 'pairings':dict(zip(ALPHABET_NUM, 'ESOVPZJAYQUIRHXLNFTGKDCMWB'))},
    'V': {'notch':{ALPHABET.index('Z')}, 'pairings':dict(zip(ALPHABET_NUM, 'VZBRGITYUPSDNHLXAWMJQOFECK'))},
    'VI': {'notch':{ALPHABET.index('Z'), ALPHABET.index('M')}, 'pairings':dict(zip(ALPHABET_NUM, 'JPGVOUMFYQBENHZRDKASXLICTW'))},
    'VII': {'notch':{ALPHABET.index('Z'), ALPHABET.index('M')}, 'pairings':dict(zip(ALPHABET_NUM, 'NZJHGRCXMYSWBOUFAIVLPEKQDT'))},
    'VIII': {'notch':{ALPHABET.index('Z'), ALPHABET.index('M')}, 'pairings':dict(zip(ALPHABET_NUM, 'FKQHTLXOCBJSPDZRAMEWNIUYGV'))}
}

class Rotor:
    available_rotor_types = {'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII'}

    # Initialize a rotor with the given type
    def __init__(self, rotor_type: str) -> None:
        self.pos = 0
        self.rotor_type = rotor_type.upper()
        self.ring_setting = 0
        
        if self.rotor_type in ROTOR_CONFIGS:
            self.notch = ROTOR_CONFIGS[self.rotor_type]['notch']
            self.pairings = ROTOR_CONFIGS[self.rotor_type]['pairings']
        else:
            raise ValueError(f"Invalid rotor type: {self.rotor_type}")
        
        self.available_rotor_types.remove(self.rotor_type)

        
    # Rotate the rotor by one position
    def rotate(self) -> bool:      
        turnover = False  
        current_position = (self.pos + self.ring_setting) % len(self.pairings)
        if current_position in self.notch:
            turnover = True
        self.pos = (self.pos + 1) % len(self.pairings)
        return turnover
    
    # Adjusts the given index based on the rotor's current position and ring setting, accounting for the direction of mapping (forward or backward).
    def _adjust_index(self, index: int, is_forward: bool) -> int:
        return (index + self.pos - self.ring_setting) if is_forward else (index - self.pos + self.ring_setting)

    # Map the letter in the forward direction through the rotor
    def forward_map(self, letter: str) -> str:
        index = utils.ALPHABET.index(letter)
        offset_index = (index + self.pos - self.ring_setting) % len(self.pairings)
        mapped_letter = self.pairings[offset_index]

        index = utils.ALPHABET.index(mapped_letter)
        encrypted_index = (index - self.pos + self.ring_setting) % len(utils.ALPHABET)
        encrypted_letter = utils.ALPHABET[encrypted_index]

        return encrypted_letter
           
    # Map the letter in the backward direction through the rotor
    def backward_map(self, letter: str) -> str:
        index = utils.ALPHABET.index(letter)
        mapped_index = (index + self.pos - self.ring_setting) % len(utils.ALPHABET)
        mapped_letter = utils.ALPHABET[mapped_index]
        
        for key,value in self.pairings.items():
            if value == mapped_letter:
                index = key
                break
        
        encrypted_index = (index - self.pos + self.ring_setting) % len(utils.ALPHABET)
        encrypted_letter = utils.ALPHABET[encrypted_index]


        return encrypted_letter

    # Change the rotor position
    def change_position(self, pos: int) -> None:
        self.pos = pos

    # Change the ring setting
    def change_ring_setting(self, ring_setting: int) -> None:
        self.ring_setting = ring_setting
