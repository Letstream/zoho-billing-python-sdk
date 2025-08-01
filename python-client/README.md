# openapi-client
An addon contains additional features that are not part of the subscribed plan, but are made available to customers on purchase of the addon. There are two kinds of addons - one-time and recurring. For a one-time addon, customers pay only once at the time of subscription, whereas for a recurring addon, customers have to pay for the addon each time they pay for the plan’s subscription. An addon can be associated with one or more plans of a product.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.14.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.zohoapis.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://www.zohoapis.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AddonsApi(api_client)
    addon_code = 'Email-basic' # str | 
    x_com_zoho_subscriptions_organizationid = '10234695' # str | ID of the organization

    try:
        # Delete an addon
        api_response = api_instance.addons_addon_code_delete(addon_code, x_com_zoho_subscriptions_organizationid)
        print("The response of AddonsApi->addons_addon_code_delete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AddonsApi->addons_addon_code_delete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://www.zohoapis.com/billing/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AddonsApi* | [**addons_addon_code_delete**](docs/AddonsApi.md#addons_addon_code_delete) | **DELETE** /addons/{addon_code} | Delete an addon
*AddonsApi* | [**addons_addon_code_get**](docs/AddonsApi.md#addons_addon_code_get) | **GET** /addons/{addon_code} | Retrieve an addon
*AddonsApi* | [**addons_addon_code_markasactive_post**](docs/AddonsApi.md#addons_addon_code_markasactive_post) | **POST** /addons/{addon_code}/markasactive | Mark as active
*AddonsApi* | [**addons_addon_code_markasinactive_post**](docs/AddonsApi.md#addons_addon_code_markasinactive_post) | **POST** /addons/{addon_code}/markasinactive | Mark as inactive
*AddonsApi* | [**addons_addon_code_put**](docs/AddonsApi.md#addons_addon_code_put) | **PUT** /addons/{addon_code} | Update an addon
*AddonsApi* | [**addons_get**](docs/AddonsApi.md#addons_get) | **GET** /addons | List all addons
*AddonsApi* | [**addons_post**](docs/AddonsApi.md#addons_post) | **POST** /addons | Create an addon


## Documentation For Models

 - [AddonResponse](docs/AddonResponse.md)
 - [AddonResponseCustomFieldsInner](docs/AddonResponseCustomFieldsInner.md)
 - [AddonResponsePlansInner](docs/AddonResponsePlansInner.md)
 - [AddonResponsePriceBracketsInner](docs/AddonResponsePriceBracketsInner.md)
 - [AddonResponseTagsInner](docs/AddonResponseTagsInner.md)
 - [CreateAnAddonRequest](docs/CreateAnAddonRequest.md)
 - [CreateAnAddonRequestOneOf](docs/CreateAnAddonRequestOneOf.md)
 - [CreateAnAddonRequestOneOf1](docs/CreateAnAddonRequestOneOf1.md)
 - [CreateAnAddonRequestOneOf1PriceBracketsInner](docs/CreateAnAddonRequestOneOf1PriceBracketsInner.md)
 - [CreateAnAddonRequestOneOf2](docs/CreateAnAddonRequestOneOf2.md)
 - [CreateAnAddonRequestOneOf2PriceBracketsInner](docs/CreateAnAddonRequestOneOf2PriceBracketsInner.md)
 - [CreateAnAddonRequestOneOf3](docs/CreateAnAddonRequestOneOf3.md)
 - [CreateAnAddonRequestOneOfPlansInner](docs/CreateAnAddonRequestOneOfPlansInner.md)
 - [CreateAnAddonResponse](docs/CreateAnAddonResponse.md)
 - [CustomFieldsInner](docs/CustomFieldsInner.md)
 - [DeleteAnAddonResponse](docs/DeleteAnAddonResponse.md)
 - [ItemTaxPreferencesInner](docs/ItemTaxPreferencesInner.md)
 - [ListAllAddonsResponse](docs/ListAllAddonsResponse.md)
 - [ListAllAddonsResponseAddonsInner](docs/ListAllAddonsResponseAddonsInner.md)
 - [ListAllAddonsResponseAddonsInnerTagsInner](docs/ListAllAddonsResponseAddonsInnerTagsInner.md)
 - [MarkAsActiveResponse](docs/MarkAsActiveResponse.md)
 - [MarkAsInactiveResponse](docs/MarkAsInactiveResponse.md)
 - [RetrieveAnAddonResponse](docs/RetrieveAnAddonResponse.md)
 - [RetrieveAnAddonResponseAddon](docs/RetrieveAnAddonResponseAddon.md)
 - [TagsInner](docs/TagsInner.md)
 - [UpdateAnAddonRequest](docs/UpdateAnAddonRequest.md)
 - [UpdateAnAddonRequestPlansInner](docs/UpdateAnAddonRequestPlansInner.md)
 - [UpdateAnAddonRequestPriceBracketsInner](docs/UpdateAnAddonRequestPriceBracketsInner.md)
 - [UpdateAnAddonRequestTagsInner](docs/UpdateAnAddonRequestTagsInner.md)
 - [UpdateAnAddonResponse](docs/UpdateAnAddonResponse.md)
 - [UpdateAnAddonResponseAddon](docs/UpdateAnAddonResponseAddon.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Zoho_Auth"></a>
### Zoho_Auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://accounts.zoho.com/oauth/v2/auth
- **Scopes**: 
 - **ZohoSubscriptions.addons.CREATE**: Create Addons
 - **ZohoSubscriptions.addons.READ**: Read Addons
 - **ZohoSubscriptions.addons.UPDATE**: Update Addons
 - **ZohoSubscriptions.addons.DELETE**: Delete Addons


## Author




