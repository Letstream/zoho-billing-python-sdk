# CreateAnItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the item. &lt;code&gt;Maximum length of the name [100]&lt;/code&gt; | 
**rate** | **float** | Per unit price of an item. | 
**description** | **str** | Description for the item. &lt;code&gt;Maximum characters to be used for describing the item [2000]&lt;/code&gt; | [optional] 
**tax_id** | **str** | ID of the tax to be associated to the item. | [optional] 
**sku** | **str** | SKU or the Stock Keeping Unit value of an item, should be unique throughout the product | [optional] 
**product_type** | **str** | Specify the type of an item. It can be either &lt;code&gt; goods&lt;/code&gt; or &lt;code&gt; service&lt;/code&gt; | [optional] 
**is_taxable** | **bool** | Boolean to track the taxability of the item. | [optional] 
**tax_exemption_id** | **str** | ID of the tax exemption applied. Mandatory, if &lt;code&gt;is_taxable&lt;/code&gt; is false. | [optional] 
**hsn_or_sac** | **str** | HSN Code | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**item_tax_preferences** | [**List[ItemTaxPreferencesInner]**](ItemTaxPreferencesInner.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for an item. | [optional] 

## Example

```python
from ls_zoho_billing_items.models.create_an_item_request import CreateAnItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnItemRequest from a JSON string
create_an_item_request_instance = CreateAnItemRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnItemRequest.to_json())

# convert the object into a dict
create_an_item_request_dict = create_an_item_request_instance.to_dict()
# create an instance of CreateAnItemRequest from a dict
create_an_item_request_from_dict = CreateAnItemRequest.from_dict(create_an_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


