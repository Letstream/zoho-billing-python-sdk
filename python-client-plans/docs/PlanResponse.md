# PlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | Unique string of your choice which lets you identify this plan. | [optional] 
**name** | **str** | Name of your choice to be displayed in the interface and invoices. | [optional] 
**description** | **str** | Short description regarding the plan. | [optional] 
**store_markup_description** | **str** | Long Description regarding the plan. | [optional] 
**status** | **str** | Status of the plan. It can be either &lt;code&gt; active &lt;/code&gt;  or &lt;code&gt; inactive &lt;/code&gt;. | [optional] 
**product_id** | **str** | Product ID to which you want to associate this plan with. | [optional] 
**account_id** | **str** | Account ID which the plan is associated. | [optional] 
**account_name** | **str** | Account name which the plan is associated. | [optional] 
**tax_id** | **str** | Tax ID to which you would like to associate with this plan. | [optional] [default to 'no tax will be associated']
**trial_period** | **int** | Number of free trial days that can be granted when a customer is subscribed to this plan. | [optional] [default to 0]
**setup_fee** | **float** | This indicates a one-time fee charged upfront while creating a subscription for this plan. | [optional] [default to 0]
**setup_fee_account_id** | **str** | Setup Fee Account ID which the setup fee of the plan is associated. | [optional] 
**setup_fee_account_name** | **str** | Setup Fee Account Name which the setup fee of the plan is associated. | [optional] 
**tags** | [**List[PlanResponseTagsInner]**](PlanResponseTagsInner.md) |  | [optional] 
**custom_fields** | [**List[PlanResponseCustomFieldsInner]**](PlanResponseCustomFieldsInner.md) | Custom fields for a Plan. | [optional] 
**recurring_price** | **float** | The customer is charged an amount over an interval for the subscription. | [optional] 
**unit** | **str** | A name of your choice to refer to one unit of the plan. | [optional] 
**interval** | **int** | Indicates the number of intervals between each billing. If interval&#x3D;2, the customer would be billed every two months or years depending on the value for interval_unit. | [optional] 
**interval_unit** | **str** | The values can be either &lt;code&gt;months&lt;/code&gt; or &lt;code&gt;years&lt;/code&gt;. For interval&#x3D;2 and interval_unit&#x3D;months, the customer is billed every two months. | [optional] [default to 'months']
**billing_cycles** | **int** | Number of cycles this plan&#39;s subscription should run for. If billing_cycles&#x3D;12, the subscription would expire after 12 cycles. If billing_cycles&#x3D;-1, the subscription would run until it is cancelled. If interval&#x3D;2, interval_unit&#x3D;months and billing_cycles&#x3D;12, the customer would be billed every 2 months and this would go on for 12 times. | [optional] [default to -1]
**product_type** | **str** | Product type for India/UK Edition. | [optional] 
**hsn_or_sac** | **str** | HSN or SAC code for Goods/Services plan | [optional] 
**sat_item_key_code** | **str** | Add SAT Item Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**unitkey_code** | **str** | Add SAT Unit Key Code for your goods/services. Download the &lt;a href&#x3D; http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/catCFDI_V_4_07122022.xls  &gt;CFDI Catalogs.&lt;/a&gt; | [optional] 
**item_tax_preferences** | [**List[ItemTaxPreferencesInner]**](ItemTaxPreferencesInner.md) | Tax preferenece for plan | [optional] 
**addons** | [**List[PlanResponseAddonsInner]**](PlanResponseAddonsInner.md) | List of addons that the plan is associated with. It holds the list of objects with &lt;code&gt;addon_code&lt;/code&gt; and &lt;code&gt;name&lt;/code&gt; as properties. | [optional] 
**url** | **str** | Unique url of the plan. | [optional] 
**created_time** | **str** | The time at which the plan was created. | [optional] 
**updated_time** | **str** | The time at which the plan details were last updated. | [optional] 

## Example

```python
from ls_zoho_billing_plans.models.plan_response import PlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponse from a JSON string
plan_response_instance = PlanResponse.from_json(json)
# print the JSON string representation of the object
print(PlanResponse.to_json())

# convert the object into a dict
plan_response_dict = plan_response_instance.to_dict()
# create an instance of PlanResponse from a dict
plan_response_from_dict = PlanResponse.from_dict(plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


