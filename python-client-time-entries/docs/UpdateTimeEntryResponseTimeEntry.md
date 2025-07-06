# UpdateTimeEntryResponseTimeEntry


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
**user_name** | **str** | User name of the current user | [optional] 
**is_current_user** | **bool** | To check if the user is currently a part of the task | [optional] 
**log_date** | **str** | Date on which the user spent on the task. &lt;code&gt;Date Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
**begin_time** | **str** | Time of starting the clock | [optional] 
**end_time** | **str** | Closing time of the task | [optional] 
**log_time** | **str** | Total time soent on the task | [optional] 
**is_billable** | **bool** | To check if the task is billable | [optional] 
**billed_status** | **str** | status of billing | [optional] 
**invoice_id** | **str** | Unique ID of the invoice | [optional] 
**notes** | **str** | Short notes on the task | [optional] 
**timer_started_at** | **str** | Opening time of the task | [optional] 
**timer_started_at_utc_time** | **str** | Time task started | [optional] 
**timer_duration_in_minutes** | **str** | Duration of task in minutes | [optional] 
**timer_duration_in_seconds** | **str** | Total task duration in seconds | [optional] 
**created_time** | **str** | Time of task creation | [optional] 
**timesheet_custom_fields** | **str** | Additional fields in timesheet | [optional] 

## Example

```python
from ls_zoho_billing_time_entries.models.update_time_entry_response_time_entry import UpdateTimeEntryResponseTimeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTimeEntryResponseTimeEntry from a JSON string
update_time_entry_response_time_entry_instance = UpdateTimeEntryResponseTimeEntry.from_json(json)
# print the JSON string representation of the object
print(UpdateTimeEntryResponseTimeEntry.to_json())

# convert the object into a dict
update_time_entry_response_time_entry_dict = update_time_entry_response_time_entry_instance.to_dict()
# create an instance of UpdateTimeEntryResponseTimeEntry from a dict
update_time_entry_response_time_entry_from_dict = UpdateTimeEntryResponseTimeEntry.from_dict(update_time_entry_response_time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


