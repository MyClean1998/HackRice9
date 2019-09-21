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
    init() {
        self.facilityNum = ["fac1", "fac2", "fac3", "fac4", "fac5"]
        self.location = [(29.755537, -95.372003), (29.716361, -95.409329), (29.712818, -95.401964), (29.721943, -95.399359), (29.717913, -95.401923)]
    }
//    static var f1 = Facility()
}
