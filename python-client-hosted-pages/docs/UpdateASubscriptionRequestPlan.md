# UpdateASubscriptionRequestPlan

Plan object for which the subscription is to be created/updated. This contains <code>plan_code</code>, <code>name</code>, <code>price</code>, <code>exclude_setup_fee</code>, <code>quantity</code>, <code>exclude_setup_fee</code>, <code>exclude_trial</code>, <code>billing_cycles</code> and <code>trial_days</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | Plan code of the plan that is to be subscribed to the customer. | 
**plan_description** | **str** | Description of the plan exclusive to this subscription. This will be displayed in place of the plan name in invoices generated for this subscription. | [optional] 
**price** | **float** | Price of a plan for a particular subscription. If a value is provided here, the plan’s price for this subscription will be changed to the given value. If no value is provided, the plan’s price would be the same as what it was when it was created. | [optional] 
**setup_fee** | **float** | Setup fee for the plan. | [optional] 
**quantity** | **int** | Required quantity of the chosen plan. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**tax_id** | **object** | Unique ID of Tax or Tax Group that must be associated with the plan. &lt;code&gt;tax_id&lt;/code&gt; must be empty for applying tax Exemption. | 
**tax_exemption_id** | **str** | Unique ID of the tax exemption. | [optional] 
**tax_exemption_code** | **str** | Unique code of the tax exemption. | [optional] 
**setup_fee_tax_exemption_id** | **str** | Unique Tax Exemption ID that must be applied to setup fee. | [optional] 
**setup_fee_tax_exemption_code** | **str** | Unique code of the tax exemption that must be applied to setup fee. | [optional] 
**exclude_trial** | **bool** | This is set to true if the respective plan&#39;s trial period needs to be excluded for this subscription. | [optional] 
**exclude_setup_fee** | **bool** | This is set to true if the respective plan&#39;s setup fee needs to be excluded for this subscription. | [optional] 
**billing_cycles** | **int** | &lt;code&gt;billing_cycles&lt;/code&gt; specified at the time of creation of the plan would be the default value. If this needs to be overridden for this particular subscription, a value can be provided here. | [optional] 
**trial_days** | **int** | Number of free trial days granted to a customer subscribed to this plan. Trial days for the subscription mentioned here will override the number of trial days provided at the time plan creation. This will be applicable even if exclude_trial&#x3D;true. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.update_a_subscription_request_plan import UpdateASubscriptionRequestPlan

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateASubscriptionRequestPlan from a JSON string
update_a_subscription_request_plan_instance = UpdateASubscriptionRequestPlan.from_json(json)
# print the JSON string representation of the object
print(UpdateASubscriptionRequestPlan.to_json())

# convert the object into a dict
update_a_subscription_request_plan_dict = update_a_subscription_request_plan_instance.to_dict()
# create an instance of UpdateASubscriptionRequestPlan from a dict
update_a_subscription_request_plan_from_dict = UpdateASubscriptionRequestPlan.from_dict(update_a_subscription_request_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


