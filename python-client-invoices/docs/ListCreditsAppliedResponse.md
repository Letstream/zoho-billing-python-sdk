# ListCreditsAppliedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**credits** | [**List[ListCreditsAppliedResponseCreditsInner]**](ListCreditsAppliedResponseCreditsInner.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.list_credits_applied_response import ListCreditsAppliedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCreditsAppliedResponse from a JSON string
list_credits_applied_response_instance = ListCreditsAppliedResponse.from_json(json)
# print the JSON string representation of the object
print(ListCreditsAppliedResponse.to_json())

# convert the object into a dict
list_credits_applied_response_dict = list_credits_applied_response_instance.to_dict()
# create an instance of ListCreditsAppliedResponse from a dict
list_credits_applied_response_from_dict = ListCreditsAppliedResponse.from_dict(list_credits_applied_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


