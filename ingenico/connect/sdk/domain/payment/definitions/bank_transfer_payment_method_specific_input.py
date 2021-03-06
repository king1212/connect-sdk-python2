# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.bank_transfer_payment_method_specific_input_base import BankTransferPaymentMethodSpecificInputBase


class BankTransferPaymentMethodSpecificInput(BankTransferPaymentMethodSpecificInputBase):

    def to_dictionary(self):
        dictionary = super(BankTransferPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
