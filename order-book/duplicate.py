def orderMatch(orders, id_list, oppOrders, oppIDList, newOrder): 
    # Key criteria: A match occurs when a buy order price is greater than, or equal to, the Price of the Sell order. 
    # Quantity will be based on the lower between the sell and the buy 
    # Price will be the price of the order matched in the OB, not the submitted order 
    matching = True
    cost = 0 
    while matching:
        if newOrder.orderType == 'LO':
            if len(orders) == 0:
                print(f"Cost: {cost}")
                oppOrders.append(newOrder)
                sortpriority(oppOrders, oppIDList)
                return cost
            else: 
                orders = sortOrders(orders)
                # for order in orders: 
                #     print(f"yosh {order.price}")
                for order in orders: 
                    if newOrder.side == 'B':
                        # print(f"Matched S = {order.orderid}")
                        if newOrder.price >= order.price: # If there exists orders that have a lower price, check for quantity 
                            if newOrder.quantity >= order.quantity: # If quantity is larger, remove existing order and restart the while loop 
                                newOrder.quantity = newOrder.quantity - order.quantity
                                orders.remove(order)
                                sortpriority(orders, id_list)
                                cost += order.price * order.quantity
                                # print(f'{order.orderid} removed')
                                # print(f'B: step 1 cost {cost}')
                                continue
                            elif newOrder.quantity < order.quantity: # If quantity is smaller, complete submitted order and break out of while loop 
                                order.quantity = order.quantity - newOrder.quantity
                                order.orderid = order.setOrderID()
                                #new order should be removed and no appending is needed 
                                sortpriority(orders, id_list)
                                cost += newOrder.quantity * order.price 
                                matching = False 
                                # print(f'B: step 2 cost {cost}')
                                return cost
                        elif (order == orders[-1]): # If there are no orders available to fill, append new order to OB and break out of while loop 
                            if newOrder.quantity == 0: 
                                return cost 
                            elif newOrder.quantity > 0:    
                                print("EXCESS")
                                newOrder.orderid = newOrder.setOrderID()
                                oppOrders.append(newOrder)
                                sortpriority(oppOrders, oppIDList) 
                                matching = False
                                # print(f'B: step 3 cost {cost}')
                                return cost
                        else: 
                            continue 
                    if newOrder.side == 'S':
                        # print(f"s = {order.orderid}")
                        # print(len(orders))
                        if newOrder.price <= order.price: # If there exists orders that have a lower price, check for quantity 
                            if newOrder.quantity >= order.quantity: # If quantity is smaller, remove existing order and restart the while loop 
                                newOrder.quantity = newOrder.quantity - order.quantity
                                orders.remove(order) 
                                sortpriority(orders, id_list)
                                cost += order.price * order.quantity
                                # print(f'S: step 1 cost {cost}')
                                continue
                            elif newOrder.quantity < order.quantity: # If quantity is smaller, complete submitted order and break out of while loop 
                                order.quantity = order.quantity - newOrder.quantity
                                order.orderid = order.setOrderID()
                                #new order should be removed and no appending is needed 
                                sortpriority(orders, id_list)
                                cost += newOrder.quantity * order.price 
                                matching = False 
                                # print(f'S: step 2 cost {cost}')
                                return cost
                        elif(order == orders[-1]): # If there are no orders available to fill, append new order to OB and break out of while loop 
                            if newOrder.quantity == 0: 
                                return cost
                            elif newOrder.quantity > 0: 
                                print("EXCESS")
                                newOrder.orderid = newOrder.setOrderID()
                                oppOrders.append(newOrder)
                                print(oppOrders)
                                sortpriority(oppOrders, oppIDList) 
                                matching = False
                                # print(f'Matched B: step 3 cost {cost}')
                                return cost
                        else: 
                            continue