import math

class QuadraticEquationSolver:
    def __init__(self, a=1, b=2, c=1):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_discriminant(self):
        return self.b**2 - 4*self.a*self.c
    
    def find_roots(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
        
        discriminant = self.calculate_discriminant()
        
        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
            return (root1.real, root2.real)
        
        elif discriminant == 0:
            root = -self.b / (2*self.a)
            return (root, root)
        
        else:
            root1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
            return (root1, root2)