#include <iostream>
using namespace std;

void change(int x[]){
   x[0]=10;
}

int main()
{
    int arr[] = {20,60,90,56,31,20};
    cout<< arr[0]<<endl;
    change(arr);
    cout << arr[0]<< endl;

       return 0;
}