
# fizz_buzz...

class FizzBuzz:
    def __init__(self,a):
        self.a = a

    def play_fizz_buzz(self):
        for i in range(1, self.a + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("Fizz_Buzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

# Example usage
f_z= FizzBuzz(15)
print(f_z.play_fizz_buzz())


