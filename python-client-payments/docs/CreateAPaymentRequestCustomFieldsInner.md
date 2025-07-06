# CreateAPaymentRequestCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Label of the custom field. | [optional] 
**value** | **str** | Value of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.create_a_payment_request_custom_fields_inner import CreateAPaymentRequestCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAPaymentRequestCustomFieldsInner from a JSON string
create_a_payment_request_custom_fields_inner_instance = CreateAPaymentRequestCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(CreateAPaymentRequestCustomFieldsInner.to_json())

# convert the object into a dict
create_a_payment_request_custom_fields_inner_dict = create_a_payment_request_custom_fields_inner_instance.to_dict()
# create an instance of CreateAPaymentRequestCustomFieldsInner from a dict
create_a_payment_request_custom_fields_inner_from_dict = CreateAPaymentRequestCustomFieldsInner.from_dict(create_a_payment_request_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


