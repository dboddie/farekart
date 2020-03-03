#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

languages = ["no", "en-GB"]

senders = {
        "no": "Meteorologisk Institutt",
        "en-GB": "MET Norway",
        }


contact= {
        "no": "https://www.met.no/kontakt-oss",
        "en-GB": "https://www.met.no/en/contact-us",
}

caption ={
        "no": "Kart over ",
        "en-GB": "Map of ",
}



sender = "noreply@met.no"
identifier_prefix= "2.49.0.1.578.0."
web = "https://www.met.no/vaer-og-klima/farevarsel-og-ekstremvaer"

instructions={
        "no":u"",
        "en-GB": u""
}

responseType = "Monitor"
urgency = "Future"

geographicDomain={
"wind":"land",
"snow":"land",
"blowingSnow":"land",
"drivingConditions": "land",
"thunder":"land",
"fog":"land",
"highTemperature":"land",
"lowTemperature":"land",
"stormSurge":"land",
"forestFire":"land",
"avalanches":"land",
"rain":"land",
"flooding":"land",
"rainFlood":"land",
"polarLow":None,
"gale":"marine",
"icing":"marine",
"uvRadiation": None,
"pollen": "land",
"airPollution": "land",
"ice":"land"
}


# mapping from ted id to administrative ids
ted2Geocode2020 = {
"0601": {"iso":"NO-01","county":"01:30", "NUTS3":"NO031",# �stfold, 30 is code for Viken from 2020
"MunicipalityId":"3015;3011;3001;3002;3003;3012;3017;3014;3016;3013;3018;3026;3004;"
},
"0602": {"iso":"NO-02","county":"02:30", "NUTS3":"NO012", # Akershus, 30 is code for Viken from 2020
"MunicipalityId":"3032;3029;3022;3019;3023;3035;3025;3033;3028;3034;3020;3036;3037;3024;3021;3031;3026;3027;3030;"
},
"0603": {"iso":"NO-03","county":"03","emma_id":"NO010","NUTS3":"NO011",  # Oslo
"MunicipalityId":"0301;"
},
"0604": {"iso":"NO-04","county":"04:34", "NUTS3":"NO021",# # Hedmark, 34 is code for Innlandet from 2020
"MunicipalityId":"3419;3414;3422;3424;3417;3411;3420;3421;3401;3416;3427;3426;3429;3403;3412;3425;3423;3415;3430;3418;3428;3413;"
},
"0605": {"iso":"NO-05","county":"05:34",  "NUTS3":"NO022",# Oppland,, 34 is code for Innlandet from 2020
"MunicipalityId":"3453;3437;3447;3435;3451;3405;3454;3436;3433;3450;3442;3440;3054;3449;3434;3443;3431;3053;3448;3439;3407;3446;3432;3438;3441;3452;"
         },
"0606": {"iso":"NO-06","county":"06:30","NUTS3":"NO032",# Buskerud, 30 is code for Viken from 2020
"MunicipalityId":"3052;3006;3045;3046;3043;3047;3048;3025;3050;3038;3049;3039;3007;3041;3040;3005;3051;3044;3042"
},
"0607": {"iso":"NO-07","county":"07:38","NUTS3":"NO033", # Vestfold, 38 is code for Telemark og Vestfold from 2020
"MunicipalityId":"3803;3804;3805;3802;3811;3005;3801;"
         },
"0608": {"iso":"NO-08","county":"08:38","NUTS3":"NO034", # Telemark, 38 is code for Telemark og Vestfold from 2020
"MunicipalityId":"3813;3814;3820;3806;3821;3823;3807;3825;3817;3824;3818;3815;3812;3819;3816;3808;3822;"
},
"0609": {"iso":"NO-09","county":"09:42","NUTS3":"NO041", # Aust-Agder, 42 is code for Agder from 2020
"MunicipalityId":"4217;4219;4214;4201;4213;4222;4218;4202;4221;4203;4220;4215;4216;4212;4211;"
         },
"0610": {"iso":"NO-10","county":"10:42",  "NUTS3":"NO042",  # Vest-Agder, 42 is code for Agder from 2020
"MunicipalityId":"4227;4205;4206;4224;4223;4228;4207;4204;4226;4225;"

},
"0611": {"iso":"NO-11","county":"11",  "NUTS3":"NO043",     # Rogaland
"MunicipalityId":"1103;1121;1127;1122;1108;1135;1124;1114;1145;1160;1134;1144;1149;1111;1130;1101;1112;1106;1146;1151;1133;1119;1120;"
},
"0612": {"iso":"NO-12","county":"12:46", "NUTS3":"NO051", # Hordaland, 46 is code for Vestlandet from 2020
"MunicipalityId":"4622;4621;4619;4627;4625;4615;4614;4633;4613;4611;4623;4618;4616;4617;4612;4632;4634;4630;4626;4629;4631;4620;4628;4601;4624;"
},
         "0614": {"iso":"NO-14","county":"14:46", "NUTS3":"NO052",# Sogn og Fjordane, 46 is code for Vestlandet from 2020
"MunicipalityId":"4646;4651;4602;4643;4648;4638;4636;4645;4644;4647;4639;4635;4640;4649;4641;1577;4637;4642;4650;"
         },
"0615": {"iso":"NO-15","county":"15", "NUTS3":"NO053",   # M�re og Romsdal
"MunicipalityId":"1511;1576;1507;1579;1566;1516;1578;1525;1532;1577;1506;1573;1520;1505;1535;1557;1514;1554;1539;1515;1528;1563;1531;1547;1517;1560;5055;5061"
},
"0616": {"iso":"NO-16","county":"50", "NUTS3":"NO061", # S�r-Tr�ndelag, 50 is new code for Tr�ndelag from 2018
         "MunicipalityId":"5001;5014;5020;5021;5022;5025;5026;5027;5028;5029;5031;5032;5033;5054;5055;5056;5057;5058;5059;5061"
         },
"0617": {"iso":"NO-17","county":"50","NUTS3":"NO062", # Nord-Tr�ndelag, 50 is new code for Tr�ndelag from 2018
         "MunicipalityId":"5006;5007;5034;5035;5036;5037;5038;5041;5042;5043;5044;5045;5046;5047;5049;5052;5053;5054;5060"
},
"0618": {"iso":"NO-18","county":"18", "NUTS3":"NO071", # Nordland
"MunicipalityId":"1859;1860;1832;1841;1867;1828;1839;1856;1865;1838;1818;1811;1822;1813;1833;1826;1875;1845;1866;1853;1812;1835;1857;1837;1820;1874;1815;1824;1825;1827;1870;1834;5412;1871;1806;1851;1848;1868;1840;1804;1836;1816;"
},
"0619": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # Troms, 54 is code for Troms og Finnmark from 2020
"MunicipalityId":"5426;5419;5420;5402;5422;5417;5413;5427;5425;5424;5423;5411;5429;5421;5415;5401;5412;5418;5416;5414;5428;"
},
"0620": {"iso":"NO-20","county":"20:54", "NUTS3":"NO073",  # Finnmark, , 54 is code for Troms og Finnmark from 2020
         "MunicipalityId":"5433;5435;5441;5430;5432;5439;5440;5443;5438;5437;5404;5403;5434;5444;5406;5442;5405;5436;"
},
"9001": {"iso":"NO-18","county":"18",  "NUTS3":"NO071",  # Helgeland
"MunicipalityId":"1811;1812;1813;1815;1816;1818;1820;1822;1824;1825;1826;1827;1828;1832;1833;1834;1835;1836;1837"
},
"9002": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Saltfjellet
         "MunicipalityId": "1833;1839;1840"},
"9003": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Salten
         "MunicipalityId":"1804;1838;1839;1840;1841;1845;1848;1875"
},
"9004": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Lofoten
         "MunicipalityId":"1856;1857;1859;1860;1865;1874"         
},
"9005": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Ofoten
         "MunicipalityId":"1806;1851;1853;1875;5412"
},
"9006": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Vester�len
         "MunicipalityId":"1866;1867;1868;1870;1871"
},
"9007": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # S�r-Troms
         "MunicipalityId":"5402;5411;5412;5413;5414;5415;5417;5416;5418;5419;5420;5421"
},
"9008": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # Nord-Troms
         "MunicipalityId":"5401;5422;5423;5424;5425;5426;5427;5428;5429"
},
"9009": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # �st-Finnmark
         "MunicipalityId":"5404;5405;5438;5439;5440;5441;5442;5443;5444"
},
"9010": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # Kyst- og fjordstr�kene i Vest-Finnmark
         "MunicipalityId":"5403;5406;5432;5433;5434;5435;5436"
},
"9011": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # Finnmarksvidda
         "MunicipalityId":"5430;5437"
},
"9018": {"iso":"NO-21","county":"21",
         "MunicipalityId":"2111"},   # Nordenski�ld Land p� Spitsbergen
# Fjellet i S�r-Norge ber�rer fylkene
    # Tr�ndelag, Oppland, Hedmark, Buskerud,Telemark, Aust-Agder, Vest-Agder, Rogaland,Hordaland,
    # Sogn og Fjordane, M�re og Romsdal
"0710" : {"iso":"NO-16:NO-05:NO-04:NO-06:NO-08:NO-09:NO-10:NO-11:NO-12:NO-14:NO-15",
          "county":"05:04:06:08:09:10:11:12:14:15:50:34:30:38:42:46",
          "NUTS3":"NO061:NO022:NO021:NO032:NO034:NO041:NO042:NO043:NO051:NO052:NO053",

          "MunicipalityId":"1134;1506;1525;1539;1563;1566;1578;3042;3043;3044;3052;3427;3429;3430;3431;3432;3433;3434;3454;3818;3823;3824;3825;4220;4221;4222;4224;4228;4618;4619;4620;4641;4642;4643;4644;4651;5021;5022;5026;5027;5033;5061"
          
},
# Mapping of area used in METs warnings to Meteolarms internal emma_id
# �stfold kyst = NO801
# Aust-Agder kyst = NO802
# Finnmark kyst = NO803
# Troms kyst = NO804
# Nordland kyst = NO805
# Nord-Tr�ndelag kyst = NO806
# S�r-Tr�ndelag kyst = NO807
# M�re og Romsdal kyst = NO808
# Sogn og Fjordane kyst = NO809
# Hordaland kyst = NO810
# Rogaland kyst = NO811
# Vest-Agder kyst = NO812
# Vestfold kyst = NO813
# Telemark kyst = NO814

#"0816": # Indre Oslofjord = Oslo, Akershus, Buskerud
"19182": {"emma_id":"NO801:NO813"},# Svenskegrensa - Stavern = �sfold, Vestfold
"19171":  {"emma_id":"NO813:NO814"}, # Stavern - Jomfruland = Vestfold, Telemark
"19180":  {"emma_id":"NO814:NO802:NO812"}, # Jomfruland - Lyng�r = Telemark, Agder
"19168":  {"emma_id":"NO802:NO812"}, # Lyng�r - Torungen = Agder
"19181":  {"emma_id":"NO802:NO812"}, # Torungen - Oks�y = Agder
"19165":  {"emma_id":"NO802:NO812"}, # Oks�y - Lindesnes = Agder
"19059":  {"emma_id":"NO802:NO812"}, # Lindesnes - �na Sira = Agder
"19028":  {"emma_id":"NO811"}, # �na Sira -Obrestad = Rogaland
"19029":  {"emma_id":"NO811"}, # Obrestad - Karm�y = Rogaland
"19030":  {"emma_id":"NO811:NO810"}, # Karm�y - Sl�tter�y = Rogaland og Hordaland
"19031":  {"emma_id":"NO810"}, # Sl�tter�y - Fedje = Hordaland
"19032":  {"emma_id":"NO810:NO809"}, # Fedje - Bulandet = Hordaland, Sogn og Fjordane
"19033":  {"emma_id":"NO809"}, # Bulandet - M�l�y = Sogn og Fjordane
"19034":  {"emma_id":"NO809"}, # M�l�y - Stad = Sogn og Fjordane
"19035":  {"emma_id":"NO809:NO808"}, # Stad - Svin�y = Sogn og Fjordane, M�re og Romsdal
"19036":  {"emma_id":"NO808"}, # Svin�y - Ona = M�re og Romsdal
"19037":  {"emma_id":"NO808:NO806:NO807"}, # Ona - Fr�ya = M�re og Romsdal, Tr�ndelag
"19038":  {"emma_id":"NO806:NO807"}, # Fr�ya -Halten = Tr�ndelag
"19039":  {"emma_id":"NO806:NO807"}, # Halten - R�rvik = Tr�ndelag
"19064":  {"emma_id":"NO806:NO807:NO805"}, # R�rvik - Sandnessj�en = Tr�ndelag og Nordland
"19043":  {"emma_id":"NO805"}, # Sandnessj�en - St�tt = Nordland
"19044":  {"emma_id":"NO805"}, # St�tt - Bod� = Nordland
"19069":  {"emma_id":"NO805"}, # Bod� - L�dingen = Nordland
"19072":  {"emma_id":"NO805"}, # Skomv�r - Melbu = Nordland
"19073":  {"emma_id":"NO805"}, # Melbu - Andenes = Nordland
"19015":  {"emma_id":"NO805:NO804"}, # Andenes - Hekkingen = Nordland, Troms
"19048":  {"emma_id":"NO804"}, # Hekkingen - Torsv�g = Troms
"19065":  {"emma_id":"NO804:NO803"}, # Torsv�g - Loppa = Troms, Finnmark
"19051":  {"emma_id":"NO803"}, # Loppa - Fruholmen = Finnmark
"19052":  {"emma_id":"NO803"}, # Fruholmen Nordkapp = Finnmark
"19066":  {"emma_id":"NO803"}, # Nordkapp - Slettnes Fyr = Finnmark
"19055":  {"emma_id":"NO803"}, # Slettnes Fyr - Vard� = Finnmark
"19056":  {"emma_id":"NO803"}, # Vard� - Grense Jakobselv = Finnmark

}





# mapping from ted id to administrative ids
ted2Geocode = {
"0601": {"iso":"NO-01","county":"01:30", "NUTS3":"NO031",# �stfold, 30 is code for Viken from 2020
         "MunicipalityId":"0101;0104;0105;0106;0111;0118;0119;0121;0122;0123;0124;0125;0127;0128;0135;0136;"
                          "0137;0138"},
"0602": {"iso":"NO-02","county":"02:30", "NUTS3":"NO012", # Akershus, 30 is code for Viken from 2020
         "MunicipalityId":"0211;0213;0214;0215;0216;0217;0219;0220;0221;0226;0227;0228;0229;0230;0231;0233;0234;"
                          "0235;0236;0237;0238;0239"},
"0603": {"iso":"NO-03","county":"03","emma_id":"NO010","NUTS3":"NO011",  # Oslo
         "MunicipalityId":"0301"},
"0604": {"iso":"NO-04","county":"04:34", "NUTS3":"NO021",# # Hedmark, 34 is code for Innlandet from 2020
         "MunicipalityId":"0402;0403;0412;0415;0417;0418;0419;0420;0423;0425;0426;0427;0428;0429;0430;0432;"
                          "0434;0436;0437;0438;0439;0441"},
"0605": {"iso":"NO-05","county":"05:34",  "NUTS3":"NO022",# Oppland,, 34 is code for Innlandet from 2020
        "MunicipalityId":"0501;0502;0511;0512;0513;0514;0515;0516;0517;0519;0520;0521;0522;0528;0529;0532;"
                         "0533;0534;0536;0538;0540;0541;0542;0543;0544;0545"
         },
"0606": {"iso":"NO-06","county":"06:30","NUTS3":"NO032",# Buskerud, 30 is code for Viken from 2020
         "MunicipalityId": "0602;0604;0605;0612;0615;0616;0617;0618;0619;0620;0621;0622;0623;0624;0625;0626;0627;"
                           "0628;0631;0632;0633"},
"0607": {"iso":"NO-07","county":"07:38","NUTS3":"NO033", # Vestfold, 38 is code for Telemark og Vestfold from 2020
         "MunicipalityId":"0701;0704;0710;0711;0712;0713;0715;0716;0729"
         },
"0608": {"iso":"NO-08","county":"08:38","NUTS3":"NO034", # Telemark, 38 is code for Telemark og Vestfold from 2020
         "MunicipalityId": "0805;0806;0807;0811;0814;0815;0817;0819;0821;0822;0826;0827;0828;0829;0830;0831;0833;"
                           "0834"},
"0609": {"iso":"NO-09","county":"09:42","NUTS3":"NO041", # Aust-Agder, 42 is code for Agder from 2020
         "MunicipalityId":"0901;0904;0906;0911;0912;0914;0919;0926;0928;0929;0935;0937;0938;0940;0941"
         },
"0610": {"iso":"NO-10","county":"10:42",  "NUTS3":"NO042",  # Vest-Agder, 42 is code for Agder from 2020
         "MunicipalityId":"1001;1002;1003;1004;1014;1017;1018;1021;1026;1027;1029;1032;1034;1037;1046"},
"0611": {"iso":"NO-11","county":"11",  "NUTS3":"NO043",     # Rogaland
         "MunicipalityId":"1101;1102;1103;1106;1111;1112;1114;1119;1120;1121;1122;1124;1127;1129;1130;1133;"
                          "1134;1135;1141;1142;1144;1145;1146;1149;1151;1154;1159;1160"},
"0612": {"iso":"NO-12","county":"12:46", "NUTS3":"NO051", # Hordaland, 46 is code for Vestlandet from 2020
         "MunicipalityId":"1201;1211;1214;1216;1219;1221;1222;1223;1224;1227;1228;1231;1232;1233;1234;1235;1238;"
                          "1241;1242;"
         "1243;1244;1245;1246;1247;1251;1252;1253;1256;1259;1260;1263;1264;1265;1266"},
         "0614": {"iso":"NO-14","county":"14:46", "NUTS3":"NO052",# Sogn og Fjordane, 46 is code for Vestlandet from 2020
         "MunicipalityId":"1401;1449;1412;1413;1416;1417;1418;1419;1420;1421;1422;1424;1426;1428;1429;1430;"
                          "1431;1432;1433;1438;1439;1441;1443;1444;1445;1411"},
"0615": {"iso":"NO-15","county":"15", "NUTS3":"NO053",   # M�re og Romsdal
         "MunicipalityId":"1573;1572;1502;1503;1504;1505;1511;1514;1515;1516;1517;1519;1520;1523;1524;1525;"
                          "1526;1528;1529;1531;1532;1534;1535;1539;1543;1545;1546;1547;1548;1551;1554;1556;"
                          "1557;1560;1563;1566;1567;1569;1571;1576"},
"0616": {"iso":"NO-16","county":"50", "NUTS3":"NO061", # S�r-Tr�ndelag, 50 is new code for Tr�ndelag from 2018
         "MunicipalityId":"5033;5054;5001;5011;5012;5013;5014;5015;5016;5017;5018;5019;5020;5021;5022;5023;"
                          "5024;5025;5026;5027;5028;5029;5030;5031;5032"},
"0617": {"iso":"NO-17","county":"50","NUTS3":"NO062", # Nord-Tr�ndelag, 50 is new code for Tr�ndelag from 2018
         "MunicipalityId":"5035:5034;5036;5037;5038;5039;5040;5041;5042;5043;5044;5045;5046;5047;5048;5049;5050;"
                          "5051;5052;5053;5004;5005;5054"},
"0618": {"iso":"NO-18","county":"18", "NUTS3":"NO071", # Nordland
         "MunicipalityId":"1804;1805;1811;1812;1813;1815;1816;1818;1820;1822;1824;1825;1826;1827;1828;1832;"
                          "1833;1834;1835;1836;1837;1838;1839;1840;1841;1842;1845;1848;1849;1850;1851;1852;1853;"
                          "1854;1856;1857;1859;1860;1865;1866;1867;1868;1870;1871;1874"},
"0619": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # Troms, 54 is code for Troms og Finnmark from 2020
         "MunicipalityId":"1931;1929;1936;1938;1939;1940;1941;1942;1943;1901;1902;1903;1911;1913;1915;1917;"
                          "1919;1920;1922;1923;1924;1925;1926;1927;1928;1933"
         },
"0620": {"iso":"NO-20","county":"20:54", "NUTS3":"NO073",  # Finnmark, , 54 is code for Troms og Finnmark from 2020
         "MunicipalityId":"2002;2030;2004;2011;2012;2014;2015;2017;2018;2019;2020;2021;2022;2023;2024;2025;2027;2028;"
                          "2003"},
"9001": {"iso":"NO-18","county":"18",  "NUTS3":"NO071",  # Helgeland
         "MunicipalityId": "1811;1812;1813;1815;1816;1818;1820;1822;1824;1825;1826;1827;1828;1832;1833;1834;1835;1836;"
                           "1837"},
"9002": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Saltfjellet
         "MunicipalityId": "1833;1839;1840"},
"9003": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Salten
         "MunicipalityId": "1804;1838;1839;1840;1841;1845;1848;1849"},
"9004": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Lofoten
         "MunicipalityId": "1856;1857;1859;1860;1865;1874"},
"9005": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Ofoten
         "MunicipalityId": "1805;1850;1851;1852;1853;1854"},
"9006": {"iso":"NO-18","county":"18", "NUTS3":"NO071",    # Vester�len
         "MunicipalityId": "1866;1867;1868;1870;1871"},
"9007": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # S�r-Troms
         "MunicipalityId": "1903;1911;1913;1917;1919;1920;1923"},
"9008": {"iso":"NO-19","county":"19:54","NUTS3":"NO072",  # Nord-Troms
         "MunicipalityId": "1902;1933;1936;1938;1939;1940;1941;1942;1943"},
"9009": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # �st-Finnmark
         "MunicipalityId": "2002;2003;2022;2023;2024;2025;2027;2028;2030"},
"9010": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # Kyst- og fjordstr�kene i Vest-Finnmark
         "MunicipalityId": "2004;2012;2014;2015;2017;2018;2019;2020"},
"9011": {"iso":"NO-20","county":"20:54","NUTS3":"NO073",  # Finnmarksvidda
         "MunicipalityId": "2011;2021"},
"9018": {"iso":"NO-21","county":"21",
         "MunicipalityId":"2111"},   # Nordenski�ld Land p� Spitsbergen
# Fjellet i S�r-Norge ber�rer fylkene
    # Tr�ndelag, Oppland, Hedmark, Buskerud,Telemark, Aust-Agder, Vest-Agder, Rogaland,Hordaland,
    # Sogn og Fjordane, M�re og Romsdal
"0710" : {"iso":"NO-16:NO-05:NO-04:NO-06:NO-08:NO-09:NO-10:NO-11:NO-12:NO-14:NO-15",
          "county":"05:04:06:08:09:10:11:12:14:15:50:34:30:38:42:46",
          "NUTS3":"NO061:NO022:NO021:NO032:NO034:NO041:NO042:NO043:NO051:NO052:NO053",
          "MunicipalityId": "437;439;441;511;512;513;514;545;618;619;620;633;826;831;833;834;938;940;941;1026;1046;1134;"
                            "1228;1231;1232;1233;1421;1422;1424;1426;1449;1524;1525;1539;1543;1563;1566;1567;5033;5021;"
                            "5022;5026;5027"},
# Mapping of area used in METs warnings to Meteolarms internal emma_id
# �stfold kyst = NO801
# Aust-Agder kyst = NO802
# Finnmark kyst = NO803
# Troms kyst = NO804
# Nordland kyst = NO805
# Nord-Tr�ndelag kyst = NO806
# S�r-Tr�ndelag kyst = NO807
# M�re og Romsdal kyst = NO808
# Sogn og Fjordane kyst = NO809
# Hordaland kyst = NO810
# Rogaland kyst = NO811
# Vest-Agder kyst = NO812
# Vestfold kyst = NO813
# Telemark kyst = NO814

#"0816": # Indre Oslofjord = Oslo, Akershus, Buskerud
"19182": {"emma_id":"NO801:NO813"},# Svenskegrensa - Stavern = �sfold, Vestfold
"19171":  {"emma_id":"NO813:NO814"}, # Stavern - Jomfruland = Vestfold, Telemark
"19180":  {"emma_id":"NO814:NO802:NO812"}, # Jomfruland - Lyng�r = Telemark, Agder
"19168":  {"emma_id":"NO802:NO812"}, # Lyng�r - Torungen = Agder
"19181":  {"emma_id":"NO802:NO812"}, # Torungen - Oks�y = Agder
"19165":  {"emma_id":"NO802:NO812"}, # Oks�y - Lindesnes = Agder
"19059":  {"emma_id":"NO802:NO812"}, # Lindesnes - �na Sira = Agder
"19028":  {"emma_id":"NO811"}, # �na Sira -Obrestad = Rogaland
"19029":  {"emma_id":"NO811"}, # Obrestad - Karm�y = Rogaland
"19030":  {"emma_id":"NO811:NO810"}, # Karm�y - Sl�tter�y = Rogaland og Hordaland
"19031":  {"emma_id":"NO810"}, # Sl�tter�y - Fedje = Hordaland
"19032":  {"emma_id":"NO810:NO809"}, # Fedje - Bulandet = Hordaland, Sogn og Fjordane
"19033":  {"emma_id":"NO809"}, # Bulandet - M�l�y = Sogn og Fjordane
"19034":  {"emma_id":"NO809"}, # M�l�y - Stad = Sogn og Fjordane
"19035":  {"emma_id":"NO809:NO808"}, # Stad - Svin�y = Sogn og Fjordane, M�re og Romsdal
"19036":  {"emma_id":"NO808"}, # Svin�y - Ona = M�re og Romsdal
"19037":  {"emma_id":"NO808:NO806:NO807"}, # Ona - Fr�ya = M�re og Romsdal, Tr�ndelag
"19038":  {"emma_id":"NO806:NO807"}, # Fr�ya -Halten = Tr�ndelag
"19039":  {"emma_id":"NO806:NO807"}, # Halten - R�rvik = Tr�ndelag
"19064":  {"emma_id":"NO806:NO807:NO805"}, # R�rvik - Sandnessj�en = Tr�ndelag og Nordland
"19043":  {"emma_id":"NO805"}, # Sandnessj�en - St�tt = Nordland
"19044":  {"emma_id":"NO805"}, # St�tt - Bod� = Nordland
"19069":  {"emma_id":"NO805"}, # Bod� - L�dingen = Nordland
"19072":  {"emma_id":"NO805"}, # Skomv�r - Melbu = Nordland
"19073":  {"emma_id":"NO805"}, # Melbu - Andenes = Nordland
"19015":  {"emma_id":"NO805:NO804"}, # Andenes - Hekkingen = Nordland, Troms
"19048":  {"emma_id":"NO804"}, # Hekkingen - Torsv�g = Troms
"19065":  {"emma_id":"NO804:NO803"}, # Torsv�g - Loppa = Troms, Finnmark
"19051":  {"emma_id":"NO803"}, # Loppa - Fruholmen = Finnmark
"19052":  {"emma_id":"NO803"}, # Fruholmen Nordkapp = Finnmark
"19066":  {"emma_id":"NO803"}, # Nordkapp - Slettnes Fyr = Finnmark
"19055":  {"emma_id":"NO803"}, # Slettnes Fyr - Vard� = Finnmark
"19056":  {"emma_id":"NO803"}, # Vard� - Grense Jakobselv = Finnmark





}
