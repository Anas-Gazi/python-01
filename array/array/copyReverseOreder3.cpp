#include<iostream>
using namespace std;

int main(){
  int arr[]= {10,20,30,40,50};
  int n=sizeof(arr)/sizeof(arr[0]);

  for(int i=0; i<n; i++){
    cout << arr[i] << " ";
  }
  cout<< endl;
  //starting point
  int i=2; // start from 3rd array
  //ending point
  int j= n-1;
  while(i<j){
   /*swap(arr[i], arr[j]);
   i++;
   j--;*/ //insted of this.. we can write
  int temp = arr[i];
  arr[i]= arr[j];
  arr[j]= temp;
  i++;
  j--;
  }
  for(int i=0; i<n; i++){
    cout<< arr[i]<< " ";
  }
  cout<<endl;
}