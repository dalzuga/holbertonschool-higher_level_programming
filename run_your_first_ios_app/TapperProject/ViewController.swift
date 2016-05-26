//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var tapsRequested: Int? = nil
    var tapsDone: Int = 0
    
    @IBOutlet weak var imgBkg: UIImageView!
    
    // elemnts for first view
    @IBOutlet weak var imgTapper: UIImageView!
    @IBOutlet weak var btnPlay: UIButton!
    @IBOutlet weak var tfHowMany: UILabel!
    
    // elements for second view
    @IBOutlet weak var lblTaps: UITextField!
    @IBOutlet weak var btnCoin: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.lblTaps.hidden = true
        self.lblTaps.text = tapsDone + " Taps!"
        
        showPlayScreen()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func showPlayScreen() {
        
    }
}

