# A Buzz number is a number that ends with 7 or is divisible by 7.
# Write a function that takes a number as input and checks if it is a Buzz number.
# The function should return 'Buzz' if the number is a Buzz number, 
# otherwise it should return 'Not a Buzz number'.

def isBuzz(n: int) -> str:
    # checks if last number is 7
    n_as_string = str(n)
    if n_as_string[-1] == "7":
        return "Buzz"

    # checks if number is divisible by 7
    if n % 7 == 0:
        return "Buzz"

    return "Not a Buzz number"


def main() -> None:
    print(isBuzz(7))
    print(isBuzz(10))
    print(isBuzz(17))
    print(isBuzz(56))
    print(isBuzz(57))
    print(isBuzz(100))
    print(isBuzz(107))


if __name__ == '__main__':
    main()

# isBuzz(7) => 'Buzz', isBuzz(10) => 'Not a Buzz number'
