# ListRecurringExpensesResponseRecurringExpensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recurring_expense_id** | **str** | ID of the recurring expense | [optional] 
**recurrence_name** | **str** | Name of the Recurring Expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**recurrence_frequency** | **str** | Frequency of the recurrance | [optional] 
**repeat_every** | **str** | The cycle of recurrance | [optional] 
**last_created_date** | **str** | Search recurring expenses by date on when last expense was generated. Variants: &lt;code&gt;last_created_date_start&lt;/code&gt;, &lt;code&gt;last_created_date_end&lt;/code&gt;, &lt;code&gt;last_created_date_before&lt;/code&gt; and &lt;code&gt;last_created_date_after&lt;/code&gt; . &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
**next_expense_date** | **str** | Search recurring expenses by date on which next expense will be generated. Variants: &lt;code&gt;next_expense_date_start&lt;/code&gt;, &lt;code&gt;next_expense_date_end&lt;/code&gt;, &lt;code&gt;next_expense_date_before&lt;/code&gt; and &lt;code&gt;next_expense_date_after&lt;/code&gt; . &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt; | [optional] 
**account_name** | **str** | For which Account the Expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**description** | **str** | Search recurring expenses by description. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**currency_id** | **str** | Unique ID of the currency used | [optional] 
**currency_code** | **str** | Code to denote th ecurrency used | [optional] 
**total** | **float** | Total expense | [optional] 
**is_billable** | **bool** | To check if the expense is billable | [optional] 
**customer_name** | **str** | Name of the Custome for which expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**status** | **str** | Status of the recurring expense | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for a recurring-expense. | [optional] 
**created_time** | **str** | Time expense was created | [optional] 
**last_modified_time** | **str** | Time the expense was last modified | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.list_recurring_expenses_response_recurring_expenses_inner import ListRecurringExpensesResponseRecurringExpensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRecurringExpensesResponseRecurringExpensesInner from a JSON string
list_recurring_expenses_response_recurring_expenses_inner_instance = ListRecurringExpensesResponseRecurringExpensesInner.from_json(json)
# print the JSON string representation of the object
print(ListRecurringExpensesResponseRecurringExpensesInner.to_json())

# convert the object into a dict
list_recurring_expenses_response_recurring_expenses_inner_dict = list_recurring_expenses_response_recurring_expenses_inner_instance.to_dict()
# create an instance of ListRecurringExpensesResponseRecurringExpensesInner from a dict
list_recurring_expenses_response_recurring_expenses_inner_from_dict = ListRecurringExpensesResponseRecurringExpensesInner.from_dict(list_recurring_expenses_response_recurring_expenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


