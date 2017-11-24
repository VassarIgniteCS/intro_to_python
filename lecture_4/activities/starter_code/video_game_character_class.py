class Warrior:
    # here's our constructor!
    def __init__(self, name, color, strength, health):
        self.name = name
        self.color = color
        self.strength = strength
        self.health = health

    # this is just a regular method, not the most interesting
    def sword_attack(self):
        print(self.name, "used sword attack, doing", self.strength, "damage")

    # this method is a mutator method! it changes the objects health
    def heal(self, num):
        self.health = self.health + num

    # this is another mutator method
    def take_damage(self, num):
        self.health = self.health - num


# use the Warrior CLASS to create an instance of Warrior,
# and store that object in variable VAR
var = Warrior("corin", 0, 100, 100)

# call the objects method, sword_attack()
var.sword_attack()

# define some more classes here!!!
