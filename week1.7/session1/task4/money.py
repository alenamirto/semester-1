# from Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        if not isinstance(pounds, int): #test_invalid_type_pound
            raise TypeError("pounds must be an integer")

        if not isinstance(pence, int): #test_invalid_type_pence
            raise TypeError("pence must be an integer")

        if pounds < 0: #test_invalid_value_pound
            raise ValueError("pounds must be >= 0")

        if pence < 0 or pence > 99: #test_invalid_value_pence
            raise ValueError("pence must be in range 0-99")

        ##################
            
        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other): #test_valid_add
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money): #test_add_invalid_type
            raise TypeError("other object must be a Money")

        sum_pounds = self.pounds + other.pounds
        extra_pound = (self.pence + other.pence) // 100
        sum_pence = (self.pence + other.pence) % 100

        return Money(sum_pounds + extra_pound, sum_pence)
