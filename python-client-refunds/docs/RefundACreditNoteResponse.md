# RefundACreditNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**refund** | [**RefundResponse**](RefundResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_a_credit_note_response import RefundACreditNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundACreditNoteResponse from a JSON string
refund_a_credit_note_response_instance = RefundACreditNoteResponse.from_json(json)
# print the JSON string representation of the object
print(RefundACreditNoteResponse.to_json())

# convert the object into a dict
refund_a_credit_note_response_dict = refund_a_credit_note_response_instance.to_dict()
# create an instance of RefundACreditNoteResponse from a dict
refund_a_credit_note_response_from_dict = RefundACreditNoteResponse.from_dict(refund_a_credit_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


