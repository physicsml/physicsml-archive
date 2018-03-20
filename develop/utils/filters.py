# -*- coding: utf-8 -*- #
import datetime

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'


def pretty_date(dt, default=None):
  """
  Returns string representing "time since" e.g.
  3 days ago, 5 hours ago etc.
  Ref: https://bitbucket.org/danjac/newsmeme/src/a281babb9ca3/newsmeme/
  """

  if default is None:
      default = 'just now'

  now = datetime.datetime.utcnow()
  diff = now - datetime.datetime.strptime(dt, '%a %d %B %Y')

  periods = (
      (diff.days / 365, 'year', 'years'),
      (diff.days / 30, 'month', 'months'),
      (diff.days / 7, 'week', 'weeks'),
      (diff.days, 'day', 'days'),
      (diff.seconds / 3600, 'hour', 'hours'),
      (diff.seconds / 60, 'minute', 'minutes'),
      (diff.seconds, 'second', 'seconds'),
  )

  for period, singular, plural in periods:

      if not period:
          continue

      if period == 1:
          return u'%d %s ago' % (period, singular)
      else:
          return u'%d %s ago' % (period, plural)

  return default