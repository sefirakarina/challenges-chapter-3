#include <iostream>
using namespace std ; 


int main(){
	
	float classA , classB , classC;
	classA=15 ; classB=12 ; classC=9;
	float totalA,totalB,totalC;
	float numberA,numberB,numberC,total;
	
	cout << "number of class A ticket = ";
	cin >> numberA ; 
	cout<<endl ;
	
	cout << "number of class B ticket = ";
	cin >> numberB ;
	cout<< endl ;
	
	cout << "number of class C ticket = ";
	cin >> numberC ;
	cout<< endl ;
	
	totalA=classA*numberA;
	totalB=classB*numberB;
	totalC=classC*numberC;
	
	total=totalA+totalB+totalC;
	
	cout << "total profit A = " << totalA<<endl;
	cout << "total profit B = " << totalB<<endl;
	cout << "total profit C = " << totalC<<endl<<endl;
	
	cout << "total all = " << total;
	
	
	
	return 0;
}

