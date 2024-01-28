#include<iostream>
#include<cstdlib>
#include<ctime>
#include<unistd.h>
using namespace std;

// Public Variables.
int userGuess, randomGuess;
char choice;
bool flag = true;

// Function Decoration
void randomGen();
void userInput();
void program();
void replay();
void compare();

// Function for random generating random int.
void randomGen(){
    srand((unsigned) time(0));
    randomGuess = rand() % 10;
}

// Function for taking the user input.
void userInput(){
    cout<<"Guess the Number: "<<endl;
    cin>>userGuess;
    compare();
}

// Starting Program.
void program(){
    cout<<endl;
    cout<<endl;
    cout<<"----| Welcome to Number Guessing Game |----"<<endl;
    cout<<"Computer Guessed the number. Now it's your turn."<<endl;
    randomGen();
    userInput();
}

// Replaying the 
void replay(){
    while(flag){
        cout<<"Do you want to play again(y/n): ";
        cin>>choice;
        if((char)tolower(choice) == 'y'){
            cout<<"restarting Game..."<<endl;
            sleep(2);
            program();
            break;
        }
        else if((char)tolower(choice) == 'n'){
            cout<<"Thank you for Playing"<<endl;
            break;
        }
        else{
            cout<<"Invalid Choice. Choose from (y/n). Try Again."<<endl;
            replay();
            break;
        }
    }
}

// Function for Comparing the numbers
void compare(){
    if(randomGuess == userGuess){
        cout<<"You Guessed the right number."<<endl;
        replay();
    }
    else if(randomGuess > userGuess){
        cout<<"Number is smaller than Computer Guess. Try Again."<<endl;
        userInput();
    }
    else if(randomGuess < userGuess){
        cout<<"Number is Higher than Computer Guess. Try Again."<<endl;
        userInput();
    }
}

//main function
int main(){
    program();
}