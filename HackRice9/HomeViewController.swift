//
//  HomeViewController.swift
//  HackRice9
//
//  Created by uselessfatty on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class HomeViewController: UIViewController {

    var tabbar: MainTabController!
    @IBOutlet weak var equipmentBox: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tabbar = tabBarController as! MainTabController
    }
    
//    private var scheduler: Scheduler!
    
    @IBOutlet weak var taskEquipment: UITextField!
    @IBOutlet weak var workerNameField: UITextField!
    
    @IBOutlet weak var workerShift: UITextField!
    @IBOutlet weak var workerLabel: UILabel!
    
    @IBOutlet weak var taskFacility: UITextField!
    
    //equipment selection
//
//    func numberOfComponents(in pickerView: UIPickerView) -> Int{
//        return 1
//    }
//
//    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int{
//
//        return list.count
//    }
//
//    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
//
//        self.view.endEditing(true)
//        return list[row]
//    }
//
//    func pickerView(_ pickerView: UIPickerView, didSelectRow row: Int, inComponent component: Int) {
//
//        self.equipmentBox.text = self.list[row]
//        self.dropBox.isHidden = true
//    }
//
//    func textFieldDidBeginEditing(_ textField: UITextField) {
//
//        if textField == self.equipmentBox {
//            self.dropBox.isHidden = false
//            //if you don't want the users to se the keyboard type:
//
//            textField.endEditing(true)
//        }
//    }
    

    
    @IBOutlet weak var timeToComplete: UITextField!
    @IBAction func AddWorker() {
        tabbar.addWorker(worker: Worker(equipment: [], name: workerNameField.text!, shifts: "morning"))
    }
    
    @IBAction func addWorkOrder() {
        let time = Int(timeToComplete.text!)!
        let newTask: WorkOrder = WorkOrder(orderNum: "testOrder", facNum: Int(taskFacility.text!)!, equipmentType: "testEquip", equipmentID: "testID", priority: 1, timeToComplete: time)
        

    }
    
    
}
