# coding: utf-8

"""
    Bank-Accounts

    A bank account  object shows the cbank account information for a particular customer

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from ls_zoho_billing_bank_account.models.retrieve_a_bank_account_information_response import RetrieveABankAccountInformationResponse

from ls_zoho_billing_bank_account.api_client import ApiClient, RequestSerialized
from ls_zoho_billing_bank_account.api_response import ApiResponse
from ls_zoho_billing_bank_account.rest import RESTResponseType


class BankAccountApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def customers_customer_id_bankaccounts_account_id_get(
        self,
        customer_id: StrictStr,
        x_com_zoho_subscriptions_organizationid: Annotated[StrictStr, Field(description="ID of the organization")],
        account_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RetrieveABankAccountInformationResponse:
        """Retrieve a bank account information

        Details of an existing bank account.

        :param customer_id: (required)
        :type customer_id: str
        :param x_com_zoho_subscriptions_organizationid: ID of the organization (required)
        :type x_com_zoho_subscriptions_organizationid: str
        :param account_id: (required)
        :type account_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._customers_customer_id_bankaccounts_account_id_get_serialize(
            customer_id=customer_id,
            x_com_zoho_subscriptions_organizationid=x_com_zoho_subscriptions_organizationid,
            account_id=account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RetrieveABankAccountInformationResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def customers_customer_id_bankaccounts_account_id_get_with_http_info(
        self,
        customer_id: StrictStr,
        x_com_zoho_subscriptions_organizationid: Annotated[StrictStr, Field(description="ID of the organization")],
        account_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[RetrieveABankAccountInformationResponse]:
        """Retrieve a bank account information

        Details of an existing bank account.

        :param customer_id: (required)
        :type customer_id: str
        :param x_com_zoho_subscriptions_organizationid: ID of the organization (required)
        :type x_com_zoho_subscriptions_organizationid: str
        :param account_id: (required)
        :type account_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._customers_customer_id_bankaccounts_account_id_get_serialize(
            customer_id=customer_id,
            x_com_zoho_subscriptions_organizationid=x_com_zoho_subscriptions_organizationid,
            account_id=account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RetrieveABankAccountInformationResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def customers_customer_id_bankaccounts_account_id_get_without_preload_content(
        self,
        customer_id: StrictStr,
        x_com_zoho_subscriptions_organizationid: Annotated[StrictStr, Field(description="ID of the organization")],
        account_id: StrictStr,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve a bank account information

        Details of an existing bank account.

        :param customer_id: (required)
        :type customer_id: str
        :param x_com_zoho_subscriptions_organizationid: ID of the organization (required)
        :type x_com_zoho_subscriptions_organizationid: str
        :param account_id: (required)
        :type account_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._customers_customer_id_bankaccounts_account_id_get_serialize(
            customer_id=customer_id,
            x_com_zoho_subscriptions_organizationid=x_com_zoho_subscriptions_organizationid,
            account_id=account_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RetrieveABankAccountInformationResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _customers_customer_id_bankaccounts_account_id_get_serialize(
        self,
        customer_id,
        x_com_zoho_subscriptions_organizationid,
        account_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if customer_id is not None:
            _path_params['customer_id'] = customer_id
        if account_id is not None:
            _path_params['account_id'] = account_id
        # process the query parameters
        # process the header parameters
        if x_com_zoho_subscriptions_organizationid is not None:
            _header_params['X-com-zoho-subscriptions-organizationid'] = x_com_zoho_subscriptions_organizationid
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'Zoho_Auth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/customers/{customer_id}/bankaccounts/{account_id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


