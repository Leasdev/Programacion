// Condicional (if/else)

/*
   if (expresion logica)
   {
        sentencia 1;
        sentencia n;
   }
   else
   {
        sentencia 1;
        sentencia n;
   }
*/
#include <iostream>

using namespace std;

int main()
{
    int x;
    cout << "Ingrese un numero: ";
    cin >> x;

    if(x%2 == 0) // si es par
        cout << "El numero es par";   
    else
        cout << "El numero es impar";
    

    return 0;
} 