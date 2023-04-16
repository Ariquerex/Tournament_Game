from Game import Game, Player, NoRegisteredException

player1 = Player('p1', 30)
player2 = Player('p2', 20)
player3 = Player('p3', 10)
Game.register(Game, player1)
Game.register(Game, player3)
try:
    print(Game.round(Game, 'p1', 'p2'))
except NoRegisteredException:
    pass
