//
//  Equipment.swift
//  HackRice9
//
//  Created by macpro on 2019/9/21.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

class Equipment {
    var equipmentName = Worker.init().equipment
    var probabilityOfFailure: [Double] = [0.00869565217391304, 0.0434782608695652,
                                          0.130434782608695, 0.0869565217391304,
                                          0.147826086956521, 0.165217391304347,
                                          0.017391304347826, 0.243478260869565,
                                          0.113043478260869, 0.0434782608695652]
    
    var hoursToFix: [Array<Int>] = [Array(1...12), Array(2...13), Array(3...5), Array(1...2),
                                    Array(1...2), Array(1...5), Array(1...3), Array(3...8),
                                    Array(4...24), Array(5...10)]
    
    var fac1: [Int] = [4, 5, 1, 13, 2, 21, 11, 4, 0, 0]
    var fac2: [Int] = [7, 4, 2, 21, 0, 38, 8, 5, 3, 2]
    var fac3: [Int] = [4, 5, 3, 4, 1, 1, 4, 3, 6, 2]
    var fac4: [Int] = [6, 5, 2, 0, 1, 7, 5, 0, 6, 1]
    var fac5: [Int] = [7, 9, 3, 2, 1, 22, 8, 6, 4, 3]
}
