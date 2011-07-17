### translate a given text from one language to another 
### using googletranslator

import urllib
import simplejson as json

class TranslateFailed(Exception):
    pass

class UNknownWxception(Exception):
    pass
    
class AristideBot(object):
	
    URI="http://ajax.googleapis.com/ajax/services/language/translate"
    default={'v':'1.0'}
    
    def __init(self):
        return

    def build_request(self,args):
        args.update({
            'langpair':'%s%%7C%s'%(self.src,self.to),
            'q':urllib.quote_plus(self.phrase),
        })
        return '%s' %('&'.join(['%s=%s' %(k,v) for (k,v) in args.iteritems()])) 

    def retrieveAnswer(self,response):
        if response['responseStatus'] == 200:
            return response['responseData']['translatedText']
        else:            
            return self.phrase
            

    def translate(self,src,to,phrase):
        self.src,self.to,self.phrase = src,to,phrase
        args=self.default.copy()
        return self.retrieveAnswer(json.load(urllib.FancyURLopener().open('%s?%s' % (self.URI,self.build_request(args)))))

######## Usage: tranlate form french to english

translator=AristideBot()
text="bonjour Aristide"
print translator.translate('fr','en',text)
