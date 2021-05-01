import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class ADboard(Model):
    __tablename__ = 'ADboard'
    id = Column(Integer, primary_key=True)
    image = Column(String(50),nullable=False)
    order = Column(Integer,nullable=True)
    expiry_day = Column(Date,nullable=True)
    disable = Column(Integer,nullable=False)
    
class Smartphone(Model):
    __tablename__ = 'Smartphone'
    id = Column(Integer, primary_key=True)
    image = Column(String(50),nullable=False)
    name = Column(String(50),nullable=False)
    model = Column(String(50),nullable=True)
    exterior = Column(String(50),nullable=True)
    price = Column(Integer,nullable=True)
    
class SIMplan(Model):
    __tablename__ = 'SIMplan'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    exterior = Column(String(50),nullable=True)
    price = Column(Integer,nullable=True)
    giveaway1 = Column(Integer,nullable=True)
    giveaway2 = Column(Integer,nullable=True)
    giveaway3 = Column(Integer,nullable=True)
    
class Service(Model):
    __tablename__ = 'Services'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)

class Menu(Model):
    __tablename__ = 'menu'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)

class RenewUpgrade(Model):
    __tablename__ = 'renewupgrade'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)

class SupportMore(Model):
    __tablename__ = 'supportmore'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    
class LoginMyHKBN(Model):
    __tablename__ = 'loginmyhkbn'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    
class ReferralProgramme(Model):
    __tablename__ = 'referralprogramme'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    
class Residential(Model):
    __tablename__ = 'residential'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    
class EnterpriseSolutions(Model):
    __tablename__ = 'enterprisesolutions'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    
class AboutUs(Model):
    __tablename__ = 'aboutus'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)

class LoginUser(Model):
    __talbename__ = 'loginuser'
    id = Column(Integer,primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    username = Column(String(64),unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(64), nullable=False)
    broadbandplan_id = Column(Integer, ForeignKey('broadbandplan.id'), nullable=False)
    broadbandplan = relationship("BroadbandPlan")
    securityplan_id = Column(Integer, ForeignKey('securityplan.id'), nullable=False)
    securityplan = relationship("SecurityPlan")
    
class SmartHome(Model):
    __tablename__ = 'smarthome'
    id = Column(Integer,primary_key=True)
    name = Column(String(64), nullable=False)
    category = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=True)
    
class SecurityPlan(Model):
    __tablename__ = 'securityplan'
    id = Column(Integer,primary_key=True)
    name = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String(64), nullable=False)
    
class BroadbandPlan(Model):
    __tablename__ = 'broadbandplan'
    id = Column(Integer,primary_key=True)
    name = Column(String(64), nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String(64), nullable=False)