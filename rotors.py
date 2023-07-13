from typing import Any
import utils

class Rotor:
    available_rotor_types = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    def __init__(self, rotor_type):
        self.pos = 0
        self.rotor_type = rotor_type.upper()
        self.ring_setting = 0
        
        if rotor_type == "I":
            self.notch = {utils.ALPHABET.index('Q')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'))
        elif rotor_type == "II":
            self.notch = {utils.ALPHABET.index('E')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'AJDKSIRUXBLHWTMCQGZNPYFVOE'))
        elif rotor_type == "III":
            self.notch = {utils.ALPHABET.index('V')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'BDFHJLCPRTXVZNYEIWGAKMUSQO'))
        elif rotor_type == "IV":
            self.notch = {utils.ALPHABET.index('J')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'ESOVPZJAYQUIRHXLNFTGKDCMWB'))
        elif rotor_type == "V":
            self.notch = {utils.ALPHABET.index('Z')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'VZBRGITYUPSDNHLXAWMJQOFECK'))
        elif rotor_type == "VI":
            self.notch = {utils.ALPHABET.index('Z'), utils.ALPHABET.index('M')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'JPGVOUMFYQBENHZRDKASXLICTW'))
        elif rotor_type == "VII":
            self.notch = {utils.ALPHABET.index('Z'), utils.ALPHABET.index('M')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'NZJHGRCXMYSWBOUFAIVLPEKQDT'))
        elif rotor_type == "VIII":
            self.notch = {utils.ALPHABET.index('Z'), utils.ALPHABET.index('M')}
            self.pairings =  dict(zip(utils.ALPHABET_NUM, 'FKQHTLXOCBJSPDZRAMEWNIUYGV'))
        else:
            raise ValueError("Invalid rotor type")
        
        self.available_rotor_types.remove(rotor_type)
        
    def rotate(self):      
        turnover = False  
        if self.notch == (self.pos + self.ring_setting) % len(self.pairings):
            turnover = True
        self.pos = (self.pos + 1) % len(self.pairings)
        return turnover

    def forward_map(self, letter):
        index = utils.ALPHABET.index(letter)
        offset_index = (index + self.pos - self.ring_setting) % len(self.pairings)
        mapped_letter = self.pairings[offset_index]

        index = utils.ALPHABET.index(mapped_letter)
        encrypted_index = (index - self.pos + self.ring_setting) % len(utils.ALPHABET)
        encrypted_letter = utils.ALPHABET[encrypted_index]

        return encrypted_letter
           
    def backward_map(self, letter):
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

    def change_position(self, pos):
        self.pos = pos

    def change_ring_setting(self, ring_setting):
        self.ring_setting = ring_setting
