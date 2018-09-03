from bottle import *
import datetime as dt
from sqlalchemy import create_engine, MetaData, select, func, and_
import os, config

@get('/')
def index():
    return template("index",a="",b="", result="")
@post('/')
def pstdata():
    a = request.forms.get("date1")
    b = request.forms.get("date2")
    the = (dt.datetime.strptime(b.replace("-"," "),"%Y %m %d")+dt.timedelta(days=1)).strftime("%Y-%m-%d")
    if a:
        result = sqlquery(a,the)
        print(a,b)
        return template("index",a=a,b=b,result=result)
    else:  return template("index",a="",b="",result="")

def sqlquery(a,b):
    connect = os.environ.get("DB") or config.config["DB"]
    e = create_engine(connect)
    feed = MetaData(bind=e)
    feed.reflect()
    table = feed.tables["feedback"]
    return list(e.execute(select([func.count(table.c.id)]).where(and_(table.c.dateya>=a,table.c.dateya<=b))))[0][0]



if __name__=="__main__":
    run(debug=True)