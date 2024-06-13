package users

import "fmt"

type User struct {
	Id      int
	Name    string
	Age     int
	friends []User
}

func (x User) Saludar() {
	println("Hola, me llamo", x.Name, "y soy el id", x.Id)
}

func (x *User) AddFriend(friend User) {
	x.friends = append(x.friends, friend)
}

func (x User) ListFriend() {
	fmt.Println("Amigos de", x.Name)
	for i, f := range x.friends {
		fmt.Printf("%d. %s. %d\n", i+1, f.Name, f.Age)
	}
}

func (x *User) RemoveFriend(Id int) {
	index := x.findFriend(Id)

	if index < 0 {
		return
	}
	x.friends = append(x.friends[:index], x.friends[index+1:]...)
}

func (x User) findFriend(Id int) int {
	for i, f := range x.friends {
		if f.Id == Id {
			return i
		}
	}
	return -1
}
