#include <iostream>
using namespace std;

int suma( int $a, int $b )
{
int $result;
__asm__ __volatile__(
        "movl %1, %%eax;"
        "movl %2, %%ebx;"
        "addl %%ebx,%%eax;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
return $result ;
}

int resta( int $a, int $b )
{
int $result;
__asm__ __volatile__(
        "movl %1, %%eax;"
        "movl %2, %%ebx;"
        "subl %%ebx,%%eax;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
return $result ;
}

int multi( int $a, int $b )
{
int $result;
__asm__ __volatile__(
        "movl %1, %%eax;"
        "movl %2, %%ecx;"
        "mull %%ecx;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
return $result ;
}

int division( int $a, int $b )
{
int $result;
__asm__ __volatile__(
        "xorl %%edx, %%edx;"
        "movl %1, %%eax;"
        "movl %2, %%ebx;"
        "divl %%ebx;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
return $result ;
}

int potencia( int $a, int $b )
{
int $result;
__asm__ __volatile__(
        "movl %2, %%ecx;"
        "decl %%ecx;"
        "movl %1, %%eax;"
        "ciclo:;"
            "movl %1, %%ebx;"
            "mull %%ebx;"
            "loopl ciclo;"
        "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));
return $result ;
}

int main(int argc, char** argv) {
    int a,b,c,opc;

    do {
        system("cls");
        cout << "\t\t---------------------------------------------------------------------------------------------------\n";
		cout << "\t\t\t\t\t      |            Calculadora           |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t\t\t   |  1.- Suma                  |  2.- Resta                 |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t\t\t   |  3.- Multiplicacion        |  4.- Division              |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t\t\t   |  5.- Potencia              |  6.- Seno                  |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t\t\t   |  7.- Coseno                |  8.- Tangente              |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t\t\t   |                        9.- Salir                        |\n";
		cout << "\t\t\t\t   -----------------------------------------------------------\n";
		cout << "\t\t---------------------------------------------------------------------------------------------------\n";
		cout << "\n -Eliga la opcion que desea realizar: ";
        cin >> opc;
        system("cls");
        switch(opc)
        {
            case 1:
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\t\t\t\t      |            Suma           |\n";
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\n -Ingresa los dos numeros: " << endl;
               cin >> a;
               cout << "+ " << endl;
               cin >> b;
               c=suma(a,b);
               cout<<"\nEl resultado de la suma de "<<a<<"+"<<b<<"="<<c<<"\n"<<endl;
               system("PAUSE");
            break;
            case 2:
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\t\t\t\t      |            Resta           |\n";
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\n -Ingresa los dos numeros: " << endl;
               cin >> a;
               cout << "- " << endl;
               cin >> b;
               c=resta(a,b);
               cout<<"\nEl resultado de la resta de "<<a<<"-"<<b<<"="<<c<<"\n"<<endl;
               system("PAUSE");
            break;
            case 3:
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\t\t\t\t      |            Multiplicacion           |\n";
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\n -Ingresa los dos numeros: " << endl;
               cin >> a;
               cout << "* " << endl;
               cin >> b;
               c=multi(a,b);
               cout<<"\nEl resultado de la multiplicacion de "<<a<<"*"<<b<<"="<<c<<"\n"<<endl;
               system("PAUSE");
            break;
            case 4:
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\t\t\t\t      |            Division           |\n";
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\n -Ingresa los dos numeros: " << endl;
               cin >> a;
               cout << "/ " << endl;
               cin >> b;
               c=division(a,b);
               cout<<"\nEl resultado de la division de "<<a<<"/"<<b<<"="<<c<<"\n"<<endl;
               system("PAUSE");
            break;
            case 5:
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\t\t\t\t      |            Potencia           |\n";
               cout << "\t\t-------------------------------------------------------------------------\n";
               cout << "\n -Ingresa los dos numeros: " << endl;
               cin >> a;
               cout << "^" << endl;
               cin >> b;
               c=potencia(a,b);
               cout<<"\nEl resultado de la potencia de "<<a<<"^"<<b<<"="<<c<<"\n"<<endl;
               system("PAUSE");
            break;
            case 6:
                cout << "\n - Saliendo del Menu... -" << endl;
            break;
            default:
                cout << "\nOpcion incorrecta\n";

        }
    } while(opc!=6);
    /*
    cout<<"\nDigite el numero a: ";
    cin>>a;
    cout<<"\nDigite el numero b: ";
    cin>>b;
    c=suma(a,b);
    cout<<"\nEl resultado de la suma de "<<a<<"+"<<b<<"="<<c<<"\n";
    c=resta(a,b);
     cout<<"\nEl resultado de la resta de "<<a<<"-"<<b<<"="<<c<<"\n";
    c=multi(a,b);
    cout<<"\nEl resultado de la multiplicacion de "<<a<<"*"<<b<<"="<<c<<"\n";
    c=division(a,b);
    cout<<"\nEl resultado de la division de "<<a<<"/"<<b<<"="<<c<<"\n";
    c=potencia(a,b);
    cout<<"\nEl resultado de la potencia de "<<a<<"^"<<b<<"="<<c<<"\n";*/
    return 0;
}
/*

#include <cmath>
#include <iostream>
#include <cstdlib>

using namespace std;
const float PI = 3.1459265;
int main()
{
    int size = 80, height = 21;
    char chart[height][size];
    size = 80, height = 21;
    double cosx[size];
    double sinx[size];


        for (int i=0; i<size; i++)
            cosx[i] = 10*cos(i/4.5);

        for (int i=0; i<height; i++)
            for (int j=0; j<size; j++)
                if (-.01 < 10 - i - round(cosx[j]) && 10 - i - round(cosx[j]) <0.01)
                    chart[i][j] = 'x';
                else if (i==height/2)
                    chart[i][j] = '-';
                else
                    chart[i][j] = ' ';

        for (int i=0; i<height; i++) {
            for (int j=0; j<size; j++) {
               cout << chart[i][j];
            }
            cout << '\n';
        }

        for (int i=0; i<size; i++)
            sinx[i] = 10*sin(i/4.5);

        for (int i=0; i<height; i++)
            for (int j=0; j<size; j++)

        if (-.01 < 10 - i - round(sinx[j]) && 10 - i - round(sinx[j]) <0.01)
            chart[i][j] = 'x';
        else if (i==height/2)
            chart[i][j] = '-';
        else
            chart[i][j] = ' ';

        for (int i=0; i<height; i++) {
            for (int j=0; j<size; j++) {
               cout << chart[i][j];
            }
            cout << '\n';
        }

}/*
#include <math.h>
#include <iostream>
#include <string>
#include <vector>

int main()
{
  int size = 80, height = 21;

  // Start with an empty chart (lots of spaces and a line in the middle)
  std::vector<std::string> chart(height, std::string(size, ' '));
  chart[height/2] = std::string(size, '-');

  // Then just put x-es where the function should be plotted
  for(int i = 0; i < size; ++i) {
    chart[static_cast<int>(std::round(10 * std::cos(i / 4.5) + 10))][i] = 'x';
  }

  // and print the whole shebang
  for(auto &&s : chart) {
    std::cout << s << '\n';
  }
}
*/
