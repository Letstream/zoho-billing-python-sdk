# ResumeARecurringExpenseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.resume_a_recurring_expense_response import ResumeARecurringExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResumeARecurringExpenseResponse from a JSON string
resume_a_recurring_expense_response_instance = ResumeARecurringExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(ResumeARecurringExpenseResponse.to_json())

# convert the object into a dict
resume_a_recurring_expense_response_dict = resume_a_recurring_expense_response_instance.to_dict()
# create an instance of ResumeARecurringExpenseResponse from a dict
resume_a_recurring_expense_response_from_dict = ResumeARecurringExpenseResponse.from_dict(resume_a_recurring_expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


