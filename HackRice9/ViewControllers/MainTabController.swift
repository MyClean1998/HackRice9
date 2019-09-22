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
    }
    
    lazy var scheduler = Scheduler()
    
    // Print log message in the log panel
    func printLogMessage(msg: String) {
//        for v in viewControllers
        
    }
    
    func updateModel(newScheduler: Scheduler) {
        scheduler = newScheduler
        updateAllViewFromModel()
    }
    
    func addWorker(worker: Worker) {
        scheduler.addWorker(withWorkerInfo: worker)
        updateAllViewFromModel()
    }
    
    func addTask(workOrder: WorkOrder) {
        
    }
    
    func updateAllViewFromModel() {
        let vc = viewControllers![2] as! ViewController
        vc.updateViewFromModel()
//        vc.updateModel(newScheduler: scheduler)
    }
}
