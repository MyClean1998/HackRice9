//
//  Facility.swift
//  HackRice9
//
//  Created by macpro on 2019/9/21.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import Foundation

class Facility{
    
    var facilityNum: [String]
    var location: [(latitude: Double, longitude: Double)]
    
    // TODO: add input params to the initializer
    init(facilityNum: [String], location: [(latitude: Double, longitude: Double)]) {
        self.facilityNum = facilityNum
        self.location = location
    }
}
