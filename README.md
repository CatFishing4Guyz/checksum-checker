## checksum-checker
A simple Python script to calculate a file's checksum.
It doesn't require any dependencies (besides Python3,
obviously). Works fast, even for very large files.
It's intended to be simple, fast, and straightforward,
with no things like installing additional modules.

Supports:
* `SHA1`
* `SHA256`
* `SHA512`
* `MD5`
* `CRC32` (WIP)

`CRC32` is a little fucked up, it shows different results
compared to archivers and online alternatives. I don't
know why it does that.

## Credits
CatFishing4Guyz, code