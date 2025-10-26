#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int arr[]= {10,20,50,9,6,8,1,98,56};
    int n= sizeof(arr)/sizeof(arr[0]);
    int mx= INT_MIN; // Maximum value (initialize with smallest possible integer)
    int smx= INT_MIN; // int second max value
    
    for(int i=0; i<n; i++){
      if(mx < arr[i])  mx = arr[i] ;
    }
    for(int i=0; i<n; i++){
      if(smx < arr[i] && arr[i] !=mx)
      smx= arr[i]; // Update second max only if it's smaller than max
    }
    cout<<mx <<" " << smx;

       return 0;
}