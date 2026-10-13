class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()

        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False

        return True