import pandas as pd


"""
Class responsible for managing the account details. Portfolio and Holdings.

Active_Backlog - stocks that still havn't been executed. Or closed positions
Active_Holdings - open positions; ShortHoldings and Long Holdings
Initial Capital - 
Net Profit = final profit - capital - expenses. Cumulative daily.
Turn over = Money made in a simple day
Transaction costs - 
Overnight Fee's
Tax - 
Holdings_Value
Active_Backlog - Value

Min position concentration - 
Max position concentration




"""
class Account:
    """This class follows the singleton pattern
    
    In python: You can use the constructor to creat an instance;
    However if you use the constructor multiple times; it will raise an exception
    Therefore once created; which can be done using get_account() or the constructor.
    You'll need the access the instance; which can be done with get_account()
    """
    account = None

    def __init__(self):
        if Account.account is not None:
            raise Exception("Call get account")
        else:
            self.__new_account()
            Account.account = self

    @staticmethod
    def get_account():
        if Account.account is None:
            Account()
        return Account.account

    def __new_account(self):
        """Setup all base parameters"""
        # TODO: How do I make this extensible
        self.UNSET = 0
        self.active_long_backlog = 0
        self.active_short_backlog = 0
        self.holdings = None
        self.INITIAL_CAPITAL = 20000
        self.net_profit = 0
        self.capital = 14000
        self.turnover = 0
        self.overnight_charge = 0
        self.tax = 0
        self.commission_charge = 0
        self.holding_value = 0
        self.min_position_concentration = 0.025
        self.max_position_concentration = 0.05


    def SET_initial_capital(self, i):
        self.INITIAL_CAPITAL = i
        self.capital += self.INITIAL_CAPITAL


    def spend_capital(self, cost):
        """ 
        Do overdraft check, if passing subtracts from capita;
        """
        if self.overdraft_check(cost):
            self.capital -= cost
            return self.capital
        return 0
        # TODO: Add Fee's 
        # TODO


    def overdraft_check(self, cost):
        """True if goes does not go into overdraft.
        If Overdraft check is successful return 
        """
        if self.capital - cost < 0:
            return False
        return True

    def get_position_concentration(self):
        """The monetary amount spendable on a single position
        Risk Min and Max are based off the Initial Capital 
        TODO need to make this on the rebalanced amount; so that risk changes based on the rebalanced amount
        """
        max_portfolio_concentration = self.INITIAL_CAPITAL * self.max_position_concentration
        min_portfolio_concentration = self.INITIAL_CAPITAL * self.min_position_concentration
        return [min_portfolio_concentration, max_portfolio_concentration]

    def add_holding(self, holding):
        """Add new position to existing holdings
        """
        if self.holdings is None:
            self.holdings = holding
        else:
            self.holdings = pd.concat([self.holdings, holding])
    



    



    
            
