// Author : Kyle Martin

#ifndef PROOF_API
#define PROOF_API 1

#include <iostream>
#include <string>
#include <vector>

//The API can have functions
void apiCall()
{
  std::cout << "API: This is an API call.\n";
}

//The API can define its own types
////////////////////////////////////////////////////////////////////////////////
class thingsInCasino
{
public:
  thingsInCasino(const std::string& name) : name(name) {};

  virtual void lookAt() const = 0;

  std::string getName() const
  {
    return name;
  }

  virtual ~thingsInCasino() {}
private:
  std::string name;
};
void thingsInCasino::lookAt() const {}
////////////////////////////////////////////////////////////////////////////////
class securityOfficer : public thingsInCasino
{
public:
  securityOfficer(const std::string& name, const int toughness)
   : thingsInCasino(name), toughness(toughness) {}

  virtual void lookAt() const override
  {
    std::cout << "API: You notice their nametag.. " << thingsInCasino::getName()
              << ".\nAPI: ";
    if(toughness<5)
      std::cout << "They don't look too tough.. Probably shouldn't "
                   "test that though.\n";
    else if(toughness<8)
      std::cout << "They look pretty tough.. Probably shouldn't "
                   "mess with them.\n";
    else if(toughness<11)
      std::cout << "Fuck they're scary.. Do not approach!\n";
  }

private:
  const int toughness; //They look scary, maybe (0-10)
};
////////////////////////////////////////////////////////////////////////////////
class alcoholType : public thingsInCasino
{
public:
  using thingsInCasino::thingsInCasino;

  virtual void lookAt() const override
  {
    std::cout << "API: Oh look! " << thingsInCasino::getName() << "! I heard it's good!\n";
  }
};
////////////////////////////////////////////////////////////////////////////////
class game : public thingsInCasino
{
public:
    using thingsInCasino::thingsInCasino;

    virtual void play() =0;
};
void game::play() { std::cout << "API: Shit fam, games are fun.\n"; }
////////////////////////////////////////////////////////////////////////////////
//You get the idea.. How one can add their types... Not shown how to add
//features like a blackjack game or something
//class restaurants : public thingsInCasino {};
////////////////////////////////////////////////////////////////////////////////


//Maybe put the WHOLE API in a class? A super structure?
class api
{
public:
  api() : money(1000000)
  {
    std::cout << "API: Casino setup: sets up Casino-specfic things... Sets the rules"
                 " of the simluation.\nAPI: So think.. What does this simulation "
                 "inherently /need/?\n";//Enter any number to continue.\n\n";

    //Think for a moment
    //std::cin >> a; //Fuck, that was patronizing of me.. Sorry, I was tired as hell

    std::cout << "API: All Casinos need:\n Money\n Security\n Alcohol\n Games\n"
                 " Restaurants\n\nAPI: What specifcally? It depends on the Casino.."
                 "\nAPI: Do they have Blackjack? Poker? Dice? Slot machines?\nAPI: "
                 "Vodka? Beer? Wine? Rum?\nAPI: Chipotle? Olive Garden? Papa John's?\n";
  }

  //What can you do at a Casino? Let's start with walking around..
  void walkAround() const
  {
    std::cerr << "API: You walk around and you see everyone clutching their money "
                 "and their drinks as they nerviously avoid the gaze of the "
                 "private security detail spotted around the casino floor.\n";

    for (const thingsInCasino* thing : thingsICanSee)
    {
      thing->lookAt();
    }
  }

  void addThingToCasino(thingsInCasino& newThing)
  {
    thingsICanSee.push_back(&newThing);
  }

  void addGameToCasino(game& newGame)
  {
    addThingToCasino(newGame);
    games.push_back(&newGame);
  }

  void chooseGame() const
  {
    std::cout << "API: You look around to see what games there are to play..."
                 "You see:\n";
    int gameNum = 1;
    for (const game* aGame : games)
    {
      std::cout << gameNum << ": " << aGame->getName() << std::endl;
      ++gameNum;
    }
    std::cout << "API: What game would you like to play?\n";
    std::cin >> gameNum;

    //Dangerous.. Will kill children.  Do not ever use. I'm being lazy in my example (haha... this is lazy. Yeah. Sure)
    games.at(gameNum-1)->play();
  }

  ~api()
  {
    for(thingsInCasino* thing : thingsICanSee)
    {
      delete thing;
    }
  }

private:
  int a;
  double money; //All
  std::vector<securityOfficer*> securityDetail;
  std::vector<alcoholType*> alcohol;
  std::vector<game*> games;
  //std::vector<restaurant*> restaurants;  //Didn't define the class
  std::vector<thingsInCasino*> thingsICanSee;
};

#endif
