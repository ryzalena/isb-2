#include<iostream>
#include<ctime>
#include<fstream>

using namespace std;

int main()
{
	srand(time(NULL));
	int randomNumber[128];
	ofstream fin("result.txt"); 
	for (int i = 0; i < 128; i++)
	{
		randomNumber[i] = rand() % 2;	
		cout << randomNumber[i];
		fin << randomNumber[i];
		fin << ",";
	}
	fin.close();
	return 0;
	

}
