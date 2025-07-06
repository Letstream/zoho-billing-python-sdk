# ListTimeEntriesResponseTimeEntriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_entry_id** | **str** | Unique ID of the time entry | [optional] 
**project_id** | **str** | Unique ID of the project | [optional] 
**project_name** | **str** | Name of the project | [optional] 
**customer_id** | **str** | Search projects by customer id. | [optional] 
**customer_name** | **str** | Name of the client for whom the project is planned | [optional] 
**task_id** | **str** | Unique ID of the task | [optional] 
**task_name** | **str** | Name of the task | [optional] 
**user_id** | **str** | Unique ID of the user of timesheet. | [optional] 
**is_current_user** | **bool** | To check if the user is currently a part of the task | [optional] 
**user_name** | **str** | User name of the current user | [optional] 
**log_date** | **str** | Date on which the user spent on the task. &lt;code&gt;Date Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
**begin_time** | **str** | Time of starting the clock | [optional] 
**end_time** | **str** | Closing time of the task | [optional] 
**log_time** | **str** | Total time soent on the task | [optional] 
**is_billable** | **bool** | To check if the task is billable | [optional] 
**billed_status** | **str** | status of billing | [optional] 
**invoice_id** | **str** | Unique ID of the invoice | [optional] 
**notes** | **str** | Short notes on the task | [optional] 
**timer_started_at** | **str** | Opening time of the task | [optional] 
**timer_duration_in_minutes** | **str** | Duration of task in minutes | [optional] 
**created_time** | **str** | Time of task creation | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.list_time_entries_response_time_entries_inner import ListTimeEntriesResponseTimeEntriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListTimeEntriesResponseTimeEntriesInner from a JSON string
list_time_entries_response_time_entries_inner_instance = ListTimeEntriesResponseTimeEntriesInner.from_json(json)
# print the JSON string representation of the object
print(ListTimeEntriesResponseTimeEntriesInner.to_json())

# convert the object into a dict
list_time_entries_response_time_entries_inner_dict = list_time_entries_response_time_entries_inner_instance.to_dict()
# create an instance of ListTimeEntriesResponseTimeEntriesInner from a dict
list_time_entries_response_time_entries_inner_from_dict = ListTimeEntriesResponseTimeEntriesInner.from_dict(list_time_entries_response_time_entries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


