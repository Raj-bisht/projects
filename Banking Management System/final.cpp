//Banking record system
#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;
using std::ios;
#include"acc.h"
int main()
{
    account_query ob;
    int choice;
    cout<<"---Account Information System---"<<endl;
    while(true)
    {
        cout<<"\n1  Add record to file";
        cout<<"\n2  Show record from file";
        cout<<"\n3  Search Record from file";
        cout<<"\n4  Update Record";
        cout<<"\n5  Delete Record";
        cout<<"\n6  Quit";
        cout<<"\nEnter your choice :";
        cin>>choice;
        switch(choice)
        {
        case 1:
            ob.write_rec();
            break;
        case 2:
            ob.read_rec();
            break;
        case 3:
            ob.search_rec();
            break;
        case 4:
            ob.edit_rec();
            break;
        case 5:
            ob.delete_rec();
            break;
        case 6:
            exit(0);
            break;
        default:
            cout<<"\nInvalid choice";
            exit(0);
        }
    }
    system("pause");
    return 0;
}
