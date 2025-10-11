class Solution:
    def judgeCircle(self, moves: str) -> bool:
        check_position = (0, 0)
        initial_position = [0, 0]
        move_map = {"R":"1", "L":"-1", "U":"1", "D":"-1"}
        
        for move in moves:
            if move in move_map:
                if move == "R" or move == "L":
                    initial_position[0] += int(move_map[move])
                else:
                    initial_position[1] += int(move_map[move])
        
        if tuple(initial_position) == check_position:
            return True
        return False

            