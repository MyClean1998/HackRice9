//
//  SendEmailViewController.swift
//  HackRice9
//
//  Created by macpro on 2019/9/22.
//  Copyright © 2019 GoldenDumplings. All rights reserved.
//

import UIKit
import MessageUI

class SendEmailViewController: UIViewController,MFMailComposeViewControllerDelegate, UITextFieldDelegate, UITextViewDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        subject.delegate = self
        body.delegate = self

        // Do any additional setup after loading the view.
    }
    
    @IBOutlet weak var subject: UITextField!
    
    @IBOutlet weak var body: UITextView!
    
    @IBAction func sendEmail(_ sender: Any) {
        let picker = MFMailComposeViewController()
        picker.mailComposeDelegate = self
        if let subjectText = subject.text {
            picker.setSubject(subjectText)
        }
        picker.setMessageBody(body.text, isHTML: true)
        if picker != nil {
        present(picker, animated: true, completion: nil)
    }
    }
    
    // MFMailComposeViewControllerDelegate
    // 1
    func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
        dismiss(animated: true, completion: nil)
    }
    
    // UITextFieldDelegate
    // 2
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
    // UITextViewDelegate
    // 3
    func textView(_ textView: UITextView, shouldChangeTextIn range: NSRange, replacementText text: String) -> Bool {
        body.text = textView.text
        if text == "\n" {
                    textView.resignFirstResponder()
                    return false
                }
                return true
            }


}
