class Player:
    def __init__(self, name, strength):
        self.id = Game.player_count + 1
        self.name = name
        self.strength = strength


class Game:
    player_count = 0
    registered = []

    def register(self, player: Player):
        self.registered.append(player)

    def round(self, p1_name, p2_name):
        p1 = self.get_player_by_name(self, p1_name)
        p2 = self.get_player_by_name(self, p2_name)
        if p1.strength > p2.strength:
            return 1
        elif p2.strength > p1.strength:
            return 2
        return 0

    def get_player_by_name(self, name):
        for player in self.registered:
            if player.name == name:
                return player
        print(f'Игрок {name} не зарегистрирован')
        raise NoRegisteredException


class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class NoRegisteredException(Error):
    """Вызывается, когда игрок не зарегистрирован"""
    pass
