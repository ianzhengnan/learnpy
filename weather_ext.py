from datetime import datetime, timedelta
from xml.parsers.expat import ParserCreate

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
    xml = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
		<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
			<channel>

<title>Yahoo! Weather - Shanghai, CN</title>
<link>http://us.rd.yahoo.com/dailynews/rss/weather/Shanghai__CN/*http://weather.yahoo.com/forecast/CHXX0116_c.html</link>
<description>Yahoo! Weather for Shanghai, CN</description>
<language>en-us</language>
<lastBuildDate>Thu, 24 Mar 2016 9:59 pm CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location city="Shanghai" region=""   country="China"/>
<yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
<yweather:wind chill="3"   direction="10"   speed="25.75" />
<yweather:atmosphere humidity="57"  visibility="9.99"  pressure="1015.92"  rising="0" />
<yweather:astronomy sunrise="5:53 am"   sunset="6:09 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif</url>
</image>
<item>
<title>Conditions for Shanghai, CN at 9:59 pm CST</title>
<geo:lat>31.25</geo:lat>
<geo:long>121.47</geo:long>
<link>http://us.rd.yahoo.com/dailynews/rss/weather/Shanghai__CN/*http://weather.yahoo.com/forecast/CHXX0116_c.html</link>
<pubDate>Thu, 24 Mar 2016 9:59 pm CST</pubDate>
<yweather:condition  text="Fair"  code="33"  temp="7"  date="Thu, 24 Mar 2016 9:59 pm CST" />
<description><![CDATA[
<img src="http://l.yimg.com/a/i/us/we/52/33.gif"/><br />
<b>Current Conditions:</b><br />
Fair, 7 C<BR />
<BR /><b>Forecast:</b><BR />
Thu - Mostly Cloudy. High: 11 Low: 6<br />
Fri - AM Clouds/PM Sun. High: 13 Low: 4<br />
Sat - Mostly Sunny. High: 16 Low: 6<br />
Sun - Sunny. High: 16 Low: 6<br />
Mon - Sunny. High: 18 Low: 9<br />
<br />
<a href="http://us.rd.yahoo.com/dailynews/rss/weather/Shanghai__CN/*http://weather.yahoo.com/forecast/CHXX0116_c.html">Full Forecast at Yahoo! Weather</a><BR/><BR/>
(provided by <a href="http://www.weather.com" >The Weather Channel</a>)<br/>
]]></description>
<yweather:forecast day="Thu" date="24 Mar 2016" low="6" high="11" text="Mostly Cloudy" code="27" />
<yweather:forecast day="Fri" date="25 Mar 2016" low="4" high="13" text="AM Clouds/PM Sun" code="30" />
<yweather:forecast day="Sat" date="26 Mar 2016" low="6" high="16" text="Mostly Sunny" code="34" />
<yweather:forecast day="Sun" date="27 Mar 2016" low="6" high="16" text="Sunny" code="32" />
<yweather:forecast day="Mon" date="28 Mar 2016" low="9" high="18" text="Sunny" code="32" />
<guid isPermaLink="false">CHXX0116_2016_03_28_7_00_CST</guid>
</item>
</channel>
</rss>
'''
    parse_weather(xml)






