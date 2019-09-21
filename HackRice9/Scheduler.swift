//
//  Scheduler.swift
//  HackRice9
//
//  Created by uselessfatty on 9/20/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

// The model that stores all the data
class Scheduler {
    // TODO: Create classes: WorkOrder, Worker, Equipment, Facility
    // Replace String with the corresponding classes
    var UnfinishedTasks: [String] // Change this to [WorkOrder]
    var UnassignedWorkers: [String] // ... to [Worker]
    var TaskInProgress: [String]    // ... to [TaskInProgress]

    init() {
        UnfinishedTasks = ["t1", "t3", "t4"]
        UnassignedWorkers = ["w1"]
        TaskInProgress = ["t2:w2"]
    }
    
    
    // Replace all the "String" with the corresponding class name
    func addTask(withTaskInfo task: String) {
        //TODO
    }
    
    func removeTask(withTaskInfo task: String) {
        //TODO
    }
    
    func addWorker(withWorkerInfo worker: String) {
        //TODO
    }
    
    func removeWorker(withWorkerInfo worker: String) {
        //TODO
    }
    
    // Assign a task to a worker,
    func assignTask(from task: String, to worker: String) {
        //TODO
    }
}
