# RetrieveChurnMessagePreferencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**churn_messages_settings** | [**RetrieveChurnMessagePreferencesResponseChurnMessagesSettings**](RetrieveChurnMessagePreferencesResponseChurnMessagesSettings.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_churn_message_preferences_response import RetrieveChurnMessagePreferencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveChurnMessagePreferencesResponse from a JSON string
retrieve_churn_message_preferences_response_instance = RetrieveChurnMessagePreferencesResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveChurnMessagePreferencesResponse.to_json())

# convert the object into a dict
retrieve_churn_message_preferences_response_dict = retrieve_churn_message_preferences_response_instance.to_dict()
# create an instance of RetrieveChurnMessagePreferencesResponse from a dict
retrieve_churn_message_preferences_response_from_dict = RetrieveChurnMessagePreferencesResponse.from_dict(retrieve_churn_message_preferences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


