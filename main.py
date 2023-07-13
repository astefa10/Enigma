import utils
from plugboard import Plugboard
from reflectors import Reflector
from rotors import *
from enigma import Enigma

def main():
    reflector = Reflector('B')
    rotors = [Rotor('I'), Rotor('II'), Rotor('III')]
    plugboard = Plugboard()
    enigma_machine = Enigma(reflector, rotors, plugboard)

    while True:
        print("\n----- Main Menu -----")
        print("1. Select reflector type")
        print("2. Select rotor types")
        print("3. Modify plugboard connections")
        print('4. View current machine state')
        print("5. Encrypt/Decrypt message")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
                reflector = utils.generate_reflector()

        elif choice == "2":
            utils.run_rotors_menu(rotors)
        
        elif choice == '3':
            utils.run_plugboard_menu(plugboard)
        
        elif choice == '4':
            utils.print_machine_state(reflector, rotors, plugboard)

        elif choice == '5':
            if None in rotors[:3]:
                print('Please choose rotors 1-3')
                continue
            if reflector.reflector_type not in ('B THIN', 'C THIN') and utils.get_num_rotors(rotors) == 4:
                print('Only thin reflectors can be used with the fourth rotor')
                continue
            if reflector.reflector_type in ('B THIN', 'C THIN') and utils.get_num_rotors(rotors) != 4:
                print('Please choose all four rotors before using a thin reflector')
                continue
                
            enigma_machine = Enigma(reflector, rotors, plugboard)
            message = input('Enter the plaintext message to encrypt/decrypt: ')
            encrypted_message = enigma_machine.encrypt(message)
            print('Ciphertext message:', encrypted_message)
        
        elif choice == '6':
            print('Exiting.')
            break

        else:
            print('Invalid choice. Please try again.') 

if __name__ == '__main__':
    main()