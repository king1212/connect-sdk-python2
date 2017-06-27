# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.domain.payment.definitions.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput


class BankTransferPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):

    def to_dictionary(self):
        dictionary = super(BankTransferPaymentMethodSpecificOutput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        return self
