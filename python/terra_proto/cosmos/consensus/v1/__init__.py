# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/consensus/v1/query.proto, cosmos/consensus/v1/tx.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from ....tendermint import types as ___tendermint_types__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class MsgUpdateParams(betterproto.Message):
    """MsgUpdateParams is the Msg/UpdateParams request type."""

    authority: str = betterproto.string_field(1)
    """
    authority is the address that controls the module (defaults to x/gov unless
    overwritten).
    """

    block: "___tendermint_types__.BlockParams" = betterproto.message_field(2)
    """
    params defines the x/consensus parameters to update. VersionsParams is not
    included in this Msg because it is tracked separarately in x/upgrade. NOTE:
    All parameters must be supplied.
    """

    evidence: "___tendermint_types__.EvidenceParams" = betterproto.message_field(3)
    validator: "___tendermint_types__.ValidatorParams" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class MsgUpdateParamsResponse(betterproto.Message):
    """
    MsgUpdateParamsResponse defines the response structure for executing a
    MsgUpdateParams message.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest defines the request type for querying x/consensus
    parameters.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse defines the response type for querying x/consensus
    parameters.
    """

    params: "___tendermint_types__.ConsensusParams" = betterproto.message_field(1)
    """
    params are the tendermint consensus params stored in the consensus module.
    Please note that `params.version` is not populated in this response, it is
    tracked separately in the x/upgrade module.
    """


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
            "/cosmos.consensus.v1.Msg/UpdateParams",
            msg_update_params,
            MsgUpdateParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def params(
        self,
        query_params_request: "QueryParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryParamsResponse":
        return await self._unary_unary(
            "/cosmos.consensus.v1.Query/Params",
            query_params_request,
            QueryParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


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
            "/cosmos.consensus.v1.Msg/UpdateParams": grpclib.const.Handler(
                self.__rpc_update_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgUpdateParams,
                MsgUpdateParamsResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def params(
        self, query_params_request: "QueryParamsRequest"
    ) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_params(
        self, stream: "grpclib.server.Stream[QueryParamsRequest, QueryParamsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.consensus.v1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
        }
