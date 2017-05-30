package main

import (
  "fmt"
  "bufio"	
  "os"
  "strings"
  "time"
)

var vowels = map[byte]bool{'a':true,'e':true,'i':true,'o':true,'u':true}
var forbidden = map[string]bool{"ab":true,"cd":true,"pq":true,"xy":true}

func is_nice1(str string) bool{
	var count_vowel = 0
	for i := 0; i < len(str); i++ {
		_, in := vowels[str[i]]
		if in {
			count_vowel++
		}
	}
	if count_vowel < 3{
		return false
	}
	var cond2 = false
	for i := 0; i < len(str) - 1; i++ {
		if str[i] == str[i+1] {
			cond2 = true
			break
		}
	}
	if (!cond2){
		return false
	}

	for key := range forbidden {
		if strings.Contains(str,key) {
			return false
		}
	}
	return true
}

func is_nice2(str string)bool{
	//condition1
	cond1 := false
	first_pair := str[0:2]
	pairs := make([]string,len(str))
	pairs[0] = first_pair
	for i := 2; i < len(str); i++ {
		pair := str[i-1:i+1]
		j := i - 3
		for {
			if j < 0 {
				break
			}
			// fmt.Println("pairs[j] " + pairs[j])
			// fmt.Println("pair: " + pair)
			if pairs[j] == pair {
				cond1 = true
				break
			}
			j--
		}
		pairs[i-1] = pair
	}
	if !cond1 {
		return false
	}

	//condition2
	for i := 0; i < len(str) - 2; i++ {
		if str[i] == str[i+2] {
			return true
		}
	}
	return false
	
}

func main(){
	start := time.Now()

	f, err := os.Open("../../Input/day5.txt")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	
	var nice_count1 = 0
	var nice_count2 = 0
	sc := bufio.NewScanner(f)
	for sc.Scan() {
		line := sc.Text()
		if is_nice1(line) {
			nice_count1++
		}
		if is_nice2(line) {
			nice_count2++
		}
	}
	fmt.Println("Part I")
	fmt.Println(nice_count1)
	fmt.Println("Part II")
	fmt.Println(nice_count2)


	elapsed := time.Since(start)
    fmt.Printf("Program Execution Time: %s", elapsed)

}