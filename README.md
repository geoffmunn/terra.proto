# Terra Proto

This repository contains three diferent native clients ([JS](./js/), [Rust](./rust/), [Python](./python/)) to interact with Terra Core. These clients are automatically generated using protoc compiler and they are individually published to the different code repositories.

## IMPORTANT NOTE

**This is a fork of the official project, found at https://github.com/terra-money/terra.proto**

This version includes the missing market module, and some minor code changes to make it work on the Luna Classic chain.

It is specifically built to work with the Terra Classic SDK: https://pypi.org/project/terra-classic-sdk/

## Recent changes

### 3.1.1

- All Python packages updated to the latest version.
 - Except betterproto which is already on a pre-release version and the latest version presented errors.

### 3.1.0

- Merged changes from the official terra.proto library. No functionality changes or improvements.

### 3.0.2

- Terra.proto for Terra Classic now has native support for Osmosis. You can send LUNC to an Osmosis address and use it to swap LUNC to any Osmosis-supported coin or token.

## Development

Each of the libraries have its own `Makefile` that contain 4 main entry commands:

- `init` : initialize the github submoudles,
- `proto-gen` : generate the proto files,
- `build` : build the project abstracting each language peculiarities,
- `publish` : push the build to the the code repository to be used by anyone (abstracting the publish peculiarities).
