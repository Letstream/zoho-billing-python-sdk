# EventResponseWebhooksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_id** | **str** | The unique ID generated for a webhook by the server. This can be used as an identifier. | [optional] 
**url** | **str** | The URL for which the webhook is sent. | [optional] 
**status** | **str** | Status of the webhook. This can be &lt;code&gt;success&lt;/code&gt;, &lt;code&gt;scheduled&lt;/code&gt; or &lt;code&gt;failure&lt;/code&gt;. | [optional] 
**last_updated_time** | **str** | The time at which the webhook was last sent. | [optional] 

## Example

```python
from ls_zoho_billing_events.models.event_response_webhooks_inner import EventResponseWebhooksInner

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseWebhooksInner from a JSON string
event_response_webhooks_inner_instance = EventResponseWebhooksInner.from_json(json)
# print the JSON string representation of the object
print(EventResponseWebhooksInner.to_json())

# convert the object into a dict
event_response_webhooks_inner_dict = event_response_webhooks_inner_instance.to_dict()
# create an instance of EventResponseWebhooksInner from a dict
event_response_webhooks_inner_from_dict = EventResponseWebhooksInner.from_dict(event_response_webhooks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


