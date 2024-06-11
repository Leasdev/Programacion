package countries

import (
	"errors"
	"fmt"
)

var (
	myCountry   string
	collection  []string
	errNotFound error = errors.New("country not found")
)

// Add Agrega el valor de un pais.
func Add(country string) {
	collection = append(collection, country)
}

// SetMyCountry selecciona un pais especifico
func SetMyCountry(country string) error {
	if !isInCollection(country) {
		return errNotFound
	}
	myCountry = country
	return nil
}

func isInCollection(country string) bool {
	for _, c := range collection {
		if c == country {
			return true
		}
	}
	return false
}

// List muestra la lista
func List() {
	for i, c := range collection {
		myCountryMsg := ""
		if c == myCountry {
			myCountryMsg = " [My Country]"
		}
		fmt.Printf("%d = %s %s\n", i+1, c, myCountryMsg)
	}
}
