# GetEstimateEmailContentResponseFromEmailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Name of the user | [optional] 
**selected** | **bool** | Selected email recepients | [optional] 
**email** | **str** | Email ID of the contact | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.get_estimate_email_content_response_from_emails_inner import GetEstimateEmailContentResponseFromEmailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEstimateEmailContentResponseFromEmailsInner from a JSON string
get_estimate_email_content_response_from_emails_inner_instance = GetEstimateEmailContentResponseFromEmailsInner.from_json(json)
# print the JSON string representation of the object
print(GetEstimateEmailContentResponseFromEmailsInner.to_json())

# convert the object into a dict
get_estimate_email_content_response_from_emails_inner_dict = get_estimate_email_content_response_from_emails_inner_instance.to_dict()
# create an instance of GetEstimateEmailContentResponseFromEmailsInner from a dict
get_estimate_email_content_response_from_emails_inner_from_dict = GetEstimateEmailContentResponseFromEmailsInner.from_dict(get_estimate_email_content_response_from_emails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


