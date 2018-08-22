# from pymongo import MongoClient
# import pandas as pd
#
# db= MongoClient("172.16.2.16",29019)["rpt_task"]["veri_report_task"]
#
#
# print(db)
#
# st = 1534694400000
# et = 1534780800000
#
# res = db.find({"update_time":{"$gte":st,"$lt":et}}, {"_id":0, "org_name":1, "id_card_num":1,"real_name":1,"update_time":1,
#                                               "cell":1}).sort([("update_time",-1)] )
#
# df = pd.DataFrame(list(res))
# print(df)
# df = df.drop_duplicates(subset=["org_name", "id_card_num","real_name","cell"])
# df.rename(columns={"org_name":"auth_org","id_card_num":"idcard","real_name":"name","cell":"phone"}, inplace="True")
# df["gray_version"] = 4.2
# df= df[['auth_org', 'gray_version','idcard','name', 'phone','update_time']]
# df.to_csv("8.20.txt", header=True, index=False, sep=",", mode="a")
res = "  "
print(res.strip()[0])
