//
//  MainTabController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation
import UIKit

class MainTabController: UITabBarController {
    override func viewDidLoad() {
        super.viewDidLoad()
        send(apd: "")
//        timer()
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
                    print("data: \(dataString)")
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
        let json: [String: Any] = ["newWorkers": ["name": "ABC", "certificates": []],
                                   ]

        let jsonData = try? JSONSerialization.data(withJSONObject: json)

        // create post request
        let url = URL(string: "http://10.36.32.6:5050" + apd)!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"

        // insert json data to the request
        request.httpBody = jsonData
        
        return request
    }
 
    func handleResponse() {
        
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
