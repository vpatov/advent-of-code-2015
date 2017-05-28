/*
--- Day 17: No Such Thing as Too Much ---
 The elves bought too much eggnog again - 150 liters this time.  To fit it all into your refrigerator, you'll need to move it into smaller containers.  You take an inventory of the capacities of the available containers. For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters.  If you need to store 25 liters, there are four ways to do it: 
15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
 15 and 10 20 and 5 (the first 5) 20 and 5 (the second 5) 15, 5, and 5 Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
*/

	
void problem_main(){

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
