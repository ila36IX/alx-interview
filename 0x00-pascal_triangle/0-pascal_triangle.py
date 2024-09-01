#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle.
"""


def pascal_triangle(n):
    """return list of lists"""
    if n < 0:
        return []
    pascal = [[1]]
    for j in range(1, n):
        row = [1]
        row += [pascal[j - 1][i] + pascal[j - 1][i + 1] for i in range(j - 1)]
        row += [1]
        pascal.append(row)
    return pascal
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    print_triangle(pascal_triangle(2))
