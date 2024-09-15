#!/usr/bin/python3

"""

This is module for giving selution to following problem
Placing N non-attacking queens on an N×N chessboard

"""
import sys


class Chessboard():
    """
    chassBoard is chessboard of size N x N
    args:
        N: Is the size of N
        N: must be a number, Or ValueError will be raised
    """

    def __init__(self, N: int):
        """Constructor"""
        self.N = N
        self.board = [[0 for i in range(0, self.N)] for j in range(0, self.N)]
        self.__result = []

    @property
    def N(self):
        """The N property."""
        return self.__N

    @N.setter
    def N(self, value):
        """set the N"""
        self.__N = value

    def put_queen(self, x, y):
        """Put a queen in the board"""
        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")

        if not self.could_fit(x, y):
            raise ValueError("Position occupied")

        for a, b in self.queen_attacks(x, y):
            self.board[a][b] = "x"

        self.board[x][y] = "Q" or "🔅"

    def could_fit(self, x, y):
        """Checks if queen could fit in position wihtout
        attack/getting attacked from another"""

        if self.board[x][y] in ("x", "Q"):
            return False

        for a, b in self.queen_attacks(x, y):
            if self.board[a][b] == "Q":
                return False

        return True

    def queen_attacks(self, x, y):
        """Return list of all the position that is attacked by Q(x, y)"""
        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")

        queen_attacks = []

        for i in range(0, self.__N):
            if (self.board[i][x] != "1"):
                queen_attacks.append((x, i))
            if (self.board[y][i] != "1"):
                queen_attacks.append((i, y))

        for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
            queen_attacks.append((i, j))

        for i, j in zip(range(y, self.__N, 1), range(x, -1, -1)):
            queen_attacks.append((i, j))

        for i, j in zip(range(x, self.__N), range(y, self.__N)):
            queen_attacks.append((i, j))

        for i, j in zip(range(x, self.__N), range(y, -1, -1)):
            queen_attacks.append((j, i))

        return queen_attacks

    def get_queen(self, x, y):
        """Remove a queen in the board"""

        if (x > self.__N or y > self.__N):
            raise ValueError("Out of board range")
        if self.board[x][y] != "Q":
            raise ValueError("no queen in the giving position")

        other_queens = []
        for i in range(0, self.__N):
            for j in range(0, self.__N):
                if (i, j) != (x, y) and self.board[i][j] == "Q":
                    other_queens.append((i, j))

        for i in range(0, self.__N):
            for j in range(0, self.__N):
                self.board[i][j] = 0

        for i in other_queens:
            self.put_queen(*i)

    def print_board(self):
        """print the board in nice way"""
        for i, sub_lis in enumerate(self.board):
            print("-"*self.__N*self.__N)
            for j, _ in enumerate(sub_lis):
                print("|", self.board[i][j], "|", end="")
            print()
        print("_"*self.__N*self.__N)

    @property
    def solutions(self):
        """Set """
        if len(self.__result) == 0:
            self.solve(0, [])
        return self.__result

    def free_board(self):
        for i in range(0, self.__N):
            for j in range(0, self.__N):
                self.board[i][j] = 0

    def solve(self, x, solutions):
        """Function that gives self.solutions it's value"""
        if x == self.__N:
            self.__result.append(tuple(solutions))
            return

        for y in range(0, self.__N):
            if self.could_fit(x, y):
                self.put_queen(x, y)
                solutions.append([x, y])
                self.solve(x + 1, solutions)
                self.get_queen(*solutions.pop())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    N = int(sys.argv[1])

    if (N < 4):
        print("N must be at least 4")
        exit(1)

    judit = Chessboard(N)

    for i in judit.solutions:
        print(list(i))
