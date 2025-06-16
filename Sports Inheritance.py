class Player:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name} is playing")

class FootballPlayer(Player):
    def kick(self):
        print(f"{self.name} is kicking the ball")

class BasketballPlayer(Player):
    def shoot(self):
        print(f"{self.name} is shooting the ball")

X = FootballPlayer("Ronaldo")
Y = BasketballPlayer("LeBron James")

X.play()
X.kick()
Y.play()
Y.shoot()