class Solution:
    def judgeCircle(self, moves: str) -> bool:
        initial_position = [0, 0]
        move_map = {
            "R":1,
            "L":-1,
            "U":1,
            "D":-1
        }
        
        for move in moves:
            if move == "R" or move == "L":
                initial_position[0] += move_map[move]
            elif move == "U" or move == "D":
                initial_position[1] += move_map[move]
        
        return initial_position == [0, 0]
            