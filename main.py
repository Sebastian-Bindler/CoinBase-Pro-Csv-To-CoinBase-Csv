# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 08:51:12 2022

@author: cj8q21
"""
import csv

filenameInput = "fills.csv"
filenameOutput = "CoinBase.csv"

CoinbaseText = '"You can use this transaction report to inform your likely tax obligations. For US customers, Sells, Converts, Rewards Income, Coinbase Earn transactions, and Donations are taxable events. For final tax obligations, please consult your tax advisor."'
CoibaseHeader = ['Timestamp','Transaction Type','Asset','Quantity Transacted','Spot Price Currency','Spot Price at Transaction','Subtotal','Total (inclusive of fees)','Fees','Notes']


if __name__ == "__main__":
    
    list = [ ]
    row_number = 0
    
    with open(filenameInput) as csvdatei:
        csv_reader_object = csv.reader(csvdatei)
        for row in csv_reader_object:
            temp = [ ]
            if row_number != 0:
                temp.append(row[4]) # Timestamp
                temp.append(row[3].title()) # Transaction Type
                temp.append(row[6]) # Asset
                temp.append(row[5]) # Quantity Transacted
                
                temp.append(row[10]) # Spot Price Currency
                temp.append(row[7]) # Spot Price at Transaction
                temp.append(float(row[9])* -1 - float(row[8]))# Subtotal
                temp.append(float(row[9]) * -1) # Total (inclusive of fees)
                temp.append(row[8]) # Fees
                temp.append('"{} {} {} for {} {}"'.format(row[3].title(), row[5], row[6], float(row[9]) * -1, row[10]))
                
                
                list.append(temp)
            row_number = row_number+ 1
        
    
        print(list)
        
        
        with open(filenameOutput, 'w+', newline = '', encoding='UTF8') as f: 
            f.write(CoinbaseText)
            f.write('\n')
            f.write('\n')
            f.write('\n')
            f.write('\n')
            f.write('Transactions')
            f.write('\n')
            f.write('User,mail@gmail.com,123')
            f.write('\n')
            f.write('\n')
            
            writer = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_NONE, quotechar=None)
            
            writer.writerow(CoibaseHeader)
            writer.writerows(list)
            
            f.close()