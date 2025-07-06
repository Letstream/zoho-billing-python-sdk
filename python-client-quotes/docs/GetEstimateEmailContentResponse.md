# GetEstimateEmailContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**body** | **str** | Body/content of an email has to be sent. | [optional] 
**error_list** | **List[str]** | Error list | [optional] 
**subject** | **str** | Subject of an email has to be sent. | [optional] 
**emailtemplates** | [**List[GetEstimateEmailContentResponseEmailtemplatesInner]**](GetEstimateEmailContentResponseEmailtemplatesInner.md) | Email template used in the quote | [optional] 
**to_contacts** | [**List[ToContactsInner]**](ToContactsInner.md) | Email recepients | [optional] 
**file_name** | **str** | The name of the file to be attached | [optional] 
**from_emails** | [**List[GetEstimateEmailContentResponseFromEmailsInner]**](GetEstimateEmailContentResponseFromEmailsInner.md) | Emails received | [optional] 
**customer_id** | **str** | Customer ID on the quote. | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.get_estimate_email_content_response import GetEstimateEmailContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEstimateEmailContentResponse from a JSON string
get_estimate_email_content_response_instance = GetEstimateEmailContentResponse.from_json(json)
# print the JSON string representation of the object
print(GetEstimateEmailContentResponse.to_json())

# convert the object into a dict
get_estimate_email_content_response_dict = get_estimate_email_content_response_instance.to_dict()
# create an instance of GetEstimateEmailContentResponse from a dict
get_estimate_email_content_response_from_dict = GetEstimateEmailContentResponse.from_dict(get_estimate_email_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


