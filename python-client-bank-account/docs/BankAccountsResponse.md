# BankAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account ID of the bank account from which payment is about to made by the customer. | [optional] 
**customer_id** | **str** | Unique ID associated with the customer. | [optional] 
**customer_name** | **str** | Name of the customer, whom the bank account is associated. | [optional] 
**gateway** | **str** | Payment gateway through which payment needs to be made. Supported payment gateway values &lt;code&gt;test_gateway&lt;/code&gt;, &lt;code&gt;payflow_pro&lt;/code&gt;, &lt;code&gt;stripe&lt;/code&gt;, &lt;code&gt;2checkout&lt;/code&gt;, &lt;code&gt;authorize_net&lt;/code&gt;, &lt;code&gt;payments_pro&lt;/code&gt;, &lt;code&gt;forte&lt;/code&gt;, &lt;code&gt;worldpay&lt;/code&gt;, &lt;code&gt;wepay&lt;/code&gt;. | [optional] 
**last_four_digits** | **int** | Last four digits of the customer&#39;s bank account. | [optional] 
**status** | **str** | Status of the bank account. | [optional] 
**last_modified_time** | **str** | Time at which the contact person details were last updated. | [optional] 
**created_time** | **str** | Time at which the contact person was created. | [optional] 
**created_by_id** | **str** | Unique ID to denote the user who added the bank account. | [optional] 
**created_by_name** | **str** | Name of the user who added the bank account. | [optional] 

## Example

```python
from ls_zoho_billing_bank_account.models.bank_accounts_response import BankAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountsResponse from a JSON string
bank_accounts_response_instance = BankAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(BankAccountsResponse.to_json())

# convert the object into a dict
bank_accounts_response_dict = bank_accounts_response_instance.to_dict()
# create an instance of BankAccountsResponse from a dict
bank_accounts_response_from_dict = BankAccountsResponse.from_dict(bank_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


