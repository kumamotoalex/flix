#include <iostream>
#include <fstream>
using namespace std;

int main()
{
  ifstream fin;
  fin.open("movies");
  string dum;
  int n;fin>>n;
  getline(fin,dum);
  int preferences[n];
  for(int i=0;i<n;i++)
  {
    string movie;
    getline(fin,movie);
    cout<<"Enter your rating (0 or 1) for "<<movie<<": ";
    cin>>preferences[i];
  }
  fin.close();

  ifstream fin2;
  fin2.open("players");
  int numplayers; fin2>>numplayers;
  for(int i=0;i<numplayers;i++)
  {
    int dotprod=0;
    for(int j=0;j<n;j++)
    {
      int playerpref;fin2>>playerpref;
      dotprod+=playerpref*preferences[j];
    }
    cout<<"Match score with player "<<(i+1)<<": "<<dotprod<<endl;
  }
  fin2.close();
  return 0;
}
