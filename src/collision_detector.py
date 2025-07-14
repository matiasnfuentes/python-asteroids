class CollisionDetector:
    def __init__(self, player, asteroids, shots, asteroid_field, score, shields):
        self.player = player
        self.asteroids = asteroids
        self.shots = shots
        self.asteroid_field = asteroid_field
        self.score = score
        self.shields = shields

    def detect_collisions(self):
        # There's actually only 1 shield per game.
        for shield in self.shields:
            if shield.is_colliding(self.player):
                shield.set_player(self.player)

        for asteroid in self.asteroids:
            for shield in self.shields:
                if asteroid.is_colliding(shield) and shield.is_protecting_player():
                    shield.destroy()
                    asteroid.split(should_explode=True)

            if asteroid.is_colliding(self.player):
                self.player.lose_life()
                self.asteroid_field.clean_field()
                break  # Stop checking after player collision

            for shot in self.shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()
                    self.score.increase()
