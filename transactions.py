import pandas as pd 
import random
from forge.account import Account

class Transactions:
    def __init__(self):
        pass

    def open_long(self, security,current_date):
        """1) Price the asset:
        Get the row of security at given date then randomly generate a buy price; and edit the account accordingly.

        2) Determines how much quantity to buy / Determines if can buy based on overdraft parameters

        3) Makes the transaction; removing capital

        4) Appropriate Logging 
        """
        # Transaction 

        # Randomly generate price between low and high
        ask_price = self.__generate_price(security, current_date)

        # Log the Transaction TODO
        s = {}
        s['date'] = current_date
        s['security'] = security.index[0][1]
        s['ask_price'] = ask_price


        # Get risk allowance thresholds; minimum and maxiumum positions cocnentrations
        mi, ma = Account.get_account().get_position_concentration()

        # Given risk allowance, what are the quantity and quantitiy costs
        quantity = self.__quantity_calc(ask_price, mi, ma)
        min_quantity = quantity[0]
        max_quantity = quantity[1]

        # Make transaction call
        # TODO add stock transactio  failure and exit the script
        if self.quantity_check(min_quantity, max_quantity) is False:
            return
        
        # Generate costs for max quantitiy and min quantity
        max_cost = max_quantity * ask_price
        min_cost = min_quantity * ask_price

        # Determine whether to purchase Min or Max
        invoice = 0
        if max_quantity > 0: 
            # Purchase Max if can afford
            invoice = Account.get_account().spend_capital(max_cost)
            s['quantity'] = max_quantity
            s['total_cost'] = max_cost
        else:
            # Purchase Min if can afford
            invoice = Account.get_account().spend_capital(min_cost)
            s['quantity'] = min_quantity
            s['total_cost'] = min_cost

        if invoice == 0:
            print("Can't afford")
            return
        

        print("REMAINING CAPITAL: " ,Account.get_account().capital)

        
        # needs to return a series: ORDER: date, security, ask price, quantity bought, cost,
        keys = list(s.keys())
        # print(s)


        # Add to Holdings
        holding = pd.DataFrame(data=s , index=[0], columns=s.keys())
        holding['transaction_type'] = 'long'
        # holding.set_index(keys='security', inplace=True, drop=True)
        Account.get_account().add_holding(holding)

        # Remove from Portfolio
        # TODO

        # 

        # print(holding)
        # return df

         # Subtracts the cost from standing capital
        # needs to return a series: ORDER: date, security, ask price, quantity bought, cost,
        # Add to Holdings
        

        # + fee's etc

      

    
    

        # TODO WEEKEND or non trading day
        # TODO Pence to Pounds issue 
        # TODO Issue with concentration; each successive trade will have a smaller position concentration because less capital in the pot; Need to base it on initial capital; which is rebalanced
        # TODO negative capital balance √
        # TODO purchase appropriate quantity √
        # TODO What happens if more expensive than min and max allowance √
        # TODO Refactor; putting quantity √






    def close_long(self):
        pass

    def open_short(self):
        pass

    def close_short(self):
        pass


    def __generate_price(self, security, current_date):
        """Randomly Generates a price"""
        ohlc = security.loc[(current_date, security.index[0][1])]
        low = ohlc['low']
        high = ohlc['high']
        return round(random.uniform(low, high), 2)

    def __quantity_calc(self, cost, min_portfolio_concentration, max_portfolio_concentration):
        """Calculates purchase quantities and price.
        """
        # TEST
        print("ASKING PRICE: ", cost)
        # TEST
        print("Maximum spendable amount" , max_portfolio_concentration)
        print("Min spendable amount" , min_portfolio_concentration)

        # How much I can buy based on the current cost and my capital allowance
        max_quantity = max_portfolio_concentration / cost
        min_quantity = min_portfolio_concentration / cost

        print("TEST MAX/MIN QUANTS", max_quantity, min_quantity)

        max_quantity = int(max_quantity)
        min_quantity = int(min_quantity)

        # TEST
        print("QUANTITIES: ")
        print(max_quantity, min_quantity)
        return [min_quantity , max_quantity]
        

# TODO fix multi format multi index bug: Datetime first vs symbol first; THERE SHOULD BE ONE STANDARDIZED FORMAT
    
    
    def quantity_check(self, min_quantity, max_quantity):
        """ 
        1) Determine whether Quantity is high enough to buy
        If they don't meet the capital allocation threshold return 0. 
        """
        if min_quantity <= 0 and max_quantity <= 0:
            print("Can't buy; too expensive for our risk")
            return False
        return True
