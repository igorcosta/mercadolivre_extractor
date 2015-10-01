#!/usr/bin/python
# -*- encoding:utf-8 -*-

class Product(object):
  name = ''
  desc = ''
  price = ''
  image = ''
  original_url = ''

  def to_json(self):
    return {
      'name': str(self.name),
      'price': str(self.price),
      'desc': str(self.desc),
      'image': str(self.image)
      'original_url':str(self.image)
    }