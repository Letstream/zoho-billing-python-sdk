# MarkAsDraftResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.mark_as_draft_response import MarkAsDraftResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkAsDraftResponse from a JSON string
mark_as_draft_response_instance = MarkAsDraftResponse.from_json(json)
# print the JSON string representation of the object
print(MarkAsDraftResponse.to_json())

# convert the object into a dict
mark_as_draft_response_dict = mark_as_draft_response_instance.to_dict()
# create an instance of MarkAsDraftResponse from a dict
mark_as_draft_response_from_dict = MarkAsDraftResponse.from_dict(mark_as_draft_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


