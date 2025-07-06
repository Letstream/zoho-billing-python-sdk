# EventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Unique ID generated for a particular event | [optional] 
**event_type** | **str** | The type of event. | [optional] 
**event_time** | **str** | The time at which the event is created. | [optional] 
**payload** | **str** | Holds information about the event that occurred. | [optional] 
**webhooks** | [**List[EventResponseWebhooksInner]**](EventResponseWebhooksInner.md) | List of objects holds information about the webhooks. Each object contains &lt;code&gt;webhook_id&lt;/code&gt;, &lt;code&gt;url&lt;/code&gt;, &lt;code&gt;status&lt;/code&gt; and &lt;code&gt;last_updated_time&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_events.models.event_response import EventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponse from a JSON string
event_response_instance = EventResponse.from_json(json)
# print the JSON string representation of the object
print(EventResponse.to_json())

# convert the object into a dict
event_response_dict = event_response_instance.to_dict()
# create an instance of EventResponse from a dict
event_response_from_dict = EventResponse.from_dict(event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


