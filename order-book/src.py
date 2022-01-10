# This is a matching engine code created for a coding test 
# There are two types of orders
# 1. Buy order 
#       Priority is given to the order with a higher price. If there are orders of the same price, time sensitivity will kick in 
# 2. Sell order 
#       Priority is given to the order with a lower price. If there are orders of the same price, time sensitive will kick in 
# What does it mean for time sensitivity? -> this meant that the order that came earlier will take priority

# IMPORTS 
import random, string 
from datetime import datetime

## DECLARATION OF VARIABLES
# Creating a string to append results 
result_str = ''
# Creating OB list for Buy and Sell 
B = [] 
S = [] 
# Creating list to contain order object 
B_list = [] 
S_list = [] 
# Creating list to contain all orders 
all_orders = []

# ORDER ATTRIBUTES AND METHODS
class Order: 

    def __init__(self, side, id, quantity, orderType, price=None, disp_size=None): 
        self.side = side 
        # self.id = self.setID() # this has to be a string 
        self.id = id #this has to be a string 
        self.price = price if price is not None else None # this has to be an integer, this needs to be a match to the market price 
        self.quantity = quantity # this has to be an interger 
        self.orderType = orderType # this takes into account of types of order and their behavior
        self.disp_size = disp_size if disp_size is not None else None 
        self.orderid = self.setOrderID() #full id to be placed in OB 
        self.timestamp = datetime.now() #needed for time priority comparison 


    # ID GENERATION 
    # id generation for unique id will not be used since they are manually being inputted 
    # def idGenerate(self): 
    #     id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    #     return id 

    # def setID(self):
    #     id = self.idGenerate()
    #     while True: 
    #         if id in orderID: 
    #             id = self.idGenerate()
    #         else: 
    #             orderID.append(id)
    #             break 
    #     return id 
    
    def setOrderID(self):
        if getattr(self, 'disp_size') == None: 
            oID = f"{self.quantity}@{self.price}#{self.id}"
        else:
            oID = f"{self.disp_size}({self.quantity})@{self.price}#{self.id}"
            
        return oID

# ADDITIONAL FUNCTIONS
def sortpriority(orders, id_list):
    # orders => list containing order objects 
    # id_list => list containing orderID only  
    # Empty existing list 
    id_list.clear() 
    # Sort existing list by price, followed by timestamp?
    # Timestamp priority => earlier takes prio
    orders = sorted(orders, key = lambda x : (x.timestamp)) 
    # Price priority => higher takes prio  
    orders = sorted(orders, key = lambda x : (x.price), reverse=True)
    for order in orders:
        id_list.append(order.orderid)
    return orders, id_list

def sortOrders(orders):
    # Timestamp priority => earlier takes prio
    orders = sorted(orders, key = lambda x : (x.timestamp)) 
    # Price priority => higher takes prio  
    orders = sorted(orders, key = lambda x : (x.price), reverse=True)
    return orders

# ORDER MATCHING FUNCTIONS/LOGIC
def matchLO(new_order): 
    matching = True 
    cost = 0 
    while matching: 
        if new_order.quantity == 0: 
            return cost
        if new_order.side == 'B':
            copy_list = S_list.copy() 
            for order in copy_list: 
                if new_order.price >= order.price:
                    if new_order.quantity >= order.quantity: 
                        new_order.quantity = new_order.quantity - order.quantity
                        S_list.remove(order)
                        all_orders.remove(order)
                        sortpriority(S_list, S)
                        cost += order.quantity * order.price 
                        if new_order.quantity > 0 and order != copy_list[-1]:
                            continue # if quantity is positive and the order in iteration is not the last in the list, continue the for loop 
                        else: 
                            break # break out of the for loop and proceed with the next statement 
                    else: # when new_order.quantity < order.quantity 
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(S_list, S)
                        cost += new_order.quantity * order.price
                        new_order.quantity = 0
                        break # no more new order since it is fulfilled, break out of the for loop 
            if new_order.quantity > 0: 
                new_order.orderid = new_order.setOrderID()
                B_list.append(new_order)
                all_orders.append(new_order)
                sortpriority(B_list, B)
                matching = False
                break   
        elif (new_order.side == 'S'):
            copy_list = B_list.copy() 
            for order in copy_list: 
                if new_order.price <= order.price:
                    if new_order.quantity >= order.quantity: 
                        new_order.quantity = new_order.quantity - order.quantity
                        B_list.remove(order)
                        all_orders.remove(order)
                        sortpriority(B_list, B)
                        cost += order.quantity * order.price 
                        if new_order.quantity > 0 and order != copy_list[-1]:
                            continue # if quantity is positive and the order in iteration is not the last in the list, continue the for loop 
                        else: 
                            break # break out of the for loop and proceed with the next statement 
                    else: # when new_order.quantity < order.quantity 
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(B_list, B)
                        cost += new_order.quantity * order.price
                        new_order.quantity = 0
                        break # no more new order since it is fulfilled, break out of the for loop 
            if new_order.quantity > 0: 
                new_order.orderid = new_order.setOrderID()
                S_list.append(new_order)
                all_orders.append(new_order)
                sortpriority(S_list, S)
                matching = False
                break
    return cost
    
def matchMO(new_order):
    cost = 0 
    matching = True
    if new_order.quantity == 0: 
        return cost
    if new_order.side == 'B':
        if not S_list: 
            return cost
        else: 
            copy_list = S_list.copy()
            while matching: 
                for order in copy_list: 
                    if not S_list: 
                        return cost
                    elif new_order.quantity >= order.quantity:
                        # MO takes whatever quantity of the highest priority in the OB  
                        new_order.quantity = new_order.quantity - order.quantity
                        cost += order.quantity * order.price 
                        S_list.remove(order) #remove first item without printing 
                        all_orders.remove(order)
                        sortpriority(S_list, S)
                        continue
                    else: # when new_order.quantity < order.quantity 
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(S_list, S)
                        cost += new_order.quantity * order.price
                        return cost
    elif (new_order.side == 'S'):
        if not B_list:
            return cost
        else: 
            copy_list = B_list.copy()
            while matching: 
                for order in copy_list: 
                    if not B_list:
                        return cost
                    elif new_order.quantity >= order.quantity:
                        # MO takes whatever quantity of the highest priority in the OB 
                        new_order.quantity = new_order.quantity - order.quantity
                        cost += order.quantity * order.price 
                        B_list.remove(order) #remove first item without printing 
                        all_orders.remove(order)
                        sortpriority(B_list, S)
                        continue
                    else: # when new_order.quantity < order.quantity 
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(B_list, B)
                        cost += new_order.quantity * order.price
                        return cost

def matchIOC(new_order):
    cost = 0 
    if new_order.quantity == 0: 
        return cost
    if new_order.side == 'B':
        copy_list = S_list.copy() 
        for order in copy_list: 
            if new_order.price >= order.price:
                if new_order.quantity >= order.quantity: 
                    new_order.quantity = new_order.quantity - order.quantity
                    S_list.remove(order)
                    all_orders.remove(order)
                    sortpriority(S_list, S)
                    cost += order.quantity * order.price 
                    break # break out of the for loop and proceed with the next statement 
                else: # when new_order.quantity < order.quantity 
                    order.quantity = order.quantity - new_order.quantity
                    order.orderid = order.setOrderID()
                    sortpriority(S_list, S)
                    cost += new_order.quantity * order.price
                    new_order.quantity = 0
                    break # no more new order since it is fulfilled, break out of the for loop 
    elif (new_order.side == 'S'):
        copy_list = B_list.copy() 
        for order in copy_list: 
            if new_order.price <= order.price:
                if new_order.quantity >= order.quantity: 
                    new_order.quantity = new_order.quantity - order.quantity
                    B_list.remove(order)
                    all_orders.remove(order)
                    sortpriority(B_list, B)
                    cost += order.quantity * order.price 
                    break # break out of the for loop and proceed with the next statement 
                else: # when new_order.quantity < order.quantity 
                    order.quantity = order.quantity - new_order.quantity
                    order.orderid = order.setOrderID()
                    sortpriority(B_list, B)
                    cost += new_order.quantity * order.price
                    new_order.quantity = 0
                    break # no more new order since it is fulfilled, break out of the for loop 
    return cost

def matchFOK(new_order):
    cost = 0 
    minQty = new_order.quantity
    availableQty = 0 # This will sum all quantities available for trade to be used for check 
    if new_order.quantity == 0: 
        return cost
    if new_order.side == 'B':
        for order in S_list: 
            if new_order.price >= order.price: 
                availableQty += order.quantity
        if minQty <= availableQty: 
            copy_list = S_list.copy() 
            for order in copy_list: 
                if new_order.price >= order.price:
                    if new_order.quantity >= order.quantity: 
                        new_order.quantity = new_order.quantity - order.quantity
                        S_list.remove(order)
                        all_orders.remove(order)
                        sortpriority(S_list, S)
                        cost += order.quantity * order.price 
                        if new_order.quantity > 0: 
                            continue 
                        else: 
                            break # break out of the for loop and proceed with the next statement   
                    else: # new_order.quantity < order.quantity
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(S_list, S)
                        cost += new_order.quantity * order.price
                        new_order.quantity = 0
                        break # no more new order since it is fulfilled, break out of the for loop 
        else: 
            return cost
    elif (new_order.side == 'S'):
        for order in B_list: 
            if new_order.price <= order.price: 
                availableQty += order.quantity
        if minQty <= availableQty: 
            copy_list = B_list.copy() 
            for order in copy_list: 
                if new_order.price <= order.price:
                    if new_order.quantity >= order.quantity: 
                        new_order.quantity = new_order.quantity - order.quantity
                        B_list.remove(order)
                        all_orders.remove(order)
                        sortpriority(B_list, B)
                        cost += order.quantity * order.price 
                        if new_order.quantity > 0: 
                            continue 
                        else: 
                            break # break out of the for loop and proceed with the next statement   
                    else: # new_order.quantity < order.quantity
                        order.quantity = order.quantity - new_order.quantity
                        order.orderid = order.setOrderID()
                        sortpriority(B_list, B)
                        cost += new_order.quantity * order.price
                        new_order.quantity = 0
                        break # no more new order since it is fulfilled, break out of the for loop 
        else: 
            return cost
    return cost

# ACTIONABLES FUNCTIONS 
def cancel(id):
    id_list = [] 
    for order in all_orders: 
        id_list.append(order.id)
    if id in id_list: 
        id_index = id_list.index(id)
        tbc_order = all_orders[id_index]
        if tbc_order.side == 'B': 
            all_orders.remove(tbc_order)
            B_list.remove(tbc_order)
            sortpriority(B_list, B)
            return True
        elif tbc_order.side == 'S': 
            all_orders.remove(tbc_order)
            S_list.remove(tbc_order)
            sortpriority(S_list, S)
            return True

def cancelAndReplace(id, new_quantity, new_price):
    for order in all_orders: 
        if order.id ==id:
            # store original order somewhere else
            tmp = order
            tmp.quantity = new_quantity
            if new_price != order.price: 
                tmp.timestamp = datetime.now()
            tmp.price = new_price
            tmp.orderid = order.setOrderID()
            if order.side == 'B':
                B_list.remove(order)
                all_orders.remove(order)
                B_list.append(tmp)
                all_orders.append(order)
                sortpriority(B_list, B)
            elif order.side == 'S':
                S_list.remove(order)
                all_orders.remove(order)
                S_list.append(tmp)
                all_orders.append(order)
                sortpriority(S_list, S)


# START TERMINAL APPLICATION LOGIC
while True: 
    # start of application 
    # constantly sort the orders to be in the correct priority 
    sortOrders(B_list)
    sortOrders(S_list)
    
    # print out necessary information 
    print(result_str)
    print(f"B: {' '.join(str(x) for x in B)}")
    print(f"S: {' '.join(str(x) for x in S)}")

    # requesting input from user 
    input_str = input('')
    data = input_str.strip().split(' ')

    # for part 1, these are the possible variations of commands 
    # 1. SUB LO [side] [order id] [quantity] [price]
    # 2. SUB MO [side] [order id] [quantity]
    # 3. CXL [order id]
    # for part 2, these are the possible variations of commands 
    # 1. SUB IOC [side] [order id] [quantity] [price]
    # 2. SUB FOK [side] [order id] [quantity] [price]
    # 3. CRP [order id] [new quantity] [new price]

    if data[0] == 'SUB': 
        dataType = data[1]
        dataSide = data[2]
        dataID = data[3] 
        dataQty = data[4]
        if data[1] == 'LO':
            # order creation
            dataPrice = data[5] # set price field of order 
            new_order = Order(dataSide, dataID, int(dataQty), dataType, int(dataPrice))
            # order matching begins 
            cost = matchLO(new_order)
            # print to result string
            if not result_str:
                result_str += str(cost)
            else: 
                result_str += '\n' + str(cost)
        elif data[1] == 'MO':
            # order creation 
            new_order = Order(dataSide, dataID, int(dataQty), dataType)
            # order matching begins
            cost = matchMO(new_order)
            # print to result string
            if not result_str:
                result_str += str(cost)
            else: 
                result_str += '\n' + str(cost)
        elif data[1] == 'IOC':
            # order creation
            dataPrice = data[5]
            new_order = Order(dataSide, dataID, int(dataQty), dataType, int(dataPrice))
            # order matching begins
            cost = matchIOC(new_order)
            # print to result string
            if not result_str:
                result_str += str(cost)
            else: 
                result_str += '\n' + str(cost)
        elif data[1] == 'FOK':
            # order creation
            dataPrice = data[5]
            new_order = Order(dataSide, dataID, int(dataQty), dataType, int(dataPrice))
            # order matching begins
            cost = matchFOK(new_order)
            # print to result string
            if not result_str:
                result_str += str(cost)
            else: 
                result_str += '\n' + str(cost)
        elif data[1] == 'ICE':
            dataPrice = data[5] # set price field of order 
            dataDispSize = data[6] # set display size 
            new_order = Order(dataSide, dataID, int(dataQty), dataType, int(dataPrice), int(dataDispSize))
            print(new_order.orderid)
            
    elif data[0] == 'CXL':
        id = data[1] 
        cancel(id)    
    elif data[0] == 'CRP':
        id = data[1]
        new_qty = data[2]
        new_price = data[3]
        cancelAndReplace(id, int(new_qty), int(new_price))
    elif data[0] == 'END':
        exit()