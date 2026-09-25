class Solution:
    def canReach(self, arr, start):
        n = len(arr)

        queue = [start]
        visited = set()

        while queue:
            i = queue.pop(0)

            # Already visited
            if i in visited:
                continue

            # Mark visited
            visited.add(i)

            # Found value 0
            if arr[i] == 0:
                return True

            # Jump right
            right = i + arr[i]
            if right < n and right not in visited:
                queue.append(right)

            # Jump left
            left = i - arr[i]
            if left >= 0 and left not in visited:
                queue.append(left)

        return False