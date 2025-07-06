# CreateAPaymentRequestInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID of the required invoice. | 
**amount_applied** | **float** | Amount paid for the invoice. | 

## Example

```python
from ls_zoho_billing_payments.models.create_a_payment_request_invoices_inner import CreateAPaymentRequestInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPaymentRequestInvoicesInner from a JSON string
create_a_payment_request_invoices_inner_instance = CreateAPaymentRequestInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(CreateAPaymentRequestInvoicesInner.to_json())

# convert the object into a dict
create_a_payment_request_invoices_inner_dict = create_a_payment_request_invoices_inner_instance.to_dict()
# create an instance of CreateAPaymentRequestInvoicesInner from a dict
create_a_payment_request_invoices_inner_from_dict = CreateAPaymentRequestInvoicesInner.from_dict(create_a_payment_request_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


