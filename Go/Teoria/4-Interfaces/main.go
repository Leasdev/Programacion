package main

import (
	"fmt"
	"users/users"
)

func main() {
	var frank users.Cashier = users.NewEmployee("frank")
	var leandro users.Admin = users.NewEmployee("Leandro")

	total := frank.CalcTotal(90, 65, 92.6)

	fmt.Println(total)

	leandro.DesactEmployee(frank)

	fmt.Println(frank.CalcTotal(90, 65, 92.6))
}
