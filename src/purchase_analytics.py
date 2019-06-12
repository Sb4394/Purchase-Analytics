#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python2
import sys
department_id_location=-1
product_id_location=-1
reordered_location=-1

def infer_header(header,separator):
    """
    Takes inputs: header, separator and required
    Captures the required columns' information, i.e., their indexes.
    """
    global department_id_location,product_id_location
    columns = header.split(separator)
    for column in columns:
        if ('DEPARTMENT_ID' in column.upper()):
            department_id_location = columns.index(column)
        if ('PRODUCT_ID' in column.upper()):
            product_id_location = columns.index(column)
        if ('REORDERED' in column.upper()):
            reordered_location = columns.index(column)
            
def custom_split(row,separator):
    """for spliting the rows into different columns with ' " ' in them """
    list_of_columns = []
    column = ''
    dont_split = False
    
    for character in row:
        if (character != separator):
            if (character == '"'):
                if (not dont_split):
                    # reached opening double quotation mark.
                    dont_split = True
                else:
                    # reached closing double quotation mark.
                    dont_split = False
                continue            # to skip the quotation mark in the result.
            column = column + character

        else:
            # reached separator,
            # check if this separator is between double quoatations.
            if (dont_split):
                # separator inside double quotations, don't split.
                column = column + character
            else:
                # regular separator, split.
                list_of_columns.append(column)   # add column data to list.
                column = ''         # reset local variable.
    list_of_columns.append(column)  # append the last column data.
    return list_of_columns


def reader(filename,required_columns):
    """for reading the requried list of data"""
    #name is the name of the class either product or order
    mydict={}
    with open(filename, 'r+') as file:
        infer_header(file.readline(),',')
        for line in file:
            line = line.strip()   #we don't want '\n' to appear, so we use strip()
            if ('"' in line):
                # if data has "", use custom split method.
                columns = custom_split(line, ',')
            else:
                columns = line.split(',')
            value1=columns[required_columns[0]()]
            value2=columns[required_columns[1]()]
            mydict[value1]=value2
    return mydict

def required_data(products,orders): #from the products and orders data, we only need department list and reordered data for the output file
    """for getting the required lists of data for our calculation for the output"""
    department_list=[]
    reorder_list=[]
    prod=[]
    mydict={}
    for product in products:
        mydict[product.product_id]=product.department_id
    #from the products class we find the department id corresponding to the product id of each of the orders
    for order in orders: #for each order get the department id from the products class and also gather the corresponding reordered data
        prod_id=order.product_id
        department_list.append(int(mydict[prod_id]))
        reorder_list.append(order.reordered)
        
    return(department_list,reorder_list)
def writer(department_list,reorder_list,file_name): 
    """writes the output given the required list"""
    output_header=('department_id,''number_of_orders,''number_of_first_orders,''percentage\n')
    l=zip(department_list,reorder_list)
    mydict={}
    for key, val in l:
        mydict.setdefault(key, []).append(val)
    sorted_dept=sorted(department_list)
    with open(file_name, 'w+') as output_file:
        # write header.
        output_file.write(output_header)  #write the header
        i=0
        while i<len(sorted_dept):
            v1=sorted_dept[i]  #department_id
            v2=sorted_dept.count(sorted_dept[i]) #number_of_orders
            v3=mydict[sorted_dept[i]].count(0) #number_of_first_orders
            v4=round(v3*v2**-1,2) #percentage. Rounded to 2nd decimal
            i+=v2
            # prepare line in specified format.
            line = (str(v1) + ',' + str(v2) + ','+ str(v3) + ','+ str(v4) + '\n')
            output_file.write(line)

if __name__ == '__main__':
    # Assign input and output files.
    product_file = sys.argv[1]
    order_file = sys.argv[2]
    report_file= sys.argv[3]
    
    required_columns=[lambda:product_id_location,lambda:department_id_location]  #we only need product_id and department_id from the products file
    filename=product_file
    products=reader(filename,required_columns)

    required_columns=[lambda:product_id_location,lambda:reordered_location]  #we only need product_id and reordere from the products file
    filename=order_file
    orders=reader(filename,required_columns)
    
    
    department_list=products.values()
    department_list = map(int, department_list)
    reorder_list=orders.values()
    reorder_list = map(int, reorder_list)
    
    writer(department_list,reorder_list,report_file)





