package main

import "packages/countries"

// go get "URL" (importar librerias de tercero)

func main() {
	countries.Add("USA")
	countries.Add("Mexico")
	countries.Add("Japan")
	countries.Add("Argentina")
	countries.Add("Spain")

	err := countries.SetMyCountry("Argentina")
	if err != nil {
		panic(err)
	}
	countries.List()
}
