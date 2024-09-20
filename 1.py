# dynamic calculator..
class DynamicCalculator:
    def __init__(self, number):
        self.number = number.replace('×', '*')

    def evaluate_number(self):
        return self._parse_number(self.number)

    def _parse_number(self,num):
        try:
            return eval(num)
        except Exception as e:
            return f"Error: {e}"

# Example usage
number = "1 + 2 * 3 * (4 - 5 / 4) - (3 / 5)"
a = DynamicCalculator(number)
result = a.evaluate_number()
print(f"The result of the expression is: {result}")
