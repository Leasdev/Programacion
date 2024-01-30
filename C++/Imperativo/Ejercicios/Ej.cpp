#include <stdio.h> //Se agrega para poder usar archivos
#include <iostream>
#include <conio.h>
#include <cstring>
using namespace std;

struct persona
{
    char nombre[50];
    char apellido[50];
    int dni;
    int iq;
};

struct juego
{
    char nombre[50];
    char plataforma[50];
    int nota;
};

struct subNodo // Nodo secundario
{
    juego info;
    subNodo *sgte = NULL;
};


struct nodo // Nodo Principal
{
    persona info;
    nodo *sgte = NULL;
    subNodo *listaJuegos = NULL;
};

char menu()
{
    char opcion;
    cout << "*******************************" << endl;
    cout << "menu: " << endl;
    cout << "1 - Cargar Persona " << endl;
    cout << "2 - Insertar Persona en una Lista " << endl;
    cout << "3 - Mostrar Archivo " << endl;
    cout << "4 - Mostrar Lista " << endl;
    cout << "5 - Cargar Juego " << endl;
    cout << "s - Salir " << endl;   
    do
    {
        opcion = getchar();
        
    } while (opcion != '1' && opcion != '2' && opcion != '3' && opcion != '4' && opcion != '5' && opcion != 's');
    
    return opcion;
}

void cargarPersona(void)
{
    FILE *f;
    f = fopen("archivos_personas","a");
    persona x;
    cout << "Ingrese el nombre: " << endl;
    cin >> x.nombre;
    cout << "Ingrese el apellido: " << endl;
    cin >> x.apellido;
    cout << "Ingrese el DNI: " << endl;
    cin >> x.dni;
    cout << "Ingrese IQ: " << endl;
    cin >> x.iq;
    fwrite(&x, sizeof(persona), 1 ,f);  
    fclose(f);
    return;
}
void cargarJuego(void)
{
    FILE *f;
    f = fopen("juego", "a");
    juego y;
  
    cout << "Ingrese nombre del juego: " << endl;
    cin >> y.nombre;
    cout << "Ingrese su plataforma: " << endl;
    cin >> y.plataforma;
    cout << "Ingrese nota: " << endl;
    cin >> y.nota;
    fwrite(&y, sizeof(juego) ,1 , f);
    fclose(f);
    cout << "Listo, se creo juego" << endl;
    return;
}

void mostrarjuego(subNodo *subLista)
{
    int i = 1;
    while(subLista)
    {
        cout << "************************************" << endl;
        cout << "Juego " << i << ": " << endl;
        cout << "Nombre: " << subLista -> info.nombre << endl;
        cout << "Plataforma: " << subLista -> info.plataforma << endl;
        cout << "Nota: " << subLista -> info.nota << endl;
        subLista = subLista -> sgte;
        i++;
    }
    return;
}

void mostrarGurimu(nodo *lista)
{  
    int i = 1;
    while(lista)
    {   
        cout << "===================================" << endl;
        cout << "Persona " << i << ": " << endl;
        cout << "Nombre: " << lista -> info.nombre << endl;
        cout << "Apellido: " << lista -> info.apellido << endl; 
        cout << "DNI: " << lista -> info.dni << endl; 
        cout << "IQ: " << lista -> info.iq << endl;  
        cout << "===================================" << endl;
        if(lista -> listaJuegos)
        {
            mostrarjuego(lista -> listaJuegos);
        }
        else
        {
            cout << "La persona no tiene juegos" << endl;
        }
        lista = lista -> sgte;
        i++;
    }
    return;
}



void insertarPersonaSiguiente(nodo *&lista, persona x)
{
    nodo *nuevo = new nodo();
    
    nuevo -> info = x;
    if(lista)
    {
        nuevo -> sgte = lista -> sgte;
        lista -> sgte = nuevo;
    }
    else
    {
        nuevo -> sgte = lista;
        lista = nuevo;
    }
    return;
}

void insertarJuegoSiguiente(subNodo *&subLista, juego y)
{
    subNodo *nuevo = new subNodo();
    
    nuevo -> info = y;
    if(subLista)
    {
        nuevo -> sgte = subLista -> sgte;
        subLista -> sgte = nuevo;
    }
    else
    {
        nuevo -> sgte = subLista;
        subLista = nuevo;
    }
    return;
}

nodo *buscarPersonaDNI(nodo *lista, int dni)
{
    while(lista && lista -> info.dni != dni)
    {
        lista = lista -> sgte;
    }
    return lista;
}

nodo *obtenerUltimoPersona(nodo *lista)
{
    while(lista && lista -> sgte)
        lista = lista -> sgte;
    return lista;

}

subNodo *obtenerUltimoJuego(subNodo *subLista)
{
    while (subLista && subLista -> sgte)
        subLista = subLista -> sgte;
    return subLista;
}

void insertarAlFinalPersona(nodo *&lista, persona x)
{
    nodo *aux;
    aux = obtenerUltimoPersona(lista);
    if(aux)
    {
        insertarPersonaSiguiente(aux, x);
    }
    else
    {
        insertarPersonaSiguiente(lista, x);
    }
    return;
}

void insertarAlFinalJuego(subNodo *&subLista, juego y)
{
    subNodo * aux;
    aux = obtenerUltimoJuego(subLista);
    if(aux)
    {
        insertarJuegoSiguiente(aux, y);
    }
    else
    {
        insertarJuegoSiguiente(subLista, y);
    }
    return;
}



int main()
{
    FILE *f;
    nodo *personas = NULL;
    nodo *aux = NULL;
    persona x;
    int dni;

    char op;
    
    do
    {     
        op = menu();
        switch(op)
        {
            case '1':
                cargarPersona();               
                break;
            case '2':
                f = fopen("archivos_personas", "r");
                fread(&x, sizeof(persona), 1, f);
                while(!feof(f))
                {
                    insertarPersonaSiguiente(personas, x);
                    fread(&x, sizeof(persona), 1, f);
                }
                fclose(f);
                cout << "Insertado en un lista!" << endl;
                break;
            case '3':
                f = fopen("archivos_personas", "r");
                while(fread(&x, sizeof(persona), 1, f))
                {
                    cout << "****************" << endl;
                    cout << x.nombre << endl;
                    cout << x.apellido << endl;
                    cout << x.dni << endl;
                    cout << x.iq << endl;
                }
                fclose(f);
                break;
            case '4':
                mostrarGurimu(personas);
                break;
            case '5':
                cout << "ingrese DNI: " << endl;
                cin >> dni;
                aux = buscarPersonaDNI(personas, dni);
                if(aux)
                {
                    juego nuevoJuego;
                    cout << "Ingrese el nombre del juego: " << endl;
                    cin >> nuevoJuego.nombre;
                    cout << "Ingrese su plataforma: " << endl;
                    cin >> nuevoJuego.plataforma;
                    cout << "Ingrese la nota: " << endl;
                    cin >> nuevoJuego.nota;
                    insertarAlFinalJuego(aux -> listaJuegos, nuevoJuego);
                    cout << "se agrego un juego" << endl;
                }
                break;
        }
    }while(op != 's');
    return 0;
}