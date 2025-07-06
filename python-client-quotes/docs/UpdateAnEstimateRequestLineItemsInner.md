# UpdateAnEstimateRequestLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** | Unique ID of the item. | 
**name** | **str** | The name of the line item | [optional] 
**description** | **str** | The description of the line items | [optional] 
**item_order** | **int** | The order of the line item_order | [optional] 
**rate** | **float** | Rate of the line item. | 
**quantity** | **float** | The quantity of line item | 
**product_type** | **str** | Enter goods/services | [optional] 
**hsn_or_sac** | **str** | Add HSN/SAC code for your goods/services | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unit** | **str** | Unit of measuring the line item e.g. kgs, Nos. | [optional] 
**discount_amount** | **float** | The discount amount on the line item | [optional] 
**discount** | **float** | Discount applied to the invoice. It can be either in % or in amount. e.g. 12.5% or 190. | [optional] 
**tax_id** | **str** | ID of the tax or tax group applied to the quote | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**tax_exemption_id** | **str** | ID of the tax exemption. | [optional] 
**avatax_tax_code** | **str** | A tax code is a unique label used to group Items (products, services, or charges) together. &lt;code&gt;Maximum length [25]&lt;/code&gt; | [optional] 
**avatax_use_code** | **str** | Used to group like customers for exemption purposes. It is a custom value that links customers to a tax rule. Select from Avalara [standard codes][1] or enter a custom code. | [optional] 
**tax_name** | **str** | The name of the tax | [optional] 
**tax_type** | **str** | The type of the tax | [optional] 
**tax_percentage** | **float** | The  percentage of tax levied | [optional] 
**item_total** | **float** | The total amount of the line items | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.update_an_estimate_request_line_items_inner import UpdateAnEstimateRequestLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAnEstimateRequestLineItemsInner from a JSON string
update_an_estimate_request_line_items_inner_instance = UpdateAnEstimateRequestLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateAnEstimateRequestLineItemsInner.to_json())

# convert the object into a dict
update_an_estimate_request_line_items_inner_dict = update_an_estimate_request_line_items_inner_instance.to_dict()
# create an instance of UpdateAnEstimateRequestLineItemsInner from a dict
update_an_estimate_request_line_items_inner_from_dict = UpdateAnEstimateRequestLineItemsInner.from_dict(update_an_estimate_request_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


