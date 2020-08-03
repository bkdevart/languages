
class Solution {
    /*
     Things learned:
     - search speed dramatically optimized using hash table structures such as dictionaries
     - similar to python, swift has a zip function for iterating through more than one list at a time
     - swift defaults to naming parameters in methods, a _ must be used if this behavior is not wanted
     - swift playgrounds on ipad is suitable enough to create algorithms such as this
 */
    var methodCall: Int = 0
    func twoSumBrute(_ nums: [Int], _ target: Int) -> [Int] {
        var currentTotal = 0
        var indices: [Int] = []
        for (index1, num1) in nums.enumerated() {
            // take initial value (outer loop)
            for (index2, num2) in nums.enumerated() {
                // filter out values from array greater than target value
                print(String(index1 != index2) + " : " + String(num1 <= target) + " : " + String(num2 <= target))
                if index1 != index2 {
                    print(String(index1) + " : " + String(index2))
                    // add remaining numbers and see if it matches target
                    currentTotal = num1 + num2
                    print(String(methodCall) + " - num1: " + String(num1) + ", num2: " + String(num2) + ", currentTotal: " + String(currentTotal))
                    print("num1Index: " + String(index1) + ", num2Index: " + String(index2))
                    if currentTotal == target {
                        // store indices and return
                        indices = [index1, index2]
                        self.methodCall += 1
                        return indices
                    }
                }
            }
        }
        return indices
    }
    
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var returnList: [Int] = []
        var searchNum: Int
        let dict = Dictionary(uniqueKeysWithValues: zip(nums.indices, nums))
        
        for (index, num) in nums.enumerated() {
            var dictMinusCurrent = dict
            // create a subset of dict without current index/num included
            dictMinusCurrent.removeValue(forKey: index)
            searchNum = target - num
            if dictMinusCurrent.values.contains(searchNum) {
                // append first index
                returnList.append(index)
                // log the searchNum, then search through array for it to get index
                for (index2, num2) in dictMinusCurrent {
                    if num2 == searchNum {
                        // append second index
                        returnList.append(index2)
                        return returnList
                    }
                }
            }
        } 
        return returnList
    }
}

let s = Solution()
// [2, 7, 11, 15], 18 = [1, 2]
// [1, 2, 3, 4], 5 = [0, 3]
// [3, 3], 6 = [0, 1]
// [0, 4, 3, 0], 0 = [0, 3]
// [-3, 4, 3, 90], 0 = [0, 2]
// [3, 2, 4], 6 = [1, 2]
var testList = [2, 7, 11, 15]
var target = 18
s.twoSum(testList, target)
s.twoSumBrute(testList, target)
