//									//
//		           CS/ECE 752 : HW1 - sieve.cpp			//
//								        //
//    The following code uses the sieve of Eratosthenes  algorithm to  	//
//    compute the number of prime numbers between 2 and user input 'n'.	//
// 	    								//
// The algorithm has been sourced from the following source  : 		//
//  Algorithm Name :  Sieve of Eratosthenes         			//
//  Wikipedia Link : https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes//
//  									//



#include <iostream>
#include <stdbool.h>
#include <cmath>
#include <vector>

using namespace std;

int main(int argc, char *argv[]){

	// declaring variables used 
	int i, j, n, count;
	// count --> to keep count of number of prime numbers 
	// n --> used to accept the input number from user
	// Accepting n value 
	//cout << "Enter the value of n : ";
	//cin >> n;
        if (argc == 1) {
       		 n = 10;
   	 } 
	
	else if (argc == 2) {
   	     n = atoi(argv[1]);
	 }

	else {
	   cout << "Multiple variables given";
	} 
	//value of count is 0 initially
	count = 0;

	if (n<=1)
		cout << "Input should be greater than 1 \n";

	else {
		// Declaring and intialising a boolean vector/array to all true
		// The vector is of size n+1, and all values are initialised to 0
		vector <bool> a(n+1, true);
	
		//The values associated with 0 and 1 should be false since they are NOT prime numbers 
		a[0] = false;
		a[1] = false;

		// Eliminating non prime numbers 
	
		for (i=2; i<=sqrt(n);i++) {
			if (a[i]) {
				for (j=i*i; j <=n; j+=i)
					a[j] = false;
			}
		}

		// Displaying the final count value 

		for (i=2; i<=n;i++){
			if (a[i])
				count++;
		}

		cout<< count << "\n";

	}

	return 0;

}

