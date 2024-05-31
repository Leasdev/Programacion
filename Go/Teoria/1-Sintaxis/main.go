package main

import "fmt"

func main() {

	// Slice
	fmt.Println("Array \n[0 3 5 6 7 8]")
	numbers := []int{0, 3, 5, 6, 7, 8}
	fmt.Println("Array append")
	numbers = append(numbers, 2, 3)
	fmt.Println(numbers)

	// For
	fmt.Println("for con len()")
	for i := 0; i < len(numbers); i++ {
		fmt.Println(numbers[i])
	}
	fmt.Println("for con range()")
	for i := range numbers {
		fmt.Println(numbers[i])
	}

	for i, number := range numbers {
		fmt.Println("index: ", i, " Value: ", number)
	}

	fruits := []string{
		"manzana", "banaba", "sandia", "naranja", "melon", "frutilla",
	}
	fmt.Println("Modificando Array")
	for i, fruit := range fruits {
		index := len(fruit) - 1
		letter := fruit[index:]

		if letter != "a" {
			continue
		}
		fmt.Println("fruit", i, ": ", fruit)
	}
}
