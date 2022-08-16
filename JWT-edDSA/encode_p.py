from point import Point
class EncodeP:
    def encodePoint(point: Point):
        x_lsb = point.x & 1  # Correct
        print("X: "  + str(x_lsb))

        y_b = bytearray(point.y.to_bytes(32, 'little'))
        print("RY: " + str(point.y))
        print("MSB Ry " + str(y_b[31])) # Got it COREECT

        if x_lsb == 1:
            mask = 128
            new_msb = y_b[31] | mask
        elif x_lsb == 0: 
            mask = 127
            new_msb = y_b[31] & mask

        print("NEW MSB " + str(new_msb))

        y_b[31] = new_msb

        print(bytes(y_b))
        y_b = bytes(y_b)

        return y_b
    
    
    