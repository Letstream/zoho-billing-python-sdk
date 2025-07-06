# RetrieveAnInvoiceResponseInvoiceCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | Unique ID denoting the credit note. | [optional] 
**creditnotes_number** | **str** | Reference number for the credit note. | [optional] 
**credited_date** | **str** | Date on which the credit were applied | [optional] 
**credited_amount** | **str** | Credited amount for the invoice | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.retrieve_an_invoice_response_invoice_credits_inner import RetrieveAnInvoiceResponseInvoiceCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAnInvoiceResponseInvoiceCreditsInner from a JSON string
retrieve_an_invoice_response_invoice_credits_inner_instance = RetrieveAnInvoiceResponseInvoiceCreditsInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAnInvoiceResponseInvoiceCreditsInner.to_json())

# convert the object into a dict
retrieve_an_invoice_response_invoice_credits_inner_dict = retrieve_an_invoice_response_invoice_credits_inner_instance.to_dict()
# create an instance of RetrieveAnInvoiceResponseInvoiceCreditsInner from a dict
retrieve_an_invoice_response_invoice_credits_inner_from_dict = RetrieveAnInvoiceResponseInvoiceCreditsInner.from_dict(retrieve_an_invoice_response_invoice_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


