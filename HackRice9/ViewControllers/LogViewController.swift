//
//  LogViewController.swift
//  HackRice9
//
//  Created by Zoey Ling on 9/21/19.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit

class LogViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var logText: UITextView!
    func printMsgs(msgs: String) {
        logText.text += msgs
    }
    
    @IBOutlet weak var logging: UILabel!
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
