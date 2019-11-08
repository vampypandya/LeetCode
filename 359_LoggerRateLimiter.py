class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.message_dictionary = {}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        message_timestamp = self.message_dictionary.get(message)
        if(message_timestamp==None or message_timestamp + 10 <=timestamp):
            self.message_dictionary[message] = timestamp
            return True
        return False
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
