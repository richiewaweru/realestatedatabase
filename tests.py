import unittest
from datetime import datetime,date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create import *
from sqlalchemy import func

#create a testing database
engine = create_engine('sqlite:///tests.db')
Session = sessionmaker(bind=engine)


class TestInsert(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        # sample data for Houses
        house1 = Houses(sellerid=1, agentid=1, officeid=1, bedrooms=3, bathrooms=2, zipcode=12345, listing_price=250000, date_listing=datetime.strptime('2022-02-15', '%Y-%m-%d').date(),sold=True)
        house2 = Houses(sellerid=2, agentid=1, officeid=1, bedrooms=4, bathrooms=3, zipcode=23456, listing_price=450000, date_listing=datetime.strptime('2022-03-01', '%Y-%m-%d').date(), sold=True)
        house3 = Houses(sellerid=3, agentid=2, officeid=1, bedrooms=2, bathrooms=1, zipcode=34567, listing_price=150000, date_listing=datetime.strptime('2022-01-10', '%Y-%m-%d').date(), sold=True)
        house4 = Houses(sellerid=4, agentid=2, officeid=2, bedrooms=5, bathrooms=4, zipcode=45678, listing_price=750000, date_listing=datetime.strptime('2022-08-05', '%Y-%m-%d').date(),sold=True)
        house5 = Houses(sellerid=5, agentid=4, officeid=3, bedrooms=3, bathrooms=2, zipcode=56789, listing_price=300000, date_listing=datetime.strptime('2022-02-20', '%Y-%m-%d').date(),sold=True)
        house6 = Houses(sellerid=6, agentid=4, officeid=3, bedrooms=2, bathrooms=1, zipcode=67890, listing_price=100000, date_listing=datetime.strptime('2022-07-20', '%Y-%m-%d').date(), sold=True)
        house7 = Houses(sellerid=2, agentid=4, officeid=3, bedrooms=3, bathrooms=2, zipcode=56789, listing_price=3000000, date_listing=datetime.strptime('2022-07-20', '%Y-%m-%d').date(),sold=True)
        house8 = Houses(sellerid=2, agentid=4, officeid=3, bedrooms=2, bathrooms=1, zipcode=67890, listing_price=1000000, date_listing=datetime.strptime('2022-07-20', '%Y-%m-%d').date(), sold=True)

        house_list=[house1,house2,house3,house4,house5,house6,house7,house8]

        # sample data for Seller
        seller1 = Seller(seller_name='John Smith', seller_email='john.smith@example.com', seller_mobile='555-1234')
        seller2 = Seller(seller_name='Jane Doe', seller_email='jane.doe@example.com', seller_mobile='555-5678')
        seller3 = Seller(seller_name='Bob Johnson', seller_email='bob.johnson@example.com', seller_mobile='555-2468')
        seller4 = Seller(seller_name='Sue Wilson', seller_email='sue.wilson@example.com', seller_mobile='555-7890')
        seller5 = Seller(seller_name='Mike Brown', seller_email='mike.brown@example.com', seller_mobile='555-1357')
        seller6 = Seller(seller_name='Lisa Davis', seller_email='lisa.davis@example.com', seller_mobile='555-8023')

        seller_list=[seller1,seller2,seller3,seller4,seller5,seller6]

        # sample data for Agent
        agent1 = Agent(agent_name='Tom Jones', agent_number='555-1111')
        agent2 = Agent(agent_name='Sarah Lee', agent_number='555-2222')
        agent3 = Agent(agent_name='Mark Smith', agent_number='555-3333')
        agent4 = Agent(agent_name='Laura Smith', agent_number='555-4444')
        agent5 = Agent(agent_name='David Lee', agent_number='555-5555')
        agent6 = Agent(agent_name='Amy Johnson', agent_number='555-6666')

        agent_list=[agent1,agent2,agent3,agent4,agent5,agent6]

        # sample data for Office
        office1 = Office(name='Downtown Office', location='123 Main St')
        office2 = Office(name='Uptown Office', location='456 Elm St')
        office3 = Office(name='Midtown Office', location='789 Oak St')

        office_list=[office1,office2,office3]

        # sample data for AgentOffice
        agentoffice1 = AgentOffice(agentid=1, officeid=1)
        agentoffice2 = AgentOffice(agentid=2, officeid=1)
        agentoffice3 = AgentOffice(agentid=3, officeid=2)
        agentoffice4 = AgentOffice(agentid=4, officeid=2)
        agentoffice5 = AgentOffice(agentid=5, officeid=3)

        agentofficeslist=[agentoffice1,agentoffice2,agentoffice3,agentoffice4,agentoffice5]
        # Buyers
        buyer1 = Buyer(buyer_name='John Smith', buyer_email='john.smith@gmail.com', buyer_phone='123-456-7890')
        buyer2 = Buyer(buyer_name='Jane Doe', buyer_email='jane.doe@gmail.com', buyer_phone='555-555-5555')
        buyer3 = Buyer(buyer_name='Mike Johnson', buyer_email='mike.johnson@gmail.com', buyer_phone='111-111-1111')
        buyer4 = Buyer(buyer_name='Emily Wilson', buyer_email='emily.wilson@gmail.com', buyer_phone='222-222-2222')
        buyer5 = Buyer(buyer_name='David Lee', buyer_email='david.lee@gmail.com', buyer_phone='333-333-3333')
        buyer6 = Buyer(buyer_name='Sarah Brown', buyer_email='sarah.brown@gmail.com', buyer_phone='444-444-4444')
        buyer7 = Buyer(buyer_name='Brian Jackson', buyer_email='brian.jackson@gmail.com', buyer_phone='777-777-7777')
        buyer8 = Buyer(buyer_name='Rachel Chen', buyer_email='rachel.chen@gmail.com', buyer_phone='888-888-8888')
        buyer9 = Buyer(buyer_name='Tom Wilson', buyer_email='tom.wilson@gmail.com', buyer_phone='999-999-9999')
        buyer10 = Buyer(buyer_name='Jessica Liu', buyer_email='jessica.liu@gmail.com', buyer_phone='777-888-9999')
        buyer_list=[buyer1,buyer2,buyer3,buyer4,buyer5,buyer6,buyer7,buyer8,buyer9,buyer10]
        # Sales
        sale1 = Sales(houseid=1, buyerid=1, agentid=1, officeid=1, sell_price=500000, sell_date=datetime.strptime('2023-01-01', '%Y-%m-%d').date(),commision=Sales.get_commision(500000))
        sale2 = Sales(houseid=2, buyerid=2, agentid=2, officeid=1, sell_price=600000, sell_date=datetime.strptime('2023-01-01', '%Y-%m-%d').date(),commision=Sales.get_commision(600000))
        sale3 = Sales(houseid=3, buyerid=3, agentid=3, officeid=2, sell_price=700000, sell_date=datetime.strptime('2023-03-01', '%Y-%m-%d').date(),commision=Sales.get_commision(700000))
        sale4 = Sales(houseid=4, buyerid=4, agentid=4, officeid=2, sell_price=800000, sell_date=datetime.strptime('2023-02-01', '%Y-%m-%d').date(),commision=Sales.get_commision(800000))
        sale5 = Sales(houseid=5, buyerid=5, agentid=5, officeid=3, sell_price=900000, sell_date=datetime.strptime('2022-05-01', '%Y-%m-%d').date(),commision=Sales.get_commision(900000))
        sale6 = Sales(houseid=6, buyerid=6, agentid=2, officeid=1, sell_price=1000000, sell_date=datetime.strptime('2022-08-01', '%Y-%m-%d').date(),commision=Sales.get_commision(1000000))
        sale7 = Sales(houseid=7, buyerid=7, agentid=3, officeid=2, sell_price=1100000, sell_date=datetime.strptime('2022-08-01', '%Y-%m-%d').date(),commision=Sales.get_commision(1100000))
        sale8 = Sales(houseid=8, buyerid=8, agentid=5, officeid=3, sell_price=1200000, sell_date=datetime.strptime('2022-08-01', '%Y-%m-%d').date(),commision=Sales.get_commision(1200000))
        sales_list=[sale1,sale2,sale3,sale4,sale5,sale6,sale7,sale8]



        # add sample data to the session
        self.session.add_all(house_list)
        self.session.add_all(seller_list)
        self.session.add_all(agent_list)
        self.session.add_all(office_list)
        self.session.add_all(agentofficeslist)
        self.session.add_all(buyer_list)
        self.session.add_all(sales_list)
        # commit the changes to the database
        self.session.commit()

    #teaardown the database after each test
    def tearDown(self):
        self.session.rollback()
        self.session.close()
        Base.metadata.drop_all(engine)
    #test whether we can insert data in our seller table
    def test_insert_seller(self):
        seller = Seller(
            seller_name='John Doe',
            seller_email='john.doe@example.com',
            seller_mobile='1234567890'
        )
        self.session.add(seller)
        self.session.commit()
        self.assertIsNotNone(seller.sellerid)

    #test whether we can insert data in our house table
    def test_insert_house(self):
        seller = Seller(
            seller_name='John Doe',
            seller_email='john.doe@example.com',
            seller_mobile='1234567890'
        )
        self.session.add(seller)
        self.session.commit()
        house = Houses(
            sellerid=seller.sellerid,
            bedrooms=3,
            bathrooms=2,
            zipcode=12345,
            listing_price=100000,
            date_listing=datetime.now(),
            sold=False
        )
        self.session.add(house)
        self.session.commit()
        self.assertIsNotNone(house.houseid)

    #test whether the query to return the top 5 offices with most sales works
    def test_top_five_offices(self):
        month = 8
        year = 2022
        results = self.session.query(Office.name, func.count(Sales.salesid)).join(Sales, Sales.officeid == Office.officeid) \
                .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                .group_by(Office.name).order_by(func.count(Sales.salesid).desc()).limit(5).all()
        self.assertEqual(results,[('Uptown Office', 1), ('Midtown Office', 1), ('Downtown Office', 1)])

    #test whether the query to return the top 5 agents with most sales works
    def test_top_five_agents(self):
        #the month and year to filter by
        month = 8
        year = 2022

        # query to find the top 5 estate agents who have sold the most in the specified month
        results = self.session.query(Agent.agent_name, Agent.agent_number, Sales.sell_date, Sales.sell_price) \
                        .join(Sales, Agent.agentid == Sales.agentid) \
                        .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                        .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                        .group_by(Agent.agent_name,Agent.agent_number, Sales.sell_date, Sales.sell_price) \
                        .order_by(func.count(Sales.salesid).desc()).limit(5).all()


        query_output=[]
        for result in results:
            name,phone_number, sell_date, sale_price = result
            output=(result[0],result[1],result[2].strftime('%Y-%m-%d'),result[3])
            query_output.append(output)
          
    
        expected_output = [
                ("David Lee", "555-5555", "2022-08-01", 1200000),
                ("Mark Smith", "555-3333", "2022-08-01", 1100000),
                ("Sarah Lee", "555-2222", "2022-08-01", 1000000)
            ]
        self.assertEqual(query_output,expected_output)

    ##test whether the query to return commision works
    def test_commison(self):
        # Query to join sales and agent tables, group by agent, and calculate commission
        results = self.session.query(Agent.agentid, func.sum(Sales.commision).label('total_commision')).\
                join(Sales, Sales.agentid == Agent.agentid).\
                group_by(Agent.agentid)

        query_out=[]
        for result in results:
            agentid,comm=result
            agent_id = result[0]
            total_commision = result[1]
            query_out.append(result)
    
        expected=[(1, 30000),(2, 80000),(3, 79000),(4, 40000),(5, 93000)]

        self.assertEqual(query_out,expected)

    #test whether the query to return the average number of days a sold house was listed works
    def test_day_market(self):

        # set the month and year to filter by
        month = 8
        year = 2022
                # query to calculate the average number of days on the market for houses sold in the specified month
        average_days = self.session.query(func.avg(func.julianday(Sales.sell_date) - func.julianday(Houses.date_listing))) \
                            .join(Houses, Sales.houseid == Houses.houseid) \
                            .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                            .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                            .scalar()
        self.assertEqual(average_days,12)

    ##test whether the query to return the average price works
    def test_avg_price(self):
        from sqlalchemy import func, extract

        #the month and year to filter by
        month = 8
        year = 2022

        # query to calculate the average selling price for houses sold in the specified month
        average_price =self.session.query(func.avg(Sales.sell_price)) \
                            .filter(func.strftime('%m', Sales.sell_date) == str(month).zfill(2)) \
                            .filter(func.strftime('%Y', Sales.sell_date) == str(year)) \
                            .scalar()

        self.assertEqual(1100000,average_price)



if __name__ == '__main__':
    unittest.main()
