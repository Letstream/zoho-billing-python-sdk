# PaymentResponseCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the custom field. It can hold any value from 1 to 10. | [optional] 
**value** | **str** | Value of the custom field. | [optional] 
**label** | **str** | Label of the custom field. | [optional] 
**data_type** | **str** | Data type of the custom field. | [optional] 

## Example

```python
from ls_zoho_billing_payments.models.payment_response_custom_fields_inner import PaymentResponseCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentResponseCustomFieldsInner from a JSON string
payment_response_custom_fields_inner_instance = PaymentResponseCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(PaymentResponseCustomFieldsInner.to_json())

# convert the object into a dict
payment_response_custom_fields_inner_dict = payment_response_custom_fields_inner_instance.to_dict()
# create an instance of PaymentResponseCustomFieldsInner from a dict
payment_response_custom_fields_inner_from_dict = PaymentResponseCustomFieldsInner.from_dict(payment_response_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


