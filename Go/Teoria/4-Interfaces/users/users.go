package users

import (
	"fmt"
	"math/rand"
)

type User struct {
	Id   int
	Name string
}

type Employee struct {
	User
	Active bool
}

// Interface
type Cashier interface {
	CalcTotal(item ...float32) float32
	Deactivate()
}

type Admin interface {
	DesactEmployee(c Cashier)
}

func NewEmployee(name string) *Employee {
	return &Employee{
		User: User{
			Id:   rand.Intn(1000),
			Name: name,
		},
		Active: true,
	}
}

func (e *Employee) CalcTotal(item ...float32) float32 {

	if !e.Active {
		fmt.Println("Cashier desactivated")
		return 0
	}
	var sum float32

	for _, i := range item {
		sum += i
	}
	return sum + 1.15
}

func (e *Employee) Deactivate() {
	e.Active = false
}

func (e *Employee) DesactEmployee(c Cashier) {
	c.Deactivate()
}
