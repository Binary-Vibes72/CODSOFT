#include<iostream>
using namespace std;

int main() {
    int a, b, choice; 
    bool flag = true;
    char repeat;

    while(flag){
        cout<<"Enter the first number: "<<endl;
        cin>>a;
        cout<<"Enter the first number: "<<endl;
        cin>>b;

        cout<<"Choice operation from following."<<endl;
        cout<<"(1)---Addtion"<<endl; 
        cout<<"(2)---Substraction"<<endl; 
        cout<<"(3)---Multiplication"<<endl; 
        cout<<"(4)---Division"<<endl;  
        cin>>choice;

        if(choice == 1){
            cout<<"Addition of "<<a<<" and "<<b<<" is: "<<a+b<<endl;
        }
        else if(choice == 2){
            cout<<"Substraction of "<<a<<" and "<<b<<" is: "<<a-b<<endl;
        }
        else if(choice == 3){
            cout<<"Multiplication of "<<a<<" and "<<b<<" is: "<<a*b<<endl;
        }
        else if(choice == 4){
            cout<<"Division of "<<a<<" and "<<b<<" is: "<<a/b<<endl;
        }
        else{
            cout<<"Invalid Choice. try again!!!";
        }
        
        cout<<"Do you want to calculate again (y/n): ";
        cin>>repeat;

        if(tolower(repeat) == 'y'){
            cout<<"Restarting..."<<endl<<endl;
        }
        else{
            cout<<"Thank you for using"<<endl;
            flag = false;
        }
    }
}