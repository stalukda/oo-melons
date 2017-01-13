import random

class AbstractMelonOrder(object):
    """A class which provides blueprint for domestic and intenational melon orders.
    """
    def __init__(self, species, qty, country_code="USA"):
        """Initialize melon order attributes"""
        self.country_code = country_code
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas":
            base_price = 7.5
        else:
            base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != "USA" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        base_price = random.randint(5,9)
        print base_price
        return base_price

class DomesticMelonOrder(AbstractMelonOrder):
    """Subclass for domestic orders
    """

    tax = .08
    order_type = "domestic"

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """Subclass for international orders
    """
    tax = .17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Subclass for govenremnt orders
    """
    
    tax = 0
    order_type = "government"

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):

        if passed:
            self.passed_inspection = True
            print "You passed your inspection!"
