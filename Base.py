import json, pprint, praw, OAuth2Util
#Define the config
CONFIG = "config.json"
#Use this to define your major version number E.G Version"1".2
VERSION_MAJOR = 0
#Use this to define your minor version number E.G Version 1."2"
VERSION_MINOR = 1
def main():
 with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  #Load config
  cfg = json.loads( str(open(CONFIG, 'rb').read(), 'utf-8') )
  #Login into Reddit
  o = OAuth2Util.OAuth2Util(r)
  o.refresh()
  reddit = praw.Reddit(user_agent='Reddit Bot Base by /u/Gilda_Griffon' % (VERSION_MAJOR, VERSION_MINOR))
  reddit.login(cfg['REDDIT_USER'], cfg['REDDIT_PASS'])