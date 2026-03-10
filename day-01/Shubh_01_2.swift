import Foundation

// same thing as p1 but we count how many it hits 0

let data = FileHandle.standardInput.readDataToEndOfFile()
let input = String(data: data, encoding: .utf8)!
let lines: [Substring] = input.split(separator: "\n")

var dial: Int = 50;
var pwd: Int = 0;

for line in lines {
    let a: Character = line.first!
    let r: Int = Int(line.dropFirst())!
    
    if a == "R" {
        var fin = dial + r;
        while (fin >= 100) {
            pwd += 1
            fin -= 100
        }
        dial = (dial + r) % 100
    } else {
        var fin = dial - r;
        while (fin < 0) {
            pwd += 1
            fin = 100 + fin;
        }
        dial = (dial - r) % 100
        if dial < 0 { 
            dial += 100
        }
    }
}

print(pwd)