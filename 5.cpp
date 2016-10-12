#include <iostream>
using namespace std ; 


int main(){
	
	int female,male;
	float total , femalePer , malePer;
	
	cout << "enter the number of female(s) = " ;
	cin>> female ;
	cout <<endl;
	
	cout << "enter the number of male(s)   = " ;
	cin>> male;
	cout <<endl;
	
	total = female+male;
	
	femalePer= female/total * 100;
	malePer=male/total *100;
	
	cout << "female percentage = " <<femalePer << " %"<<endl;
	cout << "male percentage   = " <<malePer <<" %"<<endl;
	
	
	
	
	return 0;
}
