# ListEstimatesResponseEstimatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimate_id** | **str** | The  unique id of a particular quote | [optional] 
**customer_name** | **str** | Name of the Customer to whom the quote is sent. | [optional] 
**customer_id** | **str** | Customer ID on the quote. | [optional] 
**status** | **str** | Status of the quote. Allowed Values&lt;code&gt;draft&lt;/code&gt;, &lt;code&gt;sent&lt;/code&gt;,&lt;code&gt; invoiced &lt;/code&gt;, &lt;code&gt;accepted&lt;/code&gt;, &lt;code&gt;declined&lt;/code&gt; and &lt;code&gt;expired&lt;/code&gt; | [optional] 
**estimate_number** | **str** | quote Serial number. | [optional] 
**reference_number** | **str** | Transaction reference number. | [optional] 
**var_date** | **str** | Date on the quote. | [optional] 
**currency_id** | **str** | The Unique ID of the customer | [optional] 
**currency_code** | **str** | Currency code of the currency in which the customer wants to pay. If currency_code is not specified here, the currency chosen in your Zoho Billing organization will be used for billing. currency_id and currency_symbol are set automatically in accordance to the currency_code. | [optional] 
**total** | **float** | quote total value. | [optional] 
**created_time** | **str** | The time of creation of the quote | [optional] 
**last_modified_time** | **str** | Last date of modification in quote | [optional] 
**accepted_date** | **str** | The date of acceptance of the quotes | [optional] 
**declined_date** | **str** | The date of declination of the quotes | [optional] 
**expiry_date** | **str** | The date of expiration of the quotes | [optional] 
**has_attachment** | **bool** | To check for any attachment | [optional] 
**is_viewed_by_client** | **bool** | To see view status, if viewed by client the quote from the portal or not | [optional] 
**client_viewed_time** | **str** | Time when the client viewed the quote | [optional] 

## Example

```python
from ls_zoho_billing_quotes.models.list_estimates_response_estimates_inner import ListEstimatesResponseEstimatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListEstimatesResponseEstimatesInner from a JSON string
list_estimates_response_estimates_inner_instance = ListEstimatesResponseEstimatesInner.from_json(json)
# print the JSON string representation of the object
print(ListEstimatesResponseEstimatesInner.to_json())

# convert the object into a dict
list_estimates_response_estimates_inner_dict = list_estimates_response_estimates_inner_instance.to_dict()
# create an instance of ListEstimatesResponseEstimatesInner from a dict
list_estimates_response_estimates_inner_from_dict = ListEstimatesResponseEstimatesInner.from_dict(list_estimates_response_estimates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


