# CancelWriteOffResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.cancel_write_off_response import CancelWriteOffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelWriteOffResponse from a JSON string
cancel_write_off_response_instance = CancelWriteOffResponse.from_json(json)
# print the JSON string representation of the object
print(CancelWriteOffResponse.to_json())

# convert the object into a dict
cancel_write_off_response_dict = cancel_write_off_response_instance.to_dict()
# create an instance of CancelWriteOffResponse from a dict
cancel_write_off_response_from_dict = CancelWriteOffResponse.from_dict(cancel_write_off_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


