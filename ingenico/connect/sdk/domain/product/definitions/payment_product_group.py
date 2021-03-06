# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.account_on_file import AccountOnFile
from ingenico.connect.sdk.domain.product.definitions.payment_product_display_hints import PaymentProductDisplayHints
from ingenico.connect.sdk.domain.product.definitions.payment_product_field import PaymentProductField


class PaymentProductGroup(DataObject):
    """
    | Definition of the details of a single payment product group
    """

    __accounts_on_file = None
    __display_hints = None
    __fields = None
    __id = None

    @property
    def accounts_on_file(self):
        """
        | Only populated in the Client API
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.account_on_file.AccountOnFile`]
        """
        return self.__accounts_on_file

    @accounts_on_file.setter
    def accounts_on_file(self, value):
        self.__accounts_on_file = value

    @property
    def display_hints(self):
        """
        | Object containing display hints like the order of the group when shown in a list, the name of the group and the logo. Note that the order of the group is the lowest order among the payment products that belong to the group.
        
        Type: :class:`ingenico.connect.sdk.domain.product.definitions.payment_product_display_hints.PaymentProductDisplayHints`
        """
        return self.__display_hints

    @display_hints.setter
    def display_hints(self, value):
        self.__display_hints = value

    @property
    def fields(self):
        """
        | Object containing all the fields and their details that are associated with this payment product group. If you are not interested in the these fields you can have us filter them our (using hide=fields in the query-string)
        
        Type: list[:class:`ingenico.connect.sdk.domain.product.definitions.payment_product_field.PaymentProductField`]
        """
        return self.__fields

    @fields.setter
    def fields(self, value):
        self.__fields = value

    @property
    def id(self):
        """
        | The ID of the payment product group in our system
        
        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def to_dictionary(self):
        dictionary = super(PaymentProductGroup, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'accountsOnFile', self.accounts_on_file)
        self._add_to_dictionary(dictionary, 'displayHints', self.display_hints)
        self._add_to_dictionary(dictionary, 'fields', self.fields)
        self._add_to_dictionary(dictionary, 'id', self.id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductGroup, self).from_dictionary(dictionary)
        if 'accountsOnFile' in dictionary:
            if not isinstance(dictionary['accountsOnFile'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['accountsOnFile']))
            self.accounts_on_file = []
            for accountsOnFile_element in dictionary['accountsOnFile']:
                accountsOnFile_value = AccountOnFile()
                self.accounts_on_file.append(accountsOnFile_value.from_dictionary(accountsOnFile_element))
        if 'displayHints' in dictionary:
            if not isinstance(dictionary['displayHints'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['displayHints']))
            value = PaymentProductDisplayHints()
            self.display_hints = value.from_dictionary(dictionary['displayHints'])
        if 'fields' in dictionary:
            if not isinstance(dictionary['fields'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['fields']))
            self.fields = []
            for fields_element in dictionary['fields']:
                fields_value = PaymentProductField()
                self.fields.append(fields_value.from_dictionary(fields_element))
        if 'id' in dictionary:
            self.id = dictionary['id']
        return self
