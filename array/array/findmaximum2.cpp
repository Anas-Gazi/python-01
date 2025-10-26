#include <iostream>
using namespace std;

int main()
{
    int arr[]={10,20,50,9,6,8,1,98,56};
    int n= sizeof(arr)/sizeof(arr[0]); // Calculates the total number of elements in the array
    int mx = arr[0]; // Initialize max with the first element

    for(int i=0; i<n; i++){
      if(mx<arr[i]) mx = arr[i];  // Update mx if a larger element is found
      //If mx is smaller than arr[i], update mx with arr[i].
    }
    cout<<mx;

       return 0;
}