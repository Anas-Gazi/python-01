#include <iostream>
#include<vector>
#include <algorithm> //algorithm header for sort()

using namespace std;

int main()
{
  int i;
    vector<int> v(5);
    for(i=0; i<v.size(); i++){
      cin>> v[i];  //Takes user input and stores it in the i-th position of the vector
    }
    for(i=0; i<v.size(); i++){
      cout<< v[i] <<" "; //This loop prints all elements of v before sorting.
    }
    cout<<endl;

    sort(v.begin(),v.end()); //The sort() function rearranges the elements in ascending order.
    // reverse(v.begin(),v.end()); // high to low

    for(i=0; i<v.size(); i++){
      cout<<v[i]<<" ";// final output after sorting  
    }
cout<< endl;
       return 0;
}
