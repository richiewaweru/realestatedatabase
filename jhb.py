from datetime import datetime
from random import randint, choice
from faker import Faker
from create import Houses, Seller, Agent, Office, Buyer, Sales, Base,AgentOffice,session


def insert():
    fake=Faker()

    # Create sellers
    sellers = []
    for i in range(5):
        seller = Seller(
            seller_name=fake.name(),
            seller_email=fake.email(),
            seller_mobile=fake.phone_number()
        )
        sellers.append(seller)

    session.add_all(sellers)
    session.commit()

    # Create offices
    offices = []
    for i in range(4):
        office = Office(
            name=fake.company(),
            location=fake.address(),
        )
        offices.append(office)

    session.add_all(offices)
    session.commit()

    # Create agents
    agents = []
    for i in range(10):
        agent = Agent(
            agent_name=fake.name(),
            agent_number=fake.phone_number(),
        )
        agents.append(agent)

    session.add_all(agents)
    session.commit()

    #create agentoffice
    agentoffices = []
    for i in range(10):
        agentoffice = AgentOffice(
            agentid=choice(agents).agentid,
            officeid=choice(offices).officeid,
        )
        agentoffices.append(agentoffice)

    session.add_all(agentoffices)
    session.commit()

    # Create buyers
    buyers = []
    for i in range(20):
        buyer = Buyer(
            buyer_name=fake.name(),
            buyer_email=fake.email(),
            buyer_phone=fake.phone_number()
        )
        buyers.append(buyer)

    session.add_all(buyers)
    session.commit()

    # Create houses
    houses = []
    for i in range(30):
        house = Houses(
            sellerid=choice(sellers).sellerid,
            agentid=choice(agents).agentid,
            officeid=choice(offices).officeid,
            bedrooms=randint(1, 5),
            bathrooms=randint(1, 5),
            zipcode=fake.zipcode(),
            listing_price=randint(70000, 2000000),
            date_listing=fake.date_time_between(start_date='-3y', end_date='now'),
            sold=choice([True, False])
        )
        houses.append(house)

    session.add_all(houses)
    session.commit()

    # Create sales
    sales = []
    sales_price=[]

    sales_price=[(randint(70000, 2000000)) for i in range(15)]
    for i in range(15):
        sale = Sales(
            houseid=choice(houses).houseid,
            agentid=choice(agents).agentid,
            sell_price=sales_price[i],
            sell_date=fake.date_time_between(start_date='-2y', end_date='now'),
            commision=Sales.get_commision(sales_price[i])
        )
        
        sales.append(sale)

    session.add_all(sales)
    session.commit()

if __name__ =="__main__":
    insert()
