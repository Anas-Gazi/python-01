#include <iostream>
using namespace std;

int main()
{
    int arr[] = {10, 20, 30, 40};

     // Prints the address of the first element
     cout << arr <<"\n";

    // accessing elements
    cout<< arr[2] << " " << arr[0] << "\n";

    //modifying element

    arr[2] = {100};
    cout << arr[2];

       return 0;
}
