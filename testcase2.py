from pow import mine


hyperlink = 'https://btc.com/0000000000000000001834a4c63c1c8763b61797c76a13646b94ac467d48d015'
height = '#566022'

version = 0x20000000
prev_block = "0000000000000000002612be9def114da3dba260cd13ffb8920df801ce26c101"
merkle_root = "ee0cdba8236088713e33a2591adf58fc4d8069dd61ed44145d22aabe542bae3b"
timestamp = "2019-03-07 16:35:53"
bits = 0x172e5b50


mine(version, prev_block, merkle_root, timestamp, bits)
