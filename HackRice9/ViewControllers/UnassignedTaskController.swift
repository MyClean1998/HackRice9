//
//  UnassignedTaskController.swift
//  HackRice9
//
//  Created by macpro on 2019/9/21.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

//import Foundation
import UIKit

class UnassignedTaskController: UIViewController,UICollectionViewDataSource, UICollectionViewDelegate  {
    
    let taskNum = ["T1", "T2", "T3"]
    
    let availableWorkers = ["Bob", "Lucy","Aaron"]

    override func viewDidLoad() {
        super.viewDidLoad()

    }
    
    // Unassigned Task Page
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return taskNum.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell{
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath) as! UnassignedTaskCell
        
        cell.taskNum.text = taskNum[indexPath.row]
        cell.availableWorkers.text = availableWorkers[indexPath.row]
        
        return cell
    }


}
