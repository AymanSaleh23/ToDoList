# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:50:58 2022

@author: as292
"""

toDoList = list()
doneList = list()

while (True):
    print("|--------------------------------------")
    print("|1.\tPrint List")
    print("|2.\tAdd Item")
    print("|3.\tMark Item As Done")
    print("|4.\tPrint All Done Items")
    print("|x.\tClose")
    print("|--------------------------------------")

    choice = str(input("Choice: "))
    if choice == '1':
        if len(toDoList) == 0:
            print("List is empty")
        else:
            i=1
            for item in toDoList:
                print(str(i)+"."+item)
                i = i+1;
                
                
    elif choice == '2':
        item = str(input("Add Item name: "))
        toDoList.append(item.upper())
        print ("Item "+ item + " is Added.")
        
        
    elif choice == '3':
        item = str(input("Done Item name: ")).upper()
        if toDoList.count(item) == 0:
            print("Item Not Found...")
            continue
        else :
            doneList.append(item)
            toDoList.remove(item)
            print("Well Done, Keep Going.")
            
            
    elif choice == '4':
        print("Your achievements:")
        if len(doneList) == 0:
            print("List is empty")
        else:
            i=1
            for item in doneList:
                print(str(i)+"."+item)
                i = i+1
                
                
    elif choice.upper() == 'X':
        break
print("Good Bye.")