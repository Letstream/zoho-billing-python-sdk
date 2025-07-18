# AddPaymentMethodForACustomerResponseHostedpage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostedpage_id** | **str** | Unique ID generated by the server. This is used to identify the generated hosted page. | [optional] 
**status** | **str** | Status of the hosted page generated. This can be &lt;code&gt;fresh&lt;/code&gt;, &lt;code&gt;read&lt;/code&gt;, &lt;code&gt;success&lt;/code&gt;, &lt;code&gt;failed&lt;/code&gt;, &lt;code&gt;cancelled&lt;/code&gt; or &lt;code&gt;force_cancelled&lt;/code&gt;. | [optional] 
**url** | **str** | The URL of the hosted page generated. | [optional] 
**action** | **object** |  | [optional] 
**expiring_time** | **str** | The time at which the hosted page will expire. | [optional] 
**created_time** | **str** | The time at which the hosted page was created. | [optional] 
**custom_fields** | [**List[BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner]**](BuyOneTimeAddonForASubscriptionResponseHostedpageCustomFieldsInner.md) | Additional fields for the Hosted pages. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.add_payment_method_for_a_customer_response_hostedpage import AddPaymentMethodForACustomerResponseHostedpage

# TODO update the JSON string below
json = "{}"
# create an instance of AddPaymentMethodForACustomerResponseHostedpage from a JSON string
add_payment_method_for_a_customer_response_hostedpage_instance = AddPaymentMethodForACustomerResponseHostedpage.from_json(json)
# print the JSON string representation of the object
print(AddPaymentMethodForACustomerResponseHostedpage.to_json())

# convert the object into a dict
add_payment_method_for_a_customer_response_hostedpage_dict = add_payment_method_for_a_customer_response_hostedpage_instance.to_dict()
# create an instance of AddPaymentMethodForACustomerResponseHostedpage from a dict
add_payment_method_for_a_customer_response_hostedpage_from_dict = AddPaymentMethodForACustomerResponseHostedpage.from_dict(add_payment_method_for_a_customer_response_hostedpage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


