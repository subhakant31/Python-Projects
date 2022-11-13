from art import logo
print(logo)
bid_dict={}
bid_list=[]
endloop=True
while endloop!=False:
    name=input("Enter your name")
    bid=int(input("Enter your bid amount"))
    check=input("Are there any other people ?")
    bid_dict[name]=bid
    if check!="yes":
        endloop=False
    bid_list.append(bid)
def highest(bid_list):
    bid_list.sort()
    maximum=bid_list[len(bid_list)-1]
    return maximum
maximum_bid=highest(bid_list)
max_bidder=""
for item in bid_dict:
    if bid_dict[item]==maximum_bid:
        max_bidder=item
        break
print(f"Highest Bidder is {maximum_bid} by {max_bidder}")































