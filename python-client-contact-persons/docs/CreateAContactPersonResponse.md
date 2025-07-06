# CreateAContactPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**contact_person** | [**ContactPersonResponse**](ContactPersonResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.create_a_contact_person_response import CreateAContactPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAContactPersonResponse from a JSON string
create_a_contact_person_response_instance = CreateAContactPersonResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAContactPersonResponse.to_json())

# convert the object into a dict
create_a_contact_person_response_dict = create_a_contact_person_response_instance.to_dict()
# create an instance of CreateAContactPersonResponse from a dict
create_a_contact_person_response_from_dict = CreateAContactPersonResponse.from_dict(create_a_contact_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


