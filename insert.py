
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from random import randint, choice
from faker import Faker
from create import Houses, Seller, Agent, Office, Buyer, Sales, Base,AgentOffice,sessionmaker,session


def populate(curr_session):
    """
    the function below uses the faker library to populate fake data to insert 
    into the tables
    """
    fake=Faker()

    # Create sellers
    sellers = []
    for i in range(10):
        seller = Seller(
            seller_name=fake.name(),
            seller_email=fake.email(),
            seller_mobile=fake.phone_number()
        )
        sellers.append(seller)

    curr_session.add_all(sellers)
    curr_session.commit()

    # Create offices
    offices = []
    for i in range(6):
        office = Office(
            name=fake.company(),
            location=fake.address(),
        )
        offices.append(office)

    curr_session.add_all(offices)
    curr_session.commit()

    # Create agents
    agents = []
    for i in range(15):
        agent = Agent(
            agent_name=fake.name(),
            agent_number=fake.phone_number(),
        )
        agents.append(agent)

    curr_session.add_all(agents)
    curr_session.commit()

    #create agentoffice
    #create agentoffice
    agentoffices = []
    agentofficesdict={}
    for agent in agents:
        officeid = choice(offices).officeid
        for agentoffice in agentoffices:
            if agentoffice.agentid == agent.agentid:
                officeid = agentoffice.officeid
                break
        agentoffice = AgentOffice(
            agentid=agent.agentid,
            officeid=officeid,
        )
        agentoffices.append(agentoffice)
        agentofficesdict[agent.agentid] = officeid

    curr_session.add_all(agentoffices)
    curr_session.commit()


    # Create buyers
    buyers = []
    for i in range(20):
        buyer = Buyer(
            buyer_name=fake.name(),
            buyer_email=fake.email(),
            buyer_phone=fake.phone_number()
        )
        buyers.append(buyer)

    curr_session.add_all(buyers)
    curr_session.commit()


    # Create houses
    houses = []
    for i in range(30):
        seller = choice(sellers)
        agent = choice(agents)
        officeid = agentofficesdict[agent.agentid]
        house = Houses(
            sellerid=seller.sellerid,
            agentid=agent.agentid,
            officeid=officeid,
            bedrooms=randint(1, 5),
            bathrooms=randint(1, 5),
            zipcode=fake.zipcode(),
            listing_price=randint(70000, 2000000),
            date_listing=fake.date_time_between(start_date='-3y', end_date='-1y').date(),
            sold=choice([False])
        )
        houses.append(house)

    curr_session.add_all(houses)
    curr_session.commit()


    curr_session.add_all(houses)
    curr_session.commit()

    # Create sales
    sales = []
    sales_price=[]
    used_houseids = set()

    sales_price=[(randint(70000, 2000000)) for i in range(15)]
    for i in range(15):
        house = choice(houses)
        while house.houseid in used_houseids:
            house = choice(houses)
        used_houseids.add(house.houseid)
        sale = Sales(
            houseid=house.houseid,
            buyerid=choice(buyers).buyerid,
            agentid=house.agentid,
            officeid=house.officeid,
            sell_price=sales_price[i],
            sell_date=fake.date_time_between(start_date='-1y', end_date='now').date(),
            commision=Sales.get_commision(sales_price[i])
        )
        
        sales.append(sale)
        house.sold = True
        curr_session.commit() 

    curr_session.add_all(sales)
    curr_session.commit()
if __name__ =="__main__":
    populate(session)
