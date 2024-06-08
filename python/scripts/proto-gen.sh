#!/bin/bash
set -o errexit -o nounset -o pipefail
command -v shellcheck >/dev/null && shellcheck "$0"

#echo "install betterproto... pre-release for now. stable one has some issues"
#pip install --upgrade "avast.betterproto[compiler]"
#pip install --upgrade "betterproto[compiler]" --pre
#echo "install MarkupSafe==2.3.1 due to dependency"
#pip install MarkupSafe==2.3.1

OUT_DIR="../terra_proto"

mkdir -p "$OUT_DIR"

echo "Processing proto files ..."
PROTOBUF_DIR=$(readlink -f "../../protobuf")
COSMOS_SDK_DIR=$(readlink -f "../../cosmos-sdk/proto")
ALLIANCE_DIR=$(readlink -f "../../alliance/proto")
IBC_DIR=$(readlink -f "../../ibc-go/proto")
PFM_DIR=$(readlink -f "../../ibc-apps/middleware/packet-forward-middleware/proto")
WASMD_DIR=$(readlink -f "../../wasmd/proto")
GRPC_DIR=$(readlink -f "../../grpc-gateway")
COSMOS_DIR=$(readlink -f "../../cosmos-proto/proto")
TERRA_DIR=$(readlink -f "../../terra/proto")
POB_DIR=$(readlink -f "../../pob/proto")

protoc  \
  --python_betterproto_out="${OUT_DIR}" \
  --proto_path "$PROTOBUF_DIR" \
  --proto_path "$PROTOBUF_DIR/protobuf" \
  --proto_path "$COSMOS_SDK_DIR" \
  --proto_path "$ALLIANCE_DIR" \
  --proto_path "$IBC_DIR" \
  --proto_path "$PFM_DIR" \
  --proto_path "$WASMD_DIR" \
  --proto_path "$GRPC_DIR" \
  --proto_path "$GRPC_DIR/third_party" \
  --proto_path "$GRPC_DIR/third_party/googleapis" \
  --proto_path "$COSMOS_DIR" \
  --proto_path "$TERRA_DIR" \
  --proto_path "$POB_DIR" \
  $(find $COSMOS_SDK_DIR $ALLIANCE_DIR $IBC_DIR $PFM_DIR $WASMD_DIR $COSMOS_DIR $TERRA_DIR $POB_DIR -path -prune -o -name '*.proto' -print0 | xargs -0) 

