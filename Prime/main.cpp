#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
using namespace std;

unsigned int nthPrime(unsigned int n)
{
    vector<unsigned int> primes;
    unsigned int prime = 0;
    while (primes.size() <= n)
    {
        ++prime;
        if (prime % 2 == 0 || prime % 5 == 0)
            continue;        

        bool isPrime = true;
        for (unsigned int i = 3; i < prime/2; ++i)
            if (prime % i == 0)
            {
                isPrime = false;
                break;
            }
        
        if (isPrime)
            primes.push_back(prime);
    }
    
    if (primes.size()-1 >= 0)
        return primes[primes.size()-1];
    else
        return 0;
}

int main(int argc, char* argv[])
{
    if (argc != 2)
    {
        cout << "Don't mess with me\n";
        exit(0);
    }

    cout << nthPrime(atoi(argv[1])) << endl;
}
