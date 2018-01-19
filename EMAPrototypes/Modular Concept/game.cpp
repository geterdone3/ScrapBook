#include "api.h"
//#include "pluggin.h" //Needed for pluggin
#include <iostream>
using namespace std;

//I'll think of a better way to do this, I imagine... But it's still an
  //impressive step in the right step
void loadPluggins(api& theAPI)
{
  //myPlugin plug1(theAPI);
}

int main()
{
  cout << "\nGAME: I'm a casino simulator!\n\nGAME: Here's an example API call: ";
  apiCall();

  cout << "\nGAME: Now I'm going to start up the API... This should set everything up"
          " that will be needed in the game.\n\nGAME: Initializing API:\n";

  api theAPI;

  cout << "GAME: Initialization over.\n\nGAME: Loading pluggins (through API): ";
  loadPluggins(theAPI);

  cout << "\nGAME: Finally, I can start the game (-1 to end): \n\n";

  int option = 0;
  while((option != -1))
  { //So it's 2:30 am.. I could make this a table of functons that the API holds
      //and pluggins add to, but f***ing s*** for rn. I have my proof of concept.
      //Good day.

    //This would be the series of apiCalls needed to run the game, that /make/ the game be the game
    cout << "GAME: What would you like to do?\n (1) Walk around\n (2) Play a game\n"
            "(-1) Quit\n";
    cin>>option; //Game defined user interaction
    cout << endl;

    switch(option) //Leave it up to the API to decide what to do with the rules that the game provides
    { //This is the game letting the API control what happens..
    case 1:
        theAPI.walkAround();
        break;
    case 2:
        theAPI.chooseGame();
        break;
    case -1:
        cout << "Good day!\n\n";
        return 1;
    }
  }
}
