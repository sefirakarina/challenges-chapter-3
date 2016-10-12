#include <iostream>
#include <string>
using namespace std ; 

int main(){
	
	float monthly=0;
	float annual;
	
	
	const int things = 6;
	
	string pay[things] =  {"loan","insurance","gas","oil","tires","maintainance"};
	float price[things];
	
	for (int i=0 ; i < things ; i++)
	{ 
		cout << "enter monthly payment for " << pay[i] << " = ";
		cin >> price[i];            
		cout <<endl;
		
		monthly = monthly+price[i];
		
	}

	cout << "total montly payment = " << monthly <<endl;
	
	annual = 12*monthly;
	
	cout << "annual payment = " <<annual ;
	
	return 0;
}
