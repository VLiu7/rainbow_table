import string
class Config:
    def __init__(self) -> None:
        self.COLS=2048
        self.ROWS=100 #28181820.515625
        self.MIN_PW_LENGTH=5
        self.MAX_PW_LENGTH=6
        self.LETTER_SET=string.ascii_letters + string.digits
        self.CORES=24

def get_config():
    return Config()