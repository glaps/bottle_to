from bottle import get, post, run, request, template
import bottle
import datetime as dt
from sqlalchemy import create_engine, MetaData, select, func, and_
import os, config, psycopg2 as psql

@get('/result')
def index():
    return template("index",a="",b="", result="",result_for_day=[])
@post('/result')
def pstdata():
    a = request.forms.get("date1")
    b = request.forms.get("date2")
    the = (dt.datetime.strptime(b.replace("-"," "),"%Y %m %d")+dt.timedelta(days=1)).strftime("%Y-%m-%d")
    if a and the:
        result, result_for_day = sqlquery(a,the)
        return template("index",a=a,b=b,result=result, result_for_day=result_for_day)
    else:  return template("index",a="",b="",result="",result_for_day=[])

def sqlquery(a,b):
    connect = os.environ.get("DB") or config.config["DB"]
    e = create_engine(connect)
    feed = MetaData(bind=e)
    feed.reflect()
    table = feed.tables["feedback"]
    return list(e.execute(select([func.count(table.c.id)]).where(and_(table.c.dateya>=a,table.c.dateya<=b))))[0][0], sqlall(a,b)

def sqlall(a,b):
    conn = psql.connect(config.config["DB2"])
    cur = conn.cursor()
    cur.execute(config.config["SQL1"].format(date1=a,date2=b))
    return [(d.strftime("%Y-%m-%d"),c) for d,c in cur.fetchall()]



app = bottle.default_app()


if __name__=="__main__":
    run()