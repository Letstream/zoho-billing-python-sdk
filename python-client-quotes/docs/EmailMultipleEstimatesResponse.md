# EmailMultipleEstimatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.email_multiple_estimates_response import EmailMultipleEstimatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailMultipleEstimatesResponse from a JSON string
email_multiple_estimates_response_instance = EmailMultipleEstimatesResponse.from_json(json)
# print the JSON string representation of the object
print(EmailMultipleEstimatesResponse.to_json())

# convert the object into a dict
email_multiple_estimates_response_dict = email_multiple_estimates_response_instance.to_dict()
# create an instance of EmailMultipleEstimatesResponse from a dict
email_multiple_estimates_response_from_dict = EmailMultipleEstimatesResponse.from_dict(email_multiple_estimates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


