# RetrieveChurnMessagePreferencesResponseChurnMessagesSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_advanced_version** | **str** | Boolean to denote if it is an Simple version or Advanced Version. | [optional] 
**is_reason_mandatory** | **str** | Whether reason is mandatory or not. | [optional] 
**churn_messages** | [**List[ChurnMessagesInner]**](ChurnMessagesInner.md) | List of Cancellation reasons | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.retrieve_churn_message_preferences_response_churn_messages_settings import RetrieveChurnMessagePreferencesResponseChurnMessagesSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveChurnMessagePreferencesResponseChurnMessagesSettings from a JSON string
retrieve_churn_message_preferences_response_churn_messages_settings_instance = RetrieveChurnMessagePreferencesResponseChurnMessagesSettings.from_json(json)
# print the JSON string representation of the object
print(RetrieveChurnMessagePreferencesResponseChurnMessagesSettings.to_json())

# convert the object into a dict
retrieve_churn_message_preferences_response_churn_messages_settings_dict = retrieve_churn_message_preferences_response_churn_messages_settings_instance.to_dict()
# create an instance of RetrieveChurnMessagePreferencesResponseChurnMessagesSettings from a dict
retrieve_churn_message_preferences_response_churn_messages_settings_from_dict = RetrieveChurnMessagePreferencesResponseChurnMessagesSettings.from_dict(retrieve_churn_message_preferences_response_churn_messages_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


