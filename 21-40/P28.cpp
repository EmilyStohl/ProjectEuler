// Project Euler - Problem 28
// 1/10/17

#include <iostream>

int main(){
	int size = 1001;
	int Box[size][size];
	for (int row= 0; row< size; row++){
		for (int col= 0; col< size; col++){
			Box[row][col] = 0;
		}
	}
	signed int direction[8]= {0, -1, 1, 0, 0, 1, -1, 0};
	
	signed int RowInc = direction[0];
	signed int ColInc = direction[1];
	int index = 0;
	signed int row = 0;
	signed int col = size-1;
	for (int i = size*size; i> 0; i--){
		Box[row][col] = i;
		//std::cout << i << row+RowInc << col+ColInc<< std::endl;
		// Increment: 
		if ((row+RowInc >= 0) && (row+RowInc < size) && (col+ColInc >= 0) && (col+ColInc < size) && (Box[row+RowInc][col+ColInc] == 0)){
			row=row+RowInc;
			col = col+ColInc;
			
		}
		else{
			index = (index+1)%4;
			//std::cout << "index " << index << std::endl;
			RowInc = direction[2*index ];
			ColInc = direction[2*index+1];
			row=row+RowInc;
			col = col+ColInc;
		}
		
	
	}
	int Sum = 0;
	for (int i=0; i<size;i++){
		Sum = Sum + Box[i][i];
	}
	for (int i=0; i<size;i++){
		Sum = Sum + Box[size-i-1][i];
	}
	Sum = Sum - 1;
	std::cout << Sum << std::endl;
	
	
     return 0;
};
