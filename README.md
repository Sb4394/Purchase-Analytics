# Purchase-Analytics

# Table of Contents
1. [Problem](README.md#Problem)
2. [Input](README.md#Input)
3. [Output](README.md#Output)
4. [Approach](README.md#Approach)
5. [Run Instructions](README.md#Run-Instructions)
6. [Tests](README.md#Tests)
7. [Contact](README.md#Contact)

# Problem
Instacart has published a dataset containing 3 million Instacart orders.

We want to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers.

# Input
We have two separate input data sources, `order_products.csv` and `products.csv`. They are located in the `input` folder

The `order_products.csv` file contains data of the form
```
order_id,product_id,add_to_cart_order,reordered
2,33120,1,1
2,28985,2,1
2,9327,3,0
2,45918,4,1
3,17668,1,1
3,46667,2,1
3,17461,4,1
3,32665,3,1
4,46842,1,0
```
where

order_id: unique identifier of order
product_id: unique identifier of product
add_to_cart_order: sequence order in which each product was added to shopping cart
reordered: flag indicating if the product has been ordered by this user at some point in the past. The field is 1 if the user has ordered it in the past and 0 if the user has not. While data engineers should validate their data, for the purposes of this challenge, you can take the reordered flag at face value and assume it accurately reflects whether the product has been ordered by the user before.
The file `products.csv` holds data on every product, and looks something like this:
```
product_id,product_name,aisle_id,department_id
9327,Garlic Powder,104,13
17461,Air Chilled Organic Boneless Skinless Chicken Breasts,35,12
17668,Unsweetened Chocolate Almond Breeze Almond Milk,91,16
28985,Michigan Organic Kale,83,4
32665,Organic Ezekiel 49 Bread Cinnamon Raisin,112,3
33120,Organic Egg Whites,86,16
45918,Coconut Butter,19,13
46667,Organic Ginger Root,83,4
46842,Plain Pre-Sliced Bagels,93,3
```
where

product_id: unique identifier of the product
product_name: name of the product
aisle_id: identifier of aisle in which product is located
department_id: identifier of departmen
  
# Output
Given the two input files, the program creates 1 output file:
* `report.csv`
It will be located in the `output` folder

Each line has the following data, corresponding to `department_id`
`number_of_orders`. How many times was a product requested from this department? (If the same product was ordered multiple times, we count it as multiple requests)

`number_of_first_orders`. How many of those requests contain products ordered for the first time?

`percentage`. What is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department? (e.g., `number_of_first_orders` divided by `number_of_orders`)

For example, with the input files given above, the correct output file is

```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```

*The output file adheres to the following rules*

- It is listed in ascending order by `department_id`
- A `department_id` listed only if `number_of_orders` is greater than `0`
- `percentage` rounded to the second decimal


# Approach
Steps to solve this problem were,
  read file contents line by line
  understand schema from header
  split each line into columns of data
  insert required data into dictionary
  write data to output file
  
We only need `department_id` and `reordered` data to compute the results for the output
The `order_products.csv` file has the `reordered` data, but it doesn't have the `department_id` in it.
So, we use the `products.csv` file to get the `department_id` corresponding to the `product_id` of each of the orders
We associate(using dictionary) `product_id`(key) to the `department_id`(values), since `product_id` is unique in the `products.csv` file. It makes the searching for the `department_id` easier and faster

# Run Instructions
The program uses python2 (not python3) for solving this challenge and uses only the **`sys`** standard library
Running the **`run.sh`** file in the project root directory will run the script and produce the results in the specified format in specified folder.
Use `sudo bash` to run **`run.sh`** file, if needed

# Tests
Please run the **`run_tests.sh`** script to run all the tests. The results are stored in **`results.txt`** in the same directory.
Use `sudo bash` to run **`run_tests.sh`** file, if needed

Test1:
9 orders

Test2:
~1.3 million orders

Test3:
32 million orders

Note:
Test3 which contains 32 million orders took about a minute on my system to complete
The code also accomodates for the change in the order of the data columns

# Contact
 Email: sbm4@illinois.edu
