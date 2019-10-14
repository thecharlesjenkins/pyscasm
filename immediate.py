class Immediate:
    def __init__(self, val: int):
        if val >= 2**16 or val <= -2**16:
            raise Exception(f"Immediate with value {val} doesn't fit in 16 bits")
        self.val = val