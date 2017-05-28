/*
--- Day 5: Doesn't He Have Intern-Elves For This? ---
 Santa needs help figuring out which strings in his text file are naughty or nice. A nice string is one with all of the following properties: 
It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
 It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd). It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements. For example: 
ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
 ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings. aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap. jchzalrnumimnmhp is naughty because it has no double letter. haegwjzuvuyypxyu is naughty because it contains the string xy. dvszwmarrgswjxmb is naughty because it contains only one vowel. How many strings are nice?
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
