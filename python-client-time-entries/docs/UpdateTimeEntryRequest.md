# UpdateTimeEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | ID of the project. | 
**task_id** | **str** | ID of the task. | 
**user_id** | **str** | ID of the user. | 
**log_date** | **str** | Date on which the user spent on the task. &lt;code&gt;Date Format [yyyy-mm-dd]&lt;/code&gt; | 
**log_time** | **str** | Time the user spent on this task. Either send this attribute or begin and end time attributes. &lt;code&gt;Time Format [HH:mm]&lt;/code&gt; | [optional] 
**begin_time** | **str** | Time the user started working on this task. &lt;code&gt;Time Format [HH:mm]&lt;/code&gt; | [optional] 
**end_time** | **str** | Time the user stopped working on this task. &lt;code&gt;Time Format [HH:mm]&lt;/code&gt; | [optional] 
**is_billable** | **bool** | Whether it is billable or not. | [optional] 
**notes** | **str** | Description of the work done. &lt;code&gt;Maximum length [500]&lt;/code&gt; | [optional] 
**start_timer** | **str** | Start timer. | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.update_time_entry_request import UpdateTimeEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeEntryRequest from a JSON string
update_time_entry_request_instance = UpdateTimeEntryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTimeEntryRequest.to_json())

# convert the object into a dict
update_time_entry_request_dict = update_time_entry_request_instance.to_dict()
# create an instance of UpdateTimeEntryRequest from a dict
update_time_entry_request_from_dict = UpdateTimeEntryRequest.from_dict(update_time_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


