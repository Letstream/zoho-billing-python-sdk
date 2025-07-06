# ListCreditsAppliedResponseCreditsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creditnote_id** | **str** | Unique ID denoting the credit note. | [optional] 
**creditnotes_invoice_id** | **str** | Unique identifier to denote the Associated Credits to the invoice | [optional] 
**creditnotes_number** | **str** | Reference number for the credit note. | [optional] 
**credited_date** | **str** | Date on which the credit were applied | [optional] 
**amount_applied** | **float** | Amount paid for the invoice. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_credits_applied_response_credits_inner import ListCreditsAppliedResponseCreditsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListCreditsAppliedResponseCreditsInner from a JSON string
list_credits_applied_response_credits_inner_instance = ListCreditsAppliedResponseCreditsInner.from_json(json)
# print the JSON string representation of the object
print(ListCreditsAppliedResponseCreditsInner.to_json())

# convert the object into a dict
list_credits_applied_response_credits_inner_dict = list_credits_applied_response_credits_inner_instance.to_dict()
# create an instance of ListCreditsAppliedResponseCreditsInner from a dict
list_credits_applied_response_credits_inner_from_dict = ListCreditsAppliedResponseCreditsInner.from_dict(list_credits_applied_response_credits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


