# Copyright 2013 Arunjit Singh.

import unittest

import langutil


class LangUtilTest(unittest.TestCase):

  def testGetPreferredLanguages(self):
    expected = ['da', 'en-gb', 'en']
    actual = langutil.GetPreferredLanguages('da, en-gb;q=0.8, en;q=0.7')
    self.assertEquals(expected, actual)

    self.assertEquals([], langutil.GetPreferredLanguages(None))
    self.assertEquals([], langutil.GetPreferredLanguages(''))
    self.assertEquals([], langutil.GetPreferredLanguages('   '))
    # Technically valid.
    self.assertEquals(['english'], langutil.GetPreferredLanguages('english'))

  def testGetBestMatch(self):
    available = 'de en en-gb fr-ca fr-fr'.split(' ')

    accepted = 'da, en-gb;q=0.8, en;q=0.7'
    self.assertEquals('en-gb', langutil.GetBestMatch(accepted, available))

    accepted = 'da, en-us;q=0.8, en;q=0.7'
    self.assertEquals('en', langutil.GetBestMatch(accepted, available))

    accepted = 'da'
    self.assertEquals(
        'en', langutil.GetBestMatch(accepted, available, default='en'))


if __name__ == '__main__':
  unittest.main()
