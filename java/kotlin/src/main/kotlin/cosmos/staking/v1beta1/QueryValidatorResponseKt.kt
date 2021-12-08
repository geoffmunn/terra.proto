//Generated by the protocol buffer compiler. DO NOT EDIT!
// source: cosmos/staking/v1beta1/query.proto

package cosmos.staking.v1beta1;

@kotlin.jvm.JvmSynthetic
inline fun queryValidatorResponse(block: cosmos.staking.v1beta1.QueryValidatorResponseKt.Dsl.() -> Unit): cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse =
  cosmos.staking.v1beta1.QueryValidatorResponseKt.Dsl._create(cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse.newBuilder()).apply { block() }._build()
object QueryValidatorResponseKt {
  @kotlin.OptIn(com.google.protobuf.kotlin.OnlyForUseByGeneratedProtoCode::class)
  @com.google.protobuf.kotlin.ProtoDslMarker
  class Dsl private constructor(
    @kotlin.jvm.JvmField private val _builder: cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse.Builder
  ) {
    companion object {
      @kotlin.jvm.JvmSynthetic
      @kotlin.PublishedApi
      internal fun _create(builder: cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse.Builder): Dsl = Dsl(builder)
    }

    @kotlin.jvm.JvmSynthetic
    @kotlin.PublishedApi
    internal fun _build(): cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse = _builder.build()

    /**
     * <pre>
     * validator defines the the validator info.
     * </pre>
     *
     * <code>.cosmos.staking.v1beta1.Validator validator = 1 [(.gogoproto.nullable) = false];</code>
     */
    var validator: cosmos.staking.v1beta1.Staking.Validator
      @JvmName("getValidator")
      get() = _builder.getValidator()
      @JvmName("setValidator")
      set(value) {
        _builder.setValidator(value)
      }
    /**
     * <pre>
     * validator defines the the validator info.
     * </pre>
     *
     * <code>.cosmos.staking.v1beta1.Validator validator = 1 [(.gogoproto.nullable) = false];</code>
     */
    fun clearValidator() {
      _builder.clearValidator()
    }
    /**
     * <pre>
     * validator defines the the validator info.
     * </pre>
     *
     * <code>.cosmos.staking.v1beta1.Validator validator = 1 [(.gogoproto.nullable) = false];</code>
     * @return Whether the validator field is set.
     */
    fun hasValidator(): kotlin.Boolean {
      return _builder.hasValidator()
    }
  }
}
@kotlin.jvm.JvmSynthetic
inline fun cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse.copy(block: cosmos.staking.v1beta1.QueryValidatorResponseKt.Dsl.() -> Unit): cosmos.staking.v1beta1.QueryOuterClass.QueryValidatorResponse =
  cosmos.staking.v1beta1.QueryValidatorResponseKt.Dsl._create(this.toBuilder()).apply { block() }._build()