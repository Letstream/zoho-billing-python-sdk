# ContactpersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactperson_id** | **str** | Contact person ID of the customer’s contact person. | [optional] 
**email** | **object** | Email ID of the contact person. | [optional] 
**phone** | **object** | Contactperson’s landline or fixed-line number. | [optional] 
**mobile** | **object** | Contactperson’s mobile phone number. | [optional] 
**zcrm_contact_id** | **object** | This is the Zoho CRM contact id of the contactperson if the contactperson is synced with the contacts in Zoho CRM. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.contactpersons_inner import ContactpersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactpersonsInner from a JSON string
contactpersons_inner_instance = ContactpersonsInner.from_json(json)
# print the JSON string representation of the object
print(ContactpersonsInner.to_json())

# convert the object into a dict
contactpersons_inner_dict = contactpersons_inner_instance.to_dict()
# create an instance of ContactpersonsInner from a dict
contactpersons_inner_from_dict = ContactpersonsInner.from_dict(contactpersons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


