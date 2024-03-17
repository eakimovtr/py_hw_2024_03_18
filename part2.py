from enum import Enum
import random

class Engine(Enum):
    STEAM_ENGINE = "Steam engine"
    STEAM_TURBINE = "Steam turbine"
    DIESEL_ENGINE = "Diesel engine"
    GAS_TURBINE = "Gas turbine"
    SAIL = "Sail"

# Superclass for all ships
class Ship:
    def __init__(self, name: str, deadweight: int, engine_type: Engine):
        self.__name: str = name
        self.__deadweight: int = deadweight
        self.__engine_type: Engine = engine_type
        
    def get_name(self) -> str:
        return self.__name
    
    def get_deadweight(self) -> int:
        return self.__deadweight
    
    def get_engine_type(self) -> Engine:
        return self.__engine_type
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.get_name()})"
    
    def __str__(self) -> str:
        return f"\n---SHIP INFO---\n{self.get_name()} {self.__class__.__name__}, Deadweight: {self.get_deadweight()} tons, Engine: {self.get_engine_type().value}"
    

# Superclass for all naval ships. All naval ships has some sort of artillery onboard.
# For armament we will use dictionary of (armament_type: no_of_charges) pairs.
class NavalShip(Ship):
    def __init__(self, name: str, deadweight: int, engine_type: Engine, artillery: int):
        super().__init__(name, deadweight, engine_type)
        self.armament: dict[str: int] = {"artillery": artillery}
    
    def check_armament(self, armament_type: str) -> bool:
        return True if armament_type in self.armament.keys() else False
    
    def get_armament(self, armament_type: str) -> int:
        return self.armament[armament_type] if self.check_armament(armament_type) else 0
        
    def set_armament(self, armament_type: str, no_of_charges: int) -> None:
        if self.check_armament(armament_type):
            self.armament[armament_type] = no_of_charges
        else:
            print("No such armament onboard. Can't add charges")
    
    def fire_armament(self, armament_type: str, no_of_charges: int) -> None:
            if self.get_armament(armament_type) >= no_of_charges:
                print(f"Firing {no_of_charges} from {armament_type}")
                self.set_armament(armament_type, self.get_armament(armament_type) - no_of_charges)
            else:
                print("No such weaponry available!")
                    
    def __str__(self) -> str:
        return super().__str__() + f"\nNo of artillery weapons: {self.armament['artillery']}"
        

# Destroyer is used for destroying submarines and enemy ships - it has torpedoes and depth charges onboard        
class Destroyer(NavalShip):
    def __init__(self, name: str, deadweight: int, engine_type: Engine, artillery: int, torpedoes: int, depth_charges: int):
        super().__init__(name, deadweight, engine_type, artillery)
        self.armament["torpedo_tubes"] = torpedoes
        self.armament["depth_charge_projectors"] = depth_charges
            
    # Destroyers use their sonars to attack submarines
    def locate_submarine(self) -> bool:
        print("Using sonars to locate enemy submarine")
        if random.randint(0,1):
            print("Enemy submarine located!")
            return True
        else:
            print("Enemy submarine lost!")
            return False
        
    def __str__(self) -> str:
        return super().__str__() + f"\nNo of torpedoes: {self.get_armament('torpedo_tubes')}. No of depth charges: {self.get_armament('depth_charge_projectors')}"
        

# Frigates are used for anti-air defense and destroying submarines, thus they have depth charges and anti-air guns        
class Frigate(NavalShip):
    def __init__(self, name: str, deadweight: int, engine_type: Engine, artillery: int, depth_charges: int, anti_air: int):
        super().__init__(name, deadweight, engine_type, artillery)
        self.armament["depth_charge_projectors"] = depth_charges
        self.armament["anti_air"] = anti_air
        
    # Frigates can protect their fleet with their anti-air weapons and radars
    def locate_aircraft(self) -> bool:
        print("Using sonars to locate enemy aircraft")
        if random.randint(0,1):
            print("Enemy aircraft located!")
            return True
        else:
            print("Enemy aircraft lost!")
            return False
        
    def __str__(self) -> str:
        return super().__str__() + f"\nNo of depth charges: {self.armament['depth_charge_projectors']}. No of anti-air charges {self.get_armament('anti_air')}"
    
    
# Cruisers are used for naval warfare, thus they usually only have main artillery and anti-air protection
class Cruiser(NavalShip):
    def __init__(self, name: str, deadweight: int, engine_type: Engine, artillery: int, anti_air: int):
        super().__init__(name, deadweight, engine_type, artillery)
        self.armament["anti_air"] = anti_air


class Fleet:
    def __init__(self, no: int, *ships):
        self.no = no
        self.fleet: list[Ship] = []
        self.fleet.extend(ships)
        
    def add_ship(self, ship: Ship) -> None:
        self.fleet.append(ship)
        
    def __getitem__(self, item: int) -> Ship:
        return self.fleet[item]
        
    def __str__(self) -> str:
        res = f"Fleet {self.no}\n---SHIPS---\n"
        for ship in self.fleet:
            res += ship.__repr__() + "\n"
        return res

frigate = Frigate("USS Fletcher", 2050, Engine.DIESEL_ENGINE, 10, 4, 8)
destroyer = Destroyer("USS Iowa", 3800, Engine.GAS_TURBINE, 4, 8, 16)
cruiser = Cruiser("USS Alaska", 10800, Engine.STEAM_ENGINE, 20, 10)

first_fleet = Fleet(1, frigate, destroyer, cruiser)
first_fleet.add_ship(Destroyer("USS McGowan", 3900, Engine.GAS_TURBINE, 4, 10, 5))
print(first_fleet)