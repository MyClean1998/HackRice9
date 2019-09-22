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
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tabbar = tabBarController as! MainTabController
    }
    
//    private var scheduler: Scheduler!
    
    @IBOutlet weak var workerNameField: UITextField!
    
    @IBOutlet weak var workerLabel: UILabel!
    
    @IBAction func AddWorker() {
        tabbar.addWorker(worker: Worker(equipment: [], name: workerNameField.text!, shifts: "morning"))
    }
    
    
    
}
