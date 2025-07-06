# FromEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Name of the sender of email | [optional] 
**selected** | **bool** | Boolean check for the email template. Whether selected or not | [optional] 
**email** | **str** | Email ID of the contact | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.from_emails_inner import FromEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of FromEmailsInner from a JSON string
from_emails_inner_instance = FromEmailsInner.from_json(json)
# print the JSON string representation of the object
print(FromEmailsInner.to_json())

# convert the object into a dict
from_emails_inner_dict = from_emails_inner_instance.to_dict()
# create an instance of FromEmailsInner from a dict
from_emails_inner_from_dict = FromEmailsInner.from_dict(from_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


