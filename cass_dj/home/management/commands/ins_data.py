from django.core.management.base import BaseCommand
from home.management.commands.make_db import Command as cc
from a_b_c import c_b_a

class Command(BaseCommand):

    def handle(self,*args, **kwargs):
        cc.Q.iser()
        # Q.iser();