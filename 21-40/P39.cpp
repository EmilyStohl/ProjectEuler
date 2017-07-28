// Project Euler - Problem 39
// 4/23/2017
#include <iostream>
#include <math.h>

int CheckSquare(int Num){
// Check if Num has an integer square root
// Returns 0 if sqrt is not an int, otherwise returns sqrt(num)
  int SqRt = 1;
  int Square = SqRt*SqRt;
  while (Square < Num+1){
    Square = SqRt*SqRt;
    if (Square == Num){
      return SqRt;
    }
    SqRt = SqRt + 1;
  }
  return 0;
}

int main(){
  
int P_count[4001];
for (int x = 0; x<4001; x ++){
  P_count[x] = 0;
}
for (int i = 1; i < 1000; i++){
  for (int j = i; j < 1000; j++){
    int HypSq = i*i + j*j;
    int Hyp = CheckSquare(HypSq);
    if (Hyp > 0 ){
      P_count[i+j+Hyp] = P_count[i+j+Hyp]+1;
    }
  }  
}
  
int MaxIndex;
int MaxVal = 0;  
for (int k =0; k<1001; k++){
  if (P_count[k] > MaxVal){
    MaxVal = P_count[k];
    MaxIndex = k;
  }
}
std::cout << MaxIndex << "\n";
return 0;
}



