# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
   
    Billing = '(//*[@class="fa fa-cc text-orange"])[2]'
    
    Bill  = '(//*[@class="fa fa-circle-o"])[103]'
    
    Branch = '(//*[@role="presentation"])[2]'
    
    text_box = '(//*[@role="textbox"])'
    
    Date_range = 'dt_range'
    
    Start_date = 'daterangepicker_start'
    
    End_date = 'daterangepicker_end'
    
    apply_date = '(//*[@class="applyBtn btn btn-small btn-sm btn-success"])'
    
    Search_bill ='bill_search'
    
    Show_entries = '(//*[@class="form-control input-sm"])[1]'
    
    Search_option  = '(//*[@class="form-control input-sm"])[2]'
    
    edit_option = '(//*[@class="btn btn-primary btn-edit"])'
    
    cash = 'make_pay_cash'
    
    card_payment_option = 'card_detail_modal'
    
    card_name = 'card_details[card_name][]'
    
    card_type = 'card_details[card_type][]'
    
    Device_name = 'card_details[id_device][]'
    
    card_No = 'card_details[card_no][]'
    
    card_amount = 'card_details[card_amt][]'
    
    approval = 'card_details[ref_no][]'
    
    credit_pagr_save = 'add_newcc'
    
    cheque = 'cheque_modal'

    cheque_Date = 'cheque_details[cheque_date][]'
    
    bank = 'cheque_details[id_bank][]'
    
    cheque_no = 'cheque_details[cheque_no][]'
    
    cheque_amount = 'cheque_details[payment_amount][]'
    
    cheque_page_save = 'add_newchq'
    
    net_banking = 'net_bank_modal'
    
    net_banking_type = 'nb_details[nb_type][]'
    
    net_bank = 'nb_details[id_bank][]'
    
    payment_date = 'nb_details[nb_date][]'
    
    Referral_no = 'nb_details[ref_no][]'
    
    net_banking_amount = 'nb_details[amount][]'
    
    net_bank_page_save = 'add_newnb'
    
    save_bill_edit = 'save_bill_edit'
    