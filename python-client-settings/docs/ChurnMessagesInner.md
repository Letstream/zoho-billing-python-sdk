# ChurnMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Reason for cancellation | [optional] 
**index** | **str** | Inde value of the reason | [optional] 
**churn_message_id** | **str** | Unique ID of the cancellation reason | [optional] 

## Example

```python
from ls_zoho_billing_settings.models.churn_messages_inner import ChurnMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChurnMessagesInner from a JSON string
churn_messages_inner_instance = ChurnMessagesInner.from_json(json)
# print the JSON string representation of the object
print(ChurnMessagesInner.to_json())

# convert the object into a dict
churn_messages_inner_dict = churn_messages_inner_instance.to_dict()
# create an instance of ChurnMessagesInner from a dict
churn_messages_inner_from_dict = ChurnMessagesInner.from_dict(churn_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


