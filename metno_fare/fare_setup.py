#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

senders ={
        "no": "Meteorologisk Institutt",
        "en-GB": "MET Norway",
        "en": "MET Norway",
        }

sender = "noreply@met.no"
identifier_prefix= "2.49.0.1.578.0.NO."

#event types used in old version
event_types = {
        "Wind": u"Vind",
        "snow-ice" : u"Sn�-Is",
        "Thunderstorm" : u"Tordenbyger",
        "Fog" : u"T�ke",
        "high-temperature" : u"H�ye temperaturer",
        "low-temperature" : u"Lave temperaturer",
        "coastalevent" : u"Hendelse p� kysten",
        "forest-fire" : u"Skogsbrann",
        "avalanches"  : u"Skred",
        "Rain" : u"Store nedb�rsmengder",
        "flooding" : u"Flom",
        "rain-flooding" : u"Flom fra regn",
         "Polar-low" : u"Polart lavtrykk"
    }

#mapping from Meteoalarm event types to our event types, migh be obsolete later
event_types_land = {
        "Wind": {"no":u"Vind","en-GB":"Wind"},
        "snow-ice" : {"no":u"Vanskelige kj�reforhold","en-GB":"Difficult driving conditions"},
        "Thunderstorm" : {"no":u"Tordenv�r","en-GB":"Thunderstorm"},
        "Fog" : {"no":u"T�ke","en-GB":"Fog"},
        "high-temperature" : {"no":u"H�ye temperaturer","en-GB":"High temperature"},
        "low-temperature" : {"no":u"Lave temperaturer","en-GB":"Low temperature"},
        "coastalevent" : {"no":u"Stormflo","en-GB":"Storm surge"},
        "forest-fire" : {"no":u"Skogbrann","en-GB":"Forest fire"},
        "avalanches"  : {"no":u"Skred","en-GB":"avalanches"},
        "Rain" : {"no":u"Regn","en-GB":"Rain"},
        "flooding" : {"no":u"Flom","en-GB":"flooding"},
        "rain-flooding" : {"no":u"Styrtregn","en-GB":"Flash flood"},
        "Polar-low" : {"no":u"Polart lavtrykk-land","en-GB":"Polar-low"},
    }


#mapping from Meteoalarm event types to our event types, migh be obsolete later
event_types_marine = {
        "Wind": {"no":u"Kuling","en-GB":"Gale"},
        "coastalevent" : {"no":u"Ising","en-GB":"Icing"},
        "Polar-low" : {"no":u"Polart lavtrykk-marine","en-GB":"Polar-low"}
    }

event_type_default={"no":u"Farevarsel","en-GB":"Danger warning"}

event_level_name={
    "vind":{
        "moderate":" Kraftig vind",
        "severe": "Sv�rt kraftig vind",
        "extreme": "Ekstrem vind"


    }

}

level_response ={
    "no": {
            'minor': "Ulempe",
            'moderate': u"F�lg med",
            'severe': u"V�r forberedt",
            'extreme': u'Ekstremv�r%s %s'},
    "en-GB": {
            'minor': "Inconvenience",
            'moderate': "Be aware",
            'severe': "Be prepared",
            'extreme': "Take action! Extreme weather %s"}
    }


level_type = {
    "no" :{
            'minor': "",
            'moderate': u"Utfordrende situasjon",
            'severe': u"Farlig situasjon",
            'extreme': u"Ekstrem situasjon"},
    "en-GB":{
            'minor': "",
            'moderate': "Challenging situation",
            'severe': "Dangerous situation",
            'extreme': "Extreme situation"}
    }

# awareness_type used in Meteoalarm
awareness_types = {
    'Wind': "1; Wind",
    'snow-ice': "2; snow-ice",
    'Thunderstorm': "3; Thunderstorm",
    'Fog': "4; Fog",
    'high-temperature':"5; high-temperature",
    'low-temperature':"6; low-temperature",
    'coastalevent':"7; coastalevent",
    'forest-fire':"8; forest-fire",
    'avalanches':"9; avalanches",
    'Rain':"10; Rain",
    'flooding':"12; flooding",
    'rain-flood':"13; rain-flood",
    'Polar-low':""
}

