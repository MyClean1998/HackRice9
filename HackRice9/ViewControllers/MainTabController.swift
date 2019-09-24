//
//  MainTabController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation
import UIKit
//import SwiftyJSON

class MainTabController: UITabBarController {
    override func viewDidLoad() {
        super.viewDidLoad()
        send(apd: "")
        timer()
    }
    
    lazy var scheduler = Scheduler()

    func send (apd: String) {
        
        let request = generateRequest(apd: apd)
        
        print("sent")
        print (request)
        
        let task = URLSession.shared.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) in
            if let error = error {
                print("error: \(error)")
            } else {
                if let response = response as? HTTPURLResponse {
                    print("statusCode: \(response.statusCode)")
                }
                if let data = data, let dataString = String(data: data, encoding: .utf8) {
//                    print("data: \(dataString)")
                    self.handleResponse(jsonResponse: data)
                }
            }
        })
        task.resume()
    }
    
    func timer() {
        Timer.scheduledTimer(withTimeInterval: 5.0, repeats: true) { (nil) in
            self.send(apd: "/update")
        }
    }
    
    func generateRequest(apd: String) -> URLRequest {
        var workers: [Any] = []
        for worker in scheduler.unassignedWorkers {
            var w: [String: Any] = [:]
            w["name"] = worker.name
            w["certifates"] = worker.equipment
            w["shift"] = worker.shifts
            workers.append(w)
        }
        let json: [String: Any] = ["new_workers":workers]

        let jsonData = try? JSONSerialization.data(withJSONObject: json)

        // create post request
        let url = URL(string: "http://10.127.179.51:5050" + apd)!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"

        // insert json data to the request
        request.httpBody = jsonData
        
        return request
    }
 
    func handleResponse(jsonResponse: Any) {
        let js = JSON(jsonResponse)
        var actions = js["actions"]
        var pending_tasks = js["work_orders"]["pending"]
        var ip_tasks = js["work_orders"]["in_progress"]
        var workers = js["workers"]
        print(actions)
        print(pending_tasks)
        print(ip_tasks)
        print(workers)
        print("================")
        var ws:[Worker] = []

        
        for (key,subJson):(String, JSON) in actions {
            let task = subJson["job_id"]
            let worker = subJson["worker_name"]
            scheduler.assignTask(from: getTask(id: String(task.int!)), to: getWorker(name: worker.string!))
        }
        
        
        var wos:[WorkOrder] = []
        for (key, subJson):(String, JSON) in pending_tasks {
            var p1 = String(subJson["id"].int!)
            var p2 = subJson["equipment"].string!
            var p3 = "testId"
            var p4 = subJson["priority"].int!
            var p5 = subJson["time_rest"].int!
            var wo = WorkOrder(orderNum: p1, facNum: 1, equipmentType: p2, equipmentID: p3, priority: p4, timeToComplete: p5)
            wos.append(wo)
        }
        scheduler.unfinishedTasks = wos
        print(wos)
        
        var wip:[WorkOrder] = []
        for (key, subJson):(String, JSON) in pending_tasks {
            var p1 = String(subJson["id"].int!)
            var p2 = subJson["equipment"].string!
            var p3 = "testId"
            var p4 = subJson["priority"].int!
            var p5 = subJson["time_rest"].int!

            var timeToComplete = subJson["time_rest"]
            var wo = WorkOrder(orderNum: p1, facNum: 1, equipmentType: p2, equipmentID: p3, priority: p4, timeToComplete: p5)
            wip.append(wo)
        }
        scheduler.unfinishedTasks = wip
        print(wip)
        
        for (key, subJson):(String, JSON) in workers {
            ws.append(Worker(equipment: [subJson["certification"].string!], name: subJson["name"].string!, shifts: "morning"))
        }
        scheduler.unassignedWorkers = ws
        print(ws)
    }
    
    func getWorker(name: String) -> Worker {
        for w in scheduler.unassignedWorkers {
            if w.name == name {
                return w
            }
        }
        return scheduler.workers[0]
    }
    
    func getTask(id: String) -> WorkOrder {
        for t in scheduler.unfinishedTasks {
            if t.orderNum == id {
                return t
            }
        }
        return scheduler.order2
    }
        
    // Print log message in the log panel
    func printLogMessage(msg: String) {
        let logging = viewControllers![2] as! LogViewController
        logging.printMsgs(msgs: msg)
        
    }
    
    func updateModel(newScheduler: Scheduler) {
        scheduler = newScheduler
        updateAllViewFromModel()
    }
    
    func addWorker(worker: Worker) {
        scheduler.addSampleWorker()
//        scheduler.addWorker(withWorkerInfo: worker)
//        updateAllViewFromModel()
    }
    
    func addTask(workOrder: WorkOrder) {
        scheduler.addSampleTask()
//        scheduler.addTask(withTaskInfo: workOrder)
//        updateAllViewFromModel()
    }
    
    func updateAllViewFromModel() {
//        let vc = viewControllers![2] as! ViewController
//        vc.updateViewFromModel()
//        vc.updateModel(newScheduler: scheduler)
    }
}
