package main

import (
  "fmt"
  "bufio"   
  "os"
  "strings"
  "strconv"
  "time"
)

func process_instruction1(inst string,lights *[1000][1000]int){
    parts := strings.Split(inst," ")
    var x1,y1,x2,y2 int
    var err error
    var inst_type string
    if parts[0] == "toggle" {
        x1,err = strconv.Atoi(parts[1][:strings.Index(parts[1],",")])
        y1,err = strconv.Atoi(parts[1][strings.Index(parts[1],",")+1:])
        x2,err = strconv.Atoi(parts[3][:strings.Index(parts[3],",")])
        y2,err = strconv.Atoi(parts[3][strings.Index(parts[3],",")+1:])
        if err != nil {panic(err)}
        inst_type = "toggle"
    } else {
        x1,err = strconv.Atoi(parts[2][:strings.Index(parts[2],",")])
        y1,err = strconv.Atoi(parts[2][strings.Index(parts[2],",")+1:])
        x2,err = strconv.Atoi(parts[4][:strings.Index(parts[4],",")])
        y2,err = strconv.Atoi(parts[4][strings.Index(parts[4],",")+1:])

        inst_type = parts[1]
    }
    switch inst_type {
    case "toggle":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                if (*lights)[i][j] != 0 {
                    (*lights)[i][j] = 0
                } else {
                    (*lights)[i][j] = 1
                }
            }
        }
    case "on":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                (*lights)[i][j] = 1
            }
        }
    case "off":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                (*lights)[i][j] = 0
            }
        }
    }
}
func process_instruction2(inst string,lights *[1000][1000]int){
    parts := strings.Split(inst," ")
    var x1,y1,x2,y2 int
    var err error
    var inst_type string
    if parts[0] == "toggle" {
        x1,err = strconv.Atoi(parts[1][:strings.Index(parts[1],",")])
        y1,err = strconv.Atoi(parts[1][strings.Index(parts[1],",")+1:])
        x2,err = strconv.Atoi(parts[3][:strings.Index(parts[3],",")])
        y2,err = strconv.Atoi(parts[3][strings.Index(parts[3],",")+1:])
        if err != nil {panic(err)}
        inst_type = "toggle"
    } else {
        x1,err = strconv.Atoi(parts[2][:strings.Index(parts[2],",")])
        y1,err = strconv.Atoi(parts[2][strings.Index(parts[2],",")+1:])
        x2,err = strconv.Atoi(parts[4][:strings.Index(parts[4],",")])
        y2,err = strconv.Atoi(parts[4][strings.Index(parts[4],",")+1:])

        inst_type = parts[1]
    }
    switch inst_type {
    case "toggle":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                (*lights)[i][j] += 2

            }
        }
    case "on":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                (*lights)[i][j] += 1
            }
        }
    case "off":
        for i := x1; i <= x2; i++ {
            for j := y1; j <= y2; j++ {
                if (*lights)[i][j] != 0 {
                    (*lights)[i][j] -= 1
                }
            }
        }
    }
}



func main(){
    start := time.Now()

    f, err := os.Open("../../Input/day6.txt")
    if err != nil {
        panic(err)
    }
    defer f.Close()

    // lights := make(map[string]int)
    var lights1 [1000][1000] int
    var lights2 [1000][1000] int

    sc := bufio.NewScanner(f)
    for sc.Scan() {
        line := sc.Text()
        process_instruction1(line,&lights1)
        process_instruction2(line,&lights2)
    }

    var count1 = 0
    for i := 0; i < 1000; i++ {
        for j := 0; j < 1000; j++ {
            count1 += lights1[i][j]
        }
    }

    var count2 = 0
    for i := 0; i < 1000; i++ {
        for j := 0; j < 1000; j++ {
            count2 += lights2[i][j]
        }
    }

    fmt.Println("Part I")
    fmt.Println(count1)
    fmt.Println("Part II")
    fmt.Println(count2)

    elapsed := time.Since(start)
    fmt.Printf("Program Execution Time: %s", elapsed)
}