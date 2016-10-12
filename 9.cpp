#include <iostream>
using namespace std ; 

int main (){
	
const int caloriesPerCookie = 100 ;
int cookie;
int calories;


cout << "enter how many cookie(s) you ate :  ";
cin >> cookie ;
cout <<endl;

calories = caloriesPerCookie * cookie;

cout << calories <<" calories";
	
	return 0;
}
