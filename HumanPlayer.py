class HumanPlayer: 
    def __init__(self):
        self.states_value = {}
        
    def play(self, board):
        possibleMoves = []
        count = 0
        
        for i in range(3):
            for j in range(3):
                if(board[i][j] == 0):
                    possibleMoves.append(count)
                count += 1
        print(possibleMoves)
        check = True
        while check: 
            print("Sqaure number for your move: ")
            rowNum = int(input())
            for i in range(len(possibleMoves)):
                if rowNum == possibleMoves[i]:
                    return rowNum
            print("Please try another move")