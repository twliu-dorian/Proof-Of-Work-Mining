import hashlib, time, struct, codecs

def mine(version, prev_block, merkle_root, timestamp, bits):
    
    #nonce = 0
    # testcase1.py
    #nonce = 0x7c000000

    #testcase2.py
    #nonce = 0x7a92319d
    
    #testcase3.property
    nonce = 0xae443126
    
    encodeVer = struct.pack("<L", version)
    encodePrevHash = codecs.decode(prev_block, "hex")[::-1]
    encodeMerkleRoot = codecs.decode(merkle_root, "hex")[::-1]
    encodeTime = struct.pack("<L", int(time.mktime(time.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))))
    #print('time : ',time.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
    encodeBits = struct.pack("<L", bits)
    #print('bits : ', bits)
    encodeNonce = struct.pack("<L", nonce)
    #print('nonce : ', nonce)
    hashInput = encodeVer + encodePrevHash + encodeMerkleRoot + encodeTime + encodeBits + encodeNonce
    #print('hashInput : ', hashInput)

    exp = bits >> 24

    sig = bits & 0xffffff

    threshold = '%064x' % (sig * (1 << 8*(exp - 3)))

    encodeThreshold = codecs.decode(threshold, "hex")

    #print('threshold : ',threshold)
    #print("00000000ffff0000000000000000000000000000000000000000000000000000")
    #print('encodeThreshold : ',encodeThreshold)

    count = 0
    """Mining"""
    while nonce < 0x100000000:
        hash = (hashlib.sha256(hashlib.sha256(hashInput).digest()).digest())[::-1]
        print('hash : ', codecs.encode(hash, "hex"), '     nonce : ', hex(nonce))
        if hash < encodeThreshold:
            out = codecs.encode(hash, "hex")
            print('\n\n\nSuccessfully mined a new block :','\nhash : ', out, '     nonce : ', hex(nonce))
            return out

        count+=1
        nonce+=1
        encodeNonce = struct.pack("<L", nonce)
        hashInput = encodeVer + encodePrevHash + encodeMerkleRoot + encodeTime + encodeBits + encodeNonce



