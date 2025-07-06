# UpdateAContactPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact person. | [optional] 
**last_name** | **str** | Last name of the contact person. | [optional] 
**email** | **str** | Email ID of the contact person to whom notifications regarding the subscription needs to be sent. | 
**mobile** | **str** | Mobile number of the contact person. | [optional] 
**phone** | **str** | Landline or fixed line number of the contact person. | [optional] 
**created_time** | **str** | Time at which the contact person was created. | [optional] 
**updated_time** | **str** | Time at which the contact person details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.update_a_contact_person_request import UpdateAContactPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAContactPersonRequest from a JSON string
update_a_contact_person_request_instance = UpdateAContactPersonRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAContactPersonRequest.to_json())

# convert the object into a dict
update_a_contact_person_request_dict = update_a_contact_person_request_instance.to_dict()
# create an instance of UpdateAContactPersonRequest from a dict
update_a_contact_person_request_from_dict = UpdateAContactPersonRequest.from_dict(update_a_contact_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


