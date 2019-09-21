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
    var UnfinishedTasks: [WorkOrder] // Change this to [WorkOrder]
    var UnassignedWorkers: [Worker] // ... to [Worker]
    var tip: TaskInProgress    // ... to [TaskInProgress]
    let order1 = [WorkOrder(orderNum: "1001",facNum: 1,equipmentType: "Pump",equipmentID: "P032",priority: 5,timeToComplete: 3)]
    let bob = Worker(equipment: ["Sensor", "Security", "Networking"], name: "Bob", shifts: "Morning")
    let workers = [Worker(equipment: ["Sensor", "Security", "Networking"], name: "Bob", shifts: "Morning")]
    let order2 = WorkOrder(orderNum: "1002",facNum: 3,equipmentType: "Conveyer",equipmentID: "Con391",priority: 1,timeToComplete: 9)

    init() {
        self.UnfinishedTasks = order1
        self.UnassignedWorkers = workers
        self.tip = TaskInProgress(task: order2, worker: bob)
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
