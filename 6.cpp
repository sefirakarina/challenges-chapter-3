#include <iostream>
using namespace std ; 


int main(){
	
	float sugar=1.5/48;
	float butter= 1.0/48;
	float flour=2.75/48;
	float sugarr , butterr , flourr;
	int cookie;
	
	cout << "enter how many cookie(s) you want to make : ";
	cin>>cookie ;
	
	sugarr = sugar*cookie ;
	butterr = butter*cookie;
	flourr = flour*cookie;
	
	cout << "you'll need " << sugarr <<" cups of sugar, "<<endl;
	cout << "and you'll need " << butterr <<" cups of butter, "<<endl;
	cout << "also you'll need " << flourr <<" cups of flour "<<endl;

	return 0;
}
