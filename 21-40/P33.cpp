// Project Euler - Problem 33
// 3/22/2017
#include <iostream>
#include <math.h>

int main(){

  float NumerProduct = 1.0;
  float DenomProduct = 1.0;

for (int a=1; a<10; a++){
  for (int b = 1; b<10; b++){
    for (int c = 1; c<10; c++){
      
      float Numer = a*10 + b;
      float Denom = b*10 + c;
      float AC = (float)a/(float)c;
      float frac = Numer/Denom;
      if (frac < 1.0){
        if (fabs(frac - AC) < 0.00001){
          std::cout << Numer << ", " << Denom << "\n";
          NumerProduct = NumerProduct*Numer;
          DenomProduct = DenomProduct*Denom;
          
        }
      }
       
      
    } 
  } 
}

std::cout << DenomProduct/NumerProduct << "\n";  
  
return 0;
}