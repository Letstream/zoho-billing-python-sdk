# RetrieveAContactPersonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**contact_person** | [**RetrieveAContactPersonResponseContactPerson**](RetrieveAContactPersonResponseContactPerson.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.retrieve_a_contact_person_response import RetrieveAContactPersonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAContactPersonResponse from a JSON string
retrieve_a_contact_person_response_instance = RetrieveAContactPersonResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveAContactPersonResponse.to_json())

# convert the object into a dict
retrieve_a_contact_person_response_dict = retrieve_a_contact_person_response_instance.to_dict()
# create an instance of RetrieveAContactPersonResponse from a dict
retrieve_a_contact_person_response_from_dict = RetrieveAContactPersonResponse.from_dict(retrieve_a_contact_person_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


