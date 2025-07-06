# ExpenseResponse

A cost for the company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_id** | **str** | Unique ID of the expense | [optional] 
**transaction_id** | **str** | Unique ID of the transaction | [optional] 
**transaction_type** | **str** | Type of the transaction | [optional] 
**expense_item_id** | **str** | ID of the expense item/component. | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the vendor. | [optional] 
**gst_treatment** | **str** | Choose whether the contact is GST registered/unregistered/consumer/overseas. Allowed values are &lt;code&gt; business_gst &lt;/code&gt; , &lt;code&gt; business_none &lt;/code&gt; , &lt;code&gt; overseas &lt;/code&gt; , &lt;code&gt; consumer &lt;/code&gt;. | [optional] 
**destination_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, organisation&#39;s home state will be taken) | [optional] 
**destination_of_supply_state** | **str** | State to where goods/services are supplied | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**source_of_supply** | **str** | Place from where the goods/services are supplied. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**paid_through_account_name** | **str** | Enter the name of the paid through account. | [optional] 
**vat_reg_no** | **str** | Enter VAT registration number. | [optional] 
**reverse_charge_tax_id** | **str** | ID of the reverse charge tax | [optional] 
**reverse_charge_tax_name** | **str** | Enter name of the reverse charge tax | [optional] 
**reverse_charge_tax_percentage** | **float** | Enter percentage of the reverse charge tax | [optional] 
**reverse_charge_tax_amount** | **int** | Enter amount of the reverse charge tax | [optional] 
**tax_amount** | **float** | total expense amount | [optional] 
**is_itemized_expense** | **bool** |  | [optional] 
**is_pre_gst** | **str** | Applicable for transactions that fall before july 1, 2017 | [optional] 
**trip_id** | **str** | Enter trip ID | [optional] 
**trip_number** | **str** | Enter trip number | [optional] 
**reverse_charge_vat_total** | **float** | Enter total of the reverse charge vat tax. | [optional] 
**acquisition_vat_total** | **float** | Enter acquisition vat total. | [optional] 
**acquisition_vat_summary** | [**List[AcquisitionVatSummaryInner]**](AcquisitionVatSummaryInner.md) |  | [optional] 
**reverse_charge_vat_summary** | [**List[AcquisitionVatSummaryInner]**](AcquisitionVatSummaryInner.md) |  | [optional] 
**account_id** | **str** | ID of the expense account. | [optional] 
**account_name** | **str** | Name of the expense account in which that expense is recorded | [optional] 
**var_date** | **str** | Date of the expense | [optional] 
**tax_id** | **str** | Tax ID applied | [optional] 
**tax_name** | **str** | Name of the tax levied | [optional] 
**tax_percentage** | **float** | Percentage of tax charged | [optional] 
**currency_id** | **str** | Unique ID of the currency | [optional] 
**currency_code** | **str** | Code of the currency | [optional] 
**exchange_rate** | **float** | Foreign currency exchange rate | [optional] 
**sub_total** | **float** | Sub-total of the expense amount | [optional] 
**total** | **float** | Total value of expense | [optional] 
**bcy_total** | **float** | Total value of expense in Base currency | [optional] 
**amount** | **float** | Total expense value | [optional] 
**is_inclusive_tax** | **bool** | Check if amount is inclusive of tax | [optional] 
**reference_number** | **str** | Reference number of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**description** | **str** | Description of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**is_billable** | **bool** | Check if an expense is billable | [optional] 
**is_personal** | **bool** | Check if the expense os personal | [optional] 
**customer_id** | **str** | ID of the expense account. | [optional] 
**customer_name** | **str** | Name of the Customer for whom expense is raised. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**expense_receipt_name** | **str** | Name of the expense receipt | [optional] 
**expense_receipt_type** | **str** | Type of the expense receipt | [optional] 
**last_modified_time** | **str** | Date of last modification to the expense | [optional] 
**status** | **str** | Expense status | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for an expense. | [optional] 
**invoice_id** | **str** | ID of the invoice associated | [optional] 
**invoice_number** | **str** | Serial Number of the invoice attached | [optional] 
**project_id** | **str** | ID of the project associated with the customer. | [optional] 
**project_name** | **str** | Name of the project in question | [optional] 
**mileage_rate** | **float** | Mileage rate for a particular mileage expense. | [optional] 
**mileage_type** | **str** | Milage expense type | [optional] 
**expense_type** | **str** | Type of the expense | [optional] 
**start_reading** | **float** | Start reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 
**end_reading** | **float** | End reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.expense_response import ExpenseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseResponse from a JSON string
expense_response_instance = ExpenseResponse.from_json(json)
# print the JSON string representation of the object
print(ExpenseResponse.to_json())

# convert the object into a dict
expense_response_dict = expense_response_instance.to_dict()
# create an instance of ExpenseResponse from a dict
expense_response_from_dict = ExpenseResponse.from_dict(expense_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


