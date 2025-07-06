# ListChildExpensesCreatedResponseExpensehistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_id** | **str** | Unoque ID of the expense | [optional] 
**var_date** | **str** | Date of expense creation | [optional] 
**account_name** | **str** | For which Account the Expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**customer_name** | **str** | Name of the Custome for which expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**total** | **float** | Total expense | [optional] 
**status** | **str** | Status of the recurring expense | [optional] 
**vendor_name** | **str** | Name of the seller | [optional] 
**paid_through_account_name** | **str** | Account from which payment was made | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_child_expenses_created_response_expensehistory_inner import ListChildExpensesCreatedResponseExpensehistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListChildExpensesCreatedResponseExpensehistoryInner from a JSON string
list_child_expenses_created_response_expensehistory_inner_instance = ListChildExpensesCreatedResponseExpensehistoryInner.from_json(json)
# print the JSON string representation of the object
print(ListChildExpensesCreatedResponseExpensehistoryInner.to_json())

# convert the object into a dict
list_child_expenses_created_response_expensehistory_inner_dict = list_child_expenses_created_response_expensehistory_inner_instance.to_dict()
# create an instance of ListChildExpensesCreatedResponseExpensehistoryInner from a dict
list_child_expenses_created_response_expensehistory_inner_from_dict = ListChildExpensesCreatedResponseExpensehistoryInner.from_dict(list_child_expenses_created_response_expensehistory_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


