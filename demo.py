import cmath  # Import cmath for complex number support

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Calculate two solutions
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

def main():
    # Get coefficients from the user
    print("Enter coefficients a, b, and c for the quadratic equation ax^2 + bx + c = 0:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        return

    # Solve the quadratic equation
    roots = solve_quadratic(a, b, c)
    
    # Display the results
    print(f"The solutions are: {roots[0]} and {roots[1]}")

if __name__ == "__main__":
    main()
