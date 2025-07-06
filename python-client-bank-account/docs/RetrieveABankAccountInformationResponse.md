# RetrieveABankAccountInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 
**bank_accounts** | [**List[BankAccountsResponse]**](BankAccountsResponse.md) |  | [optional] 

## Example

```python
from ls_zoho_billing_bank_account.models.retrieve_a_bank_account_information_response import RetrieveABankAccountInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveABankAccountInformationResponse from a JSON string
retrieve_a_bank_account_information_response_instance = RetrieveABankAccountInformationResponse.from_json(json)
# print the JSON string representation of the object
print(RetrieveABankAccountInformationResponse.to_json())

# convert the object into a dict
retrieve_a_bank_account_information_response_dict = retrieve_a_bank_account_information_response_instance.to_dict()
# create an instance of RetrieveABankAccountInformationResponse from a dict
retrieve_a_bank_account_information_response_from_dict = RetrieveABankAccountInformationResponse.from_dict(retrieve_a_bank_account_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


