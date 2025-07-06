# CreateARecurringExpenseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique ID of an account | 
**recurrence_name** | **str** | Name of the Recurring Expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | 
**start_date** | **str** | Start date of the recurring expense. Expenses will not be generated for dates prior to the current date. &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt;. | 
**gst_no** | **str** | 15 digit GST identification number of the vendor. | [optional] 
**source_of_supply** | **str** | Place from where the goods/services are supplied. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**destination_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, organisation&#39;s home state will be taken) | [optional] 
**reverse_charge_tax_id** | **str** | Enter reverse charge tax ID | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for a recurring-expense. | [optional] 
**line_items** | [**List[LineItemsInner]**](LineItemsInner.md) |  | [optional] 
**end_date** | **str** | Date on which recurring expense has to expire. Can be left as empty to run forever. &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt;. | [optional] 
**recurrence_frequency** | **str** | Frequency of the recurrance | 
**repeat_every** | **str** | The cycle of recurrance | 
**amount** | **float** | Recurring Expense amount. | 
**vat_treatment** | **str** | VAT treatment for the expense. VAT treatment denotes the location of the vendor, if the vendor resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;.If the vendor is in an EU country &amp; VAT registered, you are resides in Northen Ireland and purchasing Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt; and if he resides outside the EU then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt;(For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**product_type** | **str** | Type of the expense. This denotes whether the expense is to be treated as a goods or service purchase. Allowed Values: &lt;code&gt;goods&lt;/code&gt; and &lt;code&gt;service&lt;/code&gt;. | [optional] 
**acquisition_vat_id** | **str** | This is the ID of the tax applied in case this is an EU - goods expense and acquisition VAT needs to be reported. | [optional] 
**reverse_charge_vat_id** | **str** | This is the ID of the tax applied in case this is a non UK - service expense and reverse charge VAT needs to be reported. | [optional] 
**tax_id** | **str** | Unique ID for the tax | [optional] 
**is_inclusive_tax** | **bool** | To check if the total is inclusive of tax | [optional] 
**is_billable** | **bool** | To check if the expense is billable | [optional] 
**customer_id** | **str** | Search expenses by customer id. | [optional] 
**project_id** | **str** | Unique ID of the tax applied | [optional] 
**currency_id** | **str** | Unique ID of the currency used | [optional] 
**exchange_rate** | **float** | Foreign exchange rate | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.create_a_recurring_expense_request import CreateARecurringExpenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateARecurringExpenseRequest from a JSON string
create_a_recurring_expense_request_instance = CreateARecurringExpenseRequest.from_json(json)
# print the JSON string representation of the object
print(CreateARecurringExpenseRequest.to_json())

# convert the object into a dict
create_a_recurring_expense_request_dict = create_a_recurring_expense_request_instance.to_dict()
# create an instance of CreateARecurringExpenseRequest from a dict
create_a_recurring_expense_request_from_dict = CreateARecurringExpenseRequest.from_dict(create_a_recurring_expense_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


