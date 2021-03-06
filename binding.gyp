{
  "targets": [{
    "target_name": "bcoin-native",
    "sources": [
      "./src/poly1305-donna/poly1305-donna.c",
      "./src/chacha20-simple/chacha20_simple.c",
      "./src/scrypt/insecure_memzero.c",
      "./src/scrypt/sha256.c",
      "./src/scrypt/scrypt.c",
      "./src/chacha20.cc",
      "./src/poly1305.cc",
      "./src/hash.cc",
      "./src/cipher.cc",
      "./src/base58.cc",
      "./src/scrypt.cc",
      "./src/scrypt_async.cc",
      "./src/murmur3.cc",
      "./src/siphash.cc",
      "./src/bcn.cc"
    ],
    "cflags": [
      "-Wall",
      "-Wno-maybe-uninitialized",
      "-Wno-uninitialized",
      "-Wno-unused-function",
      "-Wextra",
      "-O3"
    ],
    "cflags_c": [
      "-std=c99"
    ],
    "defines": [
      "POLY1305_64BIT"
    ],
    "cflags_cc+": [
      "-std=c++0x"
    ],
    "include_dirs": [
      "/usr/local/include",
      "<(node_root_dir)/deps/openssl/openssl/include",
      "<!(node -e \"require('nan')\")"
    ],
  }]
}
