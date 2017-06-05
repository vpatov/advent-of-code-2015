package main

import (
  "fmt"
  "bufio"   
  "os"
  "strings"
  "strconv"
  "time"
)

type Wire struct {
    inst string
    wire_a string
    wire_b string
    val int
    is_val bool
}

var wires = make(map[string]Wire)

func process_instruction(instruction string){
    parts := strings.Split(instruction," ")
    end_wire := parts[len(parts) - 1]
    if parts[0] == "NOT" {
        val,err := strconv.Atoi(parts[1])
        if err != nil {
            wires[end_wire] = Wire{parts[0],parts[1],"IGNORE",0,false}
        } else {
            wires[end_wire] = Wire{parts[0],parts[1],"IGNORE",^val,true}
        }
    } else if len(parts) == 3 {
        wires[end_wire] = Wire{"SELF",parts[0],"IGNORE",0,false}
    } else {
        wires[end_wire] = Wire{parts[1],parts[0],parts[2],0,false}
    }

}

// def evaluate(wire):
//     if wire == "IGNORE": return None
//     if wire in wires:
//         try:
//             return int(wires[wire])
//         except:
//             operation,op1,op2 = wires[wire]
//             if operation == 'SELF':
//                 try:
//                     wires[wire] = int(op1)
//                     return wires[wire]
//                 except:
//                     pass
//             wires[wire] = operations[operation](evaluate(op1),evaluate(op2))
//             return wires[wire]
//     else: return int(wire)

func evaluate(wire string) Wire {
    //TODO
    return Wire{"a","b","c",0,false}
}

func main(){
    start := time.Now()

    f, err := os.Open("../../Input/day7.txt")
    if err != nil {
        panic(err)
    }
    defer f.Close()



    sc := bufio.NewScanner(f)
    for sc.Scan() {
        line := sc.Text()
        fmt.Println(line)

    }



    fmt.Println("Part I")

    fmt.Println("Part II")


    elapsed := time.Since(start)
    fmt.Printf("Program Execution Time: %s", elapsed)
}