from lesson_13.phone_practise.operators.base_operator import BaseMobOperator


class BasePhone:

    def __init__(self, model: str, mobile_operator: BaseMobOperator):
        """
        Base class for phone description
        :param model: str, like iPhone 13
        :param mobile_operator: object of BaseMobOperator
        """
        self.model = model
        self.mobile_operator = mobile_operator
