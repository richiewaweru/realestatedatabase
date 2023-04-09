
from create import Houses,Sales,Office,Agent,AgentOffice,Seller,session,sessionmaker,AgentCommision
from insert import *
from sqlalchemy import select, desc,func,Text,text

from sqlalchemy import func, extract

from sqlalchemy import func
from datetime import datetime

#month and year to filter by
month = 8
year = 2022

# query to find the top 5 offices with the most sales in the specified month
results = session.query(Office.name, func.count(Sales.salesid)).join(Sales, Sales.officeid == Office.officeid) \
                .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                .group_by(Office.name).order_by(func.count(Sales.salesid).desc()).limit(5).all()
print("The top 5 offices with the most sales in the month of {}-{}:".format(month, year))
for result in results:
    print("Office: {},Sales: {}".format(result[0],result[1]))


from sqlalchemy import func, extract

#month and year to filter by
month = 8
year = 2022

# query to find the top 5 estate agents who have sold the most in the specified month
results = session.query(Agent.agent_name, Agent.agent_number, Sales.sell_date, Sales.sell_price) \
                 .join(Sales, Agent.agentid == Sales.agentid) \
                 .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                 .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                 .group_by(Agent.agent_name,Agent.agent_number, Sales.sell_date, Sales.sell_price) \
                 .order_by(func.count(Sales.salesid).desc()).limit(5).all()


print("Top 5 estate agents with the most sales in the month of {}-{}:".format(month, year))
for result in results:
    name,phone_number, sell_date, sale_price = result
    print("Estate agent: {},Phone number: {}, Sale date: {}, Sale price: {}".format(name,phone_number, sell_date, sale_price))



from sqlalchemy import func

# Query to join sales and agent tables, group by agent, and calculate commission
query = session.query(Agent.agentid, func.sum(Sales.commision).label('total_commision')).\
        join(Sales, Sales.agentid == Agent.agentid).\
        group_by(Agent.agentid)

# Loop through the query results and store commission in separate table
for result in query:
    agent_id = result[0]
    total_commision = result[1]
    agent_commision = AgentCommision(agentid=agent_id, totalcommision=total_commision)
    session.add(agent_commision)
    
# Commit changes to database
session.commit()





from sqlalchemy import func, extract

#month and year to filter by
month = 8
year = 2022

# query to calculate the average number of days on the market for houses sold in the specified month
average_days = session.query(func.avg(func.julianday(Sales.sell_date) - func.julianday(Houses.date_listing))) \
                      .join(Houses, Sales.houseid == Houses.houseid) \
                      .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                      .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                      .scalar()
# print the results
print("The average number of days on the market for houses sold in the month of {}-{} is: {} days".format(month, year, average_days))


from sqlalchemy import func, extract

#month and year to filter by
month = 8
year = 2022

# query to calculate the average selling price for houses sold in the specified month
average_price = session.query(func.avg(Sales.sell_price)) \
                       .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                       .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                       .scalar()
# print the results
print("The average selling price for houses sold in the month of {}-{} is: ${:,.2f}".format(month, year, average_price))
