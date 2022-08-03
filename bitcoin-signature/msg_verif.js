var SHA256 = require("crypto-js/sha256");
var BigInteger = require('bigi')
const { createHash } = require('crypto');

function msg_numToVarInt(i) {
  if (i < 0xfd) {
    return [i];
  } else if (i <= 0xffff) {
    // can't use numToVarInt from bitcoinjs, BitcoinQT wants big endian here (!)
    return [0xfd, i & 255, i >>> 8];
  } else if (i <= 0xffffffff) {
    return [0xfe, i & 255, (i >>> 8) & 255, (i >>> 16) & 255, i >>> 24];
  } else {
      throw ("message too large");
  }
}

function msg_bytes(message) {
  let utf8Encode = new TextEncoder();
  var b = utf8Encode.encode(message)
  return msg_numToVarInt(b.length).concat(b);
}

function msg_digest(message) {
  var b = msg_bytes("Bitcoin Signed Message:\n").concat(msg_bytes(message));
  console.log("[" + b.toString() + "]");
}


msg_digest("Julio");
