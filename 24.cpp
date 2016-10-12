#include <iostream>
#include <string>
using namespace std ; 


int main(){
	
	int things=7;
	string arr[things] = {"name","age","city","college","proffesion","animal","pet's name"};
	string answer[things];
	
	for (int i=0 ;  i < things ;i++)
	{
		cout << "enter the " << arr[i] <<" : ";
		cin >> answer[i];
		cout << endl;
	}
	
	cout << "there once was a person named " << answer[0]<<" who lived in" << answer[2] <<". At the age of "<< answer[1]<<endl
		<< " , "<<answer[0]<<" went to college at "<<answer[3]<<" . "<<answer[0]<<" graduated and went to work as a "<<endl
		<<answer[4] << " . Then , "<<answer[0]<<" adopted a(n) "<<answer[5]<<" named "<<answer[6]<<endl
		<<" . And they both lived happily ever after!!!";
	
	
	return 0;
}
