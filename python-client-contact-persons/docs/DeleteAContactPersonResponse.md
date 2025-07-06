# DeleteAContactPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_contact_persons.models.delete_a_contact_person_response import DeleteAContactPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAContactPersonResponse from a JSON string
delete_a_contact_person_response_instance = DeleteAContactPersonResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteAContactPersonResponse.to_json())

# convert the object into a dict
delete_a_contact_person_response_dict = delete_a_contact_person_response_instance.to_dict()
# create an instance of DeleteAContactPersonResponse from a dict
delete_a_contact_person_response_from_dict = DeleteAContactPersonResponse.from_dict(delete_a_contact_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


