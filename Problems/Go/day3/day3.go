package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
)

func main(){

	dat,err := ioutil.ReadFile("../../Input/day3.txt")
	if err != nil {panic(err)}
	
	visited1 := map[string]bool{"0-0":true}
	visited2 := map[string]bool{"0-0":true}
	var x,y,rx,ry,sx,sy = 0,0,0,0,0,0
	var robots_turn = false
	for i := 0; i < len(dat); i++ {
		 switch dat[i] {
			case '<':
				if robots_turn {
					rx -= 1
				} else {sx -= 1}
				x -= 1
			case '>':
				if robots_turn {
					rx += 1
				} else {sx += 1}
				x += 1
			case 'v':
				if robots_turn {
					ry -= 1
				} else {sy -= 1}
				y -= 1
			case '^':
				if robots_turn {
					ry += 1
				} else {sy += 1}
				y += 1
		}
		
		cur1 := strconv.Itoa(x) + "-" + strconv.Itoa(y)
		cur2 := strconv.Itoa(sx) + "-" + strconv.Itoa(sy)
		if robots_turn {
			cur2 = strconv.Itoa(rx) + "-" + strconv.Itoa(ry)
		}
		visited1[cur1] = true
		visited2[cur2] = true
		robots_turn = !robots_turn
	}
	fmt.Println("Part I")
	fmt.Println(len(visited1))
	fmt.Println("Part II")
	fmt.Println(len(visited2))

}
	