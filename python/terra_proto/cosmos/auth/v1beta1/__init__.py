# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/auth/v1beta1/auth.proto, cosmos/auth/v1beta1/genesis.proto, cosmos/auth/v1beta1/query.proto, cosmos/auth/v1beta1/tx.proto
# plugin: python-betterproto
# This file has been @generated
import warnings
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ...base.query import v1beta1 as __base_query_v1_beta1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class BaseAccount(betterproto.Message):
    """
    BaseAccount defines a base account type. It contains all the necessary
    fields for basic account functionality. Any custom account type should
    extend this type for additional functionality (e.g. vesting).
    """

    address: str = betterproto.string_field(1)
    pub_key: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)
    account_number: int = betterproto.uint64_field(3)
    sequence: int = betterproto.uint64_field(4)


@dataclass(eq=False, repr=False)
class ModuleAccount(betterproto.Message):
    """
    ModuleAccount defines an account for modules that holds coins on a pool.
    """

    base_account: "BaseAccount" = betterproto.message_field(1)
    name: str = betterproto.string_field(2)
    permissions: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ModuleCredential(betterproto.Message):
    """
    ModuleCredential represents a unclaimable pubkey for base accounts
    controlled by modules. Since: cosmos-sdk 0.47
    """

    module_name: str = betterproto.string_field(1)
    """
    module_name is the name of the module used for address derivation (passed
    into address.Module).
    """

    derivation_keys: List[bytes] = betterproto.bytes_field(2)
    """
    derivation_keys is for deriving a module account address (passed into
    address.Module) adding more keys creates sub-account addresses (passed into
    address.Derive)
    """


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the auth module."""

    max_memo_characters: int = betterproto.uint64_field(1)
    tx_sig_limit: int = betterproto.uint64_field(2)
    tx_size_cost_per_byte: int = betterproto.uint64_field(3)
    sig_verify_cost_ed25519: int = betterproto.uint64_field(4)
    sig_verify_cost_secp256_k1: int = betterproto.uint64_field(5)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the auth module's genesis state."""

    params: "Params" = betterproto.message_field(1)
    """params defines all the parameters of the module."""

    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(2)
    """accounts are the accounts present at genesis."""


@dataclass(eq=False, repr=False)
class QueryAccountsRequest(betterproto.Message):
    """
    QueryAccountsRequest is the request type for the Query/Accounts RPC method.
    Since: cosmos-sdk 0.43
    """

    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryAccountsResponse(betterproto.Message):
    """
    QueryAccountsResponse is the response type for the Query/Accounts RPC
    method. Since: cosmos-sdk 0.43
    """

    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    """accounts are the existing accounts"""

    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryAccountRequest(betterproto.Message):
    """
    QueryAccountRequest is the request type for the Query/Account RPC method.
    """

    address: str = betterproto.string_field(1)
    """address defines the address to query for."""


@dataclass(eq=False, repr=False)
class QueryAccountResponse(betterproto.Message):
    """
    QueryAccountResponse is the response type for the Query/Account RPC method.
    """

    account: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)
    """account defines the account of the corresponding address."""


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest is the request type for the Query/Params RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse is the response type for the Query/Params RPC method.
    """

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class QueryModuleAccountsRequest(betterproto.Message):
    """
    QueryModuleAccountsRequest is the request type for the Query/ModuleAccounts
    RPC method. Since: cosmos-sdk 0.46
    """

    pass


@dataclass(eq=False, repr=False)
class QueryModuleAccountsResponse(betterproto.Message):
    """
    QueryModuleAccountsResponse is the response type for the
    Query/ModuleAccounts RPC method. Since: cosmos-sdk 0.46
    """

    accounts: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryModuleAccountByNameRequest(betterproto.Message):
    """
    QueryModuleAccountByNameRequest is the request type for the
    Query/ModuleAccountByName RPC method.
    """

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryModuleAccountByNameResponse(betterproto.Message):
    """
    QueryModuleAccountByNameResponse is the response type for the
    Query/ModuleAccountByName RPC method.
    """

    account: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Bech32PrefixRequest(betterproto.Message):
    """
    Bech32PrefixRequest is the request type for Bech32Prefix rpc method. Since:
    cosmos-sdk 0.46
    """

    pass


@dataclass(eq=False, repr=False)
class Bech32PrefixResponse(betterproto.Message):
    """
    Bech32PrefixResponse is the response type for Bech32Prefix rpc method.
    Since: cosmos-sdk 0.46
    """

    bech32_prefix: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AddressBytesToStringRequest(betterproto.Message):
    """
    AddressBytesToStringRequest is the request type for AddressString rpc
    method. Since: cosmos-sdk 0.46
    """

    address_bytes: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class AddressBytesToStringResponse(betterproto.Message):
    """
    AddressBytesToStringResponse is the response type for AddressString rpc
    method. Since: cosmos-sdk 0.46
    """

    address_string: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AddressStringToBytesRequest(betterproto.Message):
    """
    AddressStringToBytesRequest is the request type for AccountBytes rpc
    method. Since: cosmos-sdk 0.46
    """

    address_string: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class AddressStringToBytesResponse(betterproto.Message):
    """
    AddressStringToBytesResponse is the response type for AddressBytes rpc
    method. Since: cosmos-sdk 0.46
    """

    address_bytes: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountAddressByIdRequest(betterproto.Message):
    """
    QueryAccountAddressByIDRequest is the request type for AccountAddressByID
    rpc method Since: cosmos-sdk 0.46.2
    """

    id: int = betterproto.int64_field(1)
    """
    Deprecated, use account_id instead id is the account number of the address
    to be queried. This field should have been an uint64 (like all account
    numbers), and will be updated to uint64 in a future version of the auth
    query.
    """

    account_id: int = betterproto.uint64_field(2)
    """
    account_id is the account number of the address to be queried. Since:
    cosmos-sdk 0.47
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("id"):
            warnings.warn(
                "QueryAccountAddressByIdRequest.id is deprecated", DeprecationWarning
            )


@dataclass(eq=False, repr=False)
class QueryAccountAddressByIdResponse(betterproto.Message):
    """
    QueryAccountAddressByIDResponse is the response type for AccountAddressByID
    rpc method Since: cosmos-sdk 0.46.2
    """

    account_address: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryAccountInfoRequest(betterproto.Message):
    """
    QueryAccountInfoRequest is the Query/AccountInfo request type. Since:
    cosmos-sdk 0.47
    """

    address: str = betterproto.string_field(1)
    """address is the account address string."""


@dataclass(eq=False, repr=False)
class QueryAccountInfoResponse(betterproto.Message):
    """
    QueryAccountInfoResponse is the Query/AccountInfo response type. Since:
    cosmos-sdk 0.47
    """

    info: "BaseAccount" = betterproto.message_field(1)
    """info is the account info which is represented by BaseAccount."""


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """
    MsgUpdateParams is the Msg/UpdateParams request type. Since: cosmos-sdk
    0.47
    """

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    params: "Params" = betterproto.message_field(2)
    """
    params defines the x/auth parameters to update. NOTE: All parameters must
    be supplied.
    """


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message. Since: cosmos-sdk 0.47
    """

    pass


class QueryStub(betterproto.ServiceStub):
    async def accounts(
        self,
        query_accounts_request: "QueryAccountsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Accounts",
            query_accounts_request,
            QueryAccountsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def account(
        self,
        query_account_request: "QueryAccountRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Account",
            query_account_request,
            QueryAccountResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def account_address_by_id(
        self,
        query_account_address_by_id_request: "QueryAccountAddressByIdRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountAddressByIdResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/AccountAddressByID",
            query_account_address_by_id_request,
            QueryAccountAddressByIdResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def module_accounts(
        self,
        query_module_accounts_request: "QueryModuleAccountsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryModuleAccountsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/ModuleAccounts",
            query_module_accounts_request,
            QueryModuleAccountsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def module_account_by_name(
        self,
        query_module_account_by_name_request: "QueryModuleAccountByNameRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryModuleAccountByNameResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/ModuleAccountByName",
            query_module_account_by_name_request,
            QueryModuleAccountByNameResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def bech32_prefix(
        self,
        bech32_prefix_request: "Bech32PrefixRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "Bech32PrefixResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/Bech32Prefix",
            bech32_prefix_request,
            Bech32PrefixResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def address_bytes_to_string(
        self,
        address_bytes_to_string_request: "AddressBytesToStringRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AddressBytesToStringResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/AddressBytesToString",
            address_bytes_to_string_request,
            AddressBytesToStringResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def address_string_to_bytes(
        self,
        address_string_to_bytes_request: "AddressStringToBytesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "AddressStringToBytesResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/AddressStringToBytes",
            address_string_to_bytes_request,
            AddressStringToBytesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def account_info(
        self,
        query_account_info_request: "QueryAccountInfoRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryAccountInfoResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Query/AccountInfo",
            query_account_info_request,
            QueryAccountInfoResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgStub(betterproto.ServiceStub):
    async def update_params(
        self,
        msg_update_params: "MsgUpdateParams",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgUpdateParamsResponse":
        return await self._unary_unary(
            "/cosmos.auth.v1beta1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryBase(ServiceBase):
    async def accounts(
        self, query_accounts_request: "QueryAccountsRequest"
    ) -> "QueryAccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def account(
        self, query_account_request: "QueryAccountRequest"
    ) -> "QueryAccountResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def account_address_by_id(
        self, query_account_address_by_id_request: "QueryAccountAddressByIdRequest"
    ) -> "QueryAccountAddressByIdResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def module_accounts(
        self, query_module_accounts_request: "QueryModuleAccountsRequest"
    ) -> "QueryModuleAccountsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def module_account_by_name(
        self, query_module_account_by_name_request: "QueryModuleAccountByNameRequest"
    ) -> "QueryModuleAccountByNameResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def bech32_prefix(
        self, bech32_prefix_request: "Bech32PrefixRequest"
    ) -> "Bech32PrefixResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def address_bytes_to_string(
        self, address_bytes_to_string_request: "AddressBytesToStringRequest"
    ) -> "AddressBytesToStringResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def address_string_to_bytes(
        self, address_string_to_bytes_request: "AddressStringToBytesRequest"
    ) -> "AddressStringToBytesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def account_info(
        self, query_account_info_request: "QueryAccountInfoRequest"
    ) -> "QueryAccountInfoResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_accounts(
        self,
        stream: "grpclib.server.Stream[QueryAccountsRequest, QueryAccountsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.accounts(request)
        await stream.send_message(response)

    async def __rpc_account(
        self, stream: "grpclib.server.Stream[QueryAccountRequest, QueryAccountResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.account(request)
        await stream.send_message(response)

    async def __rpc_account_address_by_id(
        self,
        stream: "grpclib.server.Stream[QueryAccountAddressByIdRequest, QueryAccountAddressByIdResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.account_address_by_id(request)
        await stream.send_message(response)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    async def __rpc_module_accounts(
        self,
        stream: "grpclib.server.Stream[QueryModuleAccountsRequest, QueryModuleAccountsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.module_accounts(request)
        await stream.send_message(response)

    async def __rpc_module_account_by_name(
        self,
        stream: "grpclib.server.Stream[QueryModuleAccountByNameRequest, QueryModuleAccountByNameResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.module_account_by_name(request)
        await stream.send_message(response)

    async def __rpc_bech32_prefix(
        self, stream: "grpclib.server.Stream[Bech32PrefixRequest, Bech32PrefixResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.bech32_prefix(request)
        await stream.send_message(response)

    async def __rpc_address_bytes_to_string(
        self,
        stream: "grpclib.server.Stream[AddressBytesToStringRequest, AddressBytesToStringResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.address_bytes_to_string(request)
        await stream.send_message(response)

    async def __rpc_address_string_to_bytes(
        self,
        stream: "grpclib.server.Stream[AddressStringToBytesRequest, AddressStringToBytesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.address_string_to_bytes(request)
        await stream.send_message(response)

    async def __rpc_account_info(
        self,
        stream: "grpclib.server.Stream[QueryAccountInfoRequest, QueryAccountInfoResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.account_info(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.auth.v1beta1.Query/Accounts": grpclib.const.Handler(
                self.__rpc_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountsRequest,
                QueryAccountsResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Account": grpclib.const.Handler(
                self.__rpc_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountRequest,
                QueryAccountResponse,
            ),
            "/cosmos.auth.v1beta1.Query/AccountAddressByID": grpclib.const.Handler(
                self.__rpc_account_address_by_id,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountAddressByIdRequest,
                QueryAccountAddressByIdResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.auth.v1beta1.Query/ModuleAccounts": grpclib.const.Handler(
                self.__rpc_module_accounts,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryModuleAccountsRequest,
                QueryModuleAccountsResponse,
            ),
            "/cosmos.auth.v1beta1.Query/ModuleAccountByName": grpclib.const.Handler(
                self.__rpc_module_account_by_name,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryModuleAccountByNameRequest,
                QueryModuleAccountByNameResponse,
            ),
            "/cosmos.auth.v1beta1.Query/Bech32Prefix": grpclib.const.Handler(
                self.__rpc_bech32_prefix,
                grpclib.const.Cardinality.UNARY_UNARY,
                Bech32PrefixRequest,
                Bech32PrefixResponse,
            ),
            "/cosmos.auth.v1beta1.Query/AddressBytesToString": grpclib.const.Handler(
                self.__rpc_address_bytes_to_string,
                grpclib.const.Cardinality.UNARY_UNARY,
                AddressBytesToStringRequest,
                AddressBytesToStringResponse,
            ),
            "/cosmos.auth.v1beta1.Query/AddressStringToBytes": grpclib.const.Handler(
                self.__rpc_address_string_to_bytes,
                grpclib.const.Cardinality.UNARY_UNARY,
                AddressStringToBytesRequest,
                AddressStringToBytesResponse,
            ),
            "/cosmos.auth.v1beta1.Query/AccountInfo": grpclib.const.Handler(
                self.__rpc_account_info,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAccountInfoRequest,
                QueryAccountInfoResponse,
            ),
        }


class MsgBase(ServiceBase):
    async def update_params(
        self, msg_update_params: "MsgUpdateParams"
    ) -> "MsgUpdateParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_update_params(
        self, stream: "grpclib.server.Stream[MsgUpdateParams, MsgUpdateParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.auth.v1beta1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
        }
