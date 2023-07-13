import random
import string
from rotors import Rotor
from reflectors import Reflector

ALPHABET = list(string.ascii_uppercase)
ALPHABET_NUM = [x for x in range(26)]
VALID_REFLECTOR_TYPES = ['A', 'B', 'C', 'B THIN', 'C THIN']
VALID_ROTOR_TYPES = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']


def generate_rotor(rotors, index=None):
    while True:
        rotor_type_string = ', '.join(Rotor.available_rotor_types)      
        rotor_type = input('Enter the rotor type (' + rotor_type_string + '): ')
        try:
            rotor_type = validate_rotor_type(rotor_type)
            rotor = Rotor(rotor_type)
            if index is not None:
                rotors[index] = rotor
            else:
                first_index = rotors.index(None)
                rotors[first_index] = rotor
            return rotor
        except ValueError as e:
            print(str(e))

def validate_rotor_type(rotor_type):
    rotor_type = rotor_type.upper()

    if rotor_type not in VALID_ROTOR_TYPES:
        raise ValueError('Invalid rotor type')
    return rotor_type

def generate_reflector():
    while True:
        reflector_type = input('Enter the reflector type (A, B, C, B Thin, C Thin): ')
        try:
            reflector_type = validate_reflector_type(reflector_type)
            reflector = Reflector(reflector_type)
            return reflector
        except ValueError as e:
            print(str(e))

def validate_reflector_type(reflector_type):
    reflector_type = reflector_type.upper()
    
    if reflector_type not in VALID_REFLECTOR_TYPES:
        raise ValueError('Invalid reflector type')
    return reflector_type

def pos_to_letter(pos):
    if isinstance(pos, int):
        return ALPHABET[pos]
    
    # function is used for rotor position, and rotor notches
    # rotors VI, VII, and VIII have two notches
    return [ALPHABET[x] for x in pos]

def print_plugboard_pairings(pairings):
    processed_connections = set()

    print('Current plugboard pairings:')
    for letter, connection in pairings.items():
        if letter != connection and (letter, connection) not in processed_connections and (connection, letter) not in processed_connections:
            print(f"{letter} <-> {connection}")
            processed_connections.add((letter, connection))
    print('\n')

def print_machine_state(reflector, rotors, plugboard):
    print("\n----- Machine State -----")

    if reflector is not None:
        print(f"Reflector: {reflector.reflector_type}")
    else:
        print("Reflector: Not set")
    
    if rotors:
        info = ''
        i = 1
        for rotor in rotors:
            if rotor is not None:
                info += (f"\nRotor {i}: Type: {rotor.rotor_type}, "
                f"Position: {rotor.pos}({pos_to_letter(rotor.pos)}), "
                f"Notch: {rotor.notch}({pos_to_letter(rotor.notch)}), "
                f"Ring Setting: {rotor.ring_setting}({pos_to_letter(rotor.ring_setting)})")
                
            else:
                info += f'\nRotor {i}: Empty'
            i += 1
            
        print(info)
    else:
        print("Rotors not set")


    print_plugboard_pairings(plugboard.pairings)

def run_plugboard_menu(plugboard):
    while True:
                print_plugboard_pairings(plugboard.pairings)

                print("----- Plugboard Menu -----")
                print("1. Add pairing")
                print("2. Remove pairing")
                print("3. Back to main menu")
                plugboard_choice = input("Enter your choice (1-3): ")
            
                if plugboard_choice == '1':
                    connection = input('Enter two letters to connect connection (e.g., AB): ')
                    while (not connection.isalpha or len(connection) != 2):
                        print('Invalid input.')
                        connection = input('Enter two letters to connect connection (e.g., AB): ')

                    letter1, letter2 = connection
                    plugboard.remove_pairing(letter1)
                    plugboard.remove_pairing(letter2)
                    plugboard.add_pairing(letter1, letter2)

                elif plugboard_choice == '2':
                    letter = input('Enter the letter to remove the connection from (e.g., A): ')
                    while not letter.isalpha() or len(letter) != 1:
                        print('Invalid input.')
                        letter = input('Enter the letter to remove the connection from (e.g., A): ')
                    plugboard.remove_pairing(letter)

                elif plugboard_choice == '3':
                    print('Returning to main menu.')
                    break
                
                else:
                    print('Invalid choice. Please try again.')

def run_rotors_menu(rotors):
    while True:
                print("\n----- Rotor Menu -----")
                print("1. Add rotor")
                print("2. Remove rotor")
                print('3. Change rotor')
                print("4. Modify rotor settings")
                print("5. Back to main menu")
                rotor_choice = input("Enter your choice (1-4): ")

                if rotor_choice == "1":
                    if get_num_rotors(rotors) >= 4:
                          print('Maximum number of rotors reached. Cannot add more.')
                    else:
                          rotor = generate_rotor(rotors)
                          print('Rotor ' + rotor.rotor_type + ' added.')

                elif rotor_choice == '2':
                    num_rotors = get_num_rotors(rotors)
                    if num_rotors > 0:
                        mapped_choice = dict()
                        print("\n----- Rotors -----")
                        i = 1
                        for rotor in rotors:
                            if rotor is not None:
                                print(f'{i}. {rotor.rotor_type}')
                                mapped_choice[i] = rotors.index(rotor)
                                i += 1
                            else:
                                print('Empty')

                        print(f'{num_rotors+1}. Back to main menu')
                        selected_rotor = input(f"Enter your choice (1-{num_rotors+1}): ")
                        
                        if selected_rotor == str(num_rotors+1):
                            print('Returning to rotor menu.')
                            break
                        else: 
                            try:
                                selected_rotor = int(selected_rotor)
                                if selected_rotor <= num_rotors:
                                    remove_motor(rotors, mapped_choice[selected_rotor])
                                else:
                                    print('Invalid choice. Please try again.')
                            except(ValueError):
                                print('Invalid choice. Please try again.')
                    
                    else:
                        print('Invalid choice. Please try again.')
                    
                elif rotor_choice == '3':
                    change_rotors(rotors)

                elif rotor_choice == '4':
                    if len(rotors) > 0:
                        run_rotors_submenu(rotors)
                    else:
                        print('No rotors to modify.')
                    continue
                
                elif rotor_choice == '5':
                    print('Returning to main menu.')
                    break
            
                else:
                    print('Invalid choice. Please try again.')

def run_rotors_submenu(rotors):
     num_rotors = get_num_rotors(rotors)
     if num_rotors == 0:
         print('Please select at least one rotor.')

     while True:
        print("\n----- Rotors -----")
        i = 1
        for rotor in rotors:
            if rotor is not None:
                print(f'{i}. {rotor.rotor_type}')
                i += 1
            else:
                print('Empty')

        print(f'{num_rotors+1}. Back to main menu')
        selected_rotor = input(f"Enter your choice (1-{num_rotors+1}): ")

        if selected_rotor == str(num_rotors+1):
            print('Returning to rotor menu.')
            break
        else: 
            try:
                selected_rotor = int(selected_rotor)
                if selected_rotor <= num_rotors:
                    run_single_rotor_menu(rotors[selected_rotor-1], selected_rotor)
                else:
                    print('Invalid choice. Please try again.')
            except(ValueError):
                print('Invalid choice. Please try again.')

def run_single_rotor_menu(rotor, rotor_num):
    while True:
        print(f"\n----- Rotor {rotor_num}-----")
        print(f'Rotor type: {rotor.rotor_type}',
              f'\nCurrent position: {rotor.pos} ({pos_to_letter(rotor.pos)})',  
              f'\nNotche(s): {str(rotor.notch)[1:-1]} (' + ' '.join([pos_to_letter(val) for val in rotor.notch]) + ')', 
              f'\nRing Setting: {rotor.ring_setting} ({pos_to_letter(rotor.ring_setting)})')
        
        print("1. Change rotor position")
        print("2. Change ring setting")
        print("3. Back to main menu")
        mod_choice = input('Enter your choice: ')

        if mod_choice == '1':
            new_pos = input('Enter a position between 0(A) - 25(Z): ')

            if len(new_pos) == 1 and new_pos.isalpha():
                new_pos = new_pos.upper()
                new_pos = ALPHABET.index(new_pos)
                rotor.change_position(new_pos)
            else:
                try:
                    new_pos = int(new_pos)
                    if 0 <= new_pos <= 25:
                        rotor.change_position(new_pos)
                    else:
                        print('Invalid choice. Please try again.')
                except ValueError:
                    print('Invalid choice. Please try again.')

        if mod_choice == '2':
            ring_setting = input('Enter a position between 0(A) - 25(Z): ')

            if len(ring_setting) == 1 and ring_setting.isalpha():
                ring_setting = ring_setting.upper()
                ring_setting = ALPHABET.index(ring_setting)
                rotor.change_ring_setting(ring_setting)

            else:
                try:
                    ring_setting = int(ring_setting)
                    if 0 <= ring_setting <= 25:
                        rotor.change_ring_setting(ring_setting)
                    else:
                        print('Invalid choice. Please try again.')
                except ValueError:
                    print('Invalid choice. Please try again.')
                
        elif mod_choice == '3':
            break

def get_num_rotors(rotors):
    num_rotors = 0
    for rotor in rotors:
        if rotor is not None:
            num_rotors += 1

    return num_rotors

def remove_motor(rotors, index):
    Rotor.available_rotor_types.append(rotors[index].rotor_type)
    Rotor.available_rotor_types.sort()
    rotors[index] = None

def parse_message(message):
    parsed_message = ''.join(ch for ch in message if ch.isalpha())
    removed = set(message).difference(set(parsed_message))
    print('Removed: ' + ','.join(removed) + ' from message (only alphabetical characters allowed)')
    return parsed_message

def change_rotors(rotors):
    num_rotors = get_num_rotors(rotors)
    while True:
        print('Replace which rotor?')
        print("\n----- Rotors -----")
        i = 1
        for rotor in rotors:
            if rotor is not None:
                print(f'{i}. {rotor.rotor_type}')
                i += 1
            else:
                print('Empty')

        print(f'{num_rotors+1}. Back to main menu')
        selected_rotor = input(f"Enter your choice (1-{num_rotors+1}): ")

        if selected_rotor == str(num_rotors+1):
            print('Returning to rotor menu.')
            break
        else: 
            try:
                selected_rotor = int(selected_rotor) - 1
                if selected_rotor <= num_rotors:
                    print(f'Replace with which rotor?')
                    old_type = rotors[selected_rotor].rotor_type
                    
                    generate_rotor(rotors, selected_rotor)
                    Rotor.available_rotor_types.append(old_type)
                    Rotor.available_rotor_types.sort()
                    
                else:
                    print('Invalid choice. Please try again.')
            except(ValueError):
                print('Invalid choice. Please try again.')