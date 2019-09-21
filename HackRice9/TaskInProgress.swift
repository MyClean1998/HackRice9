//
//  TaskInProgress.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

class TaskInProgress {
    var task: WorkOrder
    var worker: Worker
    var timeLeft: Int
    var status: String
    
    init() {
        task = WorkOrder()
        worker = Worker()
        timeLeft = 0
        status = "IP"
    }
}