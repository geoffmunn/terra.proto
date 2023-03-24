# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/connection/v1/connection.proto, ibc/core/connection/v1/genesis.proto, ibc/core/connection/v1/query.proto, ibc/core/connection/v1/tx.proto
# plugin: python-betterproto
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

from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from ...client import v1 as __client_v1__
from ...commitment import v1 as __commitment_v1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class State(betterproto.Enum):
    """
    State defines if a connection is in one of the following states: INIT,
    TRYOPEN, OPEN or UNINITIALIZED.
    """

    STATE_UNINITIALIZED_UNSPECIFIED = 0
    """Default State"""

    STATE_INIT = 1
    """A connection end has just started the opening handshake."""

    STATE_TRYOPEN = 2
    """
    A connection end has acknowledged the handshake step on the counterparty
    chain.
    """

    STATE_OPEN = 3
    """A connection end has completed the handshake."""


@dataclass(eq=False, repr=False)
class ConnectionEnd(betterproto.Message):
    """
    ConnectionEnd defines a stateful object on a chain connected to another
    separate one. NOTE: there must only be 2 defined ConnectionEnds to
    establish a connection between two chains.
    """

    client_id: str = betterproto.string_field(1)
    """client associated with this connection."""

    versions: List["Version"] = betterproto.message_field(2)
    """
    IBC version which can be utilised to determine encodings or protocols for
    channels or packets utilising this connection.
    """

    state: "State" = betterproto.enum_field(3)
    """current state of the connection end."""

    counterparty: "Counterparty" = betterproto.message_field(4)
    """counterparty chain associated with this connection."""

    delay_period: int = betterproto.uint64_field(5)
    """
    delay period that must pass before a consensus state can be used for
    packet-verification NOTE: delay period logic is only implemented by some
    clients.
    """


@dataclass(eq=False, repr=False)
class IdentifiedConnection(betterproto.Message):
    """
    IdentifiedConnection defines a connection with additional connection
    identifier field.
    """

    id: str = betterproto.string_field(1)
    """connection identifier."""

    client_id: str = betterproto.string_field(2)
    """client associated with this connection."""

    versions: List["Version"] = betterproto.message_field(3)
    """
    IBC version which can be utilised to determine encodings or protocols for
    channels or packets utilising this connection
    """

    state: "State" = betterproto.enum_field(4)
    """current state of the connection end."""

    counterparty: "Counterparty" = betterproto.message_field(5)
    """counterparty chain associated with this connection."""

    delay_period: int = betterproto.uint64_field(6)
    """delay period associated with this connection."""


@dataclass(eq=False, repr=False)
class Counterparty(betterproto.Message):
    """
    Counterparty defines the counterparty chain associated with a connection
    end.
    """

    client_id: str = betterproto.string_field(1)
    """
    identifies the client on the counterparty chain associated with a given
    connection.
    """

    connection_id: str = betterproto.string_field(2)
    """
    identifies the connection end on the counterparty chain associated with a
    given connection.
    """

    prefix: "__commitment_v1__.MerklePrefix" = betterproto.message_field(3)
    """commitment merkle prefix of the counterparty chain."""


@dataclass(eq=False, repr=False)
class ClientPaths(betterproto.Message):
    """ClientPaths define all the connection paths for a client state."""

    paths: List[str] = betterproto.string_field(1)
    """list of connection paths"""


@dataclass(eq=False, repr=False)
class ConnectionPaths(betterproto.Message):
    """
    ConnectionPaths define all the connection paths for a given client state.
    """

    client_id: str = betterproto.string_field(1)
    """client state unique identifier"""

    paths: List[str] = betterproto.string_field(2)
    """list of connection paths"""


@dataclass(eq=False, repr=False)
class Version(betterproto.Message):
    """
    Version defines the versioning scheme used to negotiate the IBC verison in
    the connection handshake.
    """

    identifier: str = betterproto.string_field(1)
    """unique version identifier"""

    features: List[str] = betterproto.string_field(2)
    """list of features compatible with the specified identifier"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the set of Connection parameters."""

    max_expected_time_per_block: int = betterproto.uint64_field(1)
    """
    maximum expected time per block (in nanoseconds), used to enforce block
    delay. This parameter should reflect the largest amount of time that the
    chain might reasonably take to produce the next block under normal
    operating conditions. A safe choice is 3-5x the expected time per block.
    """


@dataclass(eq=False, repr=False)
class MsgConnectionOpenInit(betterproto.Message):
    """
    MsgConnectionOpenInit defines the msg sent by an account on Chain A to
    initialize a connection with Chain B.
    """

    client_id: str = betterproto.string_field(1)
    counterparty: "Counterparty" = betterproto.message_field(2)
    version: "Version" = betterproto.message_field(3)
    delay_period: int = betterproto.uint64_field(4)
    signer: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenInitResponse(betterproto.Message):
    """
    MsgConnectionOpenInitResponse defines the Msg/ConnectionOpenInit response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenTry(betterproto.Message):
    """
    MsgConnectionOpenTry defines a msg sent by a Relayer to try to open a
    connection on Chain B.
    """

    client_id: str = betterproto.string_field(1)
    previous_connection_id: str = betterproto.string_field(2)
    """
    Deprecated: this field is unused. Crossing hellos are no longer supported
    in core IBC.
    """

    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)
    counterparty: "Counterparty" = betterproto.message_field(4)
    delay_period: int = betterproto.uint64_field(5)
    counterparty_versions: List["Version"] = betterproto.message_field(6)
    proof_height: "__client_v1__.Height" = betterproto.message_field(7)
    proof_init: bytes = betterproto.bytes_field(8)
    """
    proof of the initialization the connection on Chain A: `UNITIALIZED ->
    INIT`
    """

    proof_client: bytes = betterproto.bytes_field(9)
    """proof of client state included in message"""

    proof_consensus: bytes = betterproto.bytes_field(10)
    """proof of client consensus state"""

    consensus_height: "__client_v1__.Height" = betterproto.message_field(11)
    signer: str = betterproto.string_field(12)

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("previous_connection_id"):
            warnings.warn(
                "MsgConnectionOpenTry.previous_connection_id is deprecated",
                DeprecationWarning,
            )


@dataclass(eq=False, repr=False)
class MsgConnectionOpenTryResponse(betterproto.Message):
    """
    MsgConnectionOpenTryResponse defines the Msg/ConnectionOpenTry response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenAck(betterproto.Message):
    """
    MsgConnectionOpenAck defines a msg sent by a Relayer to Chain A to
    acknowledge the change of connection state to TRYOPEN on Chain B.
    """

    connection_id: str = betterproto.string_field(1)
    counterparty_connection_id: str = betterproto.string_field(2)
    version: "Version" = betterproto.message_field(3)
    client_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(4)
    proof_height: "__client_v1__.Height" = betterproto.message_field(5)
    proof_try: bytes = betterproto.bytes_field(6)
    """
    proof of the initialization the connection on Chain B: `UNITIALIZED ->
    TRYOPEN`
    """

    proof_client: bytes = betterproto.bytes_field(7)
    """proof of client state included in message"""

    proof_consensus: bytes = betterproto.bytes_field(8)
    """proof of client consensus state"""

    consensus_height: "__client_v1__.Height" = betterproto.message_field(9)
    signer: str = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenAckResponse(betterproto.Message):
    """
    MsgConnectionOpenAckResponse defines the Msg/ConnectionOpenAck response
    type.
    """

    pass


@dataclass(eq=False, repr=False)
class MsgConnectionOpenConfirm(betterproto.Message):
    """
    MsgConnectionOpenConfirm defines a msg sent by a Relayer to Chain B to
    acknowledge the change of connection state to OPEN on Chain A.
    """

    connection_id: str = betterproto.string_field(1)
    proof_ack: bytes = betterproto.bytes_field(2)
    """
    proof for the change of the connection state on Chain A: `INIT -> OPEN`
    """

    proof_height: "__client_v1__.Height" = betterproto.message_field(3)
    signer: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgConnectionOpenConfirmResponse(betterproto.Message):
    """
    MsgConnectionOpenConfirmResponse defines the Msg/ConnectionOpenConfirm
    response type.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryConnectionRequest(betterproto.Message):
    """
    QueryConnectionRequest is the request type for the Query/Connection RPC
    method
    """

    connection_id: str = betterproto.string_field(1)
    """connection unique identifier"""


@dataclass(eq=False, repr=False)
class QueryConnectionResponse(betterproto.Message):
    """
    QueryConnectionResponse is the response type for the Query/Connection RPC
    method. Besides the connection end, it includes a proof and the height from
    which the proof was retrieved.
    """

    connection: "ConnectionEnd" = betterproto.message_field(1)
    """connection associated with the request identifier"""

    proof: bytes = betterproto.bytes_field(2)
    """merkle proof of existence"""

    proof_height: "__client_v1__.Height" = betterproto.message_field(3)
    """height at which the proof was retrieved"""


@dataclass(eq=False, repr=False)
class QueryConnectionsRequest(betterproto.Message):
    """
    QueryConnectionsRequest is the request type for the Query/Connections RPC
    method
    """

    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class QueryConnectionsResponse(betterproto.Message):
    """
    QueryConnectionsResponse is the response type for the Query/Connections RPC
    method.
    """

    connections: List["IdentifiedConnection"] = betterproto.message_field(1)
    """list of stored connections of the chain."""

    pagination: "____cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """pagination response"""

    height: "__client_v1__.Height" = betterproto.message_field(3)
    """query block height"""


@dataclass(eq=False, repr=False)
class QueryClientConnectionsRequest(betterproto.Message):
    """
    QueryClientConnectionsRequest is the request type for the
    Query/ClientConnections RPC method
    """

    client_id: str = betterproto.string_field(1)
    """client identifier associated with a connection"""


@dataclass(eq=False, repr=False)
class QueryClientConnectionsResponse(betterproto.Message):
    """
    QueryClientConnectionsResponse is the response type for the
    Query/ClientConnections RPC method
    """

    connection_paths: List[str] = betterproto.string_field(1)
    """slice of all the connection paths associated with a client."""

    proof: bytes = betterproto.bytes_field(2)
    """merkle proof of existence"""

    proof_height: "__client_v1__.Height" = betterproto.message_field(3)
    """height at which the proof was generated"""


@dataclass(eq=False, repr=False)
class QueryConnectionClientStateRequest(betterproto.Message):
    """
    QueryConnectionClientStateRequest is the request type for the
    Query/ConnectionClientState RPC method
    """

    connection_id: str = betterproto.string_field(1)
    """connection identifier"""


@dataclass(eq=False, repr=False)
class QueryConnectionClientStateResponse(betterproto.Message):
    """
    QueryConnectionClientStateResponse is the response type for the
    Query/ConnectionClientState RPC method
    """

    identified_client_state: "__client_v1__.IdentifiedClientState" = (
        betterproto.message_field(1)
    )
    """client state associated with the channel"""

    proof: bytes = betterproto.bytes_field(2)
    """merkle proof of existence"""

    proof_height: "__client_v1__.Height" = betterproto.message_field(3)
    """height at which the proof was retrieved"""


@dataclass(eq=False, repr=False)
class QueryConnectionConsensusStateRequest(betterproto.Message):
    """
    QueryConnectionConsensusStateRequest is the request type for the
    Query/ConnectionConsensusState RPC method
    """

    connection_id: str = betterproto.string_field(1)
    """connection identifier"""

    revision_number: int = betterproto.uint64_field(2)
    revision_height: int = betterproto.uint64_field(3)


@dataclass(eq=False, repr=False)
class QueryConnectionConsensusStateResponse(betterproto.Message):
    """
    QueryConnectionConsensusStateResponse is the response type for the
    Query/ConnectionConsensusState RPC method
    """

    consensus_state: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        1
    )
    """consensus state associated with the channel"""

    client_id: str = betterproto.string_field(2)
    """client ID associated with the consensus state"""

    proof: bytes = betterproto.bytes_field(3)
    """merkle proof of existence"""

    proof_height: "__client_v1__.Height" = betterproto.message_field(4)
    """height at which the proof was retrieved"""


@dataclass(eq=False, repr=False)
class QueryConnectionParamsRequest(betterproto.Message):
    """
    QueryConnectionParamsRequest is the request type for the
    Query/ConnectionParams RPC method.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryConnectionParamsResponse(betterproto.Message):
    """
    QueryConnectionParamsResponse is the response type for the
    Query/ConnectionParams RPC method.
    """

    params: "Params" = betterproto.message_field(1)
    """params defines the parameters of the module."""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ibc connection submodule's genesis state."""

    connections: List["IdentifiedConnection"] = betterproto.message_field(1)
    client_connection_paths: List["ConnectionPaths"] = betterproto.message_field(2)
    next_connection_sequence: int = betterproto.uint64_field(3)
    """the sequence for the next generated connection identifier"""

    params: "Params" = betterproto.message_field(4)


class MsgStub(betterproto.ServiceStub):
    async def connection_open_init(
        self,
        msg_connection_open_init: "MsgConnectionOpenInit",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgConnectionOpenInitResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenInit",
            msg_connection_open_init,
            MsgConnectionOpenInitResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_open_try(
        self,
        msg_connection_open_try: "MsgConnectionOpenTry",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgConnectionOpenTryResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenTry",
            msg_connection_open_try,
            MsgConnectionOpenTryResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_open_ack(
        self,
        msg_connection_open_ack: "MsgConnectionOpenAck",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgConnectionOpenAckResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenAck",
            msg_connection_open_ack,
            MsgConnectionOpenAckResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_open_confirm(
        self,
        msg_connection_open_confirm: "MsgConnectionOpenConfirm",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgConnectionOpenConfirmResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Msg/ConnectionOpenConfirm",
            msg_connection_open_confirm,
            MsgConnectionOpenConfirmResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def connection(
        self,
        query_connection_request: "QueryConnectionRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryConnectionResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connection",
            query_connection_request,
            QueryConnectionResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connections(
        self,
        query_connections_request: "QueryConnectionsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryConnectionsResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connections",
            query_connections_request,
            QueryConnectionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def client_connections(
        self,
        query_client_connections_request: "QueryClientConnectionsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryClientConnectionsResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ClientConnections",
            query_client_connections_request,
            QueryClientConnectionsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_client_state(
        self,
        query_connection_client_state_request: "QueryConnectionClientStateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryConnectionClientStateResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionClientState",
            query_connection_client_state_request,
            QueryConnectionClientStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_consensus_state(
        self,
        query_connection_consensus_state_request: "QueryConnectionConsensusStateRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryConnectionConsensusStateResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionConsensusState",
            query_connection_consensus_state_request,
            QueryConnectionConsensusStateResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def connection_params(
        self,
        query_connection_params_request: "QueryConnectionParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryConnectionParamsResponse":
        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionParams",
            query_connection_params_request,
            QueryConnectionParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):
    async def connection_open_init(
        self, msg_connection_open_init: "MsgConnectionOpenInit"
    ) -> "MsgConnectionOpenInitResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_try(
        self, msg_connection_open_try: "MsgConnectionOpenTry"
    ) -> "MsgConnectionOpenTryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_ack(
        self, msg_connection_open_ack: "MsgConnectionOpenAck"
    ) -> "MsgConnectionOpenAckResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_open_confirm(
        self, msg_connection_open_confirm: "MsgConnectionOpenConfirm"
    ) -> "MsgConnectionOpenConfirmResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_connection_open_init(
        self,
        stream: "grpclib.server.Stream[MsgConnectionOpenInit, MsgConnectionOpenInitResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_open_init(request)
        await stream.send_message(response)

    async def __rpc_connection_open_try(
        self,
        stream: "grpclib.server.Stream[MsgConnectionOpenTry, MsgConnectionOpenTryResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_open_try(request)
        await stream.send_message(response)

    async def __rpc_connection_open_ack(
        self,
        stream: "grpclib.server.Stream[MsgConnectionOpenAck, MsgConnectionOpenAckResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_open_ack(request)
        await stream.send_message(response)

    async def __rpc_connection_open_confirm(
        self,
        stream: "grpclib.server.Stream[MsgConnectionOpenConfirm, MsgConnectionOpenConfirmResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_open_confirm(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.connection.v1.Msg/ConnectionOpenInit": grpclib.const.Handler(
                self.__rpc_connection_open_init,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenInit,
                MsgConnectionOpenInitResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenTry": grpclib.const.Handler(
                self.__rpc_connection_open_try,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenTry,
                MsgConnectionOpenTryResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenAck": grpclib.const.Handler(
                self.__rpc_connection_open_ack,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenAck,
                MsgConnectionOpenAckResponse,
            ),
            "/ibc.core.connection.v1.Msg/ConnectionOpenConfirm": grpclib.const.Handler(
                self.__rpc_connection_open_confirm,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgConnectionOpenConfirm,
                MsgConnectionOpenConfirmResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def connection(
        self, query_connection_request: "QueryConnectionRequest"
    ) -> "QueryConnectionResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connections(
        self, query_connections_request: "QueryConnectionsRequest"
    ) -> "QueryConnectionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def client_connections(
        self, query_client_connections_request: "QueryClientConnectionsRequest"
    ) -> "QueryClientConnectionsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_client_state(
        self, query_connection_client_state_request: "QueryConnectionClientStateRequest"
    ) -> "QueryConnectionClientStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_consensus_state(
        self,
        query_connection_consensus_state_request: "QueryConnectionConsensusStateRequest",
    ) -> "QueryConnectionConsensusStateResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def connection_params(
        self, query_connection_params_request: "QueryConnectionParamsRequest"
    ) -> "QueryConnectionParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_connection(
        self,
        stream: "grpclib.server.Stream[QueryConnectionRequest, QueryConnectionResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection(request)
        await stream.send_message(response)

    async def __rpc_connections(
        self,
        stream: "grpclib.server.Stream[QueryConnectionsRequest, QueryConnectionsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connections(request)
        await stream.send_message(response)

    async def __rpc_client_connections(
        self,
        stream: "grpclib.server.Stream[QueryClientConnectionsRequest, QueryClientConnectionsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.client_connections(request)
        await stream.send_message(response)

    async def __rpc_connection_client_state(
        self,
        stream: "grpclib.server.Stream[QueryConnectionClientStateRequest, QueryConnectionClientStateResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_client_state(request)
        await stream.send_message(response)

    async def __rpc_connection_consensus_state(
        self,
        stream: "grpclib.server.Stream[QueryConnectionConsensusStateRequest, QueryConnectionConsensusStateResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_consensus_state(request)
        await stream.send_message(response)

    async def __rpc_connection_params(
        self,
        stream: "grpclib.server.Stream[QueryConnectionParamsRequest, QueryConnectionParamsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.connection_params(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.core.connection.v1.Query/Connection": grpclib.const.Handler(
                self.__rpc_connection,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionRequest,
                QueryConnectionResponse,
            ),
            "/ibc.core.connection.v1.Query/Connections": grpclib.const.Handler(
                self.__rpc_connections,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionsRequest,
                QueryConnectionsResponse,
            ),
            "/ibc.core.connection.v1.Query/ClientConnections": grpclib.const.Handler(
                self.__rpc_client_connections,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryClientConnectionsRequest,
                QueryClientConnectionsResponse,
            ),
            "/ibc.core.connection.v1.Query/ConnectionClientState": grpclib.const.Handler(
                self.__rpc_connection_client_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionClientStateRequest,
                QueryConnectionClientStateResponse,
            ),
            "/ibc.core.connection.v1.Query/ConnectionConsensusState": grpclib.const.Handler(
                self.__rpc_connection_consensus_state,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionConsensusStateRequest,
                QueryConnectionConsensusStateResponse,
            ),
            "/ibc.core.connection.v1.Query/ConnectionParams": grpclib.const.Handler(
                self.__rpc_connection_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryConnectionParamsRequest,
                QueryConnectionParamsResponse,
            ),
        }
