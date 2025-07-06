# CreateAContactPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact person. | [optional] 
**last_name** | **str** | Last name of the contact person. | [optional] 
**email** | **str** | Email ID of the contact person to whom notifications regarding the subscription needs to be sent. | 
**mobile** | **str** | Mobile number of the contact person. | [optional] 
**phone** | **str** | Landline or fixed line number of the contact person. | [optional] 
**fax** | **str** | Customer&#39;s fax number. | [optional] 

## Example

```python
from ls_zoho_billing_contact_persons.models.create_a_contact_person_request import CreateAContactPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAContactPersonRequest from a JSON string
create_a_contact_person_request_instance = CreateAContactPersonRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAContactPersonRequest.to_json())

# convert the object into a dict
create_a_contact_person_request_dict = create_a_contact_person_request_instance.to_dict()
# create an instance of CreateAContactPersonRequest from a dict
create_a_contact_person_request_from_dict = CreateAContactPersonRequest.from_dict(create_a_contact_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


