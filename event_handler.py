import pandas as pd
import datetime
from forge.account import Account
from forge.transactions import Transactions

class EventHandler:

    def __init__(self, _from, _to, portfolio_model, **kwargs):
        """Setup and Teardown"""
        
        # Set dates to datetime first; for input validation
        self.start_date = pd.to_datetime(_from)
        self.end_date = pd.to_datetime(_to)

        # Input Validation
        if self.end_date < self.start_date:
            raise Exception("Error: End date is smaller than smart date")


        # Constants
        self.UNSET = 0
        
        # Rebalance Parameters
        self.DEFAULT_REBALANCE = 7
        self.rebalance_on = self.DEFAULT_REBALANCE
        if 'rebalance_on' in kwargs.keys():
            self.rebalance_on = kwargs['rebalance_on']
        self.portfolio_generator = portfolio_model

        # Time Parameters 
        self.period = abs(self.start_date - self.end_date).days

        # Portfolio Parameters
        result = portfolio_model(self.start_date)
        self.short_portfolio = self.UNSET
        if len(result) > 1:
            self.short_portfolio = result[1]
        self.long_portfolio = result[0]

        
        # Module Parameters
        self.event = self.Event()
        Account.get_account()
        self.transaction = Transactions()

            
        

    def event_handler(self, **kwargs):
        """Main Event Loop"""
        variables = {k:v for k,v in kwargs.items()}
        portfolio = []
        holdings = []

        current_date = self.start_date
        for n in range(self.period):
            print(n)


            # Go through Holdings evaluate Sell Conditions
            self.evaluate_holdings(current_date)
            


            # Go through Prosective_Portfolio evaluate Buy Conditions
            # What if Portfolio is empty;
            self.evaluate_portfolio(current_date)
             


            # Order Transaction Log
            # Netprofit Value Cumulative / Individually
            # Returns Cumulative / Individually
            # Daily gain / loss


            # TODO Rebalance when portfolio is empty()

            # Where should portfolio and holdings be held
            # How should they held
            # TODO how do you keep track of Holdings and Portfolio prospectives
            # Single DF; List of DF's, DF Names list
            # TODO Call Rebalance if Portfolio is empty






            
            # Rebalance the Portfolio every n days
            if n % variables['rebalance_on'] == 0:
                self.rebalance_portfolio(self.model, current_date)
                # TODO: Consistencies between previous portfolio and new portfolio
                # 


            # Increment Current Day
            current_date += datetime.timedelta(days=1)
        # Get Results


    def rebalance_portfolio(self, model, on ):
        """Should call the Strategy; which will then produce a new portfolio. Account will then Ingest
        This new port folio.
        """
        portfolio = model(on)
        print(portfolio)
        # self.account.short_portfolio = portfolio[0]
        # self.account.long_portfolio = portfolio[1]


    def evaluate_holdings(self, current_date):
        pass


    def evaluate_portfolio(self, current_date):
        """Needs to have a buy condition"""
        # Iterates through Short List
        if self.short_portfolio != 0:
            # TODO: iterate through short_portfolio
            # TODO: Add the trade type
            pass
        # Iterate through long portfolio to buy
        for security in self.long_portfolio.groupby("symbols"):
            if self.event.BUY_CONDITION(security,current_date):
                break
                # Transaction.BUY(security, current_date)
                # TODO: Remove on BUY from portfolio
                # TODO: SUBCLASS BUY_CONDITION OR ADD FUNCTION AS PARAMETER √
                # NESTED CLASS
    

    class Event:
        """Dynamic Events"""


        def __init__(self):
            """Setup"""
            pass



        def BUY_CONDITION(self, security, current_date):
            """To Overwrite"""
            # TODO add Type: Long / Short Condition
            return True


        def SELL_CONDITION(self, security, current_date):
            """To Overwrite"""
            pass

       


    def run(self):
        """Passess everything into the Event Handler; So the event handler is not using global copies"""
        self.event_handler(start_date=self.start_date , rebalance_on=self.rebalance_on)





        



