package main

import (
  "crypto/md5"
  "fmt"
  "io"
  "strconv"
  "encoding/hex"
  "time"
)

func main(){
	start := time.Now()

	var input string = "iwrupvqb"
	var i = 0
	//Part I
	fmt.Println("Part I")
	for {
		h := md5.New()
		io.WriteString(h, input + strconv.Itoa(i))
		hash := h.Sum(nil)
		start := hex.EncodeToString(hash)[0:5]
		if start == "00000"{
			fmt.Println(i)
			break
		}
		i += 1
	}


	//Part II
	fmt.Println("Part II")
	for {
		h := md5.New()
		io.WriteString(h, input + strconv.Itoa(i))
		hash := h.Sum(nil)
		start := hex.EncodeToString(hash)[0:6]
		if start == "000000"{
			fmt.Println(i)
			break
		}
		i += 1
	}


	elapsed := time.Since(start)
    fmt.Printf("Program Execution Time: %s", elapsed)

}