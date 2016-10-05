#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.param_request import ParamRequest


class FindProductsParams(ParamRequest):
    """
    Query parameters for Get payment products
    See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products_get
    
    Attributes:
        amount:         long
        hide:           list[str]
        is_recurring:   bool
        country_code:   str
        locale:         str
        currency_code:  str
    """

    amount = None
    hide = None
    is_recurring = None
    country_code = None
    locale = None
    currency_code = None

    def add_hide(self, value):
        """
        :param value: str
        """
        if self.hide is None:
            self.hide = []
        self.hide.append(value)

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        self._add_parameter(result, "amount", self.amount)
        self._add_parameter(result, "hide", self.hide)
        self._add_parameter(result, "isRecurring", self.is_recurring)
        self._add_parameter(result, "countryCode", self.country_code)
        self._add_parameter(result, "locale", self.locale)
        self._add_parameter(result, "currencyCode", self.currency_code)
        return result
