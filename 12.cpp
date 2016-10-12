#include <iostream>
using namespace std ; 


int main(){
	
	float celcius;
	float fah;
	
	cout << "enter a celcius temprature = " ;
	cin >> celcius ;
	cout<<endl;
	
	fah = ((9/5)*celcius) +32;
	
	cout << "equal to " << fah << " degree fahrenheit";
	
	
	return 0;
}
