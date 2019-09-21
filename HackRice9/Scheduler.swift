//
//  Scheduler.swift
//  HackRice9
//
//  Created by uselessfatty on 9/20/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

class Scheduler {
    // TODO: Create classes: WorkOrder, Worker, Equipment, Facility
    // Replace String with the corresponding classes
    private var UnfinishedTasks: [String]
    private var UnassignedWorkers: [String]
    private var TaskInProgress: [String]

    init() {
        UnfinishedTasks = ["t1"]
        UnassignedWorkers = ["w1"]
        TaskInProgress = ["t2:w2"]
    }
}
