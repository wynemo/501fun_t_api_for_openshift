import web,twitUtil
from config import settings
from jinja2 import Environment,FileSystemLoader

render = settings.render

def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
            loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
            extensions=extensions,
            )
    jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)



class index: 
    def GET(self):   
        web.header('Content-Type','text/html; charset=utf-8', unique=True)               
        i = web.input()
        
        try:#callback,update token,secret
            if i.has_key('oauth_verifier'):
                credentials = {}  
                f1 = open('token.txt','r')
                str1 = f1.read()
                f1.close()
                l1 = str1.split(';')
                if '0' == l1[2].replace(r'ss=',''):
                    credentials['oauth_token'] = l1[0].replace(r'ot=','')
                    credentials['oauth_token_secret'] = l1[1].replace(r'ots=','')
                    access_token = twitUtil.get_access_token(credentials,i.oauth_verifier)
                    #print access_token
                    ot = access_token['oauth_token']#update tokens
                    ots = access_token['oauth_token_secret']#update secret
                    sc_name = access_token['screen_name']
                    us_id = access_token['user_id']
                    ss = '1'
                    str2 = 'ot=' + ot + ';' + 'ots=' + ots + ';' + 'ss=' + ss
                    str2 += ';' + 'sc_name=' + sc_name + ';' + 'us_id=' + us_id
                    f2 = open('token.txt','w')
                    f2.write(str2)
                    f2.close()
        except Exception,e:
            #print '---e is ',e
            pass
        try:
            return render.twittest()
        except:
            return render_template('twittest.html')


