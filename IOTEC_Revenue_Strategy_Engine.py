import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime



# =========================================================

# IOTEC REVENUE STRATEGY ENGINE

# =========================================================



print("")

print("===================================================")

print(" IOTEC REVENUE STRATEGY ENGINE")

print("===================================================")

print("")



# =========================================================

# SECTOR DATABASE

# =========================================================



sectors = [



    {

        "name": "Enterprise Automation",

        "market_demand": 10,

        "sales_speed": 9,

        "ticket": 10,

        "recurrence": 9,

        "global_scale": 10,

        "competition": 6

    },



    {

        "name": "Judicial Analytics",

        "market_demand": 8,

        "sales_speed": 7,

        "ticket": 10,

        "recurrence": 8,

        "global_scale": 7,

        "competition": 4

    },



    {

        "name": "Healthcare Systems",

        "market_demand": 10,

        "sales_speed": 7,

        "ticket": 10,

        "recurrence": 10,

        "global_scale": 9,

        "competition": 7

    },



    {

        "name": "Agro Intelligence",

        "market_demand": 9,

        "sales_speed": 8,

        "ticket": 9,

        "recurrence": 8,

        "global_scale": 9,

        "competition": 5

    },



    {

        "name": "Education Systems",

        "market_demand": 9,

        "sales_speed": 5,

        "ticket": 7,

        "recurrence": 9,

        "global_scale": 8,

        "competition": 7

    },



    {

        "name": "AI Concierge",

        "market_demand": 10,

        "sales_speed": 9,

        "ticket": 9,

        "recurrence": 10,

        "global_scale": 10,

        "competition": 8

    },



    {

        "name": "Premium Media Systems",

        "market_demand": 8,

        "sales_speed": 8,

        "ticket": 8,

        "recurrence": 7,

        "global_scale": 9,

        "competition": 6

    },



    {

        "name": "Public Management",

        "market_demand": 8,

        "sales_speed": 5,

        "ticket": 10,

        "recurrence": 9,

        "global_scale": 8,

        "competition": 5

    },



    {

        "name": "Industrial Automation",

        "market_demand": 9,

        "sales_speed": 8,

        "ticket": 10,

        "recurrence": 9,

        "global_scale": 10,

        "competition": 6

    },



    {

        "name": "Security Intelligence",

        "market_demand": 10,

        "sales_speed": 8,

        "ticket": 10,

        "recurrence": 9,

        "global_scale": 10,

        "competition": 5

    }

]



# =========================================================

# SCORE ENGINE

# =========================================================



for sector in sectors:
    pass



    score = (



        sector["market_demand"] +

        sector["sales_speed"] +

        sector["ticket"] +

        sector["recurrence"] +

        sector["global_scale"]



    ) - sector["competition"]



    sector["score"] = score



# =========================================================

# SORT

# =========================================================



ranking = sorted(

    sectors,

    key=lambda x: x["score"],

    reverse=True

)



# =========================================================

# DISPLAY

# =========================================================



print("========== GLOBAL REVENUE PRIORITY ==========")

print("")



position = 1



for item in ranking:
    pass



    print(

        f"{position}. "

        f"{item['name']} "

        f"| SCORE {item['score']}"

    )



    position += 1



# =========================================================

# STRATEGIC REPORT

# =========================================================



print("")

print("========== STRATEGIC ANALYSIS ==========")

print("")



top = ranking[0]



print(

    f"TOP PRIORITY: {top['name']}"

)



print("")

print("RECOMMENDATION:")

print(

    "Focus initial commercial force "

    "on highest conversion sectors."

)



print("")

print("OPERATIONAL STATUS:")

print("REVENUE STRATEGY ACTIVE")



# =========================================================

# SAVE REPORT

# =========================================================



report = []



report.append(

    "IOTEC REVENUE STRATEGY REPORT"

)



report.append(

    f"Generated: {datetime.now()}"

)



report.append("")



for item in ranking:
    pass



    report.append(

        f"{item['name']} "

        f"- SCORE {item['score']}"

    )



path = (

    r"C:\Tecnologia\reports"

    r"\revenue_strategy_report.txt"

)



with open(

    path,

    "w",

    encoding="utf-8"

) as file:



    file.write("\n".join(report))



print("")

print("REPORT SAVED:")

print(path)



print("")

print("===================================================")

print(" IOTEC REVENUE ENGINE ONLINE")

print("===================================================")







