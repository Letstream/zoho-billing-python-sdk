# EmailAnEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_quotes.models.email_an_estimate_response import EmailAnEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAnEstimateResponse from a JSON string
email_an_estimate_response_instance = EmailAnEstimateResponse.from_json(json)
# print the JSON string representation of the object
print(EmailAnEstimateResponse.to_json())

# convert the object into a dict
email_an_estimate_response_dict = email_an_estimate_response_instance.to_dict()
# create an instance of EmailAnEstimateResponse from a dict
email_an_estimate_response_from_dict = EmailAnEstimateResponse.from_dict(email_an_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


