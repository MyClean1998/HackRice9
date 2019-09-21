//
//  Worker.swift
//  HackRice9
//
//  Created by macpro on 2019/9/21.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

class Worker {
    var equipment: [String]
    var name: String
    var shifts: String
    
    init(equipment: [String], name: String, shifts: String) {
//        self.equipment = ["Pump", "Compressor", "Seperator", "Sensor", "Security", "Electricity", "Networking", "Vehicle", "HVAC", "Conveyer"]
//        self.name = ["Bob", "Sally", "Marcus", "Jackie", "Jacob", "Lilly", "Mohammed", "Celeste", "Andrew", "Anh"]
//        self.shifts = ["Morning", "Evening"]
        self.equipment = equipment
        self.name = name
        self.shifts = shifts
    }
}
