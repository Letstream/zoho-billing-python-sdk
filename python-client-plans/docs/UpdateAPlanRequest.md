# UpdateAPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | Unique string of your choice which lets you identify this plan. | 
**name** | **str** | Name of your choice to be displayed in the interface and invoices. | 
**recurring_price** | **float** | The customer is charged an amount over an interval for the subscription. | 
**unit** | **str** | A name of your choice to refer to one unit of the plan. | [optional] 
**interval** | **int** | Indicates the number of intervals between each billing. If interval&#x3D;2, the customer would be billed every two months or years depending on the value for interval_unit. | 
**interval_unit** | **str** | The values can be either &lt;code&gt;months&lt;/code&gt; or &lt;code&gt;years&lt;/code&gt;. For interval&#x3D;2 and interval_unit&#x3D;months, the customer is billed every two months. | [optional] [default to 'months']
**billing_cycles** | **int** | Number of cycles this plan&#39;s subscription should run for. If billing_cycles&#x3D;12, the subscription would expire after 12 cycles. If billing_cycles&#x3D;-1, the subscription would run until it is cancelled. If interval&#x3D;2, interval_unit&#x3D;months and billing_cycles&#x3D;12, the customer would be billed every 2 months and this would go on for 12 times. | [optional] [default to -1]
**trial_period** | **int** | Number of free trial days that can be granted when a customer is subscribed to this plan. | [optional] [default to 0]
**setup_fee** | **float** | This indicates a one-time fee charged upfront while creating a subscription for this plan. | [optional] [default to 0]
**setup_fee_account_id** | **str** | Setup Fee Account ID which the setup fee of the plan is associated. | [optional] 
**tags** | [**List[UpdateAPlanRequestTagsInner]**](UpdateAPlanRequestTagsInner.md) |  | [optional] 
**custom_fields** | [**List[UpdateAPlanRequestCustomFieldsInner]**](UpdateAPlanRequestCustomFieldsInner.md) | Custom fields for a Plan. | [optional] 
**addons** | [**List[AddonsInner]**](AddonsInner.md) | List of addons that the plan is associated with. It holds the list of objects with &lt;code&gt;addon_code&lt;/code&gt; and &lt;code&gt;name&lt;/code&gt; as properties. | [optional] 
**product_type** | **str** | Product type for India/UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services plan | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**item_tax_preferences** | [**List[ItemTaxPreferencesInner]**](ItemTaxPreferencesInner.md) | Tax preferenece for plan | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this plan. | [optional] [default to 'no tax will be associated']
**is_taxable** | **str** | Set to true if plan must be tax inclusive. | [optional] 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**description** | **str** | Short description regarding the plan. | [optional] 
**store_markup_description** | **str** | Long Description regarding the plan. | [optional] 
**can_charge_setup_fee_immediately** | **bool** | Set this value to \&quot;true\&quot;, if you want to enable upfront setup fees charges while creating or updating subscriptions with this plan. | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.update_a_plan_request import UpdateAPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAPlanRequest from a JSON string
update_a_plan_request_instance = UpdateAPlanRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAPlanRequest.to_json())

# convert the object into a dict
update_a_plan_request_dict = update_a_plan_request_instance.to_dict()
# create an instance of UpdateAPlanRequest from a dict
update_a_plan_request_from_dict = UpdateAPlanRequest.from_dict(update_a_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


