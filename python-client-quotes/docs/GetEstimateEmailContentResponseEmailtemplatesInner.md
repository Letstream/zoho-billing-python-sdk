# GetEstimateEmailContentResponseEmailtemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected** | **bool** | Selected email context | [optional] 
**name** | **str** | Name of the email receiver | [optional] 
**email_template_id** | **str** | ID of the Email Template used | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.get_estimate_email_content_response_emailtemplates_inner import GetEstimateEmailContentResponseEmailtemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEstimateEmailContentResponseEmailtemplatesInner from a JSON string
get_estimate_email_content_response_emailtemplates_inner_instance = GetEstimateEmailContentResponseEmailtemplatesInner.from_json(json)
# print the JSON string representation of the object
print(GetEstimateEmailContentResponseEmailtemplatesInner.to_json())

# convert the object into a dict
get_estimate_email_content_response_emailtemplates_inner_dict = get_estimate_email_content_response_emailtemplates_inner_instance.to_dict()
# create an instance of GetEstimateEmailContentResponseEmailtemplatesInner from a dict
get_estimate_email_content_response_emailtemplates_inner_from_dict = GetEstimateEmailContentResponseEmailtemplatesInner.from_dict(get_estimate_email_content_response_emailtemplates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


