/*
--- Day 2: I Was Told There Would Be No Math ---
 The elves are running low on wrapping paper, and so they need to submit an order for more.  They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need. Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.  The elves also need a little extra paper for each present: the area of the smallest side. For example: 
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
 A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet. All numbers in the elves' list are in feet.  How many total square feet of wrapping paper should they order?
*/
import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.Math;
public class day2{
	
	public static void problem_main() {	
		try{
			Scanner sc = new Scanner(new File("../Input/day2.txt"));
			int sum = 0;
			int ribbon = 0;
			while (sc.hasNext()){
				String line = sc.nextLine();
				String parts[] = line.split("x",3);
				int l = Integer.parseInt(parts[0]);
				int w = Integer.parseInt(parts[1]);
				int h = Integer.parseInt(parts[2]);
				int product = (2 * l*w) + (2 * w*h) + (2 * h*l);
				
				//Part 1
				sum += product;
				int min_num = Math.min(Math.min(l*w, w*h), h*l);
				sum += min_num;
				
				//Part 2
				int max_num = Math.max(Math.max(l, w), h);
				if (max_num == l) {
					ribbon += w + w + h + h;
				}
				else if (max_num == w) {
					ribbon += l + l + h + h;
				}
				else {
					ribbon += l + l + w + w;
				}
				ribbon += l * w * h;
			}
			System.out.println("Part 1: " + sum);
			System.out.println("Part 2: " + ribbon);
		}
		catch (FileNotFoundException f){
			
		}
	}

	

	public static void main(String[]args){
		long start_time = System.currentTimeMillis();
		problem_main();
		long end_time = System.currentTimeMillis();

	System.out.println("\nProgram Execution Time: " + (end_time - start_time) + "seconds.");

	}

}