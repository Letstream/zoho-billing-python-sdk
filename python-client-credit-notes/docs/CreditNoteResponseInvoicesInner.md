# CreditNoteResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | Invoice ID of the required invoice. | [optional] 
**invoice_number** | **str** | Invoice number of the required invoice. | [optional] 
**amount** | **float** | Amount paid for the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.credit_note_response_invoices_inner import CreditNoteResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResponseInvoicesInner from a JSON string
credit_note_response_invoices_inner_instance = CreditNoteResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(CreditNoteResponseInvoicesInner.to_json())

# convert the object into a dict
credit_note_response_invoices_inner_dict = credit_note_response_invoices_inner_instance.to_dict()
# create an instance of CreditNoteResponseInvoicesInner from a dict
credit_note_response_invoices_inner_from_dict = CreditNoteResponseInvoicesInner.from_dict(credit_note_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


