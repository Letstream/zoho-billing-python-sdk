# AddContactPersonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactpersons** | [**List[CreateASubscriptionRequestContactpersonsInner]**](CreateASubscriptionRequestContactpersonsInner.md) | List of contact person objects. Each object contains &lt;code&gt;contactperson_id&lt;/code&gt;. | 

## Example

```python
from ls_zoho_billing_subscription.models.add_contact_person_request import AddContactPersonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddContactPersonRequest from a JSON string
add_contact_person_request_instance = AddContactPersonRequest.from_json(json)
# print the JSON string representation of the object
print(AddContactPersonRequest.to_json())

# convert the object into a dict
add_contact_person_request_dict = add_contact_person_request_instance.to_dict()
# create an instance of AddContactPersonRequest from a dict
add_contact_person_request_from_dict = AddContactPersonRequest.from_dict(add_contact_person_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


