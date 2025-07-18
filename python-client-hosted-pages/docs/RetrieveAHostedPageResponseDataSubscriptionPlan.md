# RetrieveAHostedPageResponseDataSubscriptionPlan

Plan object for which the subscription is to be created/updated. This contains <code>plan_code</code>, <code>name</code>, <code>price</code>, <code>exclude_setup_fee</code>, <code>quantity</code>, <code>exclude_setup_fee</code>, <code>exclude_trial</code>, <code>billing_cycles</code> and <code>trial_days</code>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_code** | **str** | Plan code of the plan that is to be subscribed to the customer. | [optional] 
**name** | **str** | Name generated by concatenation of the product name and the selected plan. | [optional] 
**quantity** | **int** | Required quantity of the chosen plan. | [optional] 
**price** | **float** | Price of a plan for a particular subscription. If a value is provided here, the plan’s price for this subscription will be changed to the given value. If no value is provided, the plan’s price would be the same as what it was when it was created. | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**item_custom_fields** | [**List[ItemCustomFieldsInner]**](ItemCustomFieldsInner.md) | Custom fields for a item. | [optional] 
**discount** | **float** | Discount amount applied for the plan. | [optional] 
**total** | **float** | Total amount for the plan. | [optional] 
**setup_fee** | **float** | Setup fee for the plan. | [optional] 
**description** | **str** | Description of the plan exclusive to this subscription. This will be displayed in place of the plan name in invoices generated for this subscription. | [optional] 
**tax_id** | **str** | Unique ID of the tax or tax group that can be collected from the contact. Tax can be given only if &lt;code&gt;is_taxable&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_subscription_plan import RetrieveAHostedPageResponseDataSubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataSubscriptionPlan from a JSON string
retrieve_a_hosted_page_response_data_subscription_plan_instance = RetrieveAHostedPageResponseDataSubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataSubscriptionPlan.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_subscription_plan_dict = retrieve_a_hosted_page_response_data_subscription_plan_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataSubscriptionPlan from a dict
retrieve_a_hosted_page_response_data_subscription_plan_from_dict = RetrieveAHostedPageResponseDataSubscriptionPlan.from_dict(retrieve_a_hosted_page_response_data_subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


