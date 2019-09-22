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
    
    let availableWorkers = ["Bob", "Lucy","Aaron"]

    var scheduler: Scheduler!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // Unassigned Task Page
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return scheduler.unfinishedTasks.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell{
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell", for: indexPath) as! UnassignedTaskCell
        
        cell.taskNum.text = "Task Number: " +  scheduler.unfinishedTasks[indexPath.row].orderNum
        cell.availableWorkers.text = "Available workers: " +  availableWorkers[indexPath.row]
        cell.Priority.text = "Priority: " +  String(scheduler.unfinishedTasks[indexPath.row].priority)
        return cell
    }


}
