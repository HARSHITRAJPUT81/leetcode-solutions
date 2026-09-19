class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):

        # Find closest x-coordinate in rectangle
        closestX = max(x1, min(xCenter, x2))

        # Find closest y-coordinate in rectangle
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance
        dx = xCenter - closestX
        dy = yCenter - closestY

        distanceSquared = dx * dx + dy * dy

        return distanceSquared <= radius * radius