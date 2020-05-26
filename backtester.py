from forge.event_handler import EventHandler
class BackTester(EventHandler):
    class Event(EventHandler.Event):
        def BUY_CONDITION(self, security, current_date):
            # print(security)
            return True

        def SELL_CONDITION(self, security, current_date):
            pass

        

