from create_db import City, sessionlocal
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse
from requests import get
import redis

# Configure Redis Database
DB = redis.Redis(host='redis1',port=6379,encoding="utf-8",decode_responses=True)

# Configure MySql Database
db = sessionlocal()

# Configure FastApi App
app = FastAPI()

# Set Api address and settings
@app.get('/getweather/{city}',status_code = status.HTTP_200_OK)
def city_weather(city):
    x = 1
    # Make a loop that in 3 step and when it enters to the first step or condition, it will be end
    while(x):
        
        # Check if the data in Redis Database or not
        if DB.get(city):
            weather = DB.get(city)
            x = 0
            return JSONResponse({"weather":weather})

        # Check if the date in Mysql or not
        elif db.query(City).filter(City.name==city).first():
            item = db.query(City).filter(City.name==city).first()
            DB.set(city,item.weather)

        # Finaly we should get data from api and index it in Mysql Database
        else:
            # Get weather result from external api
            result = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2bee646137626c68366fe185e715a309").json()
            
            # Check if the city is exist or not
            if result['cod'] == '404':
                return JSONResponse({"Error":"The city not exist at all"}, 404)

            new_item = City(
            name = city,
            weather = result["weather"][0]["description"]
            )

            db.add(new_item)
            db.commit()

            db.refresh(new_item)

