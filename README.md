# LinkDecrypt

Command-Line tool to decrypt Adf.ly links in batch mode.

## Install

    pip install linkdecrypt


## Usage

    linkdecrypt [-f/--file] URI

Example

```bash
$ linkdecrypt http://adf.ly/1234
# Output: http://mega.co.nz/!#...

$ linkdecrypt -f links.txt
# Output: output.txt file with decrypted links
```

