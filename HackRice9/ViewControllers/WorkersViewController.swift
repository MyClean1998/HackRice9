//
//  WorkersViewController.swift
//  HackRice9
//
//  Created by Zoey Ling on 9/22/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class WorkersViewController: UIViewController
    ,UICollectionViewDataSource, UICollectionViewDelegate{

    let workerLabel = ["Bob", "Sally", "Marcus", "Jackie", "Jacob", "Lilly", "Mohammed", "Celeste", "Andrew", "Anh"]
    
    let equipmentCert = ["Equipment Certificates: Sensor, Security, Networking", "Equipment Certificates: Pump, HVAC", "Equipment Certificates: vehicle", "Equipment Certificates: Conveyor, Seperator", "Equipment Certificates: Compressor, Electricity", "Equipment Certificates: Sensor, Security, Networking", "Equipment Certificates: Pump, HVAC", "Equipment Certificates: Vehicle", "Equipment Certificates: Conveyor, Seperator", "Equipment Certificates: Compressor, Electricity"]
    
    let shifts = ["Morning", "Morning", "Morning", "Morning", "Morning", "Evening", "Evening", "Evening", "Evening", "Evening"]
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return workerLabel.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell{
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath) as! WorkersViewCell
        
        cell.workerLabel.text = workerLabel[indexPath.row]
        cell.equipmentCert.text = equipmentCert[indexPath.row]
        cell.shifts.text = shifts[indexPath.row]
        return cell
    }

}
