package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	dat, err := ioutil.ReadFile("C://Users/Vasia/Documents/dev/advent-of-code-2015/Problems/Input/day1.txt")

	if err != nil {
		panic(err)
	}
	var count = 0
	var found = false
	for i := 0; i < len(dat); i++ {
        if dat[i] == '(' {
			count++
		} else {
			count--
		}
		if count < 0 && !found {
			fmt.Println("goes in basement at:",i+1)
			found = true
		}
    }
	fmt.Println(count)
}