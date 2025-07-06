# ListRecurringExpenseHistoryResponseCommentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_id** | **str** | Unique ID of the comment | [optional] 
**recurring_expense_id** | **str** | ID of the recurring expense | [optional] 
**description** | **str** | Search recurring expenses by description. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**commented_by_id** | **str** | Filter to view comment by ID | [optional] 
**commented_by** | **str** | Person who added the comment | [optional] 
**var_date** | **str** | Date of expense creation | [optional] 
**time** | **str** | Time of transaction | [optional] 
**operation_type** | **str** | Operation on the expense created | [optional] 
**transaction_id** | **str** | Unique ID of the transaction | [optional] 
**transaction_type** | **str** | Type of transaction | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_recurring_expense_history_response_comments_inner import ListRecurringExpenseHistoryResponseCommentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecurringExpenseHistoryResponseCommentsInner from a JSON string
list_recurring_expense_history_response_comments_inner_instance = ListRecurringExpenseHistoryResponseCommentsInner.from_json(json)
# print the JSON string representation of the object
print(ListRecurringExpenseHistoryResponseCommentsInner.to_json())

# convert the object into a dict
list_recurring_expense_history_response_comments_inner_dict = list_recurring_expense_history_response_comments_inner_instance.to_dict()
# create an instance of ListRecurringExpenseHistoryResponseCommentsInner from a dict
list_recurring_expense_history_response_comments_inner_from_dict = ListRecurringExpenseHistoryResponseCommentsInner.from_dict(list_recurring_expense_history_response_comments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


