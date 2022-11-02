from django.core.management.base import BaseCommand
from Qurys import Qury

class Command(BaseCommand):
    Q=Qury()
    help="hhhhhhheeeeeelllllpppppppppp"
    
    def add_arguments(self, parser):
        parser.add_argument('qu', type= int,help="hhhelp forrrrrrrrr qqqquuuuu---------")

    def handle(self,*args,**kwargs):
        # Q.makedb()
        self.Q.makedb()
        print(kwargs['qu'],"will be new added........\nuser count",self.Q.i+int(kwargs['qu']))
        self.Q.add_newuser(int(kwargs['qu']))