from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, Service, RenewUpgrade, SupportMore, Menu, LoginMyHKBN, ReferralProgramme, Residential, EnterpriseSolutions, AboutUs, SmartHome, SecurityPlan, BroadbandPlan, LoginUser, ADboard, SIMplan, Smartphone, EntainmentPlan, TravelPlan, SpecialPlan
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

#class NewsPageView(BaseView):

class ADboardView(BaseView):
    default_view = 'local_news'
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'image', 'order', 'expiry_day','disable']
    
    
    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        

class ServiceView(BaseView):
    default_view = 'fibrebroadband'
  
    @expose('/fibrebroadband/')
    def fibrebroadband(self):
      param1 = 'Fibre Broadband'
      self.update_redirect()
      return self.render_template('fibrebroadband.html', param1=param1)

    @expose('/smarthome/')
    def smarthome(self):
      param1 = 'Smart Home'
      self.update_redirect()
      return self.render_template('smarthome.html', param1=param1)
    
    @expose('/voicecalls/')
    def voicecalls(self):
      param1 = 'Voice Calls'
      self.update_redirect()
      return self.render_template('voicecalls.html', param1=param1)
      
    @expose('/mobileservices/')
    def mobileservices(self):
      param1 = 'Mobile Services'
      self.update_redirect()
      return self.render_template('mobileservices.html', param1=param1)
      
    @expose('/cybersecurity/')
    def cybersecurity(self):
      param1 = 'Cyber Security'
      self.update_redirect()
      return self.render_template('cybersecurity.html', param1=param1)  
    
    @expose('/entertainment/')
    def entertainment(self):
      param1 = 'Entertainment'
      self.update_redirect()
      return self.render_template('entertainment.html', param1=param1)

    @expose('/travel/')
    def travel(self):
      param1 = 'Travel'
      self.update_redirect()
      return self.render_template('travel.html', param1=param1)
      
    @expose('/smartphonesandsmartproducts/')
    def smartphonesandsmartproducts(self):
      param1 = 'Smartphones and Smart Products'
      self.update_redirect()
      return self.render_template('smartphonesandsmartproducts.html', param1=param1)

class SupportMoreView(BaseView):
    default_view = 'myhkbnapp'
    
    @expose('/myhkbnapp/')
    def myhkbnapp(self):
      param1 = 'My HKBN App'
      self.update_redirect()
      return self.render_template('myhkbnapp.html', param1=param1)
      
    @expose('/customersupport/')
    def voicecalls(self):
      param1 = 'Customer Support'
      self.update_redirect()
      return self.render_template('customersupport.html', param1=param1)


class MenuView(BaseView):
    default_view = 'loginmyhkbn'
    
    @expose('/loginmyhkbn/')
    def loginmyhkbn(self):
      param1 = 'Login My HKBN'
      self.update_redirect()
      return self.render_template('loginmyhkbn.html', param1=param1)
      
    @expose('/renewupgrade/')
    def renewupgrade(self):
      param1 = 'Renew/Upgrade'
      self.update_redirect()
      return self.render_template('renewupgrade.html', param1=param1)
    
    @expose('/referralprogramme/')
    def referralprogramme(self):
      param1 = 'Referral Programme'
      self.update_redirect()
      return self.render_template('referralprogramme.html', param1=param1)
      
    @expose('/residential/')
    def residential(self):
      param1 = 'Residential'
      self.update_redirect()
      return self.render_template('residential.html', param1=param1)
    
    @expose('/enterprisesolutions/')
    def enterprisesolutions(self):
      param1 = 'Enterprise Solutions'
      self.update_redirect()
      return self.render_template('enterprisesolutions.html', param1=param1)
    
    @expose('/aboutus/')
    def aboutus(self):
      param1 = 'AboutUs'
      self.update_redirect()
      return self.render_template('aboutus.html', param1=param1)

class SmartHomeView(ModelView):
    datamodel = SQLAInterface(SmartHome)
    list_columns = ['id', 'name', 'category', 'price', 'amount'] 

class SecurityPlanView(ModelView):
    datamodel = SQLAInterface(SecurityPlan)
    list_columns = ['id', 'name', 'category', 'price' ]
    
class BroadbandPlanView(ModelView):
    datamodel = SQLAInterface(BroadbandPlan)
    list_columns = ['id', 'name', 'category', 'price' ]

class SmartphoneView(ModelView):
    datamodel = SQLAInterface(Smartphone)
    list_columns = ['id', 'image', 'name', 'model', 'exterior', 'price' ]
    
class SIMplanView(ModelView):
    datamodel = SQLAInterface(SIMplan)
    list_columns = ['id', 'name', 'exterior', 'price', 'giveaway1', 'giveaway2', 'giveaway3' ]
    
class EntainmentPlanView(ModelView):
    datamodel = SQLAInterface(EntainmentPlan)
    list_columns = ['id', 'name', 'price' ]
    
class TravelPlanView(ModelView):
    datamodel = SQLAInterface(TravelPlan)
    list_columns = ['id', 'name', 'price' ]

class SpecialPlanView(ModelView):
    datamodel = SQLAInterface(SpecialPlan)
    list_columns = ['id', 'name', 'price', 'date' ] 

db.create_all()


""" Page View """
appbuilder.add_view(ServiceView, 'fibrebroadband', category="Service" )
appbuilder.add_link("Smart Home", href="/serviceview/smarthome/", category="Service")
appbuilder.add_link("Voice Calls", href="/serviceview/voicecalls/", category="Service")
appbuilder.add_link("Mobile Voice", href="/serviceview/mobileservices/", category="Service")
appbuilder.add_link("Cyber Security", href="/serviceview/cybersecurity/", category="Service")
appbuilder.add_link("Entertainment", href="/serviceview/entertainment/", category="Service")
appbuilder.add_link("Travel", href="/serviceview/travel/", category="Service")
appbuilder.add_link("Smartphones and Smart Products", href="/serviceview/smartphonesandsmartproducts/", category="Service")
appbuilder.add_view(SupportMoreView, 'myhkbnapp', category="SupportMore")
appbuilder.add_link("Customer Support", href="/supportmoreview/custmoersupport/", category="SupportMore")
appbuilder.add_view(MenuView, 'loginmyhkbn', category="Menu")
appbuilder.add_link("Renew/Upgrade", href="/Menuview/renewupgrade/", category="Menu")
appbuilder.add_link("Referral Programme", href="/Menuview/referralprogramme/", category="Menu")
appbuilder.add_link("Residential", href="/Menuview/residential/", category="Menu")
appbuilder.add_link("Enterprise Solutions", href="/Menuview/enterprisesolutions/", category="Menu")
appbuilder.add_link("AboutUs", href="/Menuview/aboutus/", category="Menu")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SmartHomeView, "SmartHome", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SecurityPlanView, "SecurityPlan", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(BroadbandPlanView, "BroadbandPlan", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(ADboardView, "ADboard", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SmartphoneView, "Smartphone", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SIMplanView, "SIMplan", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(EntainmentPlanView, "EntainmentPlan", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(TravelPlanView, "TravelPlan", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SpecialPlanView, "SpecialPlan", icon="fa-folder-open-o", category="Admin")
