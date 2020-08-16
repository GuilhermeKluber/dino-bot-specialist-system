from time import time

class Obstacle:
    def __init__(self, actual_game_speed, game_height, pos):
        """ Obstacle object

        Args:
            game_height (integer): Height of the game
            pos (list[integer]): Position of obstacle x,y,x2,y2 
            actual_game_speed (float): Game speed on pixeis per second
        """
        self.game_height = game_height
        self.pos = pos
        self.type = self._is_land_or_air()
        self.distance = pos[0]
        self.length = pos[2] - pos[0]
        self.height = pos[3] - pos[1]
        self.detected_at = time()
        self.speed = actual_game_speed
        self.in_game = True

    def _is_land_or_air(self):
        # Verifica se o ponto y2 está abaixo (considerando o plano do opencv) de 0.98*y2 do game
        if self.pos[3] > self.game_height*0.98:
            return 'land'
        return 'air'

    def calculate_speed(self,last_obstacle):
        # Velocidade em pixeis por milisegundo
        elapsed = (self.detected_at - last_obstacle.detected_at)*1000
        speed = (last_obstacle.distance - self.distance )/elapsed
        if speed > 0 and  0 < (last_obstacle.pos[2] - self.pos[2]):
            self.speed = speed

    def __str__(self):
        return f"'{self.type}' obstacles with follow attributes: Length {self.length} Height {self.height} Speed {round(self.speed,4)} Distance {self.distance} In Game {self.in_game}"