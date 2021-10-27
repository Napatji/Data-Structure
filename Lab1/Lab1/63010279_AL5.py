bid = [int(e) for e in input("Enter All Bid : ").split()]
if len(bid) < 2:
    print("not enough bidder")
else:
    maxbid = max(bid) ##หาIndexที่มีค่าbidสูงสุด
    highest_bid = bid.index(maxbid) ##แสดงIndexที่มีค่าbidสูงสุด
    same_bid = bid.count(bid[bid.index(maxbid)]) ##หาIndexที่มีค่าbidสูงสุดว่ามีกี่ตัว
    if same_bid >= 2:
        print("error : have more than one highest bid")
    elif same_bid == 1:
        ref_bid = list(bid) ##สร้าง reference ของ bid
        del ref_bid[highest_bid]
        max_refbid = max(ref_bid)
        highest_refbid = ref_bid.index(max_refbid)
        print("winner bid is",bid[highest_bid], "need to pay",ref_bid[highest_refbid])
