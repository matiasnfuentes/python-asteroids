class CollisionDetector:
    def __init__(
        self, player, asteroids, shots, asteroid_field, score, power_ups, shields
    ):
        self.player = player
        self.asteroids = asteroids
        self.shots = shots
        self.asteroid_field = asteroid_field
        self.score = score
        self.power_ups = power_ups
        self.shields = shields

    def detect_collisions(self):
        # There's only 1 power_ups per game at the same moment
        power_up = next(iter(self.power_ups), None)
        if power_up is not None and power_up.is_colliding(self.player):
            power_up.set_player(self.player)

        for asteroid in self.asteroids:
            for shield in self.shields:
                if asteroid.is_colliding(shield) and shield.is_powering_up_player():
                    shield.destroy()
                    asteroid.split(should_explode=True)

            if asteroid.is_colliding(self.player):
                self.player.lose_life()
                self.asteroid_field.clean_field()
                if power_up is not None:
                    power_up.destroy()
                break  # Stop checking after player collision

            for shot in self.shots:
                if asteroid.is_colliding(shot):
                    shot.kill()
                    asteroid.split()
                    self.score.increase()
