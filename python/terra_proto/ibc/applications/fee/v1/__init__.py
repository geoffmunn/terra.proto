# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/applications/fee/v1/ack.proto, ibc/applications/fee/v1/fee.proto, ibc/applications/fee/v1/genesis.proto, ibc/applications/fee/v1/metadata.proto, ibc/applications/fee/v1/query.proto, ibc/applications/fee/v1/tx.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .....cosmos.base import v1beta1 as ____cosmos_base_v1_beta1__
from .....cosmos.base.query import v1beta1 as ____cosmos_base_query_v1_beta1__
from ....core.channel import v1 as ___core_channel_v1__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class Fee(betterproto.Message):
    """Fee defines the ICS29 receive, acknowledgement and timeout fees"""

    recv_fee: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """the packet receive fee"""

    ack_fee: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(2)
    """the packet acknowledgement fee"""

    timeout_fee: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(3)
    """the packet timeout fee"""


@dataclass(eq=False, repr=False)
class PacketFee(betterproto.Message):
    """
    PacketFee contains ICS29 relayer fees, refund address and optional list of
    permitted relayers
    """

    fee: "Fee" = betterproto.message_field(1)
    """
    fee encapsulates the recv, ack and timeout fees associated with an IBC
    packet
    """

    refund_address: str = betterproto.string_field(2)
    """the refund address for unspent fees"""

    relayers: List[str] = betterproto.string_field(3)
    """optional list of relayers permitted to receive fees"""


@dataclass(eq=False, repr=False)
class PacketFees(betterproto.Message):
    """PacketFees contains a list of type PacketFee"""

    packet_fees: List["PacketFee"] = betterproto.message_field(1)
    """list of packet fees"""


@dataclass(eq=False, repr=False)
class IdentifiedPacketFees(betterproto.Message):
    """
    IdentifiedPacketFees contains a list of type PacketFee and associated
    PacketId
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """
    unique packet identifier comprised of the channel ID, port ID and sequence
    """

    packet_fees: List["PacketFee"] = betterproto.message_field(2)
    """list of packet fees"""


@dataclass(eq=False, repr=False)
class MsgRegisterPayee(betterproto.Message):
    """MsgRegisterPayee defines the request type for the RegisterPayee rpc"""

    port_id: str = betterproto.string_field(1)
    """unique port identifier"""

    channel_id: str = betterproto.string_field(2)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(3)
    """the relayer address"""

    payee: str = betterproto.string_field(4)
    """the payee address"""


@dataclass(eq=False, repr=False)
class MsgRegisterPayeeResponse(betterproto.Message):
    """
    MsgRegisterPayeeResponse defines the response type for the RegisterPayee
    rpc
    """

    pass


@dataclass(eq=False, repr=False)
class MsgRegisterCounterpartyPayee(betterproto.Message):
    """
    MsgRegisterCounterpartyPayee defines the request type for the
    RegisterCounterpartyPayee rpc
    """

    port_id: str = betterproto.string_field(1)
    """unique port identifier"""

    channel_id: str = betterproto.string_field(2)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(3)
    """the relayer address"""

    counterparty_payee: str = betterproto.string_field(4)
    """the counterparty payee address"""


@dataclass(eq=False, repr=False)
class MsgRegisterCounterpartyPayeeResponse(betterproto.Message):
    """
    MsgRegisterCounterpartyPayeeResponse defines the response type for the
    RegisterCounterpartyPayee rpc
    """

    pass


@dataclass(eq=False, repr=False)
class MsgPayPacketFee(betterproto.Message):
    """
    MsgPayPacketFee defines the request type for the PayPacketFee rpc This Msg
    can be used to pay for a packet at the next sequence send & should be
    combined with the Msg that will be paid for
    """

    fee: "Fee" = betterproto.message_field(1)
    """
    fee encapsulates the recv, ack and timeout fees associated with an IBC
    packet
    """

    source_port_id: str = betterproto.string_field(2)
    """the source port unique identifier"""

    source_channel_id: str = betterproto.string_field(3)
    """the source channel unique identifer"""

    signer: str = betterproto.string_field(4)
    """account address to refund fee if necessary"""

    relayers: List[str] = betterproto.string_field(5)
    """optional list of relayers permitted to the receive packet fees"""


@dataclass(eq=False, repr=False)
class MsgPayPacketFeeResponse(betterproto.Message):
    """
    MsgPayPacketFeeResponse defines the response type for the PayPacketFee rpc
    """

    pass


@dataclass(eq=False, repr=False)
class MsgPayPacketFeeAsync(betterproto.Message):
    """
    MsgPayPacketFeeAsync defines the request type for the PayPacketFeeAsync rpc
    This Msg can be used to pay for a packet at a specified sequence (instead
    of the next sequence send)
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """
    unique packet identifier comprised of the channel ID, port ID and sequence
    """

    packet_fee: "PacketFee" = betterproto.message_field(2)
    """the packet fee associated with a particular IBC packet"""


@dataclass(eq=False, repr=False)
class MsgPayPacketFeeAsyncResponse(betterproto.Message):
    """
    MsgPayPacketFeeAsyncResponse defines the response type for the
    PayPacketFeeAsync rpc
    """

    pass


@dataclass(eq=False, repr=False)
class IncentivizedAcknowledgement(betterproto.Message):
    """
    IncentivizedAcknowledgement is the acknowledgement format to be used by
    applications wrapped in the fee middleware
    """

    app_acknowledgement: bytes = betterproto.bytes_field(1)
    """the underlying app acknowledgement bytes"""

    forward_relayer_address: str = betterproto.string_field(2)
    """the relayer address which submits the recv packet message"""

    underlying_app_success: bool = betterproto.bool_field(3)
    """success flag of the base application callback"""


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the ICS29 fee middleware genesis state"""

    identified_fees: List["IdentifiedPacketFees"] = betterproto.message_field(1)
    """list of identified packet fees"""

    fee_enabled_channels: List["FeeEnabledChannel"] = betterproto.message_field(2)
    """list of fee enabled channels"""

    registered_payees: List["RegisteredPayee"] = betterproto.message_field(3)
    """list of registered payees"""

    registered_counterparty_payees: List[
        "RegisteredCounterpartyPayee"
    ] = betterproto.message_field(4)
    """list of registered counterparty payees"""

    forward_relayers: List["ForwardRelayerAddress"] = betterproto.message_field(5)
    """list of forward relayer addresses"""


@dataclass(eq=False, repr=False)
class FeeEnabledChannel(betterproto.Message):
    """
    FeeEnabledChannel contains the PortID & ChannelID for a fee enabled channel
    """

    port_id: str = betterproto.string_field(1)
    """unique port identifier"""

    channel_id: str = betterproto.string_field(2)
    """unique channel identifier"""


@dataclass(eq=False, repr=False)
class RegisteredPayee(betterproto.Message):
    """
    RegisteredPayee contains the relayer address and payee address for a
    specific channel
    """

    channel_id: str = betterproto.string_field(1)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(2)
    """the relayer address"""

    payee: str = betterproto.string_field(3)
    """the payee address"""


@dataclass(eq=False, repr=False)
class RegisteredCounterpartyPayee(betterproto.Message):
    """
    RegisteredCounterpartyPayee contains the relayer address and counterparty
    payee address for a specific channel (used for recv fee distribution)
    """

    channel_id: str = betterproto.string_field(1)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(2)
    """the relayer address"""

    counterparty_payee: str = betterproto.string_field(3)
    """the counterparty payee address"""


@dataclass(eq=False, repr=False)
class ForwardRelayerAddress(betterproto.Message):
    """
    ForwardRelayerAddress contains the forward relayer address and PacketId
    used for async acknowledgements
    """

    address: str = betterproto.string_field(1)
    """the forward relayer address"""

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(2)
    """
    unique packet identifer comprised of the channel ID, port ID and sequence
    """


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketsRequest(betterproto.Message):
    """
    QueryIncentivizedPacketsRequest defines the request type for the
    IncentivizedPackets rpc
    """

    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""

    query_height: int = betterproto.uint64_field(2)
    """block height at which to query"""


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketsResponse(betterproto.Message):
    """
    QueryIncentivizedPacketsResponse defines the response type for the
    IncentivizedPackets rpc
    """

    incentivized_packets: List["IdentifiedPacketFees"] = betterproto.message_field(1)
    """list of identified fees for incentivized packets"""


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketRequest(betterproto.Message):
    """
    QueryIncentivizedPacketRequest defines the request type for the
    IncentivizedPacket rpc
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """
    unique packet identifier comprised of channel ID, port ID and sequence
    """

    query_height: int = betterproto.uint64_field(2)
    """block height at which to query"""


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketResponse(betterproto.Message):
    """
    QueryIncentivizedPacketsResponse defines the response type for the
    IncentivizedPacket rpc
    """

    incentivized_packet: "IdentifiedPacketFees" = betterproto.message_field(1)
    """the identified fees for the incentivized packet"""


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketsForChannelRequest(betterproto.Message):
    """
    QueryIncentivizedPacketsForChannelRequest defines the request type for
    querying for all incentivized packets for a specific channel
    """

    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""

    port_id: str = betterproto.string_field(2)
    channel_id: str = betterproto.string_field(3)
    query_height: int = betterproto.uint64_field(4)
    """Height to query at"""


@dataclass(eq=False, repr=False)
class QueryIncentivizedPacketsForChannelResponse(betterproto.Message):
    """
    QueryIncentivizedPacketsResponse defines the response type for the
    incentivized packets RPC
    """

    incentivized_packets: List["IdentifiedPacketFees"] = betterproto.message_field(1)
    """Map of all incentivized_packets"""


@dataclass(eq=False, repr=False)
class QueryTotalRecvFeesRequest(betterproto.Message):
    """
    QueryTotalRecvFeesRequest defines the request type for the TotalRecvFees
    rpc
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """the packet identifier for the associated fees"""


@dataclass(eq=False, repr=False)
class QueryTotalRecvFeesResponse(betterproto.Message):
    """
    QueryTotalRecvFeesResponse defines the response type for the TotalRecvFees
    rpc
    """

    recv_fees: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """the total packet receive fees"""


@dataclass(eq=False, repr=False)
class QueryTotalAckFeesRequest(betterproto.Message):
    """
    QueryTotalAckFeesRequest defines the request type for the TotalAckFees rpc
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """the packet identifier for the associated fees"""


@dataclass(eq=False, repr=False)
class QueryTotalAckFeesResponse(betterproto.Message):
    """
    QueryTotalAckFeesResponse defines the response type for the TotalAckFees
    rpc
    """

    ack_fees: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """the total packet acknowledgement fees"""


@dataclass(eq=False, repr=False)
class QueryTotalTimeoutFeesRequest(betterproto.Message):
    """
    QueryTotalTimeoutFeesRequest defines the request type for the
    TotalTimeoutFees rpc
    """

    packet_id: "___core_channel_v1__.PacketId" = betterproto.message_field(1)
    """the packet identifier for the associated fees"""


@dataclass(eq=False, repr=False)
class QueryTotalTimeoutFeesResponse(betterproto.Message):
    """
    QueryTotalTimeoutFeesResponse defines the response type for the
    TotalTimeoutFees rpc
    """

    timeout_fees: List["____cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)
    """the total packet timeout fees"""


@dataclass(eq=False, repr=False)
class QueryPayeeRequest(betterproto.Message):
    """QueryPayeeRequest defines the request type for the Payee rpc"""

    channel_id: str = betterproto.string_field(1)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(2)
    """the relayer address to which the distribution address is registered"""


@dataclass(eq=False, repr=False)
class QueryPayeeResponse(betterproto.Message):
    """QueryPayeeResponse defines the response type for the Payee rpc"""

    payee_address: str = betterproto.string_field(1)
    """the payee address to which packet fees are paid out"""


@dataclass(eq=False, repr=False)
class QueryCounterpartyPayeeRequest(betterproto.Message):
    """
    QueryCounterpartyPayeeRequest defines the request type for the
    CounterpartyPayee rpc
    """

    channel_id: str = betterproto.string_field(1)
    """unique channel identifier"""

    relayer: str = betterproto.string_field(2)
    """the relayer address to which the counterparty is registered"""


@dataclass(eq=False, repr=False)
class QueryCounterpartyPayeeResponse(betterproto.Message):
    """
    QueryCounterpartyPayeeResponse defines the response type for the
    CounterpartyPayee rpc
    """

    counterparty_payee: str = betterproto.string_field(1)
    """the counterparty payee address used to compensate forward relaying"""


@dataclass(eq=False, repr=False)
class QueryFeeEnabledChannelsRequest(betterproto.Message):
    """
    QueryFeeEnabledChannelsRequest defines the request type for the
    FeeEnabledChannels rpc
    """

    pagination: "____cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(1)
    )
    """pagination defines an optional pagination for the request."""

    query_height: int = betterproto.uint64_field(2)
    """block height at which to query"""


@dataclass(eq=False, repr=False)
class QueryFeeEnabledChannelsResponse(betterproto.Message):
    """
    QueryFeeEnabledChannelsResponse defines the response type for the
    FeeEnabledChannels rpc
    """

    fee_enabled_channels: List["FeeEnabledChannel"] = betterproto.message_field(1)
    """list of fee enabled channels"""


@dataclass(eq=False, repr=False)
class QueryFeeEnabledChannelRequest(betterproto.Message):
    """
    QueryFeeEnabledChannelRequest defines the request type for the
    FeeEnabledChannel rpc
    """

    port_id: str = betterproto.string_field(1)
    """unique port identifier"""

    channel_id: str = betterproto.string_field(2)
    """unique channel identifier"""


@dataclass(eq=False, repr=False)
class QueryFeeEnabledChannelResponse(betterproto.Message):
    """
    QueryFeeEnabledChannelResponse defines the response type for the
    FeeEnabledChannel rpc
    """

    fee_enabled: bool = betterproto.bool_field(1)
    """boolean flag representing the fee enabled channel status"""


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    """
    Metadata defines the ICS29 channel specific metadata encoded into the
    channel version bytestring See ICS004:
    https://github.com/cosmos/ibc/tree/master/spec/core/ics-004-channel-and-
    packet-semantics#Versioning
    """

    fee_version: str = betterproto.string_field(1)
    """fee_version defines the ICS29 fee version"""

    app_version: str = betterproto.string_field(2)
    """
    app_version defines the underlying application version, which may or may
    not be a JSON encoded bytestring
    """


class MsgStub(betterproto.ServiceStub):
    async def register_payee(
        self,
        msg_register_payee: "MsgRegisterPayee",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgRegisterPayeeResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Msg/RegisterPayee",
            msg_register_payee,
            MsgRegisterPayeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def register_counterparty_payee(
        self,
        msg_register_counterparty_payee: "MsgRegisterCounterpartyPayee",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgRegisterCounterpartyPayeeResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Msg/RegisterCounterpartyPayee",
            msg_register_counterparty_payee,
            MsgRegisterCounterpartyPayeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def pay_packet_fee(
        self,
        msg_pay_packet_fee: "MsgPayPacketFee",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgPayPacketFeeResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Msg/PayPacketFee",
            msg_pay_packet_fee,
            MsgPayPacketFeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def pay_packet_fee_async(
        self,
        msg_pay_packet_fee_async: "MsgPayPacketFeeAsync",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgPayPacketFeeAsyncResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Msg/PayPacketFeeAsync",
            msg_pay_packet_fee_async,
            MsgPayPacketFeeAsyncResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def incentivized_packets(
        self,
        query_incentivized_packets_request: "QueryIncentivizedPacketsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryIncentivizedPacketsResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/IncentivizedPackets",
            query_incentivized_packets_request,
            QueryIncentivizedPacketsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def incentivized_packet(
        self,
        query_incentivized_packet_request: "QueryIncentivizedPacketRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryIncentivizedPacketResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/IncentivizedPacket",
            query_incentivized_packet_request,
            QueryIncentivizedPacketResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def incentivized_packets_for_channel(
        self,
        query_incentivized_packets_for_channel_request: "QueryIncentivizedPacketsForChannelRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryIncentivizedPacketsForChannelResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel",
            query_incentivized_packets_for_channel_request,
            QueryIncentivizedPacketsForChannelResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_recv_fees(
        self,
        query_total_recv_fees_request: "QueryTotalRecvFeesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalRecvFeesResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/TotalRecvFees",
            query_total_recv_fees_request,
            QueryTotalRecvFeesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_ack_fees(
        self,
        query_total_ack_fees_request: "QueryTotalAckFeesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalAckFeesResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/TotalAckFees",
            query_total_ack_fees_request,
            QueryTotalAckFeesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_timeout_fees(
        self,
        query_total_timeout_fees_request: "QueryTotalTimeoutFeesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalTimeoutFeesResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/TotalTimeoutFees",
            query_total_timeout_fees_request,
            QueryTotalTimeoutFeesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def payee(
        self,
        query_payee_request: "QueryPayeeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryPayeeResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/Payee",
            query_payee_request,
            QueryPayeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def counterparty_payee(
        self,
        query_counterparty_payee_request: "QueryCounterpartyPayeeRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryCounterpartyPayeeResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/CounterpartyPayee",
            query_counterparty_payee_request,
            QueryCounterpartyPayeeResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def fee_enabled_channels(
        self,
        query_fee_enabled_channels_request: "QueryFeeEnabledChannelsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryFeeEnabledChannelsResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/FeeEnabledChannels",
            query_fee_enabled_channels_request,
            QueryFeeEnabledChannelsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def fee_enabled_channel(
        self,
        query_fee_enabled_channel_request: "QueryFeeEnabledChannelRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryFeeEnabledChannelResponse":
        return await self._unary_unary(
            "/ibc.applications.fee.v1.Query/FeeEnabledChannel",
            query_fee_enabled_channel_request,
            QueryFeeEnabledChannelResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):
    async def register_payee(
        self, msg_register_payee: "MsgRegisterPayee"
    ) -> "MsgRegisterPayeeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def register_counterparty_payee(
        self, msg_register_counterparty_payee: "MsgRegisterCounterpartyPayee"
    ) -> "MsgRegisterCounterpartyPayeeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def pay_packet_fee(
        self, msg_pay_packet_fee: "MsgPayPacketFee"
    ) -> "MsgPayPacketFeeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def pay_packet_fee_async(
        self, msg_pay_packet_fee_async: "MsgPayPacketFeeAsync"
    ) -> "MsgPayPacketFeeAsyncResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_register_payee(
        self,
        stream: "grpclib.server.Stream[MsgRegisterPayee, MsgRegisterPayeeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.register_payee(request)
        await stream.send_message(response)

    async def __rpc_register_counterparty_payee(
        self,
        stream: "grpclib.server.Stream[MsgRegisterCounterpartyPayee, MsgRegisterCounterpartyPayeeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.register_counterparty_payee(request)
        await stream.send_message(response)

    async def __rpc_pay_packet_fee(
        self, stream: "grpclib.server.Stream[MsgPayPacketFee, MsgPayPacketFeeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.pay_packet_fee(request)
        await stream.send_message(response)

    async def __rpc_pay_packet_fee_async(
        self,
        stream: "grpclib.server.Stream[MsgPayPacketFeeAsync, MsgPayPacketFeeAsyncResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.pay_packet_fee_async(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.applications.fee.v1.Msg/RegisterPayee": grpclib.const.Handler(
                self.__rpc_register_payee,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRegisterPayee,
                MsgRegisterPayeeResponse,
            ),
            "/ibc.applications.fee.v1.Msg/RegisterCounterpartyPayee": grpclib.const.Handler(
                self.__rpc_register_counterparty_payee,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgRegisterCounterpartyPayee,
                MsgRegisterCounterpartyPayeeResponse,
            ),
            "/ibc.applications.fee.v1.Msg/PayPacketFee": grpclib.const.Handler(
                self.__rpc_pay_packet_fee,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgPayPacketFee,
                MsgPayPacketFeeResponse,
            ),
            "/ibc.applications.fee.v1.Msg/PayPacketFeeAsync": grpclib.const.Handler(
                self.__rpc_pay_packet_fee_async,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgPayPacketFeeAsync,
                MsgPayPacketFeeAsyncResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def incentivized_packets(
        self, query_incentivized_packets_request: "QueryIncentivizedPacketsRequest"
    ) -> "QueryIncentivizedPacketsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def incentivized_packet(
        self, query_incentivized_packet_request: "QueryIncentivizedPacketRequest"
    ) -> "QueryIncentivizedPacketResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def incentivized_packets_for_channel(
        self,
        query_incentivized_packets_for_channel_request: "QueryIncentivizedPacketsForChannelRequest",
    ) -> "QueryIncentivizedPacketsForChannelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_recv_fees(
        self, query_total_recv_fees_request: "QueryTotalRecvFeesRequest"
    ) -> "QueryTotalRecvFeesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_ack_fees(
        self, query_total_ack_fees_request: "QueryTotalAckFeesRequest"
    ) -> "QueryTotalAckFeesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_timeout_fees(
        self, query_total_timeout_fees_request: "QueryTotalTimeoutFeesRequest"
    ) -> "QueryTotalTimeoutFeesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def payee(
        self, query_payee_request: "QueryPayeeRequest"
    ) -> "QueryPayeeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def counterparty_payee(
        self, query_counterparty_payee_request: "QueryCounterpartyPayeeRequest"
    ) -> "QueryCounterpartyPayeeResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fee_enabled_channels(
        self, query_fee_enabled_channels_request: "QueryFeeEnabledChannelsRequest"
    ) -> "QueryFeeEnabledChannelsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fee_enabled_channel(
        self, query_fee_enabled_channel_request: "QueryFeeEnabledChannelRequest"
    ) -> "QueryFeeEnabledChannelResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_incentivized_packets(
        self,
        stream: "grpclib.server.Stream[QueryIncentivizedPacketsRequest, QueryIncentivizedPacketsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentivized_packets(request)
        await stream.send_message(response)

    async def __rpc_incentivized_packet(
        self,
        stream: "grpclib.server.Stream[QueryIncentivizedPacketRequest, QueryIncentivizedPacketResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentivized_packet(request)
        await stream.send_message(response)

    async def __rpc_incentivized_packets_for_channel(
        self,
        stream: "grpclib.server.Stream[QueryIncentivizedPacketsForChannelRequest, QueryIncentivizedPacketsForChannelResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.incentivized_packets_for_channel(request)
        await stream.send_message(response)

    async def __rpc_total_recv_fees(
        self,
        stream: "grpclib.server.Stream[QueryTotalRecvFeesRequest, QueryTotalRecvFeesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_recv_fees(request)
        await stream.send_message(response)

    async def __rpc_total_ack_fees(
        self,
        stream: "grpclib.server.Stream[QueryTotalAckFeesRequest, QueryTotalAckFeesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_ack_fees(request)
        await stream.send_message(response)

    async def __rpc_total_timeout_fees(
        self,
        stream: "grpclib.server.Stream[QueryTotalTimeoutFeesRequest, QueryTotalTimeoutFeesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_timeout_fees(request)
        await stream.send_message(response)

    async def __rpc_payee(
        self, stream: "grpclib.server.Stream[QueryPayeeRequest, QueryPayeeResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.payee(request)
        await stream.send_message(response)

    async def __rpc_counterparty_payee(
        self,
        stream: "grpclib.server.Stream[QueryCounterpartyPayeeRequest, QueryCounterpartyPayeeResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.counterparty_payee(request)
        await stream.send_message(response)

    async def __rpc_fee_enabled_channels(
        self,
        stream: "grpclib.server.Stream[QueryFeeEnabledChannelsRequest, QueryFeeEnabledChannelsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.fee_enabled_channels(request)
        await stream.send_message(response)

    async def __rpc_fee_enabled_channel(
        self,
        stream: "grpclib.server.Stream[QueryFeeEnabledChannelRequest, QueryFeeEnabledChannelResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.fee_enabled_channel(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/ibc.applications.fee.v1.Query/IncentivizedPackets": grpclib.const.Handler(
                self.__rpc_incentivized_packets,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentivizedPacketsRequest,
                QueryIncentivizedPacketsResponse,
            ),
            "/ibc.applications.fee.v1.Query/IncentivizedPacket": grpclib.const.Handler(
                self.__rpc_incentivized_packet,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentivizedPacketRequest,
                QueryIncentivizedPacketResponse,
            ),
            "/ibc.applications.fee.v1.Query/IncentivizedPacketsForChannel": grpclib.const.Handler(
                self.__rpc_incentivized_packets_for_channel,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryIncentivizedPacketsForChannelRequest,
                QueryIncentivizedPacketsForChannelResponse,
            ),
            "/ibc.applications.fee.v1.Query/TotalRecvFees": grpclib.const.Handler(
                self.__rpc_total_recv_fees,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalRecvFeesRequest,
                QueryTotalRecvFeesResponse,
            ),
            "/ibc.applications.fee.v1.Query/TotalAckFees": grpclib.const.Handler(
                self.__rpc_total_ack_fees,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalAckFeesRequest,
                QueryTotalAckFeesResponse,
            ),
            "/ibc.applications.fee.v1.Query/TotalTimeoutFees": grpclib.const.Handler(
                self.__rpc_total_timeout_fees,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalTimeoutFeesRequest,
                QueryTotalTimeoutFeesResponse,
            ),
            "/ibc.applications.fee.v1.Query/Payee": grpclib.const.Handler(
                self.__rpc_payee,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPayeeRequest,
                QueryPayeeResponse,
            ),
            "/ibc.applications.fee.v1.Query/CounterpartyPayee": grpclib.const.Handler(
                self.__rpc_counterparty_payee,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryCounterpartyPayeeRequest,
                QueryCounterpartyPayeeResponse,
            ),
            "/ibc.applications.fee.v1.Query/FeeEnabledChannels": grpclib.const.Handler(
                self.__rpc_fee_enabled_channels,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryFeeEnabledChannelsRequest,
                QueryFeeEnabledChannelsResponse,
            ),
            "/ibc.applications.fee.v1.Query/FeeEnabledChannel": grpclib.const.Handler(
                self.__rpc_fee_enabled_channel,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryFeeEnabledChannelRequest,
                QueryFeeEnabledChannelResponse,
            ),
        }
