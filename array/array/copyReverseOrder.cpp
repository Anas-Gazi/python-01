#include<iostream>
using namespace std; 

int main(){
  int arr[] = {10,20,30,40,50};
  int n = sizeof(arr)/sizeof(arr[0]);

  for(int i=0; i<n; i++){ //printing the elements of arr[]
    cout << arr[i] <<" ";
  }
  cout << endl;

  int brr[n]; //Reversing the Array

  for(int i=0; i<n; i++){ //This loop copies elements from arr into brr in reverse order
    brr[i] = arr[n-1-i]; //arr[n-1-i] accesses elements from the last to the first.
  }
  for(int i=0; i<n; i++){
    cout << brr[i] <<" "; // Printing the Reversed Array

  }
  cout << endl;
}