//
//  InProgressTaskCell.swift
//  HackRice9
//
//  Created by macpro on 2019/9/22.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class InProgressTaskCell: UICollectionViewCell {
    
    @IBOutlet weak var taskNum: UILabel!
    @IBOutlet weak var availableWorkers: UILabel!
    @IBOutlet weak var priority: UILabel!
    
    @IBOutlet weak var timeLeft: UILabel!
}
