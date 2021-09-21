from pow import mine


hyperlink = 'https://btc.com/00000000000000000025a9c24d3f7cac8a2acf9ee6fbf627cc71cd1b8942da43'
height = '#566023'

version = 0x20000000
prev_block = "0000000000000000001834a4c63c1c8763b61797c76a13646b94ac467d48d015"
merkle_root = "86a1405f43a587ef829d61dc5c63ea7da906e8fca680fcb23b6082159d59c030"
timestamp = "2019-03-07 16:41:43"
bits = 0x172e5b50


mine(version, prev_block, merkle_root, timestamp, bits)
