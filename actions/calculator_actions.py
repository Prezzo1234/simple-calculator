from jaseci.actions.live_actions import jaseci_action

@jaseci_action()
def add(a: float, b: float) -> float:
    return a + b

@jaseci_action()
def subtract(a: float, b: float) -> float:
    return a - b

@jaseci_action()
def multiply(a: float, b: float) -> float:
    return a * b

@jaseci_action()
def divide(a: float, b: float) -> float:
    if b == 0:
        return "⚠️ Cannot divide by zero!"
    return a / b
