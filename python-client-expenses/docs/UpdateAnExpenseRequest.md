# UpdateAnExpenseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the expense account. | 
**var_date** | **str** | Date of the expense | [optional] 
**amount** | **float** | Total expense value | 
**tax_id** | **str** | Tax ID applied | [optional] 
**source_of_supply** | **str** | Place from where the goods/services are supplied. (If not given, &lt;code&gt;place of contact&lt;/code&gt; given for the contact will be taken) | [optional] 
**destination_of_supply** | **str** | Place where the goods/services are supplied to. (If not given, organisation&#39;s home state will be taken) | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**gst_no** | **str** | 15 digit GST identification number of the vendor. | [optional] 
**reverse_charge_tax_id** | **str** | ID of the reverse charge tax | [optional] 
**line_items** | [**List[LineItemsInner]**](LineItemsInner.md) |  | [optional] 
**taxes** | [**List[TaxesInner]**](TaxesInner.md) |  | [optional] 
**is_inclusive_tax** | **bool** | Check if amount is inclusive of tax | [optional] 
**is_billable** | **bool** | Check if an expense is billable | [optional] 
**reference_number** | **str** | Reference number of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**description** | **str** | Description of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for an expense. | [optional] 
**customer_id** | **str** | ID of the expense account. | [optional] 
**currency_id** | **str** | Unique ID of the currency | [optional] 
**exchange_rate** | **float** | Foreign currency exchange rate | [optional] 
**project_id** | **str** | ID of the project associated with the customer. | [optional] 
**mileage_type** | **str** | Milage expense type | [optional] 
**vat_treatment** | **str** | VAT treatment for the expense. VAT treatment denotes the location of the vendor, if the vendor resides in UK then the VAT treatment is &lt;code&gt;uk&lt;/code&gt;. If the vendor is in an EU country &amp; VAT registered, you are resides in Northen Ireland and purchasing Goods then his VAT treatment is &lt;code&gt;eu_vat_registered&lt;/code&gt; and if he resides outside the UK then his VAT treatment is &lt;code&gt;overseas&lt;/code&gt; (For Pre Brexit, this can be split as &lt;code&gt;eu_vat_registered&lt;/code&gt;, &lt;code&gt;eu_vat_not_registered&lt;/code&gt; and &lt;code&gt;non_eu&lt;/code&gt;). | [optional] 
**product_type** | **str** | Type of the expense. This denotes whether the expense is to be treated as a goods or service purchase. Allowed Values: &lt;code&gt;goods&lt;/code&gt; and &lt;code&gt;service&lt;/code&gt;. | [optional] 
**acquisition_vat_id** | **str** | This is the ID of the tax applied in case this is an EU - goods expense and acquisition VAT needs to be reported. | [optional] 
**reverse_charge_vat_id** | **str** | This is the ID of the tax applied in case this is a non UK - service expense and reverse charge VAT needs to be reported. | [optional] 
**start_reading** | **float** | Start reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 
**end_reading** | **float** | End reading of odometer when creating a mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;odometer&lt;/code&gt;. | [optional] 
**distance** | **str** | Distance travelled for a particular mileage expense where &lt;code&gt;mileage_type&lt;/code&gt; is &lt;code&gt;manual&lt;/code&gt; | [optional] 
**mileage_unit** | **str** | Unit of the distance travelled. Allowed Values: &lt;code&gt;km&lt;/code&gt; and &lt;code&gt;mile&lt;/code&gt; | [optional] 
**mileage_rate** | **float** | Mileage rate for a particular mileage expense. | [optional] 
**employee_id** | **str** | ID of the employee who has submitted this mileage expense. | [optional] 
**vehicle_type** | **str** | Vehicle type for a particular mileage expense. Allowed Values: &lt;code&gt;car&lt;/code&gt;, &lt;code&gt;van&lt;/code&gt;, &lt;code&gt;motorcycle&lt;/code&gt; and &lt;code&gt;bike&lt;/code&gt; | [optional] 
**can_reclaim_vat_on_mileage** | **str** | To specify if tax can be reclaimed for this mileage expense. | [optional] 
**fuel_type** | **str** | Fuel type for a particular mileage expense. Allowed Values: &lt;code&gt;petrol&lt;/code&gt;, &lt;code&gt;lpg&lt;/code&gt; and &lt;code&gt;diesel&lt;/code&gt; | [optional] 
**engine_capacity_range** | **str** | Engine capacity range for a particular mileage expense. Allowed Values: &lt;code&gt;less_than_1400cc&lt;/code&gt;, &lt;code&gt;between_1400cc_and_1600cc&lt;/code&gt;, &lt;code&gt;between_1600cc_and_2000cc&lt;/code&gt; and &lt;code&gt;more_than_2000cc&lt;/code&gt; | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.update_an_expense_request import UpdateAnExpenseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnExpenseRequest from a JSON string
update_an_expense_request_instance = UpdateAnExpenseRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAnExpenseRequest.to_json())

# convert the object into a dict
update_an_expense_request_dict = update_an_expense_request_instance.to_dict()
# create an instance of UpdateAnExpenseRequest from a dict
update_an_expense_request_from_dict = UpdateAnExpenseRequest.from_dict(update_an_expense_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


