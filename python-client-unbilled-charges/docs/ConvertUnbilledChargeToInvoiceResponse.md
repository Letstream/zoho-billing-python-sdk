# ConvertUnbilledChargeToInvoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**invoice** | [**ConvertUnbilledChargeToInvoiceResponseInvoice**](ConvertUnbilledChargeToInvoiceResponseInvoice.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_unbilled_charges.models.convert_unbilled_charge_to_invoice_response import ConvertUnbilledChargeToInvoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertUnbilledChargeToInvoiceResponse from a JSON string
convert_unbilled_charge_to_invoice_response_instance = ConvertUnbilledChargeToInvoiceResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertUnbilledChargeToInvoiceResponse.to_json())

# convert the object into a dict
convert_unbilled_charge_to_invoice_response_dict = convert_unbilled_charge_to_invoice_response_instance.to_dict()
# create an instance of ConvertUnbilledChargeToInvoiceResponse from a dict
convert_unbilled_charge_to_invoice_response_from_dict = ConvertUnbilledChargeToInvoiceResponse.from_dict(convert_unbilled_charge_to_invoice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


