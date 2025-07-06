# CreditNoteResponseTaxesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** | Unique to denote the tax associate dto the creditnote | [optional] 
**tax_name** | **str** | Unique name for tax. | [optional] 
**tax_amount** | **str** | Tax amount applied to the subscription. | [optional] 

## Example

```python
from ls_zoho_billing_credit_notes.models.credit_note_response_taxes_inner import CreditNoteResponseTaxesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreditNoteResponseTaxesInner from a JSON string
credit_note_response_taxes_inner_instance = CreditNoteResponseTaxesInner.from_json(json)
# print the JSON string representation of the object
print(CreditNoteResponseTaxesInner.to_json())

# convert the object into a dict
credit_note_response_taxes_inner_dict = credit_note_response_taxes_inner_instance.to_dict()
# create an instance of CreditNoteResponseTaxesInner from a dict
credit_note_response_taxes_inner_from_dict = CreditNoteResponseTaxesInner.from_dict(credit_note_response_taxes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


