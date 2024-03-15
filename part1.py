import time

class Device:
    def __init__(self, name: str):
        self.name = name
        self.power: bool = False
        
    def turn_on(self) -> None:
        print(f"Turning {self.__class__.__name__} {self.name} on")
        self.power = True
        
    def turn_off(self) -> None:
        print(f"Turning {self.__class__.__name__} {self.name} off")
        self.power = False
        
    def check_on(self) -> bool:
        return True if self.power else False
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Name: {self.name}, Power: {self.power}"
        
        
class CoffeeMachine(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.water_level: float = 0
        self.coffee_level: float = 0
        
    def refill(self, water_level: float, coffee_level: float):
        if 0 <= water_level < 100:
            self.water_level = water_level
        elif water_level < 0:
            self.water_level = 0
        else:
            self.water_level = 100
            
        if 0 <= coffee_level < 100:
            self.water_level = coffee_level
        elif coffee_level < 0:
            self.coffee_level = 0
        else:
            self.coffee_level = 100    
        
    def make_coffee(self) -> None:
        if self.check_on():
            if self.water_level >= 10 and self.coffee_level >= 5:
                print("Boiling water")
                print("Dripping coffee through filter")
                print("Pouring into cup")
                print("Adding Sugar and Milk")
                
                self.water_level -= 10
                self.coffee_level -= 5
            else:
                print("Not enough water or coffee grains")
        else:
            print("Turn on the machine before using!")
            
    def __repr__(self) -> str:
        return super().__repr__() + f", Water: {self.water_level}, Coffee: {self.coffee_level})"
            

class Blender(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.speed: int = 1
        
    def turn_on(self, speed=1) -> None:
        super().turn_on()
        self.set_speed(speed)
        
    def set_speed(self, speed: int) -> None:
        if 1 <= speed <= 5:
            self.speed = speed
        elif speed < 1:
            self.speed = 1
        else:
            self.speed = 5
            
    def blend(self, products: float) -> None:
        if self.check_on():
            if products <= 0:
                print("You can't blend nothing!")
            else:
                print(f"Blending {products} kg of products")
                while True:
                    print("Blending...")
                    time.sleep(1)
                    products -= 0.1 * self.speed
                    if products <= 0:
                        break
                    else:
                        print(f"{products} kg of products remaining")
                print("Your blend is ready")
        else:
            print("Turn on the machine before using!")
        
    def __str__(self) -> str:
        return super().__repr__() + f", Speed: {self.speed})"
    

class MeatGrinder(Device):
    def __init__(self, name: str):
        super().__init__(name)
        self.speed: int = 1
        
    def turn_on(self, speed=1) -> None:
        super().turn_on()
        self.set_speed(speed)
        
    def set_speed(self, speed: int) -> None:
        if 1 <= speed <= 5:
            self.speed = speed
        elif speed < 1:
            self.speed = 1
        else:
            self.speed = 5
            
    def mince(self, meat: float) -> None:
        if self.check_on():
            if meat <= 0:
                print("You can't mince nothing!")
            else:
                print(f"Mincing {meat} kg of meat")
                while True:
                    print("Mincing...")
                    time.sleep(1)
                    meat -= 0.1 * self.speed
                    if meat <= 0:
                        break
                    else:
                        print(f"{round(meat,2)} kg of meat remaining")
                print("Your mince is ready")
        else:
            print("Turn on the machine before using!")
        
    def __str__(self) -> str:
        return super().__repr__() + f", Speed: {self.speed})"
    
    
cm = CoffeeMachine("DeLonghi")
blender = Blender("Bosch")
mg = MeatGrinder("KitchenAid")

