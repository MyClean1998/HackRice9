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
    func printLogMessage() {
        
    }
}
