# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DiceModel'
        db.create_table(u'home_dicemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sides', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('dice', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'home', ['DiceModel'])

        # Adding model 'Games'
        db.create_table(u'home_games', (
            ('game_name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
        ))
        db.send_create_signal(u'home', ['Games'])

        # Adding model 'Character'
        db.create_table(u'home_character', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('char_class', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('char_skills', self.gf('django.db.models.fields.TextField')()),
            ('char_story', self.gf('django.db.models.fields.TextField')()),
            ('brawn', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('finesse', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('wits', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('resolve', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('panache', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'home', ['Character'])


    def backwards(self, orm):
        # Deleting model 'DiceModel'
        db.delete_table(u'home_dicemodel')

        # Deleting model 'Games'
        db.delete_table(u'home_games')

        # Deleting model 'Character'
        db.delete_table(u'home_character')


    models = {
        u'home.character': {
            'Meta': {'object_name': 'Character'},
            'brawn': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'char_class': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'char_skills': ('django.db.models.fields.TextField', [], {}),
            'char_story': ('django.db.models.fields.TextField', [], {}),
            'finesse': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'panache': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'resolve': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'wits': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'home.dicemodel': {
            'Meta': {'object_name': 'DiceModel'},
            'dice': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sides': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        },
        u'home.games': {
            'Meta': {'object_name': 'Games'},
            'game_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        }
    }

    complete_apps = ['home']