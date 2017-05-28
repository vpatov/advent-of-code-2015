/*
--- Day 2: I Was Told There Would Be No Math ---
 The elves are running low on wrapping paper, and so they need to submit an order for more.  They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need. Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.  The elves also need a little extra paper for each present: the area of the smallest side. For example: 
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
 A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in feet.  How many total square feet of wrapping paper should they order?
*/

#include <iostream>
#include <time.h>
#include <fstream>
#include <vector>
#include <sstream>

using namespace std;

std::vector<std::string> split(const std::string &s, char delim) {
	std::vector<std::string> elems;
	std::stringstream ss(s);
	std::string item;
	while (std::getline(ss, item, delim)) {
		elems.push_back(item);
	}
	return elems;
}




int parseInt(const std::string &s) {
	int i = 0;
	int ans = 0;
	int power = 1;
	for (i = s.length() - 1; i >= 0; i--) {
		ans += (((int)(s[i])) - ((int)('0'))) * power;
		power *= 10;
	}
	return ans;
}

int min(int a, int b, int c) {
	if (a <= b && a <= c)
		return a;
	else if (b <= a && b <= c)
		return b;
	else return c;
}

int max(int a, int b, int c) {
	if (a >= b && a >= c)
		return a;
	else if (b >= a && b >= c)
		return b;
	else return c;
}
void problem_main() {
	/*
	3x11x24
	13x5x19
	1x9x27

	*/
	string line;
	ifstream myfile("../Input/day2.txt");


	if (myfile.is_open())
	{
		int sum = 0;
		int ribbon = 0;
		while (getline(myfile, line))
		{
			// length, width, height : l, w, h
			std::vector<std::string> temp = split(line, 'x');
			int l = parseInt(temp[0]);
			int w = parseInt(temp[1]);
			int h = parseInt(temp[2]);
			int product = (2 * l*w) + (2 * w*h) + (2 * h*l);

			//Part I


			sum += product;
			int minNum = min(l*w, w*h, h*l);
			sum += minNum;


			//Part 2
			int maxNum = max(l, w, h);
			if (maxNum == l) {
				ribbon += w + w + h + h;
			}
			else if (maxNum == w) {
				ribbon += l + l + h + h;
			}
			else {
				ribbon += l + l + w + w;
			}

			ribbon += l * w * h;



		}
		cout << "answer is:" << sum << endl;
		cout << "ribbon is:" << ribbon << endl;
		myfile.close();

	}

	else cout << "Unable to open file";
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
