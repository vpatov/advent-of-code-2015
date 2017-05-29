/*
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
 Santa is delivering presents to an infinite two-dimensional grid of houses. He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next.  Moves are always exactly one house to the north (^), south (v), east (>), or west (<).  After each move, he delivers another present to the house at his new location. However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once.  How many houses receive at least one present? For example: 
> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
 > delivers presents to 2 houses: one at the starting location, and one to the east. ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location. ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
*/
import java.util.HashSet;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
public class day3{
	
	public static void problem_main(){
	// keep track of the places visited
	HashSet<String> visited1 = new HashSet<>();
	HashSet<String> visited2 = new HashSet<>();

	//part I coordinates 
	int x = 0, y = 0;
	//Part II robot santa coordinates, and santa coordinates
	int rx = 0, ry = 0, sx = 0, sy = 0;
	//when true, it is the robots turn
	boolean robos_turn = false;
	
	try{
		Scanner sc = new Scanner(new File("../Input/day3.txt"));
		sc.useDelimiter("");
		char ch;
		
		//Add the place we are at now to the set.
		visited1.add(x + "-" + y);
		visited2.add(sx + "-" + sy);
		
		while(sc.hasNext()){
			ch = sc.next().charAt(0);
			//garbage variable to allow ternary conditional
			int g;
			switch (ch) {
				case '<': g=(robos_turn)?(rx--):sx--; x--; break;
				case '>': g=(robos_turn)?(rx++):sx++; x++; break;
				case 'v': g=(robos_turn)?(ry--):sy--; y--; break;
				case '^': g=(robos_turn)?(ry++):sy++; y++; break;
				default:;
			}

			visited1.add(x + "-" + y);
			visited2.add(robos_turn?rx + "-" + ry:sx + "-" + sy);
			robos_turn = !robos_turn;
		}
	}
	catch(FileNotFoundException f){}

	System.out.println("Part I");
	System.out.println(visited1.size());
	System.out.println("Part II");
	System.out.println(visited2.size());
}

	public static void main(String[]args){
		long start_time = System.currentTimeMillis();
		problem_main();
		long end_time = System.currentTimeMillis();
		System.out.println("\nProgram Execution Time: " + (end_time - start_time) + "seconds.");
	}
}