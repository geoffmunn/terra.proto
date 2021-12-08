# terra.proto (Rust)

## How to use
### Cargo
```
[dependencies]
terra-proto = "{terraCoreVersion}"
```

## Maintenance
This section is for maintainers of this repo, not users.

### Requirements
* Rust
* Cargo
* protoc v3.17.3

### Getting started
```sh
make init
```

### Rebuilding types
```sh
make proto-gen

or 

cargo build
```

### Publish to Maven
```
make publish

or

cargo publish
```