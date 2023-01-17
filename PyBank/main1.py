#get the systems talking to each other so we can define a path
import os
import csv

#define file path
file = os.path.join('Resources','budget_data.csv')

with open(file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    pybank = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(pybank)

    # List to store data:
    months =[]
    pandls= []

    #Starting variable conditions
    total =0
    month_count=0
    m_count=0
    loop1=0
    loop2=0
    month_average=0
    num1=0
    num1line=0
    num2=0
    num2line=0

    #read the file and start to fill in to 'assigned' locations.
    for row in pybank:
        month=row[0] #column 0 assigned 'month'
        months.append(month) # add next line to months list/column
        
        profitandloss=row[1] #Column 1 assigned 'Profits and Losses
        pandls.append(profitandloss) # add next line to profit and losses list/column
    
    #Count and print total number of months included in the dataset
    month_count =len(months)
    #print(month_count)

    #Loop through and find the net total amount of "Profit/Losses" over the entire period (variable loop1 is my loop counter)
    for loop1 in range (month_count):
        total=total+int(pandls[loop1]) #Calculate total amount of Profit/Losses from over the months
    #print(total)

    #Second loop to average of the changes in "Profit/Losses" over the entire period. (variable loop2 is my loop counter)
    for loop2 in range(month_count-1):
        month_average= month_average +(float(pandls[loop2+1])-float(pandls[loop2]))
    #print(month_average/(month_count-1))

        monthly_change=(float(pandls[loop2+1])-float(pandls[loop2]))
        #Determine the greatest increase over the entire period
        if monthly_change > num1:
            num1=monthly_change
            num1line=loop2
            
        else:
            num1=num1
    #print(num1)
    #print(months[num1line+1])
        
        #Determine the greatest decrease over the entire period
        if monthly_change < num2:
            num2=monthly_change
            num2line=loop2
            
        else:
            num2=num2
    #print(num2)
    #print(months[num2line+1])
        
#print the summary analysis report

analysis=f'\
Financial Analysis\n\
------\n\
Total Months: {month_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(month_average)}\n\
Greatest Increase: {months[num1line+1]} (${int(num1)})\n\
Greastest Decrease: {months[num2line+1]} (${int(num2)})\n'

print(analysis)#confirm that all data results make sense and match functions

#put summary into text file.
Summary=open("pybank.txt","w") #create and open textfile
Summary.writelines(analysis) #write summary into text file
Summary.close#close file