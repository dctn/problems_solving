alphabet_dict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
rotor_I_wire = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
rotor_II_wire = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
rotor_III_wire = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

class Rotar:
    def __init__(self, setting, wire):
        self.setting = alphabet_dict[setting.upper()]
        self.wire = wire.copy()
        for i in range(self.setting):
            self.wire.append(self.wire.pop(0))

    def encode(self, letter_no):
        return self.wire[letter_no]

    def move(self):
        if self.setting < 25:
            self.setting += 1
            self.wire.append(self.wire.pop(0))
        else:
            self.setting = 0

    def move_back(self):
        if self.setting > 0:
            self.setting -= 1
            self.wire.insert(0, self.wire.pop())
        else:
            self.setting = 25

class Enigma:
    def __init__(self, rotar_1: Rotar, rotar_2: Rotar, rotar_3: Rotar):
        self.rotar_1 = rotar_1
        self.rotar_2 = rotar_2
        self.rotar_3 = rotar_3

    def encode(self, letter):
        letter_no = alphabet_dict[letter.upper()]
        rotar_1_out = self.rotar_1.encode(letter_no)
        rotar_2_out = self.rotar_2.encode(rotar_1_out)
        rotar_3_out = self.rotar_3.encode(rotar_2_out)

        self.rotar_1.move()
        if self.rotar_1.setting == 0:
            self.rotar_2.move()
        if self.rotar_2.setting == 0:
            self.rotar_3.move()
        return rotar_3_out

    def decode(self, letter):
        letter_no = alphabet_dict[letter]
        rotar_3_idx = self.rotar_3.wire.index(letter_no)
        rotar_2_idx = self.rotar_2.wire.index(rotar_3_idx)
        rotar_1_idx = self.rotar_1.wire.index(rotar_2_idx)

        self.rotar_1.move_back()
        if self.rotar_1.setting == 25:
            self.rotar_2.move_back()
        if self.rotar_2.setting == 25:
            self.rotar_3.move_back()
        return rotar_1_idx

    def encoder(self, letters):
        result = []
        for letter in letters:
            encode_no = self.encode(letter)
            result.append(list(alphabet_dict.keys())[encode_no])
        return result

    def decoder(self, letters):
        result = []
        for letter in letters:
            decode_no = self.decode(letter.upper())
            result.append(list(alphabet_dict.keys())[decode_no])
        return result

r1 = Rotar('a', wire=rotor_I_wire)
r2 = Rotar('b', wire=rotor_II_wire)
r3 = Rotar('c', wire=rotor_III_wire)
enigma = Enigma(r1, r2, r3)
encoded = enigma.encoder('ABCD')
print('encoded:', encoded)

r1 = Rotar('a', wire=rotor_I_wire)
r2 = Rotar('b', wire=rotor_II_wire)
r3 = Rotar('c', wire=rotor_III_wire)
enigma = Enigma(r1, r2, r3)
print('decoded:', enigma.decoder(''.join(encoded)))
