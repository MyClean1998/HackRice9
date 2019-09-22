//
//  TaskInProgressViewController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation
import UIKit

class TaskInProgressViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let tabbar = tabBarController as! MainTabController
        scheduler = tabbar.scheduler
//        updateViewFromModel()
    }
    
    private var scheduler: Scheduler!
    
    

}
