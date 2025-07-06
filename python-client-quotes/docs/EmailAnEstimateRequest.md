# EmailAnEstimateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_from_org_email_id** | **bool** | Boolean to trigger the email from the organization&#39;s email address | [optional] 
**to_mail_ids** | **List[str]** | Array of email addresses of the recipients. | 
**cc_mail_ids** | **List[str]** | Array of email addresses of the recipients to be CC&#39;d. | [optional] 
**subject** | **str** | Subject of an email has to be sent. | [optional] 
**body** | **str** | Body/content of an email has to be sent. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.email_an_estimate_request import EmailAnEstimateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAnEstimateRequest from a JSON string
email_an_estimate_request_instance = EmailAnEstimateRequest.from_json(json)
# print the JSON string representation of the object
print(EmailAnEstimateRequest.to_json())

# convert the object into a dict
email_an_estimate_request_dict = email_an_estimate_request_instance.to_dict()
# create an instance of EmailAnEstimateRequest from a dict
email_an_estimate_request_from_dict = EmailAnEstimateRequest.from_dict(email_an_estimate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


