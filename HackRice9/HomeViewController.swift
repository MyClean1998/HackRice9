//
//  HomeViewController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {

    var tabbar: MainTabController!
    @IBOutlet weak var equipmentBox: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tabbar = tabBarController as! MainTabController
    }
        
    @IBOutlet weak var taskEquipment: UITextField!
    @IBOutlet weak var workerNameField: UITextField!
    @IBOutlet weak var workerShift: UITextField!
    @IBOutlet weak var taskFacility: UITextField!
    @IBOutlet weak var timeToComplete: UITextField!
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let identifier = segue.identifier {
            switch identifier {
                case "inProgress":
                    if let vc = segue.destination as? InProgressTaskController {
                        vc.scheduler = tabbar.scheduler
                    }
                case "unassigned":
                    if let vc = segue.destination as? UnassignedTaskController {
                        vc.scheduler = tabbar.scheduler
                    }
                default:
                    print(identifier)
            }
        }
    }
    
    @IBAction func AddWorker() {
        tabbar.scheduler.addSampleWorker()
        tabbar.printLogMessage(msg: "Added a new worker\n")
//        tabbar.addWorker(worker: Worker(equipment: [], name: workerNameField.text!, shifts: "morning"))
    }
    
    @IBAction func addWorkOrder() {
        tabbar.scheduler.addSampleTask()
        tabbar.printLogMessage(msg: "Added a new work order\n")

//        var time: Int
//        if timeToComplete.text == nil {
//            time = 0
//        }
//        time = Int(timeToComplete.text!)!
//        let newTask: WorkOrder = WorkOrder(orderNum: "testOrder", facNum: Int(taskFacility.text!)!, equipmentType: "testEquip", equipmentID: "testID", priority: 1, timeToComplete: time)
    }
    
    
}
