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
    
    let taskNum = ["T1", "T2", "T3"]
    
    let availableWorkers = ["Bob", "Lucy","Aaron"]

    var tabbar: MainTabController!
    
    override func viewDidLoad() {
        super.viewDidLoad()
//        tabbar = tabBarController as! MainTabController
    }
    
    // Unassigned Task Page
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
//        return tabbar.scheduler.tip.count
        return 3
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell{
        
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "cell2", for: indexPath) as! InProgressTaskCell
        
//        cell.taskNum.text = tabbar.scheduler.tip[indexPath.row].task.orderNum
        cell.taskNum.text = taskNum[indexPath.row]

        cell.availableWorkers.text = availableWorkers[indexPath.row]
        
        return cell
    }


}
