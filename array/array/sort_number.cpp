#include <iostream>
#include<algorithm> // for using sort
using namespace std;

int main()
{
    int arr[5]= {9,80,65,5,0};

    // for(int i=0; i<5; i++){  // value na likhle:)
    //   cin >> arr[i];
    // }
    sort(arr, arr + 5, greater<int>());
 
    for(int i=0; i<5; i++){
      cout<<arr[i] <<" ";
    }
       return 0;
}
/*so "sort means lowest to highest.. and 
  if u need to print lowest to highest then use sort(arr, arr + 5) cz
  sort(arr, arr + 5, greater<int>()); it will print highest to lowest :)

  btw pc er file o kintu sort kora jay.. haha ekhn ei check koro:)
"*/