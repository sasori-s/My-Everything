from types import coroutine


class solution:
    def __init__(self, start_x, start_y):
        self.start_X = start_x
        self.start_y = start_y
        

    def minKnightMOves(self, x: int,y: int) -> int:
        steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        seen = set()

        q = [(0, [self.start_X,  self.start_y])]
        while q:
            moves, coords = q.pop(0)
            if coords[0] == x and coords[1] == y:
                return moves

            for s in steps:
                nxtc = (coords[0] + s[0], coords[1] + s[1])

                if not((coords[0] >= -2 and x >= -2 and
                    coords[1] >= -2 and y >= -2) or

                    (coords[0] >= -2 and x >= -2 and
                    coords[1] >= -2 and y >= -2) or

                    (coords[0] >= -2 and x >= -2 and
                    coords[1] >= -2 and y >= -2) or

                    (coords[0] >= -2 and x >= -2 and
                    coords[1] >= -2 and y >= -2)): 

                    continue


                if nxtc not in seen:
                    q.append((moves + 1, nxtc))
                    seen.add(nxtc)

kinght_moves = solution(0, 0)            
