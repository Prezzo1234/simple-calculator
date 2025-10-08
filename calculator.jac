with entry {
    # A tiny calculator written in Jac demonstrating functions and printing

    # Add and subtract (Jac syntax is very similar to Python)
    def add(a: int, b: int) -> int {
        return a + b;
    }

    def sub(a: int, b: int) -> int {
        return a - b;
    }

    def mul(a: int, b: int) -> int {
        return a * b;
    }

    def div(a: float, b: float) -> float {
        if (b == 0) {
            raise ValueError("division by zero");
        }
        return a / b;
    }

    # A small demo using the functions above
    print("Jac Simple Calculator Demo");
    print(f"2 + 3 = {add(2,3)}");
    print(f"10 - 4 = {sub(10,4)}");
    print(f"6 * 7 = {mul(6,7)}");
    print(f"8 / 2 = {div(8,2)}");

    # Show error handling (explicit check to avoid runtime exception)
    if (0 == 0) {
        # demonstrate safe check before dividing
        if (0 != 0) {
            print(f"5 / 0 = {div(5,0)}");
        } else {
            print("Demo: division by zero avoided (would raise error)");
        }
    }
}
