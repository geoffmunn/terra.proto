//Generated by the protocol buffer compiler. DO NOT EDIT!
// source: tendermint/abci/types.proto

package tendermint.abci;

@kotlin.jvm.JvmSynthetic
inline fun requestInitChain(block: tendermint.abci.RequestInitChainKt.Dsl.() -> Unit): tendermint.abci.Types.RequestInitChain =
  tendermint.abci.RequestInitChainKt.Dsl._create(tendermint.abci.Types.RequestInitChain.newBuilder()).apply { block() }._build()
object RequestInitChainKt {
  @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
  @com.google.protobuf.kotlin.ProtoDslMarker
  class Dsl private constructor(
    @kotlin.jvm.JvmField private val _builder: tendermint.abci.Types.RequestInitChain.Builder
  ) {
    companion object {
      @kotlin.jvm.JvmSynthetic
      @kotlin.PublishedApi
      internal fun _create(builder: tendermint.abci.Types.RequestInitChain.Builder): Dsl = Dsl(builder)
    }

    @kotlin.jvm.JvmSynthetic
    @kotlin.PublishedApi
    internal fun _build(): tendermint.abci.Types.RequestInitChain = _builder.build()

    /**
     * <code>.google.protobuf.Timestamp time = 1 [(.gogoproto.nullable) = false, (.gogoproto.stdtime) = true];</code>
     */
    var time: com.google.protobuf.Timestamp
      @JvmName("getTime")
      get() = _builder.getTime()
      @JvmName("setTime")
      set(value) {
        _builder.setTime(value)
      }
    /**
     * <code>.google.protobuf.Timestamp time = 1 [(.gogoproto.nullable) = false, (.gogoproto.stdtime) = true];</code>
     */
    fun clearTime() {
      _builder.clearTime()
    }
    /**
     * <code>.google.protobuf.Timestamp time = 1 [(.gogoproto.nullable) = false, (.gogoproto.stdtime) = true];</code>
     * @return Whether the time field is set.
     */
    fun hasTime(): kotlin.Boolean {
      return _builder.hasTime()
    }

    /**
     * <code>string chain_id = 2;</code>
     */
    var chainId: kotlin.String
      @JvmName("getChainId")
      get() = _builder.getChainId()
      @JvmName("setChainId")
      set(value) {
        _builder.setChainId(value)
      }
    /**
     * <code>string chain_id = 2;</code>
     */
    fun clearChainId() {
      _builder.clearChainId()
    }

    /**
     * <code>.tendermint.abci.ConsensusParams consensus_params = 3;</code>
     */
    var consensusParams: tendermint.abci.Types.ConsensusParams
      @JvmName("getConsensusParams")
      get() = _builder.getConsensusParams()
      @JvmName("setConsensusParams")
      set(value) {
        _builder.setConsensusParams(value)
      }
    /**
     * <code>.tendermint.abci.ConsensusParams consensus_params = 3;</code>
     */
    fun clearConsensusParams() {
      _builder.clearConsensusParams()
    }
    /**
     * <code>.tendermint.abci.ConsensusParams consensus_params = 3;</code>
     * @return Whether the consensusParams field is set.
     */
    fun hasConsensusParams(): kotlin.Boolean {
      return _builder.hasConsensusParams()
    }

    /**
     * An uninstantiable, behaviorless type to represent the field in
     * generics.
     */
    @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
    class ValidatorsProxy private constructor() : com.google.protobuf.kotlin.DslProxy()
    /**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     */
     val validators: com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>
      @kotlin.jvm.JvmSynthetic
      get() = com.google.protobuf.kotlin.DslList(
        _builder.getValidatorsList()
      )
    /**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     * @param value The validators to add.
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("addValidators")
    fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.add(value: tendermint.abci.Types.ValidatorUpdate) {
      _builder.addValidators(value)
    }/**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     * @param value The validators to add.
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("plusAssignValidators")
    inline operator fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.plusAssign(value: tendermint.abci.Types.ValidatorUpdate) {
      add(value)
    }/**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     * @param values The validators to add.
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("addAllValidators")
    fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.addAll(values: kotlin.collections.Iterable<tendermint.abci.Types.ValidatorUpdate>) {
      _builder.addAllValidators(values)
    }/**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     * @param values The validators to add.
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("plusAssignAllValidators")
    inline operator fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.plusAssign(values: kotlin.collections.Iterable<tendermint.abci.Types.ValidatorUpdate>) {
      addAll(values)
    }/**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     * @param index The index to set the value at.
     * @param value The validators to set.
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("setValidators")
    operator fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.set(index: kotlin.Int, value: tendermint.abci.Types.ValidatorUpdate) {
      _builder.setValidators(index, value)
    }/**
     * <code>repeated .tendermint.abci.ValidatorUpdate validators = 4 [(.gogoproto.nullable) = false];</code>
     */
    @kotlin.jvm.JvmSynthetic
    @kotlin.jvm.JvmName("clearValidators")
    fun com.google.protobuf.kotlin.DslList<tendermint.abci.Types.ValidatorUpdate, ValidatorsProxy>.clear() {
      _builder.clearValidators()
    }
    /**
     * <code>bytes app_state_bytes = 5;</code>
     */
    var appStateBytes: com.google.protobuf.ByteString
      @JvmName("getAppStateBytes")
      get() = _builder.getAppStateBytes()
      @JvmName("setAppStateBytes")
      set(value) {
        _builder.setAppStateBytes(value)
      }
    /**
     * <code>bytes app_state_bytes = 5;</code>
     */
    fun clearAppStateBytes() {
      _builder.clearAppStateBytes()
    }

    /**
     * <code>int64 initial_height = 6;</code>
     */
    var initialHeight: kotlin.Long
      @JvmName("getInitialHeight")
      get() = _builder.getInitialHeight()
      @JvmName("setInitialHeight")
      set(value) {
        _builder.setInitialHeight(value)
      }
    /**
     * <code>int64 initial_height = 6;</code>
     */
    fun clearInitialHeight() {
      _builder.clearInitialHeight()
    }
  }
}
@kotlin.jvm.JvmSynthetic
inline fun tendermint.abci.Types.RequestInitChain.copy(block: tendermint.abci.RequestInitChainKt.Dsl.() -> Unit): tendermint.abci.Types.RequestInitChain =
  tendermint.abci.RequestInitChainKt.Dsl._create(this.toBuilder()).apply { block() }._build()