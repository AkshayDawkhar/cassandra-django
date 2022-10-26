from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="hhhhhhheeeeeelllllpppppppppp"
    
    def add_arguments(self, parser):
        parser.add_argument('qu', type= int,help="hhhelp forrrrrrrrr qqqquuuuu---------")
        parser.add_argument('ou', type= str,help="hhhelp forrrrrrrrr qqqquuuuu---------")

    def handle(self,*args,**kwargs):
       for i in range(kwargs['qu']):
        print("hoo",kwargs['ou'])
    