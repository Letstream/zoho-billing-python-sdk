# CreateAnAddonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Unique string of your choice which lets you identify this addon. | 
**name** | **str** | Name of your choice to be displayed in the interface and invoices. | 
**unit_name** | **str** | A name of your choice to refer to one unit of the addon. | 
**pricing_scheme** | **object** | Pricing type of the addon can be changed and the values are &lt;code&gt;unit&lt;/code&gt;, &lt;code&gt;volume&lt;/code&gt;, &lt;code&gt;tier&lt;/code&gt; or &lt;code&gt;package&lt;/code&gt;. To know more about pricing schemes click &lt;a href&#x3D;\&quot;/billing/help/product-catalog/subscription-items/addons.html#pricing-schemes\&quot;&gt;here.&lt;/a&gt; | [optional] 
**price_brackets** | [**List[AddonResponsePriceBracketsInner]**](AddonResponsePriceBracketsInner.md) | Array of objects which contains the start quantity, end quantity and price | 
**type** | **str** | Indicates type of the addon. This could be either &lt;code&gt;recurring&lt;/code&gt; or &lt;code&gt;one_time&lt;/code&gt;. | [optional] [default to 'recurring']
**interval_unit** | **str** | The billing frequency of the addon only if type is recurring and the values can be &lt;code&gt;monthly&lt;/code&gt; or &lt;code&gt;yearly&lt;/code&gt;. | [optional] [default to 'monthly']
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldsInner]**](CustomFieldsInner.md) | Custom fields for a Addon. | [optional] 
**applicable_to_all_plans** | **bool** | If the addon is to be associated with all plans, applicable_to_all_plans is set to &lt;code&gt;true&lt;/code&gt;; otherwise, it is set to &lt;code&gt;false&lt;/code&gt;. | [optional] [default to True]
**plans** | [**List[CreateAnAddonRequestOneOfPlansInner]**](CreateAnAddonRequestOneOfPlansInner.md) | List of plans that the addon needs to be associated with. If an addon is to be associated with only two plans - \&quot;basic\&quot; and \&quot;professional\&quot;, then &lt;code&gt;applicable_to_all_plans&lt;/code&gt; is set to false. Only the plan codes of the plans that need to be associated with are required. | 
**product_id** | **str** | Product ID to which you want to associate this addon with. | 
**description** | **str** | Short description regarding the addon. | [optional] 
**store_markup_description** | **str** | Long Description regarding the plan. | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this addon. | [optional] [default to 'no tax will be associated']
**product_type** | **str** | Product type for UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services addon | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**item_tax_preferences** | [**List[ItemTaxPreferencesInner]**](ItemTaxPreferencesInner.md) | Tax preferenece for addon | [optional] 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 

## Example

```python
from ls_zoho_billing_addons.models.create_an_addon_request import CreateAnAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAnAddonRequest from a JSON string
create_an_addon_request_instance = CreateAnAddonRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAnAddonRequest.to_json())

# convert the object into a dict
create_an_addon_request_dict = create_an_addon_request_instance.to_dict()
# create an instance of CreateAnAddonRequest from a dict
create_an_addon_request_from_dict = CreateAnAddonRequest.from_dict(create_an_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


