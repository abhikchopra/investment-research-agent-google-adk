# tools/calculator_tool.py

def calculator_tool(expression: str) -> str:
    """
    Performs simple mathematical calculations.

    Example:
    expression = "100 * (1.15 ** 5)"
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"