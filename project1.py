import math

class Circle:
    def __init__(self, radius):
        """
        Initialize a Circle object with a given radius
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle
        
        Returns:
            float: The area of the circle
        """
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle
        
        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius
    
    def __str__(self):
        """
        String representation of the Circle object
        """
        return f"Circle with radius: {self.radius}"

# Example usage
if __name__ == "__main__":
    # Create a circle with radius 5
    circle1 = Circle(5)
    
    print(circle1)
    print(f"Area: {circle1.area():.2f}")
    print(f"Perimeter: {circle1.perimeter():.2f}")
    
    # Create another circle with radius 7.5
    circle2 = Circle(7.5)
    
    print(f"\n{circle2}")
    print(f"Area: {circle2.area():.2f}")
    print(f"Perimeter: {circle2.perimeter():.2f}")