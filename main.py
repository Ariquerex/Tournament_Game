from Game import Game, Player, NoRegisteredException

player1 = Player('p1', 30)
player2 = Player('p2', 20)
player3 = Player('p3', 10)
player4 = Player('p4', 10)

Game.register(Game, player1)
Game.register(Game, player3)
Game.register(Game, player4)

print(Game.round(Game, 'p1', 'p3'))
print(Game.round(Game, 'p4', 'p1'))
print(Game.round(Game, 'p2', 'p3'))
print(Game.round(Game, 'p3', 'p4'))
