#ifndef PROOF_PLUGIN
#define PROOF_PLUGIN 1

#include "api.h"
#include <iostream>
#include <string>

class monkeys : public thingsInCasino
{
public:
  monkeys(const std::string name="") : thingsInCasino(name) {} //What's in a name?

  virtual void lookAt() const override
  {
    std::cout << "PLUGIN: AW FUCK! WHO BROUGHT MONKEYS INTO A CASINO????\n";
  }
};

class guessingGame : public game
{
public:
  guessingGame(const std::string name="OKUGIN{The Guessing GAME!}", const std::string val="five")
    : game(name), val(val) {} //What's in a name?

  virtual void lookAt() const override
  {
    std::cout << "PLUGIN: Your balls start to tingle as you your gaze and grabbed by "
                 "the outstanding beauty that is 'The Guessing Game'"
                 "\nPLUGIN: Must.\nPLUGIN: Play.\n";
  }

  virtual void play() override
  {
    std::cout << "PLUGIN: Hellos and Welcomes to THE WORLDS GREATEST GUESSING GAME!!"
                 " Let's play a game... Guess a number! (the answer is "
                 << val << ")\n";
    std::string guess;
    while((std::cin>>guess) && (guess != val))
    {
      std::cout << "PLUGIN: How fucking lame are you? I TOLD you the ANSWER!\nPLUGIN: You're "
                   "worse than that security gaurd... Try again: \n";
    }
    std::cout << "PLUGIN: About time.\n\n";
  }
private:
    std::string val;
};

class myPlugin
{
public:
  myPlugin(api& theAPI)
  {
    monkeys* monk = new monkeys;
    theAPI.addThingToCasino(*monk);

    securityOfficer* sec = new securityOfficer("PULGIN{Fuckface}", 10);
    theAPI.addThingToCasino(*sec);

    alcoholType* vermin = new alcoholType("PLUGIN{Bat semen}");
    theAPI.addThingToCasino(*vermin);

    guessingGame* guessingGameRegistrator = new guessingGame();
    theAPI.addGameToCasino(*guessingGameRegistrator);

    std::cout << "PLUGIN: myPlugin loaded.";
  }
};

#endif
