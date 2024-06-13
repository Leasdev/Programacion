package main

import (
	"fmt"
	"struct/users"
)

func main() {
	pedro := users.User{Id: 2, Name: "Pedro", Age: 15}
	leandro := users.User{Id: 1, Name: "Leandro", Age: 25}
	luciano := users.User{Id: 3, Name: "Luciano", Age: 35}
	pepito := users.User{Id: 3, Name: "Pepito", Age: 45}
	martin := users.User{Id: 3, Name: "Martin", Age: 55}

	leandro.Saludar()
	leandro.AddFriend(pedro)
	leandro.AddFriend(luciano)
	leandro.AddFriend(pepito)
	leandro.AddFriend(martin)

	leandro.ListFriend()

	fmt.Println("============================")
	leandro.RemoveFriend(luciano.Id)
	leandro.ListFriend()
}
