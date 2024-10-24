package test

import "core:fmt"
print :: fmt.println

main :: proc() {

	print(isBuzz(7))
	print(isBuzz(10))
	print(isBuzz(17))
	print(isBuzz(56))
	print(isBuzz(57))
	print(isBuzz(100))
	print(isBuzz(107))

	// OUTPUT:
	// Buzz
	// Not a Buzz number
	// Buzz
	// Buzz
	// Buzz
	// Not a Buzz number
	// Buzz

}


isBuzz :: proc(n: int) -> string {
	// checks if last number is 7
	n_as_string := str(n)
	defer delete(n_as_string)

	if n_as_string[len(n_as_string) - 1] == '7' {
		return "Buzz"
	}

	// checks if number is divisible by 7
	if n % 7 == 0 {
		return "Buzz"
	}


	return "Not a Buzz number"
}
