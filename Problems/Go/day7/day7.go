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


var null_wire = Wire{"IGNORE","","",0,false}
var wires = make(map[string]Wire)

func value_wire(val int) Wire{
    return Wire{"VALUE","","",val,true}
}

func process_instruction(instruction string){
    parts := strings.Split(instruction," ")
    end_wire := parts[len(parts) - 1]
    if parts[0] == "NOT" {
        val,err := strconv.Atoi(parts[1])
        if err != nil {
            wires[end_wire] = Wire{parts[0],parts[1],"IGNORE",0,false}
        } else {
            wires[end_wire] = Wire{parts[0],parts[1],"VALUE",^val,true}
        }
    } else if len(parts) == 3 {
        wires[end_wire] = Wire{"VALUE","","",parts[0],true}
    } else {
        wires[end_wire] = Wire{parts[1],parts[0],parts[2],0,false}
    }

}




func evaluate(wire_str string) int {
    if wire_str == "IGNORE" 
}

func evaluate(wire_str string) Wire {
    //TODO
    if wire_str == "IGNORE" {
        return null_wire
    }
    wire,in := wires[wire_str]
    if in {
        if wire.is_val {
            return value_wire(wire.val)
        } else {
            if wire.inst == "SELF" {
                if wire.is_val {
                    return value_wire(wire.val)
                } 
            }
            switch wire.inst {
                case "AND": return evaluate(wire.wire_a) & evaluate(wire.wire_b)
                case "OR" : return evaluate(wire.wire_a) | evaluate(wire.wire_b)
                case "LSHIFT": return evaluate(wire.wire_a) << evaluate(wire.wire_b)
                case "RSHIFT": return evaluate(wire.wire_a) >> evaluate(wire.wire_b)
                case "NOT": return ^evaluate(wire.wire_a)
                case "SELF": return wire.wire_a
            }

        }
    } else {
        panic(1)
        return null_wire
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
        process_instruction(line)

    }



    fmt.Println("Part I")

    fmt.Println("Part II")


    elapsed := time.Since(start)
    fmt.Printf("Program Execution Time: %s", elapsed)
}