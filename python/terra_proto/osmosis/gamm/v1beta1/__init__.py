# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: balancerPool.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import List
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

from ...cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from ...cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__

if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


@dataclass(eq=False, repr=False)
class SmoothWeightChangeParams(betterproto.Message):
    """
    Parameters for changing the weights in a balancer pool smoothly from a
    start weight and end weight over a period of time. Currently, the only
    smooth change supported is linear changing between the two weights, but
    more types may be added in the future. When these parameters are set, the
    weight w(t) for pool time `t` is the following:   t <= start_time: w(t) =
    initial_pool_weights   start_time < t <= start_time + duration:     w(t) =
    initial_pool_weights + (t - start_time) *       (target_pool_weights -
    initial_pool_weights) / (duration)   t > start_time + duration: w(t) =
    target_pool_weights
    """

    start_time: datetime = betterproto.message_field(1)
    """
    The start time for beginning the weight change. If a parameter change /
    pool instantiation leaves this blank, it should be generated by the
    state_machine as the current time.
    """

    duration: timedelta = betterproto.message_field(2)
    """Duration for the weights to change over"""

    initial_pool_weights: List["PoolAsset"] = betterproto.message_field(3)
    """
    The initial pool weights. These are copied from the pool's settings at the
    time of weight change instantiation. The amount PoolAsset.token.amount
    field is ignored if present, future type refactorings should just have a
    type with the denom & weight here.
    """

    target_pool_weights: List["PoolAsset"] = betterproto.message_field(4)
    """
    The target pool weights. The pool weights will change linearly with respect
    to time between start_time, and start_time + duration. The amount
    PoolAsset.token.amount field is ignored if present, future type
    refactorings should just have a type with the denom & weight here.
    """


@dataclass(eq=False, repr=False)
class PoolParams(betterproto.Message):
    """
    PoolParams defined the parameters that will be managed by the pool
    governance in the future. This params are not managed by the chain
    governance. Instead they will be managed by the token holders of the pool.
    The pool's token holders are specified in future_pool_governor.
    """

    swap_fee: str = betterproto.string_field(1)
    exit_fee: str = betterproto.string_field(2)
    smooth_weight_change_params: "SmoothWeightChangeParams" = betterproto.message_field(
        3
    )


@dataclass(eq=False, repr=False)
class PoolAsset(betterproto.Message):
    """
    Pool asset is an internal struct that combines the amount of the token in
    the pool, and its balancer weight. This is an awkward packaging of data,
    and should be revisited in a future state migration.
    """

    token: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(1)
    """
    Coins we are talking about, the denomination must be unique amongst all
    PoolAssets for this pool.
    """

    weight: str = betterproto.string_field(2)
    """Weight that is not normalized. This weight must be less than 2^50"""


@dataclass(eq=False, repr=False)
class Pool(betterproto.Message):
    address: str = betterproto.string_field(1)
    id: int = betterproto.uint64_field(2)
    pool_params: "PoolParams" = betterproto.message_field(3)
    future_pool_governor: str = betterproto.string_field(4)
    """
    This string specifies who will govern the pool in the future. Valid forms
    of this are: {token name},{duration} {duration} where {token name} if
    specified is the token which determines the governor, and if not specified
    is the LP token for this pool.duration is a time specified as 0w,1w,2w,
    etc. which specifies how long the token would need to be locked up to count
    in governance. 0w means no lockup. TODO: Further improve these docs
    """

    total_shares: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(5)
    """sum of all LP tokens sent out"""

    pool_assets: List["PoolAsset"] = betterproto.message_field(6)
    """
    These are assumed to be sorted by denomiation. They contain the pool asset
    and the information about the weight
    """

    total_weight: str = betterproto.string_field(7)
    """sum of all non-normalized pool weights"""


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params holds parameters for the incentives module"""

    pool_creation_fee: List[
        "___cosmos_base_v1_beta1__.Coin"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the gamm module's genesis state."""

    pools: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    next_pool_number: int = betterproto.uint64_field(2)
    """will be renamed to next_pool_id in an upcoming version"""

    params: "Params" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class MsgJoinPool(betterproto.Message):
    """===================== MsgJoinPool This is really MsgJoinPoolNoSwap"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    share_out_amount: str = betterproto.string_field(3)
    token_in_maxs: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class MsgJoinPoolResponse(betterproto.Message):
    share_out_amount: str = betterproto.string_field(1)
    token_in: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgExitPool(betterproto.Message):
    """===================== MsgExitPool"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    share_in_amount: str = betterproto.string_field(3)
    token_out_mins: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(
        4
    )


@dataclass(eq=False, repr=False)
class MsgExitPoolResponse(betterproto.Message):
    token_out: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SwapAmountInRoute(betterproto.Message):
    """===================== MsgSwapExactAmountIn"""

    pool_id: int = betterproto.uint64_field(1)
    token_out_denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgSwapExactAmountIn(betterproto.Message):
    sender: str = betterproto.string_field(1)
    routes: List["SwapAmountInRoute"] = betterproto.message_field(2)
    token_in: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(3)
    token_out_min_amount: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgSwapExactAmountInResponse(betterproto.Message):
    token_out_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SwapAmountOutRoute(betterproto.Message):
    """===================== MsgSwapExactAmountOut"""

    pool_id: int = betterproto.uint64_field(1)
    token_in_denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class MsgSwapExactAmountOut(betterproto.Message):
    sender: str = betterproto.string_field(1)
    routes: List["SwapAmountOutRoute"] = betterproto.message_field(2)
    token_in_max_amount: str = betterproto.string_field(3)
    token_out: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class MsgSwapExactAmountOutResponse(betterproto.Message):
    token_in_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgJoinSwapExternAmountIn(betterproto.Message):
    """
    ===================== MsgJoinSwapExternAmountIn TODO: Rename to
    MsgJoinSwapExactAmountIn
    """

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    token_in: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(3)
    share_out_min_amount: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgJoinSwapExternAmountInResponse(betterproto.Message):
    share_out_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgJoinSwapShareAmountOut(betterproto.Message):
    """===================== MsgJoinSwapShareAmountOut"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    token_in_denom: str = betterproto.string_field(3)
    share_out_amount: str = betterproto.string_field(4)
    token_in_max_amount: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class MsgJoinSwapShareAmountOutResponse(betterproto.Message):
    token_in_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgExitSwapShareAmountIn(betterproto.Message):
    """===================== MsgExitSwapShareAmountIn"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    token_out_denom: str = betterproto.string_field(3)
    share_in_amount: str = betterproto.string_field(4)
    token_out_min_amount: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class MsgExitSwapShareAmountInResponse(betterproto.Message):
    token_out_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class MsgExitSwapExternAmountOut(betterproto.Message):
    """===================== MsgExitSwapExternAmountOut"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    token_out: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(3)
    share_in_max_amount: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class MsgExitSwapExternAmountOutResponse(betterproto.Message):
    share_in_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryPoolRequest(betterproto.Message):
    """=============================== Pool"""

    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryPoolResponse(betterproto.Message):
    pool: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryPoolsRequest(betterproto.Message):
    """=============================== Pools"""

    pagination: "___cosmos_base_query_v1_beta1__.PageRequest" = (
        betterproto.message_field(2)
    )
    """pagination defines an optional pagination for the request."""


@dataclass(eq=False, repr=False)
class QueryPoolsResponse(betterproto.Message):
    pools: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    pagination: "___cosmos_base_query_v1_beta1__.PageResponse" = (
        betterproto.message_field(2)
    )
    """pagination defines the pagination in the response."""


@dataclass(eq=False, repr=False)
class QueryNumPoolsRequest(betterproto.Message):
    """=============================== NumPools"""

    pass


@dataclass(eq=False, repr=False)
class QueryNumPoolsResponse(betterproto.Message):
    num_pools: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryPoolParamsRequest(betterproto.Message):
    """=============================== PoolParams"""

    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryPoolParamsResponse(betterproto.Message):
    params: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalPoolLiquidityRequest(betterproto.Message):
    """=============================== PoolLiquidity"""

    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalPoolLiquidityResponse(betterproto.Message):
    liquidity: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalSharesRequest(betterproto.Message):
    """=============================== TotalShares"""

    pool_id: int = betterproto.uint64_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalSharesResponse(betterproto.Message):
    total_shares: "___cosmos_base_v1_beta1__.Coin" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QuerySpotPriceRequest(betterproto.Message):
    """
    QuerySpotPriceRequest defines the gRPC request structure for a SpotPrice
    query.
    """

    pool_id: int = betterproto.uint64_field(1)
    base_asset_denom: str = betterproto.string_field(2)
    quote_asset_denom: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class QuerySpotPriceResponse(betterproto.Message):
    """
    QuerySpotPriceResponse defines the gRPC response structure for a SpotPrice
    query.
    """

    spot_price: str = betterproto.string_field(1)
    """String of the Dec. Ex) 10.203uatom"""


@dataclass(eq=False, repr=False)
class QuerySwapExactAmountInRequest(betterproto.Message):
    """=============================== EstimateSwapExactAmountIn"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    token_in: str = betterproto.string_field(3)
    routes: List["SwapAmountInRoute"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class QuerySwapExactAmountInResponse(betterproto.Message):
    token_out_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QuerySwapExactAmountOutRequest(betterproto.Message):
    """=============================== EstimateSwapExactAmountOut"""

    sender: str = betterproto.string_field(1)
    pool_id: int = betterproto.uint64_field(2)
    routes: List["SwapAmountOutRoute"] = betterproto.message_field(3)
    token_out: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class QuerySwapExactAmountOutResponse(betterproto.Message):
    token_in_amount: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalLiquidityRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class QueryTotalLiquidityResponse(betterproto.Message):
    liquidity: List["___cosmos_base_v1_beta1__.Coin"] = betterproto.message_field(1)


class MsgStub(betterproto.ServiceStub):
    async def join_pool(
        self,
        msg_join_pool: "MsgJoinPool",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgJoinPoolResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/JoinPool",
            msg_join_pool,
            MsgJoinPoolResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def exit_pool(
        self,
        msg_exit_pool: "MsgExitPool",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgExitPoolResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/ExitPool",
            msg_exit_pool,
            MsgExitPoolResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def swap_exact_amount_in(
        self,
        msg_swap_exact_amount_in: "MsgSwapExactAmountIn",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgSwapExactAmountInResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/SwapExactAmountIn",
            msg_swap_exact_amount_in,
            MsgSwapExactAmountInResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def swap_exact_amount_out(
        self,
        msg_swap_exact_amount_out: "MsgSwapExactAmountOut",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgSwapExactAmountOutResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/SwapExactAmountOut",
            msg_swap_exact_amount_out,
            MsgSwapExactAmountOutResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def join_swap_extern_amount_in(
        self,
        msg_join_swap_extern_amount_in: "MsgJoinSwapExternAmountIn",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgJoinSwapExternAmountInResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/JoinSwapExternAmountIn",
            msg_join_swap_extern_amount_in,
            MsgJoinSwapExternAmountInResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def join_swap_share_amount_out(
        self,
        msg_join_swap_share_amount_out: "MsgJoinSwapShareAmountOut",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgJoinSwapShareAmountOutResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/JoinSwapShareAmountOut",
            msg_join_swap_share_amount_out,
            MsgJoinSwapShareAmountOutResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def exit_swap_extern_amount_out(
        self,
        msg_exit_swap_extern_amount_out: "MsgExitSwapExternAmountOut",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgExitSwapExternAmountOutResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/ExitSwapExternAmountOut",
            msg_exit_swap_extern_amount_out,
            MsgExitSwapExternAmountOutResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def exit_swap_share_amount_in(
        self,
        msg_exit_swap_share_amount_in: "MsgExitSwapShareAmountIn",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "MsgExitSwapShareAmountInResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Msg/ExitSwapShareAmountIn",
            msg_exit_swap_share_amount_in,
            MsgExitSwapShareAmountInResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class QueryStub(betterproto.ServiceStub):
    async def pools(
        self,
        query_pools_request: "QueryPoolsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryPoolsResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/Pools",
            query_pools_request,
            QueryPoolsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def num_pools(
        self,
        query_num_pools_request: "QueryNumPoolsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryNumPoolsResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/NumPools",
            query_num_pools_request,
            QueryNumPoolsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_liquidity(
        self,
        query_total_liquidity_request: "QueryTotalLiquidityRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalLiquidityResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/TotalLiquidity",
            query_total_liquidity_request,
            QueryTotalLiquidityResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def pool(
        self,
        query_pool_request: "QueryPoolRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryPoolResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/Pool",
            query_pool_request,
            QueryPoolResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def pool_params(
        self,
        query_pool_params_request: "QueryPoolParamsRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryPoolParamsResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/PoolParams",
            query_pool_params_request,
            QueryPoolParamsResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_pool_liquidity(
        self,
        query_total_pool_liquidity_request: "QueryTotalPoolLiquidityRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalPoolLiquidityResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/TotalPoolLiquidity",
            query_total_pool_liquidity_request,
            QueryTotalPoolLiquidityResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def total_shares(
        self,
        query_total_shares_request: "QueryTotalSharesRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QueryTotalSharesResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/TotalShares",
            query_total_shares_request,
            QueryTotalSharesResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def spot_price(
        self,
        query_spot_price_request: "QuerySpotPriceRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySpotPriceResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/SpotPrice",
            query_spot_price_request,
            QuerySpotPriceResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def estimate_swap_exact_amount_in(
        self,
        query_swap_exact_amount_in_request: "QuerySwapExactAmountInRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySwapExactAmountInResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountIn",
            query_swap_exact_amount_in_request,
            QuerySwapExactAmountInResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def estimate_swap_exact_amount_out(
        self,
        query_swap_exact_amount_out_request: "QuerySwapExactAmountOutRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "QuerySwapExactAmountOutResponse":
        return await self._unary_unary(
            "/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountOut",
            query_swap_exact_amount_out_request,
            QuerySwapExactAmountOutResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class MsgBase(ServiceBase):
    async def join_pool(self, msg_join_pool: "MsgJoinPool") -> "MsgJoinPoolResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def exit_pool(self, msg_exit_pool: "MsgExitPool") -> "MsgExitPoolResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def swap_exact_amount_in(
        self, msg_swap_exact_amount_in: "MsgSwapExactAmountIn"
    ) -> "MsgSwapExactAmountInResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def swap_exact_amount_out(
        self, msg_swap_exact_amount_out: "MsgSwapExactAmountOut"
    ) -> "MsgSwapExactAmountOutResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def join_swap_extern_amount_in(
        self, msg_join_swap_extern_amount_in: "MsgJoinSwapExternAmountIn"
    ) -> "MsgJoinSwapExternAmountInResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def join_swap_share_amount_out(
        self, msg_join_swap_share_amount_out: "MsgJoinSwapShareAmountOut"
    ) -> "MsgJoinSwapShareAmountOutResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def exit_swap_extern_amount_out(
        self, msg_exit_swap_extern_amount_out: "MsgExitSwapExternAmountOut"
    ) -> "MsgExitSwapExternAmountOutResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def exit_swap_share_amount_in(
        self, msg_exit_swap_share_amount_in: "MsgExitSwapShareAmountIn"
    ) -> "MsgExitSwapShareAmountInResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_join_pool(
        self, stream: "grpclib.server.Stream[MsgJoinPool, MsgJoinPoolResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.join_pool(request)
        await stream.send_message(response)

    async def __rpc_exit_pool(
        self, stream: "grpclib.server.Stream[MsgExitPool, MsgExitPoolResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.exit_pool(request)
        await stream.send_message(response)

    async def __rpc_swap_exact_amount_in(
        self,
        stream: "grpclib.server.Stream[MsgSwapExactAmountIn, MsgSwapExactAmountInResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.swap_exact_amount_in(request)
        await stream.send_message(response)

    async def __rpc_swap_exact_amount_out(
        self,
        stream: "grpclib.server.Stream[MsgSwapExactAmountOut, MsgSwapExactAmountOutResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.swap_exact_amount_out(request)
        await stream.send_message(response)

    async def __rpc_join_swap_extern_amount_in(
        self,
        stream: "grpclib.server.Stream[MsgJoinSwapExternAmountIn, MsgJoinSwapExternAmountInResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.join_swap_extern_amount_in(request)
        await stream.send_message(response)

    async def __rpc_join_swap_share_amount_out(
        self,
        stream: "grpclib.server.Stream[MsgJoinSwapShareAmountOut, MsgJoinSwapShareAmountOutResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.join_swap_share_amount_out(request)
        await stream.send_message(response)

    async def __rpc_exit_swap_extern_amount_out(
        self,
        stream: "grpclib.server.Stream[MsgExitSwapExternAmountOut, MsgExitSwapExternAmountOutResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.exit_swap_extern_amount_out(request)
        await stream.send_message(response)

    async def __rpc_exit_swap_share_amount_in(
        self,
        stream: "grpclib.server.Stream[MsgExitSwapShareAmountIn, MsgExitSwapShareAmountInResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.exit_swap_share_amount_in(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.gamm.v1beta1.Msg/JoinPool": grpclib.const.Handler(
                self.__rpc_join_pool,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgJoinPool,
                MsgJoinPoolResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/ExitPool": grpclib.const.Handler(
                self.__rpc_exit_pool,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgExitPool,
                MsgExitPoolResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/SwapExactAmountIn": grpclib.const.Handler(
                self.__rpc_swap_exact_amount_in,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSwapExactAmountIn,
                MsgSwapExactAmountInResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/SwapExactAmountOut": grpclib.const.Handler(
                self.__rpc_swap_exact_amount_out,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSwapExactAmountOut,
                MsgSwapExactAmountOutResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/JoinSwapExternAmountIn": grpclib.const.Handler(
                self.__rpc_join_swap_extern_amount_in,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgJoinSwapExternAmountIn,
                MsgJoinSwapExternAmountInResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/JoinSwapShareAmountOut": grpclib.const.Handler(
                self.__rpc_join_swap_share_amount_out,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgJoinSwapShareAmountOut,
                MsgJoinSwapShareAmountOutResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/ExitSwapExternAmountOut": grpclib.const.Handler(
                self.__rpc_exit_swap_extern_amount_out,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgExitSwapExternAmountOut,
                MsgExitSwapExternAmountOutResponse,
            ),
            "/osmosis.gamm.v1beta1.Msg/ExitSwapShareAmountIn": grpclib.const.Handler(
                self.__rpc_exit_swap_share_amount_in,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgExitSwapShareAmountIn,
                MsgExitSwapShareAmountInResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def pools(
        self, query_pools_request: "QueryPoolsRequest"
    ) -> "QueryPoolsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def num_pools(
        self, query_num_pools_request: "QueryNumPoolsRequest"
    ) -> "QueryNumPoolsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_liquidity(
        self, query_total_liquidity_request: "QueryTotalLiquidityRequest"
    ) -> "QueryTotalLiquidityResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def pool(self, query_pool_request: "QueryPoolRequest") -> "QueryPoolResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def pool_params(
        self, query_pool_params_request: "QueryPoolParamsRequest"
    ) -> "QueryPoolParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_pool_liquidity(
        self, query_total_pool_liquidity_request: "QueryTotalPoolLiquidityRequest"
    ) -> "QueryTotalPoolLiquidityResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_shares(
        self, query_total_shares_request: "QueryTotalSharesRequest"
    ) -> "QueryTotalSharesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def spot_price(
        self, query_spot_price_request: "QuerySpotPriceRequest"
    ) -> "QuerySpotPriceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def estimate_swap_exact_amount_in(
        self, query_swap_exact_amount_in_request: "QuerySwapExactAmountInRequest"
    ) -> "QuerySwapExactAmountInResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def estimate_swap_exact_amount_out(
        self, query_swap_exact_amount_out_request: "QuerySwapExactAmountOutRequest"
    ) -> "QuerySwapExactAmountOutResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_pools(
        self, stream: "grpclib.server.Stream[QueryPoolsRequest, QueryPoolsResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.pools(request)
        await stream.send_message(response)

    async def __rpc_num_pools(
        self,
        stream: "grpclib.server.Stream[QueryNumPoolsRequest, QueryNumPoolsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.num_pools(request)
        await stream.send_message(response)

    async def __rpc_total_liquidity(
        self,
        stream: "grpclib.server.Stream[QueryTotalLiquidityRequest, QueryTotalLiquidityResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_liquidity(request)
        await stream.send_message(response)

    async def __rpc_pool(
        self, stream: "grpclib.server.Stream[QueryPoolRequest, QueryPoolResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.pool(request)
        await stream.send_message(response)

    async def __rpc_pool_params(
        self,
        stream: "grpclib.server.Stream[QueryPoolParamsRequest, QueryPoolParamsResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.pool_params(request)
        await stream.send_message(response)

    async def __rpc_total_pool_liquidity(
        self,
        stream: "grpclib.server.Stream[QueryTotalPoolLiquidityRequest, QueryTotalPoolLiquidityResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_pool_liquidity(request)
        await stream.send_message(response)

    async def __rpc_total_shares(
        self,
        stream: "grpclib.server.Stream[QueryTotalSharesRequest, QueryTotalSharesResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.total_shares(request)
        await stream.send_message(response)

    async def __rpc_spot_price(
        self,
        stream: "grpclib.server.Stream[QuerySpotPriceRequest, QuerySpotPriceResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.spot_price(request)
        await stream.send_message(response)

    async def __rpc_estimate_swap_exact_amount_in(
        self,
        stream: "grpclib.server.Stream[QuerySwapExactAmountInRequest, QuerySwapExactAmountInResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.estimate_swap_exact_amount_in(request)
        await stream.send_message(response)

    async def __rpc_estimate_swap_exact_amount_out(
        self,
        stream: "grpclib.server.Stream[QuerySwapExactAmountOutRequest, QuerySwapExactAmountOutResponse]",
    ) -> None:
        request = await stream.recv_message()
        response = await self.estimate_swap_exact_amount_out(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/osmosis.gamm.v1beta1.Query/Pools": grpclib.const.Handler(
                self.__rpc_pools,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPoolsRequest,
                QueryPoolsResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/NumPools": grpclib.const.Handler(
                self.__rpc_num_pools,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryNumPoolsRequest,
                QueryNumPoolsResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/TotalLiquidity": grpclib.const.Handler(
                self.__rpc_total_liquidity,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalLiquidityRequest,
                QueryTotalLiquidityResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/Pool": grpclib.const.Handler(
                self.__rpc_pool,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPoolRequest,
                QueryPoolResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/PoolParams": grpclib.const.Handler(
                self.__rpc_pool_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryPoolParamsRequest,
                QueryPoolParamsResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/TotalPoolLiquidity": grpclib.const.Handler(
                self.__rpc_total_pool_liquidity,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalPoolLiquidityRequest,
                QueryTotalPoolLiquidityResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/TotalShares": grpclib.const.Handler(
                self.__rpc_total_shares,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalSharesRequest,
                QueryTotalSharesResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/SpotPrice": grpclib.const.Handler(
                self.__rpc_spot_price,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySpotPriceRequest,
                QuerySpotPriceResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountIn": grpclib.const.Handler(
                self.__rpc_estimate_swap_exact_amount_in,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySwapExactAmountInRequest,
                QuerySwapExactAmountInResponse,
            ),
            "/osmosis.gamm.v1beta1.Query/EstimateSwapExactAmountOut": grpclib.const.Handler(
                self.__rpc_estimate_swap_exact_amount_out,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySwapExactAmountOutRequest,
                QuerySwapExactAmountOutResponse,
            ),
        }