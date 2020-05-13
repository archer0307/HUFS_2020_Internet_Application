class USER: #user에 대한 class
    def __init__(self):
        self.health = 150
        self.mana = 150
        self.level = 1
        self.attack = 100
    def level_up(self):
        self.level += 1
        self.health += 10
        self.mana += 10
        self.attack +=10