from machine import Pin
import time

# Connect switch pins 1, 2, 4, 8 to D0–D3 (GPIO 0–3)
pins = [
    Pin(26, Pin.IN, Pin.PULL_DOWN),  # Rotary Pin 1
    Pin(29, Pin.IN, Pin.PULL_DOWN),  # Rotary Pin 2
    Pin(27, Pin.IN, Pin.PULL_DOWN),  # Rotary Pin 4
    Pin(28, Pin.IN, Pin.PULL_DOWN)  # Rotary Pin 8
]

rotaryMap = {
    (1, 1, 1, 1): 0,
    (0, 1, 1, 1): 1,
    (1, 0, 1, 1): 2,
    (0, 0, 1, 1): 3,
    (1, 1, 0, 1): 4,
    (0, 1, 0, 1): 5,
    (1, 0, 0, 1): 6,
    (0, 0, 0, 1): 7,
    (1, 1, 1, 0): 8,
    (0, 1, 1, 0): 9
}
map(sum, [1,2,3])
def setPWMlimit(int) -> None:
    ...

def mode0():
    """
    BYPASS MODE
    This mode disables the speed controller entirely and allows the motor to draw any current it wants 
    """
    print("BYPASS MODE")
def mode1():
    """
    
    """
    print("TEST MODE")

def mode2():
    print("mode2")

def mode3():
    print("mode3")

def mode4():
    print("mode4")

def mode5():
    print("mode5")

def mode6():
    print("mode6")

def mode7():
    print("mode7")

def mode8():
    print("mode8")

def mode9():
    print("mode9")

def err():
    print("ERROR")

prev = None

functions = [mode0, mode1, mode2, mode3, mode4, mode5, mode6, mode7, mode8, mode9]



while True:
    pinValues = tuple(pin.value() for pin in pins)
    position = rotaryMap.get(pinValues, None)

    if position is not None and position != prev:
        #print(f"Switch Position: {position}")
        prev = position
        functions[position]()
    elif position is None:
        print(f"Unknown position: {pinValues}")
        err()

    time.sleep(0.2)
    
    
    # MAIN EXECTION LOOP
   
    
    
    


