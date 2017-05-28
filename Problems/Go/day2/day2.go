package main

import (
	"fmt"
	"strings"
	"bufio"
	"os"
	"strconv"
	"math"
)

func min(a,b int)int{
	return int(math.Min(float64(a),float64(b)))
}

func max(a,b int)int{
	return int(math.Max(float64(a),float64(b)))
}

func main() {
	f, err := os.Open("../../Input/day2.txt")

	if err != nil {
		panic(err)
	}
	defer f.Close()
	
	sc := bufio.NewScanner(f)
	var sum = 0 
	var ribbon = 0 
	for sc.Scan() {
		s := strings.Split(sc.Text(), "x")
		l, err := strconv.Atoi(s[0])
		w, err := strconv.Atoi(s[1])
		h, err := strconv.Atoi(s[2])
		var product = (2 * l*w) + (2 * w*h) + (2 * h*l)
		
		if err != nil {
			panic(err)
		}
		//Part 1
		sum += product
		var min_num = min(min(l*w, w*h), h*l)
		sum += min_num
		
		//Part 2
		var max_num = max(max(l, w), h)
		if (max_num == l) {
			ribbon += w + w + h + h
		} else if (max_num == w) {
			ribbon += l + l + h + h
		} else {
			ribbon += l + l + w + w
		}
		ribbon += l * w * h
		
    }
	
	fmt.Println("Part 1: " + strconv.Itoa(sum));
	fmt.Println("Part 2: " + strconv.Itoa(ribbon));

}