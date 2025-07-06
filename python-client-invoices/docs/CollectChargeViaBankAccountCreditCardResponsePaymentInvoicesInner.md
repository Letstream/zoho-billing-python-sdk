# CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Unique ID generated for an invoice. | [optional] 
**invoice_number** | **str** | Unique ID (starts with INV) of an invoice. | [optional] 
**var_date** | **object** | Date on which the invoice was raised. | [optional] 
**invoice_amount** | **float** | Total amount raised for the invoice. | [optional] 
**amount_applied** | **float** | Amount paid for the invoice. | [optional] 
**balance_amount** | **float** | Unpaid amount of the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.collect_charge_via_bank_account_credit_card_response_payment_invoices_inner import CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner from a JSON string
collect_charge_via_bank_account_credit_card_response_payment_invoices_inner_instance = CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner.to_json())

# convert the object into a dict
collect_charge_via_bank_account_credit_card_response_payment_invoices_inner_dict = collect_charge_via_bank_account_credit_card_response_payment_invoices_inner_instance.to_dict()
# create an instance of CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner from a dict
collect_charge_via_bank_account_credit_card_response_payment_invoices_inner_from_dict = CollectChargeViaBankAccountCreditCardResponsePaymentInvoicesInner.from_dict(collect_charge_via_bank_account_credit_card_response_payment_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


