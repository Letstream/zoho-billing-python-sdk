# UpdateAContactPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**contact_person** | [**RetrieveAContactPersonResponseContactPerson**](RetrieveAContactPersonResponseContactPerson.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.update_a_contact_person_response import UpdateAContactPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAContactPersonResponse from a JSON string
update_a_contact_person_response_instance = UpdateAContactPersonResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateAContactPersonResponse.to_json())

# convert the object into a dict
update_a_contact_person_response_dict = update_a_contact_person_response_instance.to_dict()
# create an instance of UpdateAContactPersonResponse from a dict
update_a_contact_person_response_from_dict = UpdateAContactPersonResponse.from_dict(update_a_contact_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


