class Immediate:
    def __init__(self, val: int):
        if val >= 2**16 or val <= -2**16:
            raise Exception(f"Immediate with value {val} doesn't fit in 11 bits")
        self.val = val
        if val > 0:
            self.smval = val & 0xFF
        else:
            self.smval = ((-val) & 0xFF) | 0b10000000000
