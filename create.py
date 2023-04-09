import sqlalchemy
from sqlalchemy import create_engine, Column, Text, Integer, DateTime, Numeric, ForeignKey, Index,String,Date,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker 

# Create the tables
Base = declarative_base()
# Create the database
engine = create_engine('sqlite:///exame1.db')

Session = sessionmaker(bind=engine)
session = Session()

#this is the houses table
class Houses(Base):
    __tablename__ = 'houses'
    houseid = Column(Integer, primary_key = True)
    sellerid= Column(Integer,ForeignKey("seller.sellerid"),index=True)#foreign key
    agentid=Column(Integer,ForeignKey("agent.agentid"),index=True)#foreign key
    officeid=Column(Integer,ForeignKey("office.officeid"),index=True)#foreign key
    bedrooms = Column(Integer)
    bathrooms= Column(Integer)
    zipcode=Column(Integer)
    listing_price=Column(Integer)
    date_listing=Column(Date)
    sold=Column(Boolean)

    def __repr__(self):
             
        return "<Houses(houseid={0}, sellerid={1}, agentid={2},officeid={3},bedrooms={4},bathrooms={5},zipcode={6},listing_price={7},\
        date_listing={8},sold={9})>".format(self.houseid, self.sellerid, self.agentid,self.officeid,self.bedrooms,self.bathrooms,\
                                                        self.zipcode,self.listing_price,self.date_listing,self.sold)

#this is the sellers table
class Seller(Base):
    __tablename__ = 'seller'
    sellerid= Column(Integer, primary_key = True)
    seller_name = Column(Text)
    seller_email=Column(String)
    seller_mobile=Column(String)

    def __repr__(self):
        return "<Seller(sellerid={0}, seller_name={1},seller_email={2},seller_mobile={3})>".format(self.sellerid, self.seller_name,\
                                                                                                    self.seller_email,self.seller_mobile)
  
#this is the agents table
class Agent(Base):
    __tablename__ = 'agent'
    agentid = Column(Integer, primary_key = True)
    agent_name = Column(Text)
    agent_number=Column(String)

    def __repr__(self):     
        return "<Agent(agentid={0}, agent_name={1},agent_number={2})>".format(self.agentid, self.agent_name, self.agent_number)
  


    
   
#this is the offices table
class Office(Base):
    __tablename__ = 'office'
    officeid = Column(Integer, primary_key = True)
    name = Column(Text)
    location=Column(Text)

    def __repr__(self):    
        return "<Office(officeid={0}, name={1},location={2})>".format(self.officeid, self.name, self.location)

#this is the relational table linking agents and their respective offices
class AgentOffice(Base):
    __tablename__='agentoffice'
    agentofficeid=Column(Integer,primary_key=True)
    agentid = Column(Integer,ForeignKey("agent.agentid"))
    officeid = Column(Integer,ForeignKey("office.officeid"))

    def __repr__(self):    
        return "<AgentOffice(agentofficeid={0}, agentid={1},officeid={2})>".format(self.agentofficeid, self.agentid, self.officeid)

#this is the buyers table
class Buyer(Base):
    __tablename__ = 'buyer'
    buyerid = Column(Integer, primary_key = True)
    buyer_name = Column(Text)
    buyer_email=Column(String)
    buyer_phone=Column(String)

    def __repr__(self):    
        return "<Buyer(buyerid={0}, buyer_name={1},buyer_email={2},buyer_phone={3})>".format(self.buyerid, self.buyer_name, \
                                                                                             self.buyer_email,self.buyer_phone)

#this is the sales table
class Sales(Base):
    __tablename__ = 'sales'
    salesid=Column(Integer,primary_key=True)
    houseid=Column(Integer,ForeignKey("houses.houseid"),index=True)
    buyerid=Column(Integer,ForeignKey("buyer.buyerid"))
    agentid = Column(Integer,ForeignKey("agent.agentid"),index=True)#foreign
    officeid = Column(Integer, ForeignKey("office.officeid"),index=True)
    sell_price=Column(Integer)
    sell_date=Column(Date)
    commision=Column(Integer,nullable=True)

    def __repr__(self):   
        return "<Sales(salesid={0},houseid={1},agentid={2},sell_price={3},sell_date={4},commision={5})>".format(self.salesid,self.houseid, self.agentid,\
                                            self.sell_price,self.sell_date,self.commision)

    def get_commision(sell_price):
        if sell_price > 1000000:
            commission = sell_price * 0.04
        elif sell_price > 500000:
            commission = sell_price * 0.05
        elif sell_price > 200000:
            commission = sell_price * 0.06
        elif sell_price > 100000:
            commission = sell_price * 0.075
        elif sell_price <= 100000:
            commission = sell_price * 0.1
        return commission
    

#table for storing each agent and their commision
class AgentCommision(Base):
    __tablename__ = 'agentcommision'
    accountid = Column(Integer, primary_key = True)
    agentid = Column(Integer,ForeignKey("agent.agentid"))#foreign
    totalcommision=Column(Integer)

    def __repr__(self):    
        return "<AgentCommision(accountid={0}, agentid={1},totalcommision={2})>".format(self.accountid, self.agentid, self.totalcommision)

Base.metadata.create_all(engine)

    

