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

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let tabbar = tabBarController as! MainTabController
        scheduler = tabbar.scheduler
        updateViewFromModel()
    }
    
    @IBOutlet weak var taskStack: UIStackView!
    @IBOutlet weak var workerStack: UIStackView!
    
    private var scheduler: Scheduler!
    
    func makeTaskWithText(text:String) -> UILabel {
        //Set the attributes of the label
        let myLabel = UILabel()
//        myLabel.frame = CGRect(x: 30, y: 200, width: 150, height: 36)
//        myLabel.font = UIFont(name: "Chalkduster", size: 18)
        myLabel.text = text
        myLabel.textAlignment = .left
        return myLabel
    }
    
    func updateViewFromModel() {
        for task in scheduler.UnfinishedTasks {
            // TODO: Replace this with a property of task
            taskStack.addArrangedSubview(makeTaskWithText(text: task))
        }
        // Do the same intialization for workerStack
        for worker in scheduler.UnassignedWorkers {
            workerStack.addArrangedSubview(makeTaskWithText(text: worker))
        }
    }
    
    // TODO: AddTask and AddWorker buttons
    @IBOutlet weak var AddTask: UIButton!
    @IBAction func AddTaskFunc(_ sender: UIButton) {
    }
    @IBOutlet weak var AddWorker: UIButton!
    @IBAction func AddWorkerFunc(_ sender: UIButton) {
    }
}

