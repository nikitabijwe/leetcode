class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # current = (0, 0)
        # curr_direction = N
        # for i in instructions:
        #     if i == G:
        #         current[1]+=1
        #     elif:
        #         i == L:
        #             direction = curr_direction +90
        #     else:
        #         i == R:
        #             direction = curr_direction - 90
        # if current = (0, 0):
        #     return true:
        # return false
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  # Initial position
        dx, dy = 0, 1  # Initial direction (north)

        for instruction in instructions:
            if instruction == 'G':
                x += dx
                y += dy
            elif instruction == 'L':
                # Rotate 90 degrees anti-clockwise
                dx, dy = -dy, dx
            elif instruction == 'R':
                # Rotate 90 degrees clockwise
                dx, dy = dy, -dx

        # If the robot is not facing north or it returns to the initial position after one cycle,
        # it will form a circle
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)