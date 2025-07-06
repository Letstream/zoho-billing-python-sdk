# UpdateAnInvoiceRequestInvoiceItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The ID of the item included in the invoice. | 
**project_id** | **str** | Unique ID of the projet associated to an invoice | [optional] 
**time_entry_ids** | **List[str]** | Unique ID&#39;s of all the time entries associated to the linked project | [optional] 
**expense_id** | **str** | Unique ID of the expenses associated | [optional] 
**name** | **str** | Name of the item included in the invoice. | [optional] 
**product_type** | **str** | Product type for UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**description** | **str** | Small description of the payment made for the invoice. | [optional] 
**item_order** | **int** | The order of the line item_order | [optional] 
**price** | **str** | Price of the item included in the invoice. | [optional] 
**quantity** | **int** | Quantity of the item included in the invoice. | [optional] 
**unit** | **str** | Unit of the line item e.g. kgs, Nos. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. &lt;code&gt;Maximum length [100]&lt;/code&gt; | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this plan. | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**tax_exemption_id** | **str** | Unique Tax Exemption ID if you dont want to associate a tax to the plan. | [optional] 
**avatax_use_code** | **str** | Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**avatax_exempt_no** | **str** | Exemption certificate number of the customer. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**tax_name** | **str** | The name of the tax | [optional] 
**tax_type** | **str** | The type of the tax | [optional] 
**tax_percentage** | **float** | The  percentage of tax levied | [optional] 
**item_total** | **int** | Cost of an item included in the invoice. This would be the product of quantity of the item included and the price of that item. | [optional] 

## Example

```python
from ls_zoho_billing_invoices.models.update_an_invoice_request_invoice_items_inner import UpdateAnInvoiceRequestInvoiceItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnInvoiceRequestInvoiceItemsInner from a JSON string
update_an_invoice_request_invoice_items_inner_instance = UpdateAnInvoiceRequestInvoiceItemsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAnInvoiceRequestInvoiceItemsInner.to_json())

# convert the object into a dict
update_an_invoice_request_invoice_items_inner_dict = update_an_invoice_request_invoice_items_inner_instance.to_dict()
# create an instance of UpdateAnInvoiceRequestInvoiceItemsInner from a dict
update_an_invoice_request_invoice_items_inner_from_dict = UpdateAnInvoiceRequestInvoiceItemsInner.from_dict(update_an_invoice_request_invoice_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


