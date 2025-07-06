# WriteOffRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Description for Write off. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.write_off_request import WriteOffRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WriteOffRequest from a JSON string
write_off_request_instance = WriteOffRequest.from_json(json)
# print the JSON string representation of the object
print(WriteOffRequest.to_json())

# convert the object into a dict
write_off_request_dict = write_off_request_instance.to_dict()
# create an instance of WriteOffRequest from a dict
write_off_request_from_dict = WriteOffRequest.from_dict(write_off_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


