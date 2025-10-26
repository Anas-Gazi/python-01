#include <iostream>
using namespace std;

int main()
{
    int arr[] = { 0,10,20,50,60,50,80,90,69};
    int n = sizeof(arr) / sizeof(arr[0]);

    // cout <<n;  // display the number of ellement 
    for(int i = 0 ; i<= n-1; i++){
      cout << arr[i] << " ";
    }
   

       return 0;
}