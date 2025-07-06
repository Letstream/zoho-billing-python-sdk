# RetrieveAHostedPageResponseDataInvoiceCouponInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_code** | **str** | The coupon code of the coupon which is to be applied to the subscription. | [optional] 
**coupon_name** | **str** | Name of the coupon applied to the subscription. | [optional] 
**discount_amount** | **float** | The discount amount included in an invoice on applying a coupon. | [optional] 

## Example

```python
from ls_zoho_billing_hosted_pages.models.retrieve_a_hosted_page_response_data_invoice_coupon_inner import RetrieveAHostedPageResponseDataInvoiceCouponInner

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveAHostedPageResponseDataInvoiceCouponInner from a JSON string
retrieve_a_hosted_page_response_data_invoice_coupon_inner_instance = RetrieveAHostedPageResponseDataInvoiceCouponInner.from_json(json)
# print the JSON string representation of the object
print(RetrieveAHostedPageResponseDataInvoiceCouponInner.to_json())

# convert the object into a dict
retrieve_a_hosted_page_response_data_invoice_coupon_inner_dict = retrieve_a_hosted_page_response_data_invoice_coupon_inner_instance.to_dict()
# create an instance of RetrieveAHostedPageResponseDataInvoiceCouponInner from a dict
retrieve_a_hosted_page_response_data_invoice_coupon_inner_from_dict = RetrieveAHostedPageResponseDataInvoiceCouponInner.from_dict(retrieve_a_hosted_page_response_data_invoice_coupon_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


