//
//  WorkOrder.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

// TODO: Do the same thing as the other three classes
class WorkOrder {
    var orderNum: String
    var facilities = Facility()
    var facility: String
//    var equipment: Equipment
    var equipmentType: String
    var equipmentID: String
    var priority: Int
    var timeToComplete: Int
//    var submissionTimeStamp: String
    
    init(orderNum: String, facNum: Int, equipmentType: String, equipmentID: String, priority: Int, timeToComplete: Int) {
        self.orderNum = orderNum
        self.facility = facilities.facilityNum[facNum-1]
        self.equipmentType = equipmentType
        self.equipmentID = equipmentID
        self.priority = priority
        self.timeToComplete = timeToComplete
    }
}
