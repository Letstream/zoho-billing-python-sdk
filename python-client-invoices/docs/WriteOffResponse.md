# WriteOffResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_invoices.models.write_off_response import WriteOffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WriteOffResponse from a JSON string
write_off_response_instance = WriteOffResponse.from_json(json)
# print the JSON string representation of the object
print(WriteOffResponse.to_json())

# convert the object into a dict
write_off_response_dict = write_off_response_instance.to_dict()
# create an instance of WriteOffResponse from a dict
write_off_response_from_dict = WriteOffResponse.from_dict(write_off_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


