//
//  ViewController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/20/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        UnfinishedTasks[0].text = "t1"
    }
    
    @IBOutlet var UnfinishedTasks: [UILabel]!
    
    
    private lazy var scheduler = Scheduler()
}

