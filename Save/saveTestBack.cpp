#include <iostream> /* For debug output */
#include <fstream>  /* For saving */
using namespace std;

//Compile:
// g++ -Wall -Wextra -pedantic -std=c++1y saveTest.cpp -o testP

class Test
{
public:
    unsigned int var1 = 8;
};

void save(Test* test);
Test* load();

int main()
{
    //Save
    Test* savedTest = new Test();
    savedTest->var1 = 177;
    save(savedTest);

    //Load
    Test* loadedTest = load();
    cerr << loadedTest->var1 << endl;
    cerr << "Done!\n";
}

void save(Test* test)
{
    //Open the save file
    string saveFilename = "test.dat";
    ofstream file(saveFilename, std::ios::binary);
    if (!file)
    {
        cerr << "Could not create file.\n" << saveFilename << endl;
        return;
    }

    /* <Write Data> */
    //Way #1:
    for (size_t byteCount = 0; byteCount < sizeof(Test); ++byteCount)
    {
        file << *( (char*)test + byteCount);
    }

    //Way #2:
    // file.write((char *)test, sizeof(Test));

    /* </Write Data> */

    file.close();
}

Test* load()
{
    //Open the save file
    string filename = "test.dat";
    ifstream file(filename, std::ios::binary);
    if (!file)
    {
        cerr << "File failed to open.\n";
        return nullptr;
    }

    /* <Load Data> */
    //Get a place to overwrite
    Test* newTest = new Test;

    //Way #1:
    unsigned char byte = ' ';
    for (size_t byteCount = 0; byteCount < sizeof(Test); ++byteCount)
    {
        file >> byte;
        *( (char*)newTest + byteCount) = byte;
    }

    //Way #2:
    //file.read((char *)newTest, sizeof(Test));

    /* </Load Data> */

    file.close();

    return newTest;
}
