#include <iostream>
using namespace std ;

int main (){
	
	int construction ;
	float minInsurance = 0.8 ; 
	float insurance;
	
	cout << "enter building's replacement cost = ";
	cin >> construction;
	cout <<endl;
	
	insurance = construction*minInsurance;
	
	cout << "the min insurance is " <<insurance;
	
	
	
	
	return 0;
}
