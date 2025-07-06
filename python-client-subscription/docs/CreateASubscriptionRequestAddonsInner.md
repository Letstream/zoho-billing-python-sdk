# CreateASubscriptionRequestAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_code** | **str** | Addon code of the addon. | 
**addon_description** | **str** | Description of the addon exclusive to this subscription. This will be displayed in place of the addon name in invoices generated for this subscription. | [optional] 
**price** | **float** | Price of a plan for a particular subscription. If a value is provided here, the plan’s price for this subscription will be changed to the given value. If no value is provided, the plan’s price would be the same as what it was when it was created. | [optional] 
**quantity** | **object** | Required quantity of the chosen addon. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the addon. &lt;code&gt;tax_id&lt;/code&gt; must be empty for applying tax Exemption. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**tds_tax_id** | **str** | ID of the TDS tax. | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 

## Example

```python
from ls_zoho_billing_subscription.models.create_a_subscription_request_addons_inner import CreateASubscriptionRequestAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateASubscriptionRequestAddonsInner from a JSON string
create_a_subscription_request_addons_inner_instance = CreateASubscriptionRequestAddonsInner.from_json(json)
# print the JSON string representation of the object
print(CreateASubscriptionRequestAddonsInner.to_json())

# convert the object into a dict
create_a_subscription_request_addons_inner_dict = create_a_subscription_request_addons_inner_instance.to_dict()
# create an instance of CreateASubscriptionRequestAddonsInner from a dict
create_a_subscription_request_addons_inner_from_dict = CreateASubscriptionRequestAddonsInner.from_dict(create_a_subscription_request_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


