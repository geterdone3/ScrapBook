#include <iostream>
#include <thread> //Need to set compiler flag ... "-pthread" or soemthing
using namespace std;

void someFunc()
{
    cerr << "In somefunc\n";
}

int main()
{
    cerr << "Calling someFunc\n";
    thread myThread(someFunc);
    cerr << "Back from thread\n";
    myThread.join(); //Or myThread.detach() - let it go off and do it's stuff
    cerr << "Main out\n";
}
