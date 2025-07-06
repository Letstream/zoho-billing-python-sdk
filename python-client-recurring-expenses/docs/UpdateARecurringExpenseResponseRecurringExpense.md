# UpdateARecurringExpenseResponseRecurringExpense


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Unique ID of an account | [optional] 
**recurrence_name** | **str** | Name of the Recurring Expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**start_date** | **str** | Start date of the recurring expense. Expenses will not be generated for dates prior to the current date. &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt;. | [optional] 
**end_date** | **str** | Date on which recurring expense has to expire. Can be left as empty to run forever. &lt;code&gt;Format [yyyy-mm-dd]&lt;/code&gt;. | [optional] 
**is_pre_gst** | **bool** | Applicable for transactions that fall before july 1, 2017 | [optional] 
**source_of_supply** | **str** | Place from where the goods/services are supplied. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**destination_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, organisation&#39;s home state will be taken) | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the vendor. | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**destination_of_supply_state** | **str** | Place to where the goods/services are supplied | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**vat_treatment** | **str** | VAT treatment for the expense. VAT treatment denotes the location of the vendor, if the vendor resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;.If the vendor is in an EU country &amp; VAT registered, you are resides in Northen Ireland and purchasing Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt; and if he resides outside the EU then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt;(For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**reverse_charge_tax_id** | **str** | Enter reverse charge tax ID | [optional] 
**reverse_charge_tax_name** | **str** | Enter reverse charge tax name | [optional] 
**reverse_charge_tax_percentage** | **float** | Tax percentage of the reverse charge | [optional] 
**reverse_charge_tax_amount** | **float** | Tax amount of the reverse charge | [optional] 
**is_reverse_charge_applied** | **bool** | Applicable for transactions where you pay reverse charge | [optional] 
**acquisition_vat_total** | **float** | Enter the total acquisition vat. | [optional] 
**reverse_charge_vat_total** | **float** | Enter the total of the reverse charge vat. | [optional] 
**acquisition_vat_summary** | [**List[AcquisitionVatSummaryInner]**](AcquisitionVatSummaryInner.md) | Summary of the VAT Acquistion | [optional] 
**reverse_charge_vat_summary** | [**List[AcquisitionVatSummaryInner]**](AcquisitionVatSummaryInner.md) | Summary of the Reverse Charge | [optional] 
**recurrence_frequency** | **str** | Frequency of the recurrance | [optional] 
**repeat_every** | **str** | The cycle of recurrance | [optional] 
**amount** | **str** | Recurring Expense amount. | [optional] 
**total** | **float** | Total expense | [optional] 
**sub_total** | **float** | Sub total of the expenses | [optional] 
**bcy_total** | **float** | Total in base currency | [optional] 
**product_type** | **str** | Type of the expense. This denotes whether the expense is to be treated as a goods or service purchase. Allowed Values: &lt;code&gt;goods&lt;/code&gt; and &lt;code&gt;service&lt;/code&gt;. | [optional] 
**acquisition_vat_id** | **str** | This is the ID of the tax applied in case this is an EU - goods expense and acquisition VAT needs to be reported. | [optional] 
**reverse_charge_vat_id** | **str** | This is the ID of the tax applied in case this is a non UK - service expense and reverse charge VAT needs to be reported. | [optional] 
**tax_id** | **str** | Unique ID for the tax | [optional] 
**tax_name** | **str** | Name of the tax | [optional] 
**tax_percentage** | **float** | Percentage of tax levied | [optional] 
**created_time** | **str** | Time expense was created | [optional] 
**last_modified_time** | **str** | Time the expense was last modified | [optional] 
**is_inclusive_tax** | **bool** | To check if the total is inclusive of tax | [optional] 
**is_billable** | **bool** | To check if the expense is billable | [optional] 
**customer_id** | **str** | Search expenses by customer id. | [optional] 
**currency_id** | **str** | Unique ID of the currency used | [optional] 
**exchange_rate** | **float** | Foreign exchange rate | [optional] 
**project_id** | **str** | Unique ID of the tax applied | [optional] 
**project_name** | **str** | Name of the project being billed | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for a recurring-expense. | [optional] 
**line_item** | [**RecurringExpenseResponseLineItem**](RecurringExpenseResponseLineItem.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_recurring_expenses.models.update_a_recurring_expense_response_recurring_expense import UpdateARecurringExpenseResponseRecurringExpense

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateARecurringExpenseResponseRecurringExpense from a JSON string
update_a_recurring_expense_response_recurring_expense_instance = UpdateARecurringExpenseResponseRecurringExpense.from_json(json)
# print the JSON string representation of the object
print(UpdateARecurringExpenseResponseRecurringExpense.to_json())

# convert the object into a dict
update_a_recurring_expense_response_recurring_expense_dict = update_a_recurring_expense_response_recurring_expense_instance.to_dict()
# create an instance of UpdateARecurringExpenseResponseRecurringExpense from a dict
update_a_recurring_expense_response_recurring_expense_from_dict = UpdateARecurringExpenseResponseRecurringExpense.from_dict(update_a_recurring_expense_response_recurring_expense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


