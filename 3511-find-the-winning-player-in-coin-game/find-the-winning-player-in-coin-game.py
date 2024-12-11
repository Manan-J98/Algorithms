class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        total_x, total_y = x * 75, y * 10
        player1 = True
        p1Score, p2Score = 0, 0
        while total_x >= 75 and total_y >= 40:
            if player1:
                p1Score += 115
                player1 = False
            else:
                p2Score += 115
                player1 = True
            total_x -= 75
            total_y -= 40
        return "Alice" if p1Score > p2Score else "Bob"
