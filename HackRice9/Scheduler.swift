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
    var unfinishedTasks: [WorkOrder] // Change this to [WorkOrder]
    var unassignedWorkers: [Worker] // ... to [Worker]
    var tip: [TaskInProgress]    // ... to [TaskInProgress]
    let order1 = [WorkOrder(orderNum: "1001",facNum: 1,equipmentType: "Pump",equipmentID: "P032",priority: 5,timeToComplete: 3)]
    let bob = Worker(equipment: ["Sensor", "Security", "Networking"], name: "Bob", shifts: "Morning")
    var workers = [Worker(equipment: ["Sensor", "Security", "Networking"], name: "Bob", shifts: "Morning"), Worker(equipment: ["Sensor", "Security", "Networking"], name: "Bob", shifts: "Morning")]
    let order2 = WorkOrder(orderNum: "1002",facNum: 3,equipmentType: "Conveyer",equipmentID: "Con391",priority: 1,timeToComplete: 9)

    init() {
        self.unfinishedTasks = order1
        self.unassignedWorkers = workers
        self.tip = [TaskInProgress(task: order2, worker: bob), TaskInProgress(task: order2, worker: bob)]
    }
    
    
    // Replace all the "String" with the corresponding class name
    func addTask(withTaskInfo task: WorkOrder) {
        unfinishedTasks.append(task)
    }
    
    func addSampleTask() {
        unfinishedTasks.append(order2)
    }
 
    func removeTask(withTaskInfo task: WorkOrder) {
//        let index: Int = unfinishedTasks.index(of: task)
//        unfinishedTasks.remove(at: index)
        for i in unfinishedTasks.indices {
            if unfinishedTasks[i] === task {
                unfinishedTasks.remove(at: i)
                return;
            }
        }
    }
    
    func addWorker(withWorkerInfo worker: Worker) {
        unassignedWorkers.append(worker)
    }
    
    func addSampleWorker() {
        unassignedWorkers.append(workers[0])
    }
    
    func removeWorker(withWorkerInfo worker: Worker) {
        for i in unassignedWorkers.indices {
            if unassignedWorkers[i] === worker {
                unassignedWorkers.remove(at: i)
                return;
            }
        }
    }
    
    // Assign a task to a worker,
    func assignTask(from task: WorkOrder, to worker: Worker) {
        tip.append(TaskInProgress(task: task, worker: worker))
        removeTask(withTaskInfo: task)
        removeWorker(withWorkerInfo: worker)
    }
}
