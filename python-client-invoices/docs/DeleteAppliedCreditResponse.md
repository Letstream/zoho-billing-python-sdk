# DeleteAppliedCreditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.delete_applied_credit_response import DeleteAppliedCreditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAppliedCreditResponse from a JSON string
delete_applied_credit_response_instance = DeleteAppliedCreditResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAppliedCreditResponse.to_json())

# convert the object into a dict
delete_applied_credit_response_dict = delete_applied_credit_response_instance.to_dict()
# create an instance of DeleteAppliedCreditResponse from a dict
delete_applied_credit_response_from_dict = DeleteAppliedCreditResponse.from_dict(delete_applied_credit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


