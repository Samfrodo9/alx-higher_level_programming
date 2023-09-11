class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


"""    def __repr__(self):
        return f"Point({self.x}, {self.y})"
"""
    
p = Point(2, 3)

print(repr(p))  # Output: Point(2, 3)
print(str(p))   # Output: (2, 3)
