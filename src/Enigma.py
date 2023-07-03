from Rotor import Rotor
from Plugboard import Plugboard
from Reflector import Reflector
from Keyboard import Keyboard

class Enigma:
    rotor_Dict = {  "I":['EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q'],
                    "II":['AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E'],
                    "III":['BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V'],
                    "IV":['ESOVPZJAYQUIRHXLNFTGKDCMWB', 'J']
                    }
    reflector_Dict = {'UKW-A':'EJMZALYXVBWFCRQUONTSPIKHGD',
                    'UKW-B':'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                    'UKW-C':'FVPJIAOYEDRZXWGCTKUQSBNMHL'
                    }
    # Left to Right (A, B, C)
    def __init__(self, RotorA_num, RotorB_num, RotorC_num, ukw, plug_connections, rotor_positions, ring_settings):
        self.ukw = ukw
        self.RotorA_num = RotorA_num
        self.RotorB_num = RotorB_num
        self.RotorC_num = RotorC_num
        self.plug_connections = plug_connections
        self.encryption_path = []
        self.Kb = Keyboard()
        self.RotorA = Rotor(self.rotor_Dict[RotorA_num][0], self.rotor_Dict[RotorA_num][1])
        self.RotorB = Rotor(self.rotor_Dict[RotorB_num][0], self.rotor_Dict[RotorB_num][1])
        self.RotorC = Rotor(self.rotor_Dict[RotorC_num][0], self.rotor_Dict[RotorC_num][1])
        self.ReflectorRotor = Reflector(self.reflector_Dict[ukw])
        self.Board = Plugboard(plug_connections)

        self.setRotorSettings(rotor_positions, ring_settings)
    
    def setRotorSettings(self, rotor_positions, ring_settings):
        self.RotorA.setRing(self.Kb.forward(ring_settings[0]))
        self.RotorB.setRing(self.Kb.forward(ring_settings[1]))
        self.RotorC.setRing(self.Kb.forward(ring_settings[2]))

        self.RotorA.step(self.Kb.forward(rotor_positions[0]))
        self.RotorB.step(self.Kb.forward(rotor_positions[1]))
        self.RotorC.step(self.Kb.forward(rotor_positions[2]))
    
    # run the letter through the machine to encode it
    def encode(self, input_String) -> str:

        output_String = ''
        self.encryption_path = []
        for letter in input_String:
            # rotate rotors
            # check if All Rotor needs to rotate
            if self.RotorC.rotor_alphabet[0] == self.RotorC.notch and self.RotorB.rotor_alphabet[0] == self.RotorB.notch:
                self.RotorA.step(1)
                self.RotorB.step(1)
                self.RotorC.step(1)
            # Double step scenario
            elif self.RotorB.rotor_alphabet[0] == self.RotorB.notch:
                self.RotorA.step(1)
                self.RotorB.step(1)
                self.RotorC.step(1)
            # check if B Rotor needs to rotate
            elif self.RotorC.rotor_alphabet[0] == self.RotorC.notch:
                self.RotorB.step(1)
                self.RotorC.step(1)
            # right rotor step
            else: 
                self.RotorC.step(1)

            # foward
            signal = self.Kb.forward(letter)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            for component in [self.Board, self.RotorC, self.RotorB, self.RotorA]:
                signal = component.forward(signal)
                self.encryption_path.append(signal)
                self.encryption_path.append(signal)
            # Reflector
            signal = self.ReflectorRotor.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            # backward
            for component in [self.RotorA, self.RotorB, self.RotorC, self.Board]:
                signal = component.backward(signal)
                self.encryption_path.append(signal)
                self.encryption_path.append(signal)
            '''
            signal = self.Board.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.RotorC.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.RotorB.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.RotorA.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            # signal is reflected back
            signal = self.ReflectorRotor.forward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            # back into the rotors
            signal = self.RotorA.backward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.RotorB.backward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.RotorC.backward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            signal = self.Board.backward(signal)
            self.encryption_path.append(signal)
            self.encryption_path.append(signal)
            '''
            output_String += self.Kb.backward(signal)
        return output_String

# testMachine = Enigma('IV', 'II', 'I', 'UKW-B', 'AB CD EF', 'CAT', 'EZB')
# print(testMachine.encode("THISCOOLENIGMAMACHINE")) # IEOVQMZCIGPYCVBYPDXHS
