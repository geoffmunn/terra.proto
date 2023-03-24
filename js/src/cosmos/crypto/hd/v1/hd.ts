/* eslint-disable */
import Long from "long";
import _m0 from "protobufjs/minimal";

export const protobufPackage = "cosmos.crypto.hd.v1";

/** Since: cosmos-sdk 0.46 */

/** BIP44Params is used as path field in ledger item in Record. */
export interface BIP44Params {
  /** purpose is a constant set to 44' (or 0x8000002C) following the BIP43 recommendation */
  purpose: number;
  /** coin_type is a constant that improves privacy */
  coinType: number;
  /** account splits the key space into independent user identities */
  account: number;
  /**
   * change is a constant used for public derivation. Constant 0 is used for external chain and constant 1 for internal
   * chain.
   */
  change: boolean;
  /** address_index is used as child index in BIP32 derivation */
  addressIndex: number;
}

const baseBIP44Params: object = { purpose: 0, coinType: 0, account: 0, change: false, addressIndex: 0 };

export const BIP44Params = {
  encode(message: BIP44Params, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.purpose !== 0) {
      writer.uint32(8).uint32(message.purpose);
    }
    if (message.coinType !== 0) {
      writer.uint32(16).uint32(message.coinType);
    }
    if (message.account !== 0) {
      writer.uint32(24).uint32(message.account);
    }
    if (message.change === true) {
      writer.uint32(32).bool(message.change);
    }
    if (message.addressIndex !== 0) {
      writer.uint32(40).uint32(message.addressIndex);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): BIP44Params {
    const reader = input instanceof _m0.Reader ? input : new _m0.Reader(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = { ...baseBIP44Params } as BIP44Params;
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          message.purpose = reader.uint32();
          break;
        case 2:
          message.coinType = reader.uint32();
          break;
        case 3:
          message.account = reader.uint32();
          break;
        case 4:
          message.change = reader.bool();
          break;
        case 5:
          message.addressIndex = reader.uint32();
          break;
        default:
          reader.skipType(tag & 7);
          break;
      }
    }
    return message;
  },

  fromJSON(object: any): BIP44Params {
    const message = { ...baseBIP44Params } as BIP44Params;
    if (object.purpose !== undefined && object.purpose !== null) {
      message.purpose = Number(object.purpose);
    } else {
      message.purpose = 0;
    }
    if (object.coinType !== undefined && object.coinType !== null) {
      message.coinType = Number(object.coinType);
    } else {
      message.coinType = 0;
    }
    if (object.account !== undefined && object.account !== null) {
      message.account = Number(object.account);
    } else {
      message.account = 0;
    }
    if (object.change !== undefined && object.change !== null) {
      message.change = Boolean(object.change);
    } else {
      message.change = false;
    }
    if (object.addressIndex !== undefined && object.addressIndex !== null) {
      message.addressIndex = Number(object.addressIndex);
    } else {
      message.addressIndex = 0;
    }
    return message;
  },

  toJSON(message: BIP44Params): unknown {
    const obj: any = {};
    message.purpose !== undefined && (obj.purpose = message.purpose);
    message.coinType !== undefined && (obj.coinType = message.coinType);
    message.account !== undefined && (obj.account = message.account);
    message.change !== undefined && (obj.change = message.change);
    message.addressIndex !== undefined && (obj.addressIndex = message.addressIndex);
    return obj;
  },

  fromPartial(object: DeepPartial<BIP44Params>): BIP44Params {
    const message = { ...baseBIP44Params } as BIP44Params;
    if (object.purpose !== undefined && object.purpose !== null) {
      message.purpose = object.purpose;
    } else {
      message.purpose = 0;
    }
    if (object.coinType !== undefined && object.coinType !== null) {
      message.coinType = object.coinType;
    } else {
      message.coinType = 0;
    }
    if (object.account !== undefined && object.account !== null) {
      message.account = object.account;
    } else {
      message.account = 0;
    }
    if (object.change !== undefined && object.change !== null) {
      message.change = object.change;
    } else {
      message.change = false;
    }
    if (object.addressIndex !== undefined && object.addressIndex !== null) {
      message.addressIndex = object.addressIndex;
    } else {
      message.addressIndex = 0;
    }
    return message;
  },
};

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined | Long;
export type DeepPartial<T> = T extends Builtin
  ? T
  : T extends Array<infer U>
  ? Array<DeepPartial<U>>
  : T extends ReadonlyArray<infer U>
  ? ReadonlyArray<DeepPartial<U>>
  : T extends {}
  ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

if (_m0.util.Long !== Long) {
  _m0.util.Long = Long as any;
  _m0.configure();
}
