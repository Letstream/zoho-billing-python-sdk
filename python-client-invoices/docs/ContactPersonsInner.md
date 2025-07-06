# ContactPersonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactperson_id** | **str** | Unique ID of the contact person. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.contact_persons_inner import ContactPersonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContactPersonsInner from a JSON string
contact_persons_inner_instance = ContactPersonsInner.from_json(json)
# print the JSON string representation of the object
print(ContactPersonsInner.to_json())

# convert the object into a dict
contact_persons_inner_dict = contact_persons_inner_instance.to_dict()
# create an instance of ContactPersonsInner from a dict
contact_persons_inner_from_dict = ContactPersonsInner.from_dict(contact_persons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


