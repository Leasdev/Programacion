#include <iostream>

using namespace std;

// Struct
struct Juego
{
    char nombre[50];
    char categoria[50];
    int nota;
};

struct ListaPersona
{
    Juego info;
    ListaPersona *sgte;
};

// Funciones
char menu()
{
    char opcion;
    cout << "===================================" << endl;
    cout << "Menu:" << endl;
    cout << "1 - Cargar Juego" << endl;
    cout << "s - Salir " << endl;
    do
    {
        opcion = getchar();
    }while(opcion != '1' && opcion != 's');
    return opcion; 
}



int main()
{
    char opcion;
    
    opcion = menu();
    switch(opcion)
    {
        case '1':
            cout << "bien" << endl;
            break;
        case 's':
            cout << "salio" << endl;
            break;
    }
    




    return 0;
}