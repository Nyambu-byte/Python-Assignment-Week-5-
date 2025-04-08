# Base class
class Superhero:
    def __init__(self, name, power, weakness, health):
        self.name = name
        self.power = power
        self.weakness = weakness
        self.health = health

    def introduce(self):
        return f"I am {self.name}, and my power is {self.power}!"

    def take_damage(self, damage):
        self.health -= damage
        return f"{self.name} took {damage} damage! Health is now {self.health}."

    def is_alive(self):
        return self.health > 0

# Subclass: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, health, flight_speed):
        super().__init__(name, power, weakness, health)
        self.flight_speed = flight_speed

    # Polymorphism: Overriding introduce method
    def introduce(self):
        return f"I am {self.name}, I soar through the skies at {self.flight_speed} km/h!"

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Creating instances
hero1 = Superhero("ShadowStrike", "Invisibility", "Bright Light", 100)
hero2 = FlyingSuperhero("SkyBlazer", "Firestorm", "Water", 120, 500)

# Using methods
print(hero1.introduce())
print(hero2.introduce())
print(hero2.fly())
print(hero1.take_damage(30))
print(f"Is {hero1.name} alive? {'Yes' if hero1.is_alive() else 'No'}")