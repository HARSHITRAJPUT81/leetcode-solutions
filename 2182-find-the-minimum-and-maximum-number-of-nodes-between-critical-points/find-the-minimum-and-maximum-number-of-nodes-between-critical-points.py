class Solution:
    def nodesBetweenCriticalPoints(self, head):
        first = -1
        last = -1
        min_dist = float('inf')

        pos = 1

        prev = head
        curr = head.next

        while curr is not None and curr.next is not None:
            next_node = curr.next

            # Check if current node is a critical point
            is_critical = (
                (curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)
            )

            if is_critical:

                # First critical point
                if first == -1:
                    first = pos
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = next_node
            pos += 1

        # Fewer than two critical points
        if first == -1 or first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]  