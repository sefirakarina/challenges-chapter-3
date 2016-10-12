#include <iostream>
#include <math.h>
using namespace std ; 


int main(){
	
	float N,L; // N = number of payment , L = amount of loan
	float rate = 0.01 ;
	float x; 
	float y;
	float payment ;
	
	cout << "enter number of payment = " ;
	cin >> N ;
	cout <<endl;
	
	cout <<"enter amount of loan = ";
	cin >> L ;
	cout <<endl;
	
	x = rate+1;
	y = pow(x,N);
	
	payment = ((rate*y)/(y-1))*L;
	
	cout << "monthly payment = " << payment ;
	
	return 0;
}
