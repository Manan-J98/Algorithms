class Solution {
    func calPoints(_ ops: [String]) -> Int {
        var resultArray = [Int]()
        for operation in ops {
            if operation == "C" {
                resultArray.removeLast()
            } else if operation == "D" {
                resultArray.append(2*resultArray[resultArray.count-1])
            } else if operation == "+" {                
                resultArray.append(resultArray[resultArray.count-1] + resultArray[resultArray.count-2])
            } else {
                resultArray.append(Int(operation) ?? 0) 
            }
        }
        return resultArray.reduce(0,+)
    }
}