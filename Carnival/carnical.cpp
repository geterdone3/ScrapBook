////////////////////////////////////////////////////////////////////////////////
// So to solve this, you need to enjoy yourself a little and play one of the  //
//  games to get money and buy some food, which will make a food object on    //
//  heap.  When you eat the food, it will delete the object, but it won't     //
//  delete the pointer to it, so you can still
////////////////////////////////////////////////////////////////////////////////

#include <iostream> /* For debug output */
#include <string>
using namespace std;

//Compile:
// g++ -Wall -Wextra -pedantic -std=c++1y carnical.cpp -o ObjectP

class inHandObject {}

class Merch() : public inHandObject
{
public:
    virtual void playWith() = 0;
}

class Food() : public inHandObject
{
public:
    virtual void eat() = 0;
    virtual void remember() = 0;
}

void eatFood()
{

}

int main()
{
    cout << "Welcome to the carnival! Please, play some games!\n\n";

    //Player Attibutes
    unsigned int money = 0;
    string name = "You";
    inHandObject* objectInHand = nullptr;
    vector<Merch*> merch;
    vector<Food*> food;

    while(1)
    {
        //Options:
        cout << "1: Check stats\n"
        cout << "2: Play a game\n";
        cout << "3: Buy some awesome merch\n";
        cout << "4: Grab a snack\n";
        cout << "5: Change item in hand\n";
        cout << "6: Buy the flag\n";


    }
}


void dataOverwrite()
{
    //Make object
    Object* object1 = new Object();

    cout << "Do you like apples?";
    cin >> object1->answer;

    /* <Load Data> */
    Object* object2 = new Object();

    for (size_t byteCount = 0; byteCount < sizeof(Object); ++byteCount)
    {
        *( (char*)object2 + byteCount) = object1->answer[byteCount];
    }
    /* </Load Data> */
}
