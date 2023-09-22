# Enigma
Enigma Machine Simulator

This Python project simulates the operation of the Enigma machine, a famous encryption device used during World War II. The simulator allows users to encrypt and decrypt messages using various configurations of the Enigma machine.
Features

    Multiple Rotors and Reflectors: The simulator supports multiple types of rotors (I to VIII) and reflectors (A, B, C, B THIN, C THIN).
    Plugboard Functionality: Users can establish connections between letters on the plugboard to further modify the encryption.
    Interactive Menus: The program provides interactive menus for selecting reflector types, rotor types, and modifying plugboard connections.
    Machine State: View the current state of the machine, including the rotor types, positions, notches, ring settings, and plugboard pairings.

Files

    main.py: The main entry point of the program. Allows the user to interact with the Enigma machine through various menus.
    plugboard.py: Contains the Plugboard class which simulates the operation of the Enigma machine's plugboard.
    reflectors.py: Contains the Reflector class which simulates the operation of the Enigma machine's reflectors.
    rotors.py: Contains the Rotor class which simulates the operation of the Enigma machine's rotors.
    enigma.py: Contains the Enigma class which brings together all components of the machine and manages the encryption and decryption processes.
    utils.py: Contains utility functions and menus for managing rotors, reflectors, and the plugboard.

Usage

    Run the main.py script.
    Navigate through the main menu to select reflectors, rotor types, and modify plugboard connections.
    Encrypt or decrypt messages based on your selected configuration.
    View the current state of the Enigma machine at any time through the main menu.

    Menu Options

        When you run main.py, the simulator presents you with the main menu, which offers the following options:

        1. Select reflector type: Choose from available reflector types (A, B, C, B THIN, C THIN). Reflectors are responsible for reflecting the electrical signal back through the rotors in the Enigma machine.

        2. Select rotor types: You can select the types of rotors you want to use. This option lets you choose from rotor types I through VIII. Each rotor has a different internal wiring configuration, affecting the encrypted output.

        3. Modify plugboard connections: The plugboard is a part of the Enigma machine that allowed for additional scrambling of the input. This option lets you establish or remove connections between pairs of letters. For example, connecting A to B means that every A in the plaintext gets encrypted as B and vice versa.

        4. View current machine state: Displays the current configuration of the Enigma machine, including:
            The selected reflector type
            Rotor types, their positions, notches, and ring settings
            Current plugboard connections

        5. Encrypt/Decrypt message: Allows you to input a message that you want to encrypt or decrypt based on the current machine configuration. Non-alphabetical characters are removed from the input message.

        6. Quit: Exit the simulator.

    In addition, there are sub-menus when you choose to modify the rotors or the plugboard:
    
    Rotor Menu

        Add rotor: Allows you to add a rotor to the Enigma machine. The rotor types used are removed from the available options.
        Remove rotor: Remove a rotor from the current configuration, making its type available again.
        Change rotor: Swap out a rotor for a different type.
        Modify rotor settings: Alter a rotor's position and ring setting. Each rotor can be set to a position ranging from 0 (A) to 25 (Z).

    Plugboard Menu

        Add pairing: Establish a new letter connection on the plugboard.
        Remove pairing: Break an existing letter connection.
        Back to main menu: Return to the main menu from the plugboard menu.

Limitations

    Messages are restricted to alphabetic characters. All non-alphabetical characters are removed before encryption.
