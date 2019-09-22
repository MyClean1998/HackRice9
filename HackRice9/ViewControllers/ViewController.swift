//
//  ViewController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/20/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

// This view controller shouldn't store any data. It obtains all the data from the model: scheduler
class ViewController: UIViewController {

    var tabbar: MainTabController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        tabbar = tabBarController as! MainTabController
        tabbar.printLogMessage(msg: "loaded")
        updateViewFromModel()
    }
    
    @IBOutlet var taskStack: UIStackView!
    @IBOutlet var workerStack: UIStackView!
    
//    private var scheduler: Scheduler!
    
    func makeTaskWithText(text:String) -> UILabel {
        //Set the attributes of the label
        let myLabel = UILabel()
        myLabel.text = text
        myLabel.textAlignment = .left
        return myLabel
    }
    
        func makeWorkerWithText(text:String) -> UILabel {
            //Set the attributes of the label
            let myLabel = UILabel()
            myLabel.text = text
            myLabel.textAlignment = .left
            return myLabel
        }
    
//    func updateModel(newScheduler: Scheduler) {
//        scheduler = newScheduler
//        updateViewFromModel()
//    }
    
    func updateViewFromModel() {
        taskStack.removeAllArrangedSubviews()
        for task in tabbar.scheduler.unfinishedTasks {
            // TODO: Replace this with a property of task
            taskStack.addArrangedSubview(makeTaskWithText(text: task.orderNum))
        }
        workerStack.removeAllArrangedSubviews()
        // Do the same intialization for workerStack
        for worker in tabbar.scheduler.unassignedWorkers {
            workerStack.addArrangedSubview(makeWorkerWithText(text: worker.name))
        }
    }
    
    // TODO: AddTask and AddWorker buttons
    @IBAction func AddTaskFunc(_ sender: UIButton) {
        tabbar.scheduler.addSampleTask()
        updateViewFromModel()
        let tabbar = tabBarController as! MainTabController
        tabbar.printLogMessage(msg: "Add task")
    }
    
    @IBAction func AddWorkerFunc(_ sender: UIButton) {
        tabbar.scheduler.addSampleWorker()
        updateViewFromModel()
        let tabbar = tabBarController as! MainTabController
        tabbar.printLogMessage(msg: "Add worker")
    }
}

extension UIStackView {
    
    func removeAllArrangedSubviews() {
        
        let removedSubviews = arrangedSubviews.reduce([]) { (allSubviews, subview) -> [UIView] in
            self.removeArrangedSubview(subview)
            return allSubviews + [subview]
        }
        
        // Deactivate all constraints
        NSLayoutConstraint.deactivate(removedSubviews.flatMap({ $0.constraints }))
        
        // Remove the views from self
        removedSubviews.forEach({ $0.removeFromSuperview() })
    }
}
