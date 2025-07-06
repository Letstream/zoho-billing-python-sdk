# ToContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact person | [optional] 
**selected** | **bool** | Boolean check for the email template. Whether selected or not | [optional] 
**phone** | **str** | phone number of the contact person | [optional] 
**email** | **str** | Email ID of the contact | [optional] 
**last_name** | **str** | Last name of the contact person | [optional] 
**salutation** | **str** | Salutation for the contact | [optional] 
**contact_person_id** | **str** | The ID of the contact person | [optional] 
**mobile** | **str** | mobile number of the contact person | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.to_contacts_inner import ToContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ToContactsInner from a JSON string
to_contacts_inner_instance = ToContactsInner.from_json(json)
# print the JSON string representation of the object
print(ToContactsInner.to_json())

# convert the object into a dict
to_contacts_inner_dict = to_contacts_inner_instance.to_dict()
# create an instance of ToContactsInner from a dict
to_contacts_inner_from_dict = ToContactsInner.from_dict(to_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


