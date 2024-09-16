
from typing import Literal
INPUT = Literal["INPUT"]
OUTPUT = Literal["OUTPUT"]

class PinError(Exception):
    pass

class Pin:

    def __init__(self, pinNumber: int, mode: Literal["INPUT", "OUTPUT"]) -> None:
        self.__pinNumber = pinNumber
        self.__mode = mode
        self.__value = 0
    
    def getPin(self) -> int:
        return self.__pinNumber
    
    def getMode(self) -> Literal["INPUT", "OUTPUT"]:
        return self.__mode
    
    def getValue(self) -> int:
        if self.__mode == "OUTPUT":
            raise PinError("Cannot read from output pin")
        else:
            return self.__value

    def setValue(self, value: int) -> None:
        if self.__mode == "INPUT":
            raise PinError("Cannot write to input pin")
        else:
            self.__value = value
            print(f"Writing {value} to pin {self.__pinNumber}")
            ## Code to write to pin goes here   

        return None

    writeValue = setValue
    readValue = getValue





