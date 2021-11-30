#include "prototypes.h"
#include <iostream>
using namespace std;
int main()
{
int length=0;
int width=0;
 cout << "Please enter the length and width of a rectangle\n ";
 cin >> length;
 cin >> width;

int perimetercalc= perimeter(length,width);
int areacalc= area(length,width);

cout << "The perimeter is " << perimetercalc << "\n";
cout << "The area is " << areacalc << "\n";
cout << "Good-bye\n";
return 0;


}
