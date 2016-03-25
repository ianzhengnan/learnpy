from datetime import datetime
from xml.parsers.expat import ParserCreate
from urllib import request
import json

class WeatherSaxHandler(object):

    weather = {}

    def start_element(self, name, attrs):

        if name == 'yweather:location':
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']


        now_dt = datetime.now()
        if name == 'yweather:forecast':
            cday = datetime.strptime(attrs['date'], '%d %b %Y')
            if (now_dt.day + 1) == cday.day:
                self.weather['tomorrow'] = {'text': attrs['text'],
                                            'low': attrs['low'],
                                            'high': attrs['high']}
            elif now_dt.day == cday.day:
                self.weather['today'] = {'text': attrs['text'],
                                        'low': attrs['low'],
                                        'high': attrs['high']}



    def end_element(self, name):
        pass

    def char_data(self,text):
        pass


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    print(handler.weather)



if __name__ == '__main__':

    # #open weather site and get xml file
    # req = request.Request('http://apis.baidu.com/heweather/pro/attractions?cityid=101020100')
    # req.add_header('apikey', '8dee7971484b94b760f9245ace16a874')
    # data = ''
    # with request.urlopen(req) as f:
    #     data = f.read().decode('utf-8')



    baseurl = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22shanghai%22)"
    yql_query = "select wind from weather.forecast where woeid=2151849"
    yql_url = baseurl + "&format=xml"
    result = request.urlopen(yql_url).read()
    # data = json.loads(result.decode('utf-8'))
    data = result.decode('utf-8')
    # print(data['query']['results'])
    # print(data)
    parse_weather(data)





