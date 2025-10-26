#include <iostream>
#include <climits>// must use if use INT_MIN
using namespace std;

int main()
{
    int arr[]={10,20,50,9,6,8,1,98,56};
    int n= sizeof(arr)/sizeof(arr[0]); // Calculates the total number of elements in the array
    int mx = INT_MIN;  // Initialize mx with the smallest possible integer
    int mn = INT_MAX;  // Initialize mn with the largest possible integer

    for(int i=0; i<n; i++){
      mx= max(mx,arr[i]); // Update mx if arr[i] is greater 
      //The built-in max() function compares mx with arr[i] and assigns the larger value to mx
      mn = min(mn,arr[i]); //update mn to store the min value
    }
    cout<<"Max value: " <<mx <<"\n" << "Min value: " << mn;

       return 0;
}