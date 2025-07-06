# RefundACreditNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount to be refund. | 
**description** | **str** | A small description about the refund. | [optional] 

## Example

```python
from ls_zoho_billing_refunds.models.refund_a_credit_note_request import RefundACreditNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundACreditNoteRequest from a JSON string
refund_a_credit_note_request_instance = RefundACreditNoteRequest.from_json(json)
# print the JSON string representation of the object
print(RefundACreditNoteRequest.to_json())

# convert the object into a dict
refund_a_credit_note_request_dict = refund_a_credit_note_request_instance.to_dict()
# create an instance of RefundACreditNoteRequest from a dict
refund_a_credit_note_request_from_dict = RefundACreditNoteRequest.from_dict(refund_a_credit_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


