#include <iostream>
using namespace std ; 


int main(){
	
//	float numberA,numberB,numberC,numberD,numberE;
	float average;
	
	const int student = 5;
	float score[student];
	
	float total = 0;

	
	for(int i=0 ; i<student ; i++)
	{
		cout << "score " <<i+1 << " = ";
		cin >> score[i];	
		cout<<endl;
		 
		total = total + score[i]; 
	}
	
		average = total/student;
		
		cout << "average score = " << average;
		 

	 
	 	
/* MANUAL WAY :

	cout << "SCORE 1 = ";
	cin >> numberA ; 
	cout<<endl ;
	
	cout << "SCORE 2 =  ";
	cin >> numberB ;
	cout<< endl ;
	
	cout << "SCORE 3 =  ";
	cin >> numberC ;
	cout<< endl ; 
	
	cout << "SCORE 4 =  ";
	cin >> numberD ;
	cout<< endl ; 
	
	cout << "SCORE 5 =  ";
	cin >> numberE ;
	cout<< endl ; 

	
	average = (numberA+numberB+numberC+numberD+numberE)/5;
	
	cout <<"average = "<<average;
*/	
	return 0;
}
