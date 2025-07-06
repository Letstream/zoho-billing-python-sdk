# LineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **str** | ID of the items in the expense | [optional] 
**account_id** | **str** | ID of the expense account. | [optional] 
**description** | **str** | Description of the expense. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**amount** | **float** | Total expense value | [optional] 
**tax_id** | **str** | Tax ID applied | [optional] 
**item_order** | **str** | Order of the items | [optional] 
**product_type** | **str** | Type of the expense. This denotes whether the expense is to be treated as a goods or service purchase. Allowed Values: &lt;code&gt;goods&lt;/code&gt; and &lt;code&gt;service&lt;/code&gt;. | [optional] 
**acquisition_vat_id** | **str** | This is the ID of the tax applied in case this is an EU - goods expense and acquisition VAT needs to be reported. | [optional] 
**reverse_charge_vat_id** | **str** | This is the ID of the tax applied in case this is a non UK - service expense and reverse charge VAT needs to be reported. | [optional] 
**reverse_charge_tax_id** | **str** | ID of the reverse charge tax | [optional] 
**tax_exemption_code** | **str** | Enter tax exemption code | [optional] 
**tax_exemption_id** | **str** | Enter tax exemption ID | [optional] 

## Example

```python
from ls_zoho_billing_expenses.models.line_items_inner import LineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemsInner from a JSON string
line_items_inner_instance = LineItemsInner.from_json(json)
# print the JSON string representation of the object
print(LineItemsInner.to_json())

# convert the object into a dict
line_items_inner_dict = line_items_inner_instance.to_dict()
# create an instance of LineItemsInner from a dict
line_items_inner_from_dict = LineItemsInner.from_dict(line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


