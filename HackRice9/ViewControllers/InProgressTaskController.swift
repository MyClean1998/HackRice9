//
//  InProgressTaskController.swift
//  HackRice9
//
//  Created by macpro on 2019/9/22.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

//import Foundation
import UIKit

class InProgressTaskController: UIViewController,UICollectionViewDataSource, UICollectionViewDelegate  {
        
    let availableWorkers = ["Bob", "Lucy","Aaron"]

    var tabbar: MainTabController!
        
    var scheduler: Scheduler!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    // Unassigned Task Page
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return scheduler.tip.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell{
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell2", for: indexPath) as! InProgressTaskCell
        
        cell.taskNum.text = "task Number: " +  scheduler.tip[indexPath.row].task.orderNum
//        cell.taskNum.text = taskNum[indexPath.row]

        cell.availableWorkers.text = "current worker:" +  scheduler.tip[indexPath.row].worker.name
        cell.priority.text = "Priority: " + String( scheduler.tip[indexPath.row].task.priority)
        cell.timeLeft.text = "Time to Complete: " + String( scheduler.tip[indexPath.row].timeLeft)
        return cell
    }


}
