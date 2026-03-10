import Foundation

let data = FileHandle.standardInput.readDataToEndOfFile()
let input = String(data: data, encoding: .utf8)!
let lines: [Substring] = input.split(separator: "\n")

var dial: Int = 50;
var pwd: Int = 0;

for line in lines {
    let a: Character = line.first!
    let r: Int = Int(line.dropFirst())!
    
    if a == "R" {
        dial = (dial + r) % 100
    } else {
        dial = (dial - r) % 100
        if dial < 0 { 
            dial += 100
        }
    }
    
    if (dial == 0) {
        pwd += 1
    }
}

print(pwd)