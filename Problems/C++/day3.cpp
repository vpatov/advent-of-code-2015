/*
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
 Santa is delivering presents to an infinite two-dimensional grid of houses. He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next.  Moves are always exactly one house to the north (^), south (v), east (>), or west (<).  After each move, he delivers another present to the house at his new location. However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once.  How many houses receive at least one present? For example: 
> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
 > delivers presents to 2 houses: one at the starting location, and one to the east. ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location. ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
*/

#include <fstream>
#include <iostream>
#include <string>
#include <time.h>
#include <map>
#include <set>

using namespace std;


void problem_main(){
	// keep track of the places visited
	map<pair<int,int>,int> visited1 = *new map<pair<int,int>,int>;
	map<pair<int,int>,int> visited2 = *new map<pair<int,int>,int>;
	//part I coordinates 
	int x = 0, y = 0;
	//Part II robot santa coordinates, and santa coordinates
	int rx = 0, ry = 0, sx = 0, sy = 0;
	//when true, it is the robots turn
	bool robos_turn = false;
	
	ifstream infile("../Input/day3.txt");
	char ch;
	if (!infile.is_open()){
		cout << "file not found" << endl;
	}
	
	visited1.insert(make_pair(make_pair(x,y),0));
	//they both start at the same place, either sx or rx will do.
	visited2.insert(make_pair(make_pair(sx,sy),0));
	while (infile >> ch) {	
		switch (ch) {
			case '<': robos_turn?rx--:sx--; x--; break;
			case '>': robos_turn?rx++:sx++; x++; break;
			case 'v': robos_turn?ry--:sy--; y--; break;
			case '^': robos_turn?ry++:sy++; y++; break;
			default: ;
		}
		pair<int,int> cur1 = make_pair(x,y);
		pair<int,int> cur2 = robos_turn?make_pair(rx,ry):make_pair(sx,sy);
		
		map<pair<int,int>,int>::iterator it1 = visited1.find(cur1);
		if (it1 != visited1.end()){
			it1->second++;
		}
		else {		
			visited1.insert(make_pair(cur1,0));
		}
		
		map<pair<int,int>,int>::iterator it2 = visited2.find(cur2);
		if (it2 != visited2.end()){
			it2->second++;
		}
		else {		
			visited2.insert(make_pair(cur2,0));
		}
		
		robos_turn = !robos_turn;
	}
	cout << "Part I" << endl;
	cout << visited1.size() << endl;
	cout << "Part II" << endl;
	cout << visited2.size() << endl;
	
}


	
int main(){
	std::cout<<"\n";
	clock_t t1,t2;
    t1=clock();
	
	problem_main();
		
    t2=clock();
	cout<<"\nProgram Execution Time: ";
    float diff ((float)t2-(float)t1);
	float seconds = diff / CLOCKS_PER_SEC;
    cout<<seconds<<" seconds."<<endl;
    return 0;

}
