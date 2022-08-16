from polynomial import Polynomial


class Point:
    def __init__(self, x=None, y=None, a=-1, d=(-121665 * pow(121666, -1, 2**255 - 19)), m=(2**255 - 19)): # lower d is the mod_inv of 121666 for modulus m
        self.x: int = x
        self.y: int = y
        self.a = a ## Quick hack
        self.d = d
        self.m = m
        
    
    def encode(self):
        y_b = bytearray(self.y.to_bytes(32, 'little'))
        if y_b[31] | (self.x & 1):
            y_b[31] = 128
        else:
            y_b[31] = 0
        return bytes(y_b)
    
    def encodePoint(self):
        point = self
        x_lsb = point.x & 1  # Correct
       

        y_b = bytearray(point.y.to_bytes(32, 'little'))
        

        if x_lsb == 1:
            mask = 128
            new_msb = y_b[31] | mask
        elif x_lsb == 0: 
            mask = 127
            new_msb = y_b[31] & mask

        y_b[31] = new_msb

        y_b = bytes(y_b)

        return y_b
    
    def __add__(self, other):
        new_point = Point()
        if isinstance(other, Point):
            new_point.x = ((self.x*other.y + self.y*other.x) * pow(1 + self.d*self.x*other.x*self.y*other.y, -1, self.m)) % self.m  ## https://bibliotecadigital.ipb.pt/bitstream/10198/24067/1/Nakai_Eduardo.pdf  I added finite fields here
            new_point.y = ((self.y*other.y - self.a*self.x*other.x) * pow(1 - self.d*self.x*other.x*self.y*other.y, -1, self.m)) % self.m # Point addition and doubling are the same for twisted edwards curves
            # i am 90% sure this is correct
            return new_point
    
    def __mul__(self, multiplier: int):
        new_point = Point()
        new_point.x = self.x
        new_point.y = self.y

        multiplier = list(bin(multiplier)[3:])

        for x_a in multiplier:
            new_point = new_point + new_point  #2P
            if x_a == '1':
                new_point = new_point + self  #P + G
        return new_point
    
   