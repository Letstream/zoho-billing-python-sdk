# PaymentResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID of the required invoice. | [optional] 
**invoice_number** | **str** | Unique ID (starts with INV) of an invoice. | [optional] 
**var_date** | **object** | Date on which the invoice was raised. | [optional] 
**invoice_amount** | **float** | Total amount raised for the invoice. | [optional] 
**amount_applied** | **float** | Amount paid for the invoice. | [optional] 
**balance_amount** | **float** | Unpaid amount of the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.payment_response_invoices_inner import PaymentResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseInvoicesInner from a JSON string
payment_response_invoices_inner_instance = PaymentResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(PaymentResponseInvoicesInner.to_json())

# convert the object into a dict
payment_response_invoices_inner_dict = payment_response_invoices_inner_instance.to_dict()
# create an instance of PaymentResponseInvoicesInner from a dict
payment_response_invoices_inner_from_dict = PaymentResponseInvoicesInner.from_dict(payment_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


