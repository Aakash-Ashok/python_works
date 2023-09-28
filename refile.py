from re import *
# violations=["kl-08-av-2794",
#             "kl-08-av-4970",
#             "kl-01-av-14",
#             "kl-01-av-1",
#             "kl-01-av-12",
#             "TN-01-av-1",
#             "ghz-01-avO-1",
#             "0kl-01-av-10"
#             ]

# rule="[k][l][-][\d]{2}[-][a-z]{2}[-][\d]{1,4}"

# for i in violations:
#     matcher=fullmatch(rule,i)
#     if matcher!=None:
#         print(i)



tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
rule="[@][a-zA-Z0-9_]+"
matcher=finditer(rule,tweets)
for m in matcher:
    print(m.group()) 