'''Task:

 - You are the manager of a supermarket.
 - You have a list of N items together with their prices 
   that consumers bought on a particular day.
 - Your task is to print each item_name and net_price in order of its first occurrence.

 - item_name = Name of the item.
 - net_price = Quantity of the item sold multiplied by the price of each item.

Input Format:

  - The first line contains the number of items, N.
 - The next N lines contains the item's name and price, 
   separated by a space.

Constraints:

 - 0 < N <= 100

Output Format:

 - Print the item_name and net_price in order of its first occurrence.

Sample Input:

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output:

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

Explanation:

BANANA FRIES: Quantity bought: 1, Price: 12 
Net Price: 12

POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60

APPLE JUICE: Quantity bought: 2, Price: 10
Net Price: 20

CANDY: Quantity bought: 4, Price: 5
Net Price: 20


'''


def price_counter(items,n):


    if 0 < n <= 100:

        unique_items = []
        for i in range(n):
        
            if items[i] not in unique_items:
                unique_items.append(items[i].copy())

    

        for i in range(len(unique_items)):

            count = items.count(unique_items[i])
            unique_items[i].append(count)
                

        price = []

        for i in range(len(unique_items)):

            price_item = int(unique_items[i][-2]) * unique_items[i][-1]

            unique_items[i][-2] = price_item
            unique_items[i].pop()

        return unique_items



N = int(input())

items = []

for i in range(N):

    itemname_netprice = input().split()
    items.append(itemname_netprice)

result = price_counter(items,N)

for i in range(len(result)):
    item = " ".join(map(str, result[i]))
    print(item)