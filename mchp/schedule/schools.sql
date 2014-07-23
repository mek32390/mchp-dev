--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: schedule_school; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE schedule_school (
    id integer NOT NULL,
    domain character varying(200) NOT NULL,
    name character varying(100) NOT NULL,
    phone_number character varying(20) NOT NULL,
    address character varying(60) NOT NULL,
    city character varying(60) NOT NULL,
    state character varying(20) NOT NULL,
    country character varying(45) NOT NULL
);


--
-- Name: schedule_school_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE schedule_school_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: schedule_school_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE schedule_school_id_seq OWNED BY schedule_school.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY schedule_school ALTER COLUMN id SET DEFAULT nextval('schedule_school_id_seq'::regclass);


--
-- Data for Name: schedule_school; Type: TABLE DATA; Schema: public; Owner: -
--

COPY schedule_school (id, domain, name, phone_number, address, city, state, country) FROM stdin;
1	www.mctc.mnscu.edu	Minneapolis Community and Technical College	6126596000	1501 Hennepin Ave	Minneapolis	MN	United States of America
2	www.aihs.edu	American University of Health Sciences	5629882278	1600 East Hill Street	Signal Hill	CA	United States of America
3	www.alliedteched.edu	Fortis Institute - Scranton	5705581818	517 Ash Street	Scranton	PA	United States of America
4	www.ashdowncollege.edu	Ashdown College of Health Sciences	9097934263	101 East Redlands Blvd. Suite 285	Redlands	CA	United States of America
5	www.awc.edu	Allegheny Wesleyan College	3303376403	2161 Woodsdale Rd	Salem	OH	United States of America
6	www.beacon.edu	Beacon University	7063235364	6003 Veterans Parkway	Columbus	GA	United States of America
7	www.bealcollege.edu	Beal College	2079474591	99 Farm Road	Bangor	ME	United States of America
8	www.beautyschool.edu	Career Academy of Hair Design	4797566060	346 East Robinson Avenue	Springdale	AR	United States of America
9	www.peralta.edu	Berkeley City College	5109812800	2050 Center Street	Berkeley	CA	United States of America
10	www.ab.edu	Alderson Broaddus University	3044571700	101 College Hill Drive	Philippi	WV	United States of America
11	www.brc.edu	Baton Rouge College	2252925464	1900 North Lobdall Avenue	Baton Rouge	LA	United States of America
12	www.Californiacareerschool.edu	California Career School	7146356585	1100 Technology Cir	Anaheim	CA	United States of America
13	www.canadacollege.edu	Canada College	6503063100	4200 Farm Hill Blvd.	Redwood City	CA	United States of America
14	www.capitol-college.edu	Capitol College	3013692800	11301 Springfield Rd	Laurel	MD	United States of America
15	www.careerta.edu	Career Training Academy	7243371000	950 5th Ave	New Kensington	PA	United States of America
16	www.cccua.edu	Cossatot Community College of the University of Arkansas	8705844471	183 Hwy 399	De Queen	AR	United States of America
17	www.cci.edu	Everest Institute - Hayward	5105829500	22336 Main Street	Hayward	CA	United States of America
18	www.chase.edu	Chase College	2133651999	3580 Wilshire Blvd #400	Los Angeles	CA	United States of America
19	www.cccd.edu	Coastline Community College	7145467600	11460 Warner Ave	Fountain Valley	CA	United States of America
20	www.cos.edu	College of the Sequoias	5597303700	915 S Mooney Blvd	Visalia	CA	United States of America
21	www.csb.edu	Consolidated School of Business	7173946211	2124 Ambassador Cir	Lancaster	PA	United States of America
22	daley.ccc.edu	City Colleges of Chicago-Richard J Daley College	7738387500	7500 S Pulaski Rd	Chicago	IL	United States of America
23	www.daymarcollege.edu	Daymar College-Louisville	5024951040	4400 Breckenridge Lane Suite 415	Louisville	KY	United States of America
24	www.dinecollege.edu	Dine College	5207246600	P.O. Box 126	Tsaile	AZ	United States of America
25	www.donnelly.edu	Donnelly College	9136216070	608 N 18th St	Kansas City	KS	United States of America
26	www.remingtoncollege.edu	Remington College-Houston Campus	2818991240	3110 Hayes Road Suite 380	Houston	TX	United States of America
27	www.erwin.edu	D.G. Erwin Technical Center	8132311903	2010 E Hillsborough Ave	Tampa	FL	United States of America
28	ewc.wy.edu	Eastern Wyoming College	3075328200	3200 West C St	Torrington	WY	United States of America
29	www.federico.edu	Federico Beauty Institute	9169294242	1515 Sports Drive    Ste 100	Sacramento	CA	United States of America
30	gateway.kingsuniversity.edu	The King's University	8187798040	2121 East Southlake Boulevard	Southlake	TX	United States of America
31	www.glenoaks.edu	Glen Oaks Community College	2694679945	62249 Shimmel Rd	Centreville	MI	United States of America
32	www.gretnacareercollege.edu	Gretna Career College	5043665409	1415 Whitney Ave	Gretna	LA	United States of America
33	www.hci.edu	Harrison Career Institute - Vineland	8566960500	1386 S Delsea Dr	Vineland	NJ	United States of America
34	henderson.kctcs.edu	Henderson Community College	2708271867	2660 S Green St	Henderson	KY	United States of America
35	www.hightechinstitute.edu	High-Tech Institute - Atlanta	6782797000	1090 Northchase Pkwy-Ste 150	Marietta	GA	United States of America
36	www.cfcc.edu	Cape Fear Community College	9103627000	411 North Front Street	Wilmington	NC	United States of America
37	www.northface.edu	Neumont University	8017332800	143 South Main Street	Salt Lake City	UT	United States of America
38	www.sscms.edu	SS. Cyril & Methodius Seminary	2486830310	3535 Indian Trail	Orchard Lake	MI	United States of America
39	www.stanford.edu	Stanford University Residency in Clinical Child Psychology		450 Serra Mall	Stanford	CA	United States of America
40	www.uvm.edu	University of Vermont Psychology Internship	8026563131	85 S Prospect St	Burlington	VT	United States of America
41	hwashington.ccc.edu	City Colleges of Chicago-Harold Washington College	3125535600	30 E Lake St	Chicago	IL	United States of America
42	www.IBConline.edu	International Baptist College	4808387070	2211 Germann Road	Chandler	AZ	United States of America
43	www.idi.edu	Interior Designers Institute	9496754451	1061 Camelback Rd	Newport Beach	CA	United States of America
44	www.intlbusinesscollege.edu	International Business College - Fort Wayne	2604594500	5699 Coventry Lane	Fort Wayne	IN	United States of America
45	www.jccmi.edu	Jackson Community College	5177870800	2111 Emmons Rd	Jackson	MI	United States of America
46	www.kcma.edu	Kettering College of Medical Arts	9373958601	3737 Southern Blvd	Kettering	OH	United States of America
47	kennedyking.ccc.edu	City Colleges of Chicago-Kennedy-King College	7736025000	6301 South Halsted Street	Chicago	IL	United States of America
48	www.kenrick.edu	Kenrick-Glennon Seminary	3147926100	5200 Glennon Dr.	St. Louis	MO	United States of America
49	www.kilian.edu	Kilian Community College	6052213100	300 E. 6th Street	Sioux Falls	SD	United States of America
50	www.laredo.edu	Laredo Community College	9567215394	West End Washington Street	Laredo	TX	United States of America
51	law.rwu.edu	Roger Williams University School of Law	4012544500	Ten Metacom Ave	Bristol	RI	United States of America
52	www.lbwcc.edu	Lurleen B Wallace Community College	3342226591	1000 Dannelly Blvd.	Andalusia	AL	United States of America
53	malcolmx.ccc.edu	City Colleges of Chicago-Malcolm X College	3128507000	1900 W Van Buren	Chicago	IL	United States of America
54	www.matcmadison.edu	Madison Area Technical College	6082466100	3550 Anderson St	Madison	WI	United States of America
55	www.mbbc.edu	Maranatha Baptist Bible College	9202619300	745 W. Main St.	Watertown	WI	United States of America
56	mcc.cccoes.edu	Morgan Community College	9705423100	920 Barlow Road	Fort  Morgan	CO	United States of America
57	medicine.utah.edu	University of Utah Health Sciences Center	8015817200	30 North 1900 East #1A971	Salt Lake City	UT	United States of America
58	www.medixschool.edu	Fortis Institute - Towson	4103375155	700 York Road	Towson	MD	United States of America
59	www.merrelluniversity.edu	Merrell University of Beauty Arts and Science	5736354433	1753 Woodclift Drive	Jefferson City	MO	United States of America
60	www.metropolitancollege.edu	Metropolitan College	4058431000	1900 NW Expressway #r302	Oklahoma City	OK	United States of America
61	www.minneapolisbusinesscollege.edu	Minneapolis Business College	6516367406	1711 W County Rd B	Roseville	MN	United States of America
62	www.naes.edu	NAES College	7737615000	2838 West Peterson Avenue	Chicago	IL	United States of America
63	www.nationalinstituteoftechnology.edu	National Institute of Technology	3309239959	2545 Bailey Road	Cuyahoga Falls	OH	United States of America
64	www.nechristian.edu	Nebraska Christian College	4023795000	12550 S. 114th St.	Papillion	NE	United States of America
65	www.NMC.edu	Northwestern Michigan College	2319951000	1701 E Front St	Traverse City	MI	United States of America
66	www.nnmcc.edu	Northern New Mexico College	5057472100	PO Box 160	El Rito	NM	United States of America
67	www.northcentralcollege.edu	North Central College	6306375100	30 N Brainard St	Naperville	IL	United States of America
68	www.northwesterncollege.edu	Northwestern College - Chicago	7737774220	4829 North Lipps Avenue	Chicago	IL	United States of America
69	www.oaa.edu	Oakbridge Academy of Arts	7243355336	1250 Greensburg Rd	Lower Burrell	PA	United States of America
70	www.obi.edu	Olean Business Institute	7163727978	301 N Union St	Olean	NY	United States of America
71	www.ocb.edu	Oceanside College of Beauty	7607576161	1575 S Coast Hwy	Oceanside	CA	United States of America
72	oliveharvey.ccc.edu	City Colleges of Chicago-Olive-Harvey College	7732916100	10001 S Woodlawn Ave	Chicago	IL	United States of America
73	online.kaplanuniversity.edu	Kaplan University	5633553500	1801 E Kimberly Rd Ste 1	Davenport	IA	United States of America
74	www.oregonstate.edu	Oregon State University	5417370123		Corvallis	OR	United States of America
75	www.oru.edu	Oral Roberts University	9184956161	7777 S Lewis	Tulsa	OK	United States of America
76	www.parisjc.edu	Paris Junior College	9037857661	2400 Clarksville St	Paris	TX	United States of America
77	www.pcom.edu	Philadelphia College of Osteopathic Medicine	2158716770	4170 City Ave	Philadelphia	PA	United States of America
78	pert.uwlax.edu	Franciscan Skemp Healthcare School of Anesthesia		700 West Avenue	La Crosse	WI	United States of America
79	www.pgi.edu	Phillips Graduate Institute	8183865600	5445 Balboa Blvd	Encino	CA	United States of America
80	pio.okstate.edu	Oklahoma State University	4057445000	107 Whitehurst Hall	Stillwater	OK	United States of America
81	www.pioneerpacific.edu	Pioneer Pacific College	5036823903	27501 SW Parkway Ave	Wilsonville	OR	United States of America
82	www.potomac.edu	Potomac College	2026860876	1401 H Street NW	Washington	DC	United States of America
83	www.ptmcaz.edu	Phoenix Therapeutic Massage College	4809459461	8010 East McDowell Road #214	Scottsdale	AZ	United States of America
84	www.pvbi.edu	Penn View Bible Institute	5708371855	125 Penn View Drive	Penns Creek	PA	United States of America
85	region3.ltc.edu	South Central Louisiana Technical College	9853802436	900 Youngs Road	Morgan City	LA	United States of America
86	www.remingtoncollege.edu	Remington College - Lafayette Campus	3379814010	303 Rue Louis XIV	Lafayette	LA	United States of America
87	www.ridley.edu	Ridley-Lowell Business and Technical Institute - Poughkeepsie	8454710330	26 S Hamilton St	Poughkeepsie	NY	United States of America
88	www.sacn.edu	Saint Anthony College of Nursing	8153955091	5658 E State St	Rockford	IL	United States of America
89	sci.odu.edu/	Virginia Consortium for Professional Psychology		1881 University Drive	Virginia Beach	VA	United States of America
90	seminary.cbs.edu	Calvary Baptist Theological Seminary	2153687538	1380 S. Valley Forge Rd.	Lansdale	PA	United States of America
91	www.seu.edu	Southeastern University	8636675000	1000 Longfellow Blvd	Lakeland	FL	United States of America
92	www.sfccmo.edu	State Fair Community College	6605305800	3201 W 16th Street	Sedalia	MO	United States of America
93	www.sjvcs.edu	Saint John Vianney College Seminary	3052234561	2900 SW 87th Ave	Miami	FL	United States of America
94	www.southeasterncareercollege.edu	Kaplan Career Institute - Nashville	8003364457	750 Envious Lane	Nashville	TN	United States of America
95	www.southuniversity.edu	South University-Montgomery	3343958800	5355 Vaughn Road	Montgomery	AL	United States of America
96	www.specshoward.edu	Specs Howard School of Media Arts	2483589000	19900 W Nine Mile Rd	Southfield	MI	United States of America
97	www.stevenshenager.edu	Stevens-Henager College-Ogden	8013947791	1350 W. 1890 S.	West Haven	UT	United States of America
98	www.talmudicu.edu	Talmudic College of Florida	3055347050	4000 Alton Road	Miami Beach	FL	United States of America
99	www.thompson.edu	Thompson Institute	7177099400	2593 Philadelphia Ave	Chambersburg	PA	United States of America
100	www.trinitycollege.edu	Trinity College of Florida	7273766911	2430 Welbilt Blvd	Trinity	FL	United States of America
101	www.uindy.edu	University of Indianapolis	3177883368	1400 E Hanna Ave	Indianapolis	IN	United States of America
102	www.usiouxfalls.edu	University of Sioux Falls	6053315000	1101 W 22nd St	Sioux Falls	SD	United States of America
103	www.uwf.edu	The University of West Florida	8504742000	11000 University Pky	Pensacola	FL	United States of America
104	www.uwplatt.edu	University of Wisconsin - Platteville	6083421421	1 University Plz	Platteville	WI	United States of America
105	www.valenciacc.edu	Valencia College	4072992187	190 South Orange Avenue	Orlando	FL	United States of America
106	www.vatterott-college.edu	Vatterott College - Oklahoma City	4059450088	4621 NW 23	Oklahoma City	OK	United States of America
107	www.wccc.edu	Westmoreland County Community College	7249254000	145 Pavilion Lane	Youngwood	PA	United States of America
108	web.indstate.edu	Indiana State University	8122376311	200 N 7th St	Terre Haute	IN	United States of America
109	web.mit.edu	Massachusetts Institute of Technology	6172531000	77 Massachusetts Avenue	Cambridge	MA	United States of America
110	www.woodtobecoburn.edu	Wood Tobe-Coburn School	2126869040	8 E 40th St	New  York	NY	United States of America
111	wright.ccc.edu	City Colleges of Chicago - Wilbur Wright College	7734818200	4300 N Narragansett Avenue	Chicago	IL	United States of America
112	www.wschiro.edu	University of Western States	5032563180	2900 NE 132nd Ave	Portland	OR	United States of America
113	www.aaart.edu	American Academy of Art	3124610600	332 S Michigan Ave	Chicago	IL	United States of America
114	www.aacc.edu	Anne Arundel Community College	4107774444	101 College Parkway	Arnold	MD	United States of America
115	www.aai.edu	Arizona Automotive Institute	8005280717	6829 N 46th Ave	Glendale	AZ	United States of America
116	www.aamu.edu	Alabama A & M University	2563725000	4900 Meridian St	Normal	AL	United States of America
117	www.abac.edu	Abraham Baldwin Agricultural College	2293863236	2802 Moore Hwy	Tifton	GA	United States of America
118	www.abc.edu	Appalachian Bible College	3048776428	161 College Drive	Mt. Hope	WV	United States of America
119	www.abcnash.edu	American Baptist College	6152561463	1800 Baptist World Ctr Dr	Nashville	TN	United States of America
120	www.abconline.edu	Arlington Baptist College	8174618741	3001 W Division	Arlington	TX	United States of America
121	www.abctx.edu	Austin Business College	5124479415	2101 I H 35 South Ste 300	Austin	TX	United States of America
122	www.absw.edu	American Baptist Seminary of the West	5108411905	2606 Dwight Way	Berkeley	CA	United States of America
123	www.abtech.edu	Asheville Buncombe Technical Community College	8282541921	340 Victoria Rd	Asheville	NC	United States of America
124	www.aca.edu	Atlanta College of Art	4047335001	1280 Peachtree St N E	Atlanta	GA	United States of America
125	www.acacia.edu	Acacia University	4805577970	7665 S. Research Drive	Tempe	AZ	United States of America
126	www.academyart.edu	Academy of Art University	4152742200	79 New Montgomery	San Francisco	CA	United States of America
127	www.academycollege.edu	Academy College	9528510066	1600 W. 82nd Street	Bloomington	MN	United States of America
128	www.academypacific.edu	Academy Pacific Travel College	3234623211	1777 N Vine St	Los Angeles	CA	United States of America
129	www.acaom.edu	American College of Acupuncture and Oriental Medicine	7137809777	9100 Park West Drive	Houston	TX	United States of America
130	www.acc.commnet.edu	Asnuntuck Community College	8602533000	170 Elm St	Enfield	CT	United States of America
131	www.acc.edu	Point University	4047618861	2605 Ben Hill Road	East Point	GA	United States of America
132	www.acchs.edu	Academy of Chinese Culture and Health Sciences	5107637787	1601 Clay St	Oakland	CA	United States of America
133	www.accutech.edu	Accutech Career Institute	3016940211	5310 Spectrum Dr	Frederick	MD	United States of America
134	www.achs.edu	American College of Healthcare Sciences	8004878839	5940 SW Hood Ave	Portland	OR	United States of America
135	www.acot.edu	American Business and Technology University		2700 N. Belt Highway	Saint Joseph	MO	United States of America
136	www.acphs.edu	Albany College of Pharmacy	5184457200	106 New Scotland Avenue	Albany	NY	United States of America
137	www.actcm.edu	American College of Traditional Chinese Medicine	4152827600	455 Arkansas St	San Francisco	CA	United States of America
138	www.actx.edu	Amarillo College	8063653631	2200 S. Washington	Amarillo	TX	United States of America
139	www.acu.edu	Abilene Christian University	3256742000	1600 Campus Court	Abilene	TX	United States of America
140	www.acupuncturecollege.edu	Southwest Acupuncture College - Santa Fe	5054388884	1622 Galisteo Street	Santa Fe	NM	United States of America
141	www.acupuncturist.edu	Academy for Five Element Acupuncture	3523352332	305 SE 2nd Avenue	Gainesville	FL	United States of America
142	www.adams.edu	Adams State University	7195877011	208 Edgemont Blvd	Alamosa	CO	United States of America
143	www.adconsys.edu	ATI College	5628640506	12440 Firestone Blvd Ste 2001	Norwalk	CA	United States of America
144	www.adler.edu	Adler School of Professional Psychology	3122015900	65 E Wacker Pl Ste 2100	Chicago	IL	United States of America
145	www.adrian.edu	Adrian College	5172655161	110 S Madison St	Adrian	MI	United States of America
146	www.agnesscott.edu	Agnes Scott College	4044716000	141 E. College Ave	Decatur	GA	United States of America
147	www.agts.edu	Assemblies of God Theological Seminary	4172681000	1435 N Glenstone Ave	Springfield	MO	United States of America
148	www.agu.edu	American Graduate University		733 North Dodsworth Avenue	Covina	CA	United States of America
149	www.ahcp.edu	The College of Health Care Professions	7134253100	240 Northwest Mall	Houston	TX	United States of America
150	www.ai.edu	Aquinas Institute of Theology	3149773882	23 South Spring Avenue	St. Louis	MO	United States of America
151	www.aiam.edu	American Institute of Alternative Medicine	6148256278	6685 Doubletree Ave	Columbus	OH	United States of America
152	www.aib.edu	AIB College of Business	5152444221	2500 Fleur Drive	Des Moines	IA	United States of America
153	www.aic.artinstitutes.edu	The Art Institute of Colorado	3038370825	1200 Lincoln Street	Denver	CO	United States of America
154	www.aic.edu	American International College	4137377000	1000 State Street	Springfield	MA	United States of America
155	www.aica.artinstitutes.edu	The Art Institute of California - San Diego	8662752422	7650 Mission Valley Road	San Diego	CA	United States of America
156	www.aicag.edu	American Indian College of the Assemblies of God	6029443335	10020 N 15th Ave	Phoenix	AZ	United States of America
157	www.aicdc.artinstitutes.edu	The Art Institute of California - Hollywood	2132513636	5250 Lankershim Boulevard	North Hollywood	CA	United States of America
158	www.aifl.edu	The Art Institute of Fort Lauderdale Inc	9544633000	1799 SE 17th St	Fort Lauderdale	FL	United States of America
159	www.aii.edu	The Illinois Institute of Art - Chicago	3122803500	350 N Orleans St	Chicago	IL	United States of America
160	www.aila.artinstitutes.edu	The Art Institute of California - Los Angeles	3107524700	2900 31st St	Santa Monica	CA	United States of America
216	www.amherst.edu	Amherst College	4135422000	Boltwood Avenue	Amherst	MA	United States of America
161	www.aim.artinstitutes.edu	The Art Institutes International Minnesota	6123323361	15 S 9th St	Minneapolis	MN	United States of America
162	www.aimc.edu	Acupuncture and Integrative Medicine College - Berkeley	5106668248	2550 Shattuck Ave	Berkeley	CA	United States of America
163	www.aims.edu	Aims Community College	9703308008	5401 W. 20th St.	Greeley	CO	United States of America
164	www.ainyc.artinstitute.edu	The Art Institute of New York City	2122265500	218 West 40th Street	New York	NY	United States of America
165	www.aip.aii.edu	The Art Institute of Pittsburgh	4122916200	420 Boulevard of the Allies	Pittsburgh	PA	United States of America
166	www.aipd.artinstitutes.edu	The Art Institute of Portland	5032286528	1122 NW Davis St.	Portland	OR	United States of America
167	www.aiph.aii.edu	The Art Institute of Philadelphia	8002752474	1622 Chestnut Street	Philadelphia	PA	United States of America
168	www.aipx.aii.edu	The Art Institute of Phoenix	6026784300	2233 W Dunlap Ave	Phoenix	AZ	United States of America
169	www.ais.edu	The Art Institute of Seattle	2064480900	2323 Elliott Ave	Seattle	WA	United States of America
170	www.alamancecc.edu	Alamance Community College	3365782002	1247 Jimmie Kerr Road	Graham	NC	United States of America
171	www.alamo.edu	Northwest Vista College	2103482001	3535 North West Ellison Dr	San Antonio	TX	United States of America
172	www.alamo.edu	Palo Alto College	2109215000	1400 West Villaret	San Antonio	TX	United States of America
173	www.alamo.edu	San Antonio College	2107332000	1300 San Pedro Ave	San Antonio	TX	United States of America
174	www.alamo.edu	St. Philip's College	2105313591	1801 Martin Luther King Drive	San Antonio	TX	United States of America
175	www.alaskapacific.edu	Alaska Pacific University	9075611266	4101 University Dr	Anchorage	AK	United States of America
176	www.alasu.edu	Alabama State University	3342294400	915 S Jackson Street	Montgomery	AL	United States of America
177	www.albany.edu	SUNY at Albany	5184423300	1400 Washington Avenue	Albany	NY	United States of America
178	www.albanytech.edu	Albany Technical College	2294303500	1704 South Slappey Boulevard	Albany	GA	United States of America
179	www.albemarle.edu	College of the Albemarle	2523350821	1208 North Road Street	Elizabeth City	NC	United States of America
180	www.albertus.edu	Albertus Magnus College	2037738550	700 Prospect St	New Haven	CT	United States of America
181	www.albion.edu	Albion College	5176291000	611 E Porter St	Albion	MI	United States of America
182	www.albright.edu	Albright College	6109212381	1621 N. 13th St.	Reading	PA	United States of America
183	www.alc.edu	Alice Lloyd College	6063682101	100 Purpose Rd	Pippa Passes	KY	United States of America
184	www.alcorn.edu	Alcorn State University	6018776100	1000 ASU Dr Ste 359	Alcorn State	MS	United States of America
185	www.alextech.edu	Alexandria Technical College	3207620221	1601 Jefferson Streeet	Alexandria	MN	United States of America
186	www.alfred.edu	Alfred University	6078712111	One Saxon Dr	Alfred	NY	United States of America
187	www.alfredadler.edu	Adler Graduate School	6129884170	1550 East 78th Street	Richfield	MN	United States of America
188	www.alfredstate.edu	SUNY College of Technology at Alfred	6075874111	Huntington Administration Building	Alfred	NY	United States of America
189	www.allegany.edu	Allegany College of Maryland	3017845000	12401 Willowbrook Rd SE	Cumberland	MD	United States of America
190	www.allegheny.edu	Allegheny College	8143323100	520 N Main St	Meadville	PA	United States of America
191	www.allencc.edu	Allen County Community College	6203655116	1801 N Cottonwood	Iola	KS	United States of America
192	www.allencollege.edu	Allen College	3192262000	1825 Logan Avenue	Waterloo	IA	United States of America
193	www.allenschool.edu	Allen School - Jamaica	7182912200	163-18 Jamaica Avenue	Jamaica	NY	United States of America
194	www.allenuniversity.edu	Allen University	8032544165	1530 Harden Street	Columbia	SC	United States of America
195	www.alliant.edu	Alliant International University	8582714300	10455 Pomerado Road	San Diego	CA	United States of America
196	www.Alliedteched.edu	Fortis Institute - Forty Fort	5702888400	166 Slocum Street	Forty Fort	PA	United States of America
197	www.alliedteched.edu	Allied Medical and Technical Institute	9738371818	201 Willowbrook Blvd.	Wayne	NJ	United States of America
198	www.alma.edu	Alma College	9894637111	614 W. Superior Street	Alma	MI	United States of America
199	www.alpenacc.edu	Alpena Community College	9893569021	665 Johnson Street	Alpena	MI	United States of America
200	www.als.edu	Albany Law School	5184452311	80 New Scotland Avenue	Albany	NY	United States of America
201	www.altamahatech.edu	Altamaha Technical College	9124275800	1777 W Cherry St	Jesup	GA	United States of America
202	www.alvernia.edu	Alvernia University	6107968200	400 Saint Bernardine St	Reading	PA	United States of America
203	www.alverno.edu	Alverno College	4143826000	3400 S 43rd  St	Milwaukee	WI	United States of America
204	www.alvincollege.edu	Alvin Community College	2817563500	3110 Mustang Rd	Alvin	TX	United States of America
205	www.amberton.edu	Amberton University	9722796511	1700 Eastgate Dr	Garland	TX	United States of America
206	www.ambs.edu	Anabaptist Mennonite Biblical Seminary	5742953726	3003 Benham Ave	Elkhart	IN	United States of America
207	www.amc.edu	Albany Medical College	5182625582	47 New Scotland Ave	Albany	NY	United States of America
208	www.AMCOLLEGE.edu	Acupuncture and Massage College	3055959500	10506 N Kendall Dr	Miami	FL	United States of America
209	www.amda.edu	American Musical and Dramatic Academy - New York	2127875300	211 West 61st Street	New York	NY	United States of America
210	www.amercoll.edu	American College	6105261000	270 Bryn Mawr Ave	Bryn Mawr	PA	United States of America
211	www.american.edu	American University	2028851000	4400 Massachusetts Avenue N.W.	Washington	DC	United States of America
212	www.americanacademy.edu	American Academy of Hair Design	7852675800	901 SW 37th St	Topeka	KS	United States of America
213	www.americanhealth.edu	American Health Institute	7272320175	10138 US Highway 19	Port Richey	FL	United States of America
214	www.americanparalegal.edu	American Institute for Paralegal	8005532420	560 Lans Way	Ann Arbor	MI	United States of America
215	www.ameritech.edu	AmeriTech College - Provo	8013772900	2035 North 550 West	Provo	UT	United States of America
217	www.amridgeuniversity.edu	Amridge University	3343873877	1200 Taylor Rd	Montgomery	AL	United States of America
218	www.anc.edu	Arkansas Northeastern College	8707621020	2501 South Division Street	Blytheville	AR	United States of America
219	www.ancilla.edu	Ancilla College	5749368898	9601 Union Road	Donaldson	IN	United States of America
220	www.anderson.edu	Anderson University	7656499071	1100 E 5th St	Anderson	IN	United States of America
221	www.andersonuniversity.edu	Anderson University	8642312000	316 Boulevard	Anderson	SC	United States of America
222	www.ANDOVERCOLLEGE.edu	Andover College	2077746126	265 Western Avenue	South Portland	ME	United States of America
223	www.andrewcollege.edu	Andrew College	2297322171	413 College St	Cuthbert	GA	United States of America
224	www.andrews.edu	Andrews University	8002532874	US 31 North	Berrien Springs	MI	United States of America
225	www.angelina.edu	Angelina College	9366391301	3500 South First	Lufkin	TX	United States of America
226	www.angelo.edu	Angelo State University	3259422555	2601 W Avenue N	San Angelo	TX	United States of America
227	www.annamaria.edu	Anna Maria College	5088493300	10 Sunset Lane	Paxton	MA	United States of America
228	www.anokaramsey.edu	Anoka-Ramsey Community College	7634272600	11200 Mississippi Blvd. NW	Coon Rapids	MN	United States of America
229	www.anokatech.edu	Anoka Technical College	7635764700	1355 W Hwy 10	Anoka	MN	United States of America
230	www.anselm.edu	Saint Anselm College	6036417000	100 Saint Anselm Drive	Manchester	NH	United States of America
231	www.antioch.edu	Antioch University	9377691340	900 Dayton Street	Yellow Springs	OH	United States of America
232	www.antonelli.edu	Antonelli Institute	2158362222	300 Montgomery Ave	Erdenheim	PA	United States of America
233	www.ants.edu	Andover Newton Theological School	6179641100	210 Herrick Rd	Newton Centre	MA	United States of America
234	www.aoma.edu	AOMA Graduate School of Integrative Medicine	5124541188	2700 W Anderson Ln Ste 204	Austin	TX	United States of America
235	www.apollocollege.edu	Carrington College - Phoenix	6024331333	8503 N 27th Ave	Phoenix	AZ	United States of America
236	www.appalachiantech.edu	Appalachian Technical College	7062534500	100 Campus Drive	Jasper	GA	United States of America
237	www.appstate.edu	Appalachian State University	8282622000		Boone	NC	United States of America
238	www.apsu.edu	Austin Peay State University	9312217011	601 College St	Clarksville	TN	United States of America
239	www.apu.edu	Azusa Pacific University	6269693434	901 E Alosta	Azusa	CA	United States of America
240	www.apu.edu/	Azusa Pacific Online University	6268153887	511 West Citrus Edge Street	Glendora	CA	United States of America
241	www.apus.edu	American Public University System		111 West Congress Street	Charles Town	WV	United States of America
242	www.aquinas.edu	Aquinas College	6166328900	1607 Robinson Rd SE	Grand Rapids	MI	United States of America
243	www.aquinascollege.edu	Aquinas College	6152977545	4210 Harding Roadd	Nashville	TN	United States of America
244	www.arapahoe.edu	Arapahoe Community College	3037975954	5900 S. Santa Fe Dr.	Littleton	CO	United States of America
245	www.arbor.edu	Spring Arbor University	5177501200	106 E. Main St	Spring Arbor	MI	United States of America
246	www.arc.losrios.edu	American River College	9164848350	4700 College Oak Dr	Sacramento	CA	United States of America
247	www.arcadia.edu	Arcadia University	2155722900	450 S Easton Rd	Glenside	PA	United States of America
248	www.arizona.edu	University of Arizona	5206212211	1401 E University	Tucson	AZ	United States of America
249	www.arkansasbaptist.edu	Arkansas Baptist College	5013747856	1621 Dr. Martin Luther King Drive	Little Rock	AR	United States of America
250	www.armstrong.edu	Armstrong Atlantic State University	9129275211	11935 Abercorn St	Savannah	GA	United States of America
251	www.artacademy.edu	Art Academy of Cincinnati	5135628767	1212 Jackson Street	Cincinnati	OH	United States of America
252	www.artcenter.edu	Art Center College of Design	6263962200	1700 Lida St	Pasadena	CA	United States of America
253	www.artic.edu	School of the Art Institute of Chicago	3128995100	37 S Wabash	Chicago	IL	United States of America
254	www.artinstitutes.edu/	The Art Institute of Dallas	2146928080	8080 Park Lane #100	Dallas	TX	United States of America
255	www.artinstitutes.edu/	The Art Institute of Houston	7136232040	1900 Yorktown Street	Houston	TX	United States of America
256	www.artinstitutes.edu/	Miami International University of Art and Design	3054285700	1501 Biscayne Boulevard	Miami	FL	United States of America
257	www.artinstitutes.edu	The Art Institute of York	7177552300	1409 Williams Road	York	PA	United States of America
258	www.artinstructionschools.edu	Art Instruction Schools	6123635060	3400 Technology Drive	Minneapolis	MN	United States of America
259	www.asa.edu	ASA Institute of Business and Computer Technology	7185229073	151 Lawrence Street	Brooklyn	NY	United States of America
260	www.asbury.edu	Asbury University	8598583511	1 Macklem Drive	Wilmore	KY	United States of America
261	www.asburyseminary.edu	Asbury Theological Seminary	8598583581	204 N Lexington Ave	Wilmore	KY	United States of America
262	www.ascc.edu	Alabama Southern Community College	2515753156	2800 South Alabama Avenue	Monroeville	AL	United States of America
263	www.ashford.edu	Ashford University	5632424023	400 North Bluff Blvd.	Clinton	IA	United States of America
264	www.ashland.edu	Ashland University	4192894142	401 College Ave	Ashland	OH	United States of America
265	www.ashland.kctcs.edu	Ashland Community and Technical College	6063262000	1400 College Drive	Ashland	KY	United States of America
266	www.ashworthcollege.edu	Ashworth College	7707298400	6625 The Corners Parkway	Norcross	GA	United States of America
267	www.asianinstitute.edu	Han University of Traditional Medicine	5203226330	2856 E. Fort Lowell Road	Tucson	AZ	United States of America
268	www.asl.edu	Appalachian School of Law	2769354349	1169 Edgewater Drive	Grundy	VA	United States of America
269	www.assumption.edu	Assumption College	5087677000	500 Salisbury St	Worcester	MA	United States of America
270	www.ast.edu	American School of Technology	6144364820	4599 Morse Center Road	Columbus	OH	United States of America
271	www.astate.edu	Arkansas State University	8709723056	P.O. Box 600	State University	AR	United States of America
272	www.asu.edu	Arizona State University	4809659011	P.O. Box 2203	Tempe	AZ	United States of America
273	www.asumh.edu	Arkansas State University Mountain Home	8705086100	1600 South College Street	Mountain Home	AR	United States of America
274	www.asun.edu	Arkansas State University - Newport	8705127800	7648 Victory Blvd.	Newport	AR	United States of America
275	www.at-homeprofessions.edu	At-Home Professions	9702256300	2001 Lowe Street	Fort Collins	CO	United States of America
276	www.atc.edu	Aiken Technical College	8035939231	2276 Jefferson Davis Highway	Graniteville	SC	United States of America
277	www.athenaeum.edu	Athenaeum of Ohio	5132312223	6616 Beechmont Ave	Cincinnati	OH	United States of America
278	www.athens.edu	Athens State University	2562338100	300 N Beaty St	Athens	AL	United States of America
279	www.athenstech.edu	Athens Technical College	7063555000	800 US Hwy 29 N	Athens	GA	United States of America
280	www.aticareertraining.edu	ATI Career Training Center - Fort Lauderdale	9549734760	2890 Northwest 62nd Street	Fort Lauderdale	FL	United States of America
281	www.atlanticuniv.edu	Atlantic University	7576318101	215 67th Street	Virginia Beach	VA	United States of America
282	www.auburn.edu	Auburn University Main Campus	3348444000		Auburn University	AL	United States of America
283	www.auc.edu	Atlantic Union College	9783682000	338 Main St	South Lancaster	MA	United States of America
284	www.aug.edu	Augusta State University	7067371400	2500 Walton Way	Augusta	GA	United States of America
285	www.augie.edu	Augustana College	6052740770	2001 S Summit Ave	Sioux Falls	SD	United States of America
286	www.augsburg.edu	Augsburg College	6123301000	2211 Riverside Ave	Minneapolis	MN	United States of America
287	www.augustana.edu	Augustana College	3097947000	639 38th St	Rock Island	IL	United States of America
288	www.augustatech.edu	Augusta Technical College	7067714000	3200 Augusta Tech Drive	Augusta	GA	United States of America
289	www.aum.edu	Auburn University-Montgomery	3342443000	7440 East Drive P.O. Box 244023	Montgomery	AL	United States of America
290	www.aurora.edu	Aurora University	6308926431	347 S Gladstone Ave	Aurora	IL	United States of America
291	www.austincc.edu	Austin Community College	5122237000	5930 Middle Fiskville Rd	Austin	TX	United States of America
292	www.austincollege.edu	Austin College	9038132000	900 N Grand Ave	Sherman	TX	United States of America
293	www.austingrad.edu	Austin Graduate School of Theology	5124762772	1909 University Ave	Austin	TX	United States of America
294	www.austinseminary.edu	Austin Presbyterian Theological Seminary	5124726736	100 E 27th St	Austin	TX	United States of America
295	www.auto.edu	Advanced Technology Institute	7574901241	5700 Southern Blvd Ste 100	Virginia Beach	VA	United States of America
296	www.autotraining.edu	Automotive Training Center	6103636716	114 Pickering Way	Exton	PA	United States of America
297	www.avc.edu	Antelope Valley College	6617226300	3041 W Ave K	Lancaster	CA	United States of America
298	www.avemaria.edu	Ave Maria University		5050 Ave Maria Boulevard	Ave Maria	FL	United States of America
299	www.avemarialaw.edu	Ave Maria School of Law	2396875300	1025 Commons Circle	Naples	FL	United States of America
300	www.averett.edu	Averett University	4347915600	420 W Main St	Danville	VA	United States of America
301	www.aviation.eocc.edu	Alabama Aviation College	3347745113	3405 South U.S. Highway 231	Ozark	AL	United States of America
302	www.aviationmaintenance.edu	Aviation Institute of Maintenance - Houston	7136447777	7651 Airport Blvd.	Houston	TX	United States of America
303	www.Avila.edu	Avila University	8169428400	11901 Wornall Rd	Kansas City	MO	United States of America
304	www.azwestern.edu	Arizona Western College	9283176000	P.O. Box 929	Yuma	AZ	United States of America
305	www.babel.edu	Babel University Professional School of Translation		1833 Kalakaua Avenue #208	Honolulu	HI	United States of America
306	www.babson.edu	Babson College	7812351200	Babson Park	Wellesley	MA	United States of America
307	www.bacone.edu	Bacone College	9186834581	2299 Old Bacone Rd.	Muskogee	OK	United States of America
308	www.bainbridge.edu	Bainbridge State College	2292482500	2500 E Shotwell St	Bainbridge	GA	United States of America
309	www.baker.edu	Baker College	8107664000	1050 West Bristol Road	Flint	MI	United States of America
310	www.bakersfieldcollege.edu	Bakersfield College	6613954011	1801 Panorama Dr	Bakersfield	CA	United States of America
311	www.bakeru.edu	Baker University	7855946451	618 Eighth Street	Baldwin City	KS	United States of America
312	www.bankstreet.edu	Bank Street College of Education	2128754400	610 W 112 St	New York	NY	United States of America
313	www.baptistcollege.edu	The Baptist College of Florida	8502633261	5400 College Dr	Graceville	FL	United States of America
314	www.baptistseminary.edu	Virginia Beach Theological Seminary	7574793406	2221 Centerville Turnpike	Virginia Beach	VA	United States of America
315	www.barclaycollege.edu	Barclay College	6208625252	607 N Kingman	Haviland	KS	United States of America
316	www.bard.edu	Bard College	8457586822	30 Campus Road	Annandale-On-Hudson	NY	United States of America
317	www.barnard.edu	Barnard College	2128545262	3009 Broadway	New York	NY	United States of America
318	www.barnesjewishcollege.edu	Goldfarb School of Nursing at Barnes-Jewish College	3144547055	306 S Kingshighway Blvd	St. Louis	MO	United States of America
319	www.barrett.edu	Barrett and Company School of Hair Design	8598859136	973 Kimberly Square	Nicholasville	KY	United States of America
320	www.barry.edu	Barry University	8007566000	11300 NE 2nd Ave	Miami Shores	FL	United States of America
321	www.barstow.edu	Barstow Community College	7602522411	2700 Barstow Road	Barstow	CA	United States of America
322	www.barton.edu	Barton College	2523996300	200 Atlantic Christian College Drive	Wilson	NC	United States of America
323	www.bartonccc.edu	Barton County Community College	6207922701	245 NE 30th Road	Great Bend	KS	United States of America
324	www.baruch.cuny.edu	Baruch College of the City University of New York	6463123310	One Bernard Baruch Way	New York	NY	United States of America
325	www.bastyr.edu	Bastyr University	4258231300	14500 Juanita Drive NE	Kenmore	WA	United States of America
326	www.bates.ctc.edu	Bates Technical College	2536807000	1101 S Yakima Ave	Tacoma	WA	United States of America
327	www.baycollege.edu	Bay de Noc Community College	9067865802	2001 N Lincoln Road	Escanaba	MI	United States of America
328	www.baylor.edu	Baylor University	2547101011	500 Speight Ave.	Waco	TX	United States of America
329	www.baypath.edu	Bay Path College	4135651000	588 Longmeadow Street	Longmeadow	MA	United States of America
330	www.baystate.edu	Bay State College - Boston	6172368000	122 Commonwealth Avenue	Boston	MA	United States of America
331	www.bc3.edu	Butler County Community College	7242878711	College Drive Oak Hills	Butler	PA	United States of America
332	www.bcc.cuny.edu	Bronx Community College of the City University of New York	7182845100	2155 University Avenue	Bronx	NY	United States of America
333	www.bcc.edu	Burlington County College	6098949311	601 Pemberton Browns Mills Road	Pemberton	NJ	United States of America
334	www.bccc.edu	Baltimore City Community College	4104628000	2901 Liberty Hts Ave	Baltimore	MD	United States of America
335	www.bchs.edu	Baptist Memorial College of Health Sciences	9015722468	1003 Monroe Ave	Memphis	TN	United States of America
336	www.bcm.edu	Baylor College of Medicine	7137984951	One Baylor Plaza BCM 365	Houston	TX	United States of America
337	www.bcu.edu	Bethesda University	7145171945	730 N. Euclid St	Anaheim	CA	United States of America
338	www.beaconcollege.edu	Beacon College	3527877660	105 E Main St	Leesburg	FL	United States of America
339	www.beaufortcc.edu	Beaufort County Community College	2529406202	5337 Highway 264 East	Washington	NC	United States of America
340	www.beckercollege.edu	Becker College	5087919241	61 Sever St	Worcester	MA	United States of America
341	www.beckfield.edu	Beckfield College	8593719393	16 Spiral Drive	Florence	KY	United States of America
342	www.belhaven.edu	Belhaven University	6019685930	1500 Peachtree St	Jackson	MS	United States of America
343	www.bellarmine.edu	Bellarmine University	5024528000	2001 Newburg Rd	Louisville	KY	United States of America
344	www.bellevuecollege.edu	Bellevue College	4255641000	3000 Landerholm Circle SE	Bellevue	WA	United States of America
345	www.bellincollege.edu	Bellin College	9204333560	725 S Webster Ave	Green Bay	WI	United States of America
346	www.belmont.edu	Belmont University	6154606000	1900 Belmont Blvd	Nashville	TN	United States of America
347	www.belmontabbeycollege.edu	Belmont Abbey College	7048256700	100 Belmont-Mt Holly Road	Belmont	NC	United States of America
348	www.beloit.edu	Beloit College	6083632000	700 College St	Beloit	WI	United States of America
349	www.bemidjistate.edu	Bemidji State University	8004752001	1500 Birchmont Drive NE	Bemidji	MN	United States of America
350	www.ben.edu	Benedictine University	6308296090	5700 College Road	Lisle	IL	United States of America
351	www.benedict.edu	Benedict College	8032564220	1600 Harden Street	Columbia	SC	United States of America
352	www.benedictine.edu	Benedictine College	9133675340	1020 N 2nd St	Atchison	KS	United States of America
353	www.bennett.edu	Bennett College for Women	3362734431	900 E Washington St	Greensboro	NC	United States of America
354	www.bennington.edu	Bennington College	8024425401	One College Drive	Bennington	VT	United States of America
355	www.bentley.edu	Bentley University	7818912000	175 Forest St	Waltham	MA	United States of America
356	www.berea.edu	Berea College	8599853000	101 Chestnut Street	Berea	KY	United States of America
357	www.bergen.edu	Bergen Community College	2014477200	400 Paramus Rd	Paramus	NJ	United States of America
358	www.berkeley.edu	University of California - Berkeley	5106426000	200 California Hall	Berkeley	CA	United States of America
359	www.BerkeleyCollege.edu	Berkeley College	9732785400	44 Rifle Camp Rd	West Paterson	NJ	United States of America
360	www.berklee.edu	Berklee College of Music	6177472222	1140 Boylston St	Boston	MA	United States of America
361	www.berkshirecc.edu	Berkshire Community College	4134994660	1350 West Street	Pittsfield	MA	United States of America
362	www.berry.edu	Berry College	7062325374	2277 Martha Berry Hwy NW	Mount Berry	GA	United States of America
363	www.betatech.edu	Centura College	8435690889	8088 Rivers Ave	North Charleston	SC	United States of America
364	www.bethany.edu	Bethany University	8314383800	800 Bethany Dr	Scotts Valley	CA	United States of America
365	www.bethanylb.edu	Bethany College	7852273311	335 E. Swensson Street	Lindsborg	KS	United States of America
366	www.bethanywv.edu	Bethany College	3048297000	Old Main	Bethany	WV	United States of America
367	www.bethel.edu	Bethel University	6516386400	3900 Bethel Drive	St. Paul	MN	United States of America
368	www.bethelcollege.edu	Bethel College	5742598511	1001 W McKinley Ave	Mishawaka	IN	United States of America
369	www.bethelks.edu	Bethel College	3162832500	300 E 27th St	North Newton	KS	United States of America
370	www.bethelu.edu	Bethel University	7313524000	325 Cherry Avenue	McKenzie	TN	United States of America
371	www.bethune.cookman.edu	Bethune - Cookman University	3864812000	640 Dr Mary McLeod Bethune Blvd	Daytona Beach	FL	United States of America
372	www.bexley.edu	Bexley Hall Seminary	6142313095	583 Sheridan Avenue	Columbus	OH	United States of America
373	www.bfit.edu	Benjamin Franklin Institute of Technology	6174234630	41 Berkeley St	Boston	MA	United States of America
374	www.bgsp.edu	Boston Graduate School of Psychoanalysis Inc	6172773915	1581 Beacon St	Brookline	MA	United States of America
375	www.bgsu.edu	Bowling Green State University	4193722531	1001 East Wooster Street	Bowling Green	OH	United States of America
376	www.bhc.edu	Black Hawk College - Quad-Cities Campus	3097965000	6600 34th Avenue	Moline	IL	United States of America
377	www.bhcc.mass.edu	Bunker Hill Community College	6172282000	250 New Rutherford Ave	Boston	MA	United States of America
378	www.bhsu.edu	Black Hills State University	6056426011	1200 University St	Spearfish	SD	United States of America
379	www.bhu.edu	Baltimore Hebrew University Inc	3015786900	5800 Park Heights Avenue	Baltimore	MD	United States of America
380	www.bible.edu	Washington Bible College and Capital Bible Seminary	3015521400	7852 Walker Drive	Greenbelt	MD	United States of America
381	www.biblical.edu	Biblical Theological Seminary	2153685000	200 N Main St	Hatfield	PA	United States of America
382	www.bigbend.edu	Big Bend Community College	5097625351	7662 Chanute Street	Moses Lake	WA	United States of America
383	www.bigsandy.kctcs.edu	Big Sandy Community and Technical College	6068863863	One Bert Combs Dr	Prestonsburg	KY	United States of America
384	www.binghamton.edu	SUNY at Binghamton	6077772000	Vestal Pky E	Binghamton	NY	United States of America
385	www.biola.edu	Biola University	5629036000	13800 Biola Ave	La Mirada	CA	United States of America
386	www.biop.edu	Laurel Technical Institute - Sharon	7249830700	200 Sterling Avenue	Sharon	PA	United States of America
387	www.birthingway.edu	Birthingway College of Midwifery	5037603131	12113 SE Foster Rd	Portland	OR	United States of America
388	www.birtraining.edu	BIR Training Center - West Belmont	7738660111	6240 West Belmont	Chicago	IL	United States of America
389	www.bishop.edu	Bishop State Community College	2514057130	351 North Broad Street	Mobile	AL	United States of America
390	www.bismarckstate.edu	Bismarck State College	7012245400	P.O. Box 5587	Bismarck	ND	United States of America
391	www.bju.edu	Bob Jones University	8642425100	1700 Wade Hampton Boulevard	Greenville	SC	United States of America
392	www.blackburn.edu	Blackburn College	2178543231	700 College Ave	Carlinville	IL	United States of America
393	www.blackrivertech.edu	Black River Technical College	8702484000	1410 Hwy 304 East	Pocahontas	AR	United States of America
394	www.blackstone.edu	Blackstone Career Institute	8008269228	1011 Brookside Road Suite 300	Allentown	PA	United States of America
395	www.blc.edu	Bethany Lutheran College	5073447000	700 Luther Dr	Mankato	MN	United States of America
396	www.blessedjohnxxiii.edu	Blessed John XXIII National Seminary	7818995500	558 South Ave	Weston	MA	United States of America
397	www.blinn.edu	Blinn College	9798304000	902 College Ave	Brenham	TX	United States of America
398	www.bloomfield.edu	Bloomfield College	9737489000	467 Franklin St	Bloomfield	NJ	United States of America
399	www.bloomu.edu	Bloomsburg University of Pennsylvania	5703894000	400 E Second St	Bloomsburg	PA	United States of America
400	www.bluecc.edu	Blue Mountain Community College	5412761260	2411 NW Carden Ave	Pendleton	OR	United States of America
401	www.bluefield.edu	Bluefield College	2763263682	3000 College Dr	Bluefield	VA	United States of America
402	www.bluefieldstate.edu	Bluefield State College	3043274000	219 Rock St	Bluefield	WV	United States of America
403	www.bluegrass.kctcs.edu	Bluegrass Community and Technical College	8592462400	470 Cooper Drive	Lexington	KY	United States of America
404	www.blueridge.edu	Blue Ridge Community College	8286941700	180 West Campus Drive	Flat Rock	NC	United States of America
405	www.bluffton.edu	Bluffton University	4193583000	1 University Drive	Bluffton	OH	United States of America
406	www.bmats.edu	Baptist Missionary Association Theological Seminary	9035862501	1530 E Pine St	Jacksonville	TX	United States of America
407	www.bmc.edu	Blue Mountain College	6626854771	201 W Main St	Blue Mountain	MS	United States of America
408	www.bmcc.cuny.edu	Borough of Manhattan Community College of the City University of New York	2122208000	199 Chambers St	New York	NY	United States of America
409	www.bmcc.edu	Bay Mills Community College	9062483354	12214 W Lakeshore Dr	Brimley	MI	United States of America
410	www.boisestate.edu	Boise State University	2084261011	1910 University Dr	Boise	ID	United States of America
411	www.boricuacollege.edu	Boricua College	2126941000	3755 Broadway	New York	NY	United States of America
412	www.boscotech.edu	Don Bosco Technical Institute	6269402000	1151 San Gabriel Blvd	Rosemead	CA	United States of America
413	www.boston.edu	Boston Baptist College	6173643510	950 Metropolitan Ave	Boston	MA	United States of America
414	www.bostonconservatory.edu	The Boston Conservatory	6175366340	8 the Fenway	Boston	MA	United States of America
415	www.bowdoin.edu	Bowdoin College	2077253000	5700 College Station - President's Office	Brunswick	ME	United States of America
416	www.bowiestate.edu	Bowie State University	3018604000	14000 Jericho Park Rd	Bowie	MD	United States of America
417	www.bowlinggreen.kctcs.edu	Southcentral Kentucky Community and Technical College	2709011000	1845 Loop Drive	Bowling Green	KY	United States of America
418	www.bpc.edu	Brewton-Parker College	9125832241	201 David-Eliza Fountain Circle	Mount Vernon	GA	United States of America
419	www.bpcc.edu	Bossier Parish Community College	3187469851	6220 East Texas	Bossier City	LA	United States of America
420	www.bradfordschoolcolumbus.edu	Bradford School	6144166200	2469 Stelzer Road	Columbus	OH	United States of America
421	www.BradfordSchoolHouston.edu	Vet Tech Institute of Houston	7136291500	4669 Southwest Fwy Ste 300	Houston	TX	United States of America
422	www.bradley.edu	Bradley University	3096767611	1501 W Bradley Ave	Peoria	IL	United States of America
423	www.brandeis.edu	Brandeis University	7817362000	415 South St	Waltham	MA	United States of America
424	www.brandman.edu	Brandman University	9493419800	16355 Laguna Canyon Road	Irvine	CA	United States of America
425	www.brazosport.edu	Brazosport College	9792303000	500 College Dr	Lake Jackson	TX	United States of America
426	www.brcc.edu	Blue Ridge Community College	5402349261	1 College Lane	Weyers Cave	VA	United States of America
427	www.brenau.edu	Brenau University	7705346299	500 Washington Street SE	Gainesville	GA	United States of America
428	www.brescia.edu	Brescia University	2706853131	717 Frederica St	Owensboro	KY	United States of America
429	www.brevard.edu	Brevard College	8288838292	400 North Broad Street	Brevard	NC	United States of America
430	www.brevardcc.edu	Eastern Florida State College	3216321111	1519 Clearlake Rd	Cocoa	FL	United States of America
431	www.briarcliff.edu	Briar Cliff University	7122795321	3303 Rebecca St	Sioux City	IA	United States of America
432	www.briarcliffe.edu	Briarcliffe College	5169183600	1055 Stewart Ave	Bethpage	NY	United States of America
433	www.bridgemont.edu	Bridgemont Community and Technical College	3044423071	619 2nd Avenue	Montgomery	WV	United States of America
434	www.bridgeport.edu	University of Bridgeport	2035764000	126 Park Avenue	Bridgeport	CT	United States of America
435	www.bridgewater.edu	Bridgewater College	5408288000	402 E College St	Bridgewater	VA	United States of America
436	www.bristolcc.edu	Bristol Community College	5086782811	777 Elsbree St	Fall River	MA	United States of America
602	www.chipola.edu	Chipola College	8505262761	3094 Indian Circle	Marianna	FL	United States of America
437	www.brite.tcu.edu	Brite Divinity School of Texas Christian University	8172577000	2800 S. University Drive	Ft. Worth	TX	United States of America
438	www.brockport.edu	SUNY College at Brockport	7163952211	350 New Campus Dr	Brockport	NY	United States of America
439	www.brookdalecc.edu	Brookdale Community College	7322242345	765 Newman Springs Rd	Lincroft	NJ	United States of America
440	www.brookhavencollege.edu	Brookhaven College	9728604700	3939 Valley View Lane	Farmers Branch	TX	United States of America
441	www.brooklaw.edu	Brooklyn Law School	7186252200	250 Joralemon St	Brooklyn	NY	United States of America
442	www.brooklyn.cuny.edu	Brooklyn College of the City University of New York	7189515000	2900 Bedford Ave	Brooklyn	NY	United States of America
443	www.brookscollege.edu	Brooks College	5625976611	4825 E. Pacific Coast Hwy	Long Beach	CA	United States of America
444	www.brookstone.edu	Brookstone College of Business - Charlotte	7045478600	10125 Berkeley Place Drive	Charlotte	NC	United States of America
445	www.broward.edu	Broward College	9542017400	225 E las Olas Blvd	Fort Lauderdale	FL	United States of America
446	www.brown.edu	Brown University	4018631000	Prospect St	Providence	RI	United States of America
447	www.brunswickcc.edu	Brunswick Community College	9107557300	50 College Road	Supply	NC	United States of America
448	www.bryan.edu	Bryan College	4237752041	721 Bryan Drive	Dayton	TN	United States of America
449	www.bryancollege.edu	Bryan University	2134848850	3580 Wilshire Boulevard Suite 400	Los Angeles	CA	United States of America
450	www.bryant.edu	Bryant University	4012326000	1150 Douglas Pike	Smithfield	RI	United States of America
451	www.bryantstratton.edu	Bryant and Stratton College	7162507500	2350 North Forest Road	Getzville	NY	United States of America
452	www.brynathyn.edu	Bryn Athyn College of the New Church	2675022543	801 Tomlinson Rd	Bryn Athyn	PA	United States of America
453	www.brynmawr.edu	Bryn Mawr College	6105265000	101 N Merion Avenue	Bryn Mawr	PA	United States of America
454	www.bsc.edu	Birmingham Southern College	2052264600	900 Arkadelphia Road	Birmingham	AL	United States of America
455	www.bscc.edu	Bevill State Community College	2056483271	101 State St	Sumiton	AL	United States of America
456	www.bshp.edu	Baptist Health System School of Health Professions	2102979630	8400 Datapoint Drive	San Antonio	TX	United States of America
457	www.btc.ctc.edu	Bellingham Technical College	3607380221	3028 Lindbergh Ave	Bellingham	WA	United States of America
458	www.btc.edu	Belmont Technical College	7406959500	120 Fox Shannon Pl	St. Clairsville	OH	United States of America
459	www.BTS.edu	Bangor Theological Seminary	2079426781	Two College Circle	Bangor	ME	United States of America
460	www.btsr.edu	Baptist Theological Seminary at Richmond	8043558135	3400 Brook Road	Richmond	VA	United States of America
461	www.bu.edu	Boston University	6173532000	One Sherborn St.	Boston	MA	United States of America
462	www.bua.edu	Baptist University of the Americas	2109244338	8019 S. Pan Am Expressway	San Antonio	TX	United States of America
463	www.bucknell.edu	Bucknell University	5705772000	Dent Drive	Lewisburg	PA	United States of America
464	www.bucks.edu	Bucks County Community College	2159688000	275 Swamp Rd	Newtown	PA	United States of America
465	www.buffalo.edu	SUNY at Buffalo	7166452000	501 Capen Hall	Buffalo	NY	United States of America
466	www.buffalostate.edu	SUNY College at Buffalo	7168784000	1300 Elmwood Ave	Buffalo	NY	United States of America
467	www.burlcol.edu	Burlington College	8028629616	95 North Ave	Burlington	VT	United States of America
468	www.butler.edu	Butler University	3179408000	4600 Sunset Ave	Indianapolis	IN	United States of America
469	www.butlercc.edu	Butler County Community College	3163212222	901 S Haverhill Rd	El Dorado	KS	United States of America
470	www.butte.edu	Butte College	5308952511	3536 Butte Campus Drive	Oroville	CA	United States of America
471	www.bvu.edu	Buena Vista University	7127492400	610 W 4th St	Storm Lake	IA	United States of America
472	www.bw.edu	Baldwin-Wallace College	4408262900	275 Eastland Rd	Berea	OH	United States of America
473	www.byu.edu	Brigham Young University	8014224636	Main Campus	Provo	UT	United States of America
474	www.byuh.edu	Brigham Young University - Hawaii	8082933211	55-220 Kulanui Street	Laie	HI	United States of America
475	www.byui.edu	Brigham Young University - Idaho	2084962011	525 S Center	Rexburg	ID	United States of America
476	www.c-tec.edu	Career and Technology Education Centers of Licking County	7403642251	150 Price Rd	Newark	OH	United States of America
477	www.cabarruscollege.edu	Cabarrus College of Health Sciences	7047831555	401 Medical Park Drive	Concord	NC	United States of America
478	www.cabrillo.edu	Cabrillo College	8314796100	6500 Soquel Dr	Aptos	CA	United States of America
479	www.cabrini.edu	Cabrini College	6109028100	610 King of Prussia Rd	Radnor	PA	United States of America
480	www.cacc.edu	Central Alabama Community College	2562346346	1675 Cherokee Road	Alexander City	AL	United States of America
481	www.calarts.edu	California Institute of the Arts	6612551050	24700 W McBean Pky	Valencia	CA	United States of America
482	www.calbaptist.edu	California Baptist University	9516895771	8432 Magnolia Ave	Riverside	CA	United States of America
483	www.calcoast.edu	California Coast University	7145479625	925 North Spurgeon Street	Santa Ana	CA	United States of America
484	www.caldwell.edu	Caldwell College	9736183000	120 Bloomfield Avenue	Caldwell	NJ	United States of America
485	www.calhoun.edu	John C Calhoun State Community College	2563062500	6250 U S Highway 31 N	Tanner	AL	United States of America
486	www.callutheran.edu	California Lutheran University	8054922411	60 W Olsen Rd	Thousand Oaks	CA	United States of America
487	www.calpoly.edu	California Polytechnic State University-San Luis Obispo	8057561111		San Luis Obispo	CA	United States of America
488	www.calsouthern.edu	California Southern University	8004772254	930 Roosevelt	Irvine	CA	United States of America
489	www.calstatela.edu	California State University - Los Angeles	3233433000	5151 State University Dr	Los Angeles	CA	United States of America
490	www.caltech.edu	California Institute of Technology	6263956811	1200 E California Blvd	Pasadena	CA	United States of America
491	www.calu.edu	California University of Pennsylvania	7249384400	250 University Ave	California	PA	United States of America
492	www.calumet.purdue.edu	Purdue University Calumet	2199892400	2200 169th Street	Hammond	IN	United States of America
493	www.calums.edu	California University of Management and Sciences		721 North Euclid Street	Anaheim	CA	United States of America
494	www.calvary.edu	Calvary Bible College and Theological Seminary	8163220110	15800 Calvary Road	Kansas City	MO	United States of America
495	www.calvin.edu	Calvin College	6165266000	3201 Burton Street SE	Grand Rapids	MI	United States of America
496	www.calvinseminary.edu	Calvin Theological Seminary	6169576036	3233 Burton St SE	Grand Rapids	MI	United States of America
497	www.camdencc.edu	Camden County College	8562277200	College Drive	Blackwood	NJ	United States of America
498	www.cameron.edu	Cameron University	5805812225	2800 Gore Blvd	Lawton	OK	United States of America
499	www.campbell.edu	Campbell University	9108931200	PO Box 567	Buies Creek	NC	United States of America
500	www.campbellsville.edu	Campbellsville University	5027895000	1 University Dr	Campbellsville	KY	United States of America
501	www.canisius.edu	Canisius College	7168837000	2001 Main St	Buffalo	NY	United States of America
502	www.canton.edu	SUNY College of Technology at Canton	3153867011	34 Cornell Dr	Canton	NY	United States of America
503	www.canyons.edu	College of the Canyons	6612597800	26455 Rockwell Canyon Rd	Santa Clarita	CA	United States of America
504	www.capecod.mass.edu	Cape Cod Community College	5083622131	2240 Iyanough Rd	West Barnstable	MA	United States of America
505	www.capital.edu	Capital University	6142366011	1 College and Main	Columbus	OH	United States of America
506	www.cappscollege.edu	Fortis College - Mobile	2513441203	3590 Pleasant Valley Road	Mobile	AL	United States of America
507	www.carlalbert.edu	Carl Albert State College	9186471200	1507 S McKenna	Poteau	OK	United States of America
508	www.carleton.edu	Carleton College	5076464000	One North College Street	Northfield	MN	United States of America
509	www.carlow.edu	Carlow University	4125786000	3333 Fifth Ave	Pittsburgh	PA	United States of America
510	www.carolina.edu	Carolina Christian College	3367440900	4209 Indiana Avenue	Winston Salem	NC	United States of America
511	www.carrington.edu	Carrington College California - Sacramento	9163611660	8909 Folsom Blvd	Sacramento	CA	United States of America
512	www.carroll.edu	Carroll College	4064474300	1601 N Benton Ave	Helena	MT	United States of America
513	www.carrollcc.edu	Carroll Community College	4103868000	1601 Washington Rd	Westminster	MD	United States of America
514	www.carrollu.edu	Carroll University	2625471211	100 N East Ave	Waukesha	WI	United States of America
515	www.carteret.edu	Carteret Community College	2522226000	3505 Arendell St	Morehead City	NC	United States of America
516	www.carthage.edu	Carthage College	2625518500	2001 Alford Park Dr	Kenosha	WI	United States of America
517	www.carver.edu	Carver College	4045274520	3870 Cascade Rd	Atlanta	GA	United States of America
518	www.cascadia.edu	Cascadia Community College	4253528000	18345 Campus Way NE	Bothell	WA	United States of America
519	www.case.edu	Case Western Reserve University	2163682000	10900 Euclid Ave	Cleveland	OH	United States of America
520	www.caspercollege.edu	Casper College	3072682110	125 College Dr	Casper	WY	United States of America
521	www.castleton.edu	Castleton State College	8024685611	62 Alumni Dr	Castleton	VT	United States of America
522	www.catawba.edu	Catawba College	4046374111	2300 W Innes St	Salisbury	NC	United States of America
523	www.catherinehinds.edu	Catherine Hinds Institute of Esthetics	7819353344	300 Wildwood Avenue	Woburn	MA	United States of America
524	www.cau.edu	Clark Atlanta University	4048808000	223 James P Brawley Drive	Atlanta	GA	United States of America
525	www.cayuga-cc.edu	Cayuga County Community College	3152551743	197 Franklin St	Auburn	NY	United States of America
526	www.cazenovia.edu	Cazenovia College	3156557000	22 Sullivan St	Cazenovia	NY	United States of America
527	www.cbc.edu	Central Baptist College	5013296872	1501 College Ave	Conway	AR	United States of America
528	www.cbcag.edu	Central Bible College	4178332551	3000 N Grant Ave	Springfield	MO	United States of America
529	www.cbshouston.edu	College of Biblical Studies-Houston	7137855995	7000 Regency Square Blvd.	Houston	TX	United States of America
530	www.cbts.edu	Central Baptist Theological Seminary	9133715313	6601 Monticello Road	Shawnee	KS	United States of America
531	www.cbu.edu	Christian Brothers University	9013213200	650 E Parkway S	Memphis	TN	United States of America
532	www.cca.edu	California College of the Arts	5105943600	5212 Broadway	Oakland	CA	United States of America
533	www.ccac.edu	Community College of Allegheny County	4123232323	800 Allegheny Ave	Pittsburgh	PA	United States of America
534	www.ccaurora.edu	Community College of Aurora	3033604700	16000 E. CentreTech Parkway	Aurora	CO	United States of America
535	www.ccbbc.edu	Clear Creek Baptist Bible College	6063373196	300 Clear Creek Rd	Pineville	KY	United States of America
536	www.ccbc.edu	Community College of Beaver County	7247758561	One Campus Dr	Monaca	PA	United States of America
537	www.ccbcmd.edu	The Community College of Baltimore County	4108691211	800 South Rolling Road	Baltimore	MD	United States of America
538	www.ccc.commnet.edu	Capital Community College	8609065000	950 Main Street	Hartford	CT	United States of America
539	www.cccb.edu	Central Christian College of the Bible	6602633900	911 E Urbandale Dr	Moberly	MO	United States of America
540	www.cccc.edu	Central Carolina Community College	9197755401	1105 Kelly Dr	Sanford	NC	United States of America
541	www.cccneb.edu	Central Community College	3083984222	P.O. Box 4903	Grand Island	NE	United States of America
542	www.cccollege.edu	Community Christian College	9093358863	1849 N. Wabash Avenue	Redlands	CA	United States of America
543	www.cccti.edu	Caldwell Community College and Technical Institute	8287262200	2855 Hickory Blvd.	Hudson	NC	United States of America
544	www.ccctraining.edu	Career Institute of Health andTechnology	5168771225	75 Rushmore Street	Westbury	NY	United States of America
545	www.ccd.edu	Community College of Denver	3035562600	1111 W. Colfax Ave.	Denver	CO	United States of America
546	www.ccga.edu	College of Coastal Georgia	9122647235	One College Drive	Brunswick	GA	United States of America
547	www.cci.edu	Everest College - Alhambra	6269794940	2215 Mission Rd	Alhambra	CA	United States of America
548	www.ccis.edu	Columbia College	5738758700	1001 Rogers Street	Columbia	MO	United States of America
549	www.cciutah.edu	Vista College	8017749900	775 South  2000 East	Clearfield	UT	United States of America
550	www.ccm.edu	County College of Morris	9733285000	214 Center Grove Rd	Randolph	NJ	United States of America
551	www.ccnn.edu	Career College of Northern Nevada	7758562266	1421 Pullman Drive	Sparks	NV	United States of America
552	www.ccp.edu	Community College of Philadelphia	2157518000	1700 Spring Garden St	Philadelphia	PA	United States of America
553	www.ccri.edu	Community College of Rhode Island	4018251000	400 East Ave	Warwick	RI	United States of America
554	www.ccsf.edu	City College of San Francisco	4152393000	50 Phelan Ave	San Francisco	CA	United States of America
555	www.ccsj.edu	Calumet College of St. Joseph	2194737770	2400 New York Ave	Whiting	IN	United States of America
556	www.ccsu.edu	Central Connecticut State University	8608323200	1615 Stanley St	New Britain	CT	United States of America
557	www.cctech.edu	Central Carolina Technical College	8037781961	506 N Guignard Dr	Sumter	SC	United States of America
558	www.ccuniversity.edu	Cincinnati Christian University	5132448100	2700 Glenway Ave	Cincinnati	OH	United States of America
559	www.ccv.vsc.edu	Community College of Vermont	8022413535	103 South Main Street	Waterbury	VT	United States of America
560	www.cdkc.edu	Chief Dull Knife College	4064776215	One College Drive	Lame Deer	MT	United States of America
561	www.cdrewu.edu	Charles R Drew University of Medicine and Science	3235634800	1731 E 120th St	Los Angeles	CA	United States of America
562	www.cdsp.edu	Church Divinity School of the Pacific	5102040700	2451 Ridge Road	Berkeley	CA	United States of America
563	www.cdu.edu	Catholic Distance University	8882544238	120 East Colonial Highway	Hamilton	VA	United States of America
564	www.cecil.edu	Cecil Community College	4102876060	One Seahawk Dr	North East	MD	United States of America
565	www.cedarcrest.edu	Cedar Crest College	6104374471	100 College Drive	Allentown	PA	United States of America
566	www.cedarvalleycollege.edu	Cedar Valley College	9728608258	3030 N Dallas Ave	Lancaster	TX	United States of America
567	www.cedarville.edu	Cedarville University	9377662211	251 N. Main Street	Cedarville	OH	United States of America
568	www.ceds.edu	Carolina Graduate School of Divinity	3368823370	2400 Old Chapman Street	Greensboro	NC	United States of America
569	www.centenary.edu	Centenary College of Louisiana	3188695011	2911 Centenary Boulevard	Shreveport	LA	United States of America
570	www.centenarycollege.edu	Centenary College	9088521400	400 Jefferson St	Hackettstown	NJ	United States of America
571	www.central.edu	Central College	6416289000	812 University	Pella	IA	United States of America
572	www.centralaz.edu	Central Arizona College	5204264444	8470 N Overfield Rd	Coolidge	AZ	United States of America
573	www.centralchristian.edu	Central Christian College of Kansas	6202410723	1200 S Main	McPherson	KS	United States of America
574	www.centralcoastcollege.edu	Central Coast College	8317536660	480 S Main Street	Salinas	CA	United States of America
575	www.centralia.ctc.edu	Centralia College	3607369391	600 W Locust St	Centralia	WA	United States of America
576	www.centralmethodist.edu	Central Methodist University	6602486378	411 Central Methodist Square	Fayette	MO	United States of America
577	www.centralpenn.edu	Central Penn College	8007592727	College Hill & Valley Rds	Summerdale	PA	United States of America
578	www.centralseminary.edu	Central Baptist Theological Seminary of Minneapolis	7634178250	900 Forestview Lane North	Plymouth	MN	United States of America
579	www.centralstate.edu	Central State University	9373766011	1400 Brush Row Rd	Wilberforce	OH	United States of America
580	www.centre.edu	Centre College	8592385200	600 W Walnut St	Danville	KY	United States of America
581	www.century.mnscu.edu	Century College	6517703300	3300 Century Ave. North	White Bear Lake	MN	United States of America
582	www.cerrocoso.edu	Cerro Coso Community College	7603846100	3000 College Hts Blvd	Ridgecrest	CA	United States of America
583	www.ceu.edu	College of Eastern Utah	4356372120	451 E 400 N	Price	UT	United States of America
584	www.cf.edu	College of Central Florida	3528735800	3001 SW College Road	Ocala	FL	United States of America
585	www.cga.edu	United States Coast Guard Academy	8604448444	15 Mohegan Avenue	New London	CT	United States of America
586	www.cgu.edu	Claremont Graduate University	9096218000	150 E Tenth St	Claremont	CA	United States of America
587	www.chamberlain.edu	Chamberlain College of Nursing		3005 Highland Parkway	Downers Grove	IL	United States of America
588	www.chaminade.edu	Chaminade University of Honolulu	8087354711	3140 Waialae Ave	Honolulu	HI	United States of America
589	www.champlain.edu	Champlain College	8026582700	163 S. Willard St	Burlington	VT	United States of America
590	www.chapman.edu	Chapman University	7149976815	One University Dr.	Orange	CA	United States of America
591	www.charlestonlaw.edu	Charleston School of Law	8433772145	81 Mary Street	Charleston	SC	United States of America
592	www.chartercollege.edu	Charter College	9072771000	2221 E Northern Lights Blvd Ste 120	Anchorage	AK	United States of America
593	www.chatfield.edu	Chatfield College	5138753344	20918 State Route 251	St. Martin	OH	United States of America
594	www.chatham.edu	Chatham University	4123651100	Woodland Rd	Pittsburgh	PA	United States of America
595	www.chattahoocheetech.edu	Chattahoochee Technical College	7705284545	980 S Cobb Drive	Marietta	GA	United States of America
596	www.chattanoogastate.edu	Chattanooga State Community College	4236974400	4501 Amnicola Hwy	Chattanooga	TN	United States of America
597	www.chc.edu	Chestnut Hill College	2152487000	9601 Germantown Ave	Philadelphia	PA	United States of America
598	www.chemeketa.edu	Chemeketa Community College	5033995000	4000 Lancaster Dr NE	Salem	OR	United States of America
599	www.chesapeake.edu	Chesapeake College	4108225400	1000 College Circle	Wye Mills	MD	United States of America
600	www.chestercollege.edu	Chester College of New England	6038874401	40 Chester St	Chester	NH	United States of America
601	www.cheyney.edu	Cheyney University of Pennsylvania	6103992000	1837 University Circle	Cheyney	PA	United States of America
603	www.chowan.edu	Chowan University	2523986500	One University Place	Murfreesboro	NC	United States of America
604	www.christendom.edu	Christendom College	5406362900	134 Christendom Drive	Front Royal	VA	United States of America
605	www.christianheritage.edu	San Diego Christian College	6194412200	2100 Greenfield Dr	El Cajon	CA	United States of America
606	www.christianlifecollege.edu	Christian Life College	8472591840	400 E Gregory St	Mount Prospect	IL	United States of America
607	www.chubbinstitute.edu	Anthem Institute - Parsippany	9736304900	959 Rt 46 East	Parsippany	NJ	United States of America
608	www.cia.edu	Cleveland Institute of Art	2164217000	11141 East Blvd	Cleveland	OH	United States of America
609	www.cie-wc.edu	Cleveland Institute of Electronics	8002436446	1776 East 17th Street	CLEVELAND	OH	United States of America
610	www.ciis.edu	California Institute of Integral Studies	4155756100	1453 Mission St 4th Fl	San Francisco	CA	United States of America
611	www.cim.edu	Cleveland Institute of Music	2167915000	11021 East Blvd	Cleveland	OH	United States of America
612	www.cincinnatistate.edu	Cincinnati State Technical and Community College	5135691500	3520 Central Parkway	Cincinnati	OH	United States of America
613	www.cisco.edu	Cisco Junior College	2544425000	101 College Heights	Cisco	TX	United States of America
614	www.citadel.edu	The Citadel	8439535000	171 Moultrie Street	Charleston	SC	United States of America
615	www.citruscollege.edu	Citrus College	6269630323	1000 W Foothill Blvd	Glendora	CA	United States of America
616	www.citycollege.edu	City College - Fort Lauderdale	9544925353	2000 W. Commerical Boulevard	Fort Lauderdale	FL	United States of America
617	www.citycollegeorlando.edu	City College - Altamonte Springs	4078319816	177 Montgomery Road	Altamonte Springs	FL	United States of America
618	www.citytech.cuny.edu	New York City College of Technology of the City University of New York	7182605000	300 Jay St	Brooklyn	NY	United States of America
619	www.cityu.edu	City University of Seattle	2062394500	521 Wall Street Suite 100	Seattle	WA	United States of America
620	www.cityvision.edu	City Vision College	8169602008	712 E 31st Street	Kansas City	MO	United States of America
621	www.ciu.edu	Columbia International University	8037544100	7435 Monticello Rd	Columbia	SC	United States of America
622	www.cks.edu	Christ the King Seminary	7166528900	711 Knox Rd	East Aurora	NY	United States of America
623	www.clackamas.edu	Clackamas Community College	5036576958	19600 South Molalla Ave	Oregon City	OR	United States of America
624	www.claflin.edu	Claflin University	8035355000	400 Magnolia Street	Orangeburg	SC	United States of America
625	www.claremontmckenna.edu	Claremont McKenna College	9096218000	500 E 9th St	Claremont	CA	United States of America
626	www.clarendoncollege.edu	Clarendon College	8068743571	1122 College Drive	Clarendon	TX	United States of America
627	www.clarion.edu	Clarion University of Pennsylvania	8143932000	840 Wood St	Clarion	PA	United States of America
628	www.clark.edu	Clark College	3609922000	1800 E McLoughlin Blvd	Vancouver	WA	United States of America
629	www.clarke.edu	Clarke University	5635886300	1550 Clarke Drive	Dubuque	IA	United States of America
630	www.clarkson.edu	Clarkson University	3152686400		Potsdam	NY	United States of America
631	www.clarksoncollege.edu	Clarkson College	4025523100	101 S 42nd St	Omaha	NE	United States of America
632	www.clarkstate.edu	Clark State Community College	9373286070	570 E Leffel Ln	Springfield	OH	United States of America
633	www.clatsopcc.edu	Clatsop Community College	5033250910	1653 Jerome Ave	Astoria	OR	United States of America
634	www.clayton.edu	Clayton  State University	7709613400	2000 Clayton State Boulevard	Morrow	GA	United States of America
635	www.clc.uc.edu	University of Cincinnati - Clermont College	5137325200	4200 Clermont College Dr	Batavia	OH	United States of America
636	www.clearwater.edu	Clearwater Christian College	7277261153	3400 Gulf to Bay Blvd	Clearwater	FL	United States of America
637	www.cleary.edu	Cleary University	7343324477	3601 Plymouth Rd	Ann Arbor	MI	United States of America
638	www.clemson.edu	Clemson University	8646564636	201 Sikes Hall	Clemson	SC	United States of America
639	www.cleveland.edu	Cleveland University-Kansas City	8165010100	10850 Lowell Avenue	Overland Park	KS	United States of America
640	www.clevelandcommunitycollege.edu	Cleveland Community College	7044844000	137 S Post Rd	Shelby	NC	United States of America
641	www.clevelandstatecc.edu	Cleveland State Community College	4234786204	3535 Adkisson Drive	Cleveland	TN	United States of America
642	www.clinton.edu	Clinton Community College	5185624200	136 Clinton Point Drive	Plattsburgh	NY	United States of America
643	www.clintonjuniorcollege.edu	Clinton College	8033277402	1029 Crawford Rd	Rock Hill	SC	United States of America
644	www.cll.edu	Granite State College	6032283000	8 Old Suncook Road	Concord	NH	United States of America
645	www.cln.edu	YTI Career Institute - Altoona	8149445643	2900 Fairway Dr	Altoona	PA	United States of America
646	www.cloud.edu	Cloud County Community College	7852431435	2221 Campus Dr	Concordia	KS	United States of America
647	www.clovis.edu	Clovis Community College	5057692811	417 Schepps Blvd	Clovis	NM	United States of America
648	www.cmcc.edu	Central Maine Community College	2077555100	1250 Turner St	Auburn	ME	United States of America
649	www.cmccd.edu	Copper Mountain College	7603663791	6162 Rotary Way	Joshua Tree	CA	United States of America
650	www.cmmcson.edu	Central Maine Medical Center College of Nursing and Health Professions	2077952840	70 Middle Street	Lewiston	ME	United States of America
651	www.cmu.edu	Carnegie Mellon University	4122682000	5000 Forbes Ave	Pittsburgh	PA	United States of America
652	www.cn.edu	Carson-Newman University	8654712000	1646 Russell Avenue	Jefferson City	TN	United States of America
653	www.cncc.edu	Colorado Northwestern Community College	9706752261	500 Kennedy Drive	Rangely	CO	United States of America
654	www.cnicollege.edu	CNI College	7144379697	702 Town and Country Road	Orange	CA	United States of America
655	www.cnr.edu	The College of New Rochelle	9146325300	29 Castle Place	New Rochelle	NY	United States of America
656	www.cnu.edu	Christopher Newport University	7575947000	1 University Place	Newport News	VA	United States of America
657	www.coa.edu	College of the Atlantic	2072885015	105 Eden St	Bar Harbor	ME	United States of America
658	www.coahomacc.edu	Coahoma Community College	6626272571	3240 Friars Point Rd	Clarksdale	MS	United States of America
659	www.coastal.edu	Coastal Carolina University	8433473161	108 James P. Blantono Circle	Conway	SC	United States of America
660	www.coastalbend.edu	Coastal Bend College	3613582838	3800 Charco Rd	Beeville	TX	United States of America
661	www.coastalcarolina.edu	Coastal Carolina Community College	9104551221	444 Western Blvd	Jacksonville	NC	United States of America
662	www.coba.edu	COBA Academy	7146335950	102 N. Glassell Street	Orange	CA	United States of America
663	www.cobleskill.edu	SUNY College of Agriculture and Technology at Cobleskill	5182555523		Cobleskill	NY	United States of America
664	www.cocc.edu	Central Oregon Community College	5413837500	2600 NW College Way	Bend	OR	United States of America
665	www.cochise.edu	Cochise College	5203647943	4190 W. Highway 80	Douglas	AZ	United States of America
666	www.coconino.edu	Coconino County Community College	5205271222	2800 S. Lone Tree Rd.	Flagstaff	AZ	United States of America
667	www.cod.edu	College of DuPage	6309422800	425 Fawell Blvd.	Glen Ellyn	IL	United States of America
668	www.coe.edu	Coe College	3193998000	1220 First Ave NE	Cedar Rapids	IA	United States of America
669	www.cofc.edu	College of Charleston	8439535500	66 George Street	Charleston	SC	United States of America
670	www.coffeyville.edu	Coffeyville Community College	6202517700	400 W 11th St	Coffeyville	KS	United States of America
671	www.cofo.edu	College of the Ozarks	4173346411	P.O.Box 17	Point Lookout	MO	United States of America
672	www.cogswell.edu	Cogswell Polytechnical College	4085410100	1175 Bordeaux  Drive	Sunnyvale	CA	United States of America
673	www.coker.edu	Coker College	8433838000	300 E College Ave	Hartsville	SC	United States of America
674	www.colburnschool.edu	The Colburn School	2136214530	200 South Grand Avenue	Los Angeles	CA	United States of America
675	www.colby-sawyer.edu	Colby-Sawyer College	6035263000	541 Main St	New London	NH	United States of America
676	www.colby.edu	Colby College	2078723000	Mayflower Hill Drive	Waterville	ME	United States of America
677	www.colbycc.edu	Colby Community College	7854623984	1255 S Range	Colby	KS	United States of America
678	www.coleman.edu	Coleman University	6194653990	8888 Balboa Ave	San Diego	CA	United States of America
679	www.colgate.edu	Colgate University	3152281000	13 Oak Dr	Hamilton	NY	United States of America
680	www.colin.edu	Copiah-Lincoln Community College	6016438306	1028 J.C. Redd Drive	Wesson	MS	United States of America
681	www.collegeamerica.edu	College America - Flagstaff	9285260763	1800 South Milton Road	Flagstaff	AZ	United States of America
682	www.collegeforcreativestudies.edu	College for Creative Studies	3136647890	201 East Kirby Street	Detroit	MI	United States of America
683	www.collegeofidaho.edu	College of Idaho	2084595011	2112 Cleveland Boulevard	Caldwell	ID	United States of America
684	www.collegeofsanmateo.edu	College of San Mateo	6505746161	1700 W Hillsdale Blvd	San Mateo	CA	United States of America
685	www.collegeofthedesert.edu	College of the Desert	7603468041	43-500 Monterey Ave	Palm Desert	CA	United States of America
686	www.collin.edu	Collin County Community College District	9728815790	4800 Preston Park Blvd.	Plano	TX	United States of America
687	www.colorado.edu	University of Colorado at Boulder	3034921411	17 UCB	Boulder	CO	United States of America
688	www.coloradocollege.edu	Colorado College	7193896000	14 East Cache La Poudre Street	Colorado Springs	CO	United States of America
689	www.coloradomesa.edu	Colorado Mesa University	9702481020	1100 North Avenue	Grand Junction	CO	United States of America
690	www.coloradomtn.edu	Colorado Mountain College	9709458691	802 Grand Avenue	Glenwood Springs	CO	United States of America
691	www.coloradotech.edu	Colorado Technical University	7195980200	4435 N Chestnut Street	Colorado Springs	CO	United States of America
692	www.colostate-pueblo.edu	Colorado State University - Pueblo	7195492100	2200 Bonforte Blvd	Pueblo	CO	United States of America
693	www.colostate.edu	Colorado State University	9704911101	102 Administration Building	Fort Collins	CO	United States of America
694	www.colum.edu	Columbia College Chicago	3126631600	600 South Michigan Avenue	Chicago	IL	United States of America
695	www.columbia.edu	Columbia University in the City of New York	2128541754	2960 Broadway	New York	NY	United States of America
696	www.columbiabasin.edu	Columbia Basin College	5095470511	2600 N 20th Ave	Pasco	WA	United States of America
697	www.columbiacollege.edu	Columbia College Hollywood	8183458414	18618 Oxnard Street	Tarzana	CA	United States of America
698	www.columbiasc.edu	Columbia College	8037863012	1301 Columbia College Drive	Columbia	SC	United States of America
699	www.columbiasouthern.edu	Columbia Southern University	8009778449	21982 University Lane	Orange Beach	AL	United States of America
700	www.columbiastate.edu	Columbia State Community College	9315402722	1665 Hampshire Pike	Columbia	TN	United States of America
701	www.columbusstate.edu	Columbus State University	7065682001	4225 University Ave	Columbus	GA	United States of America
702	www.com.edu	College of the Mainland	4099381211	1200 Amburn Road	Texas City	TX	United States of America
703	www.commonwealth.edu	Commonwealth Institute of Funeral Service	2818730262	415 Barren Springs Dr	Houston	TX	United States of America
704	www.communitybusinessscollege.edu	Community Business College	2095293648	3800 McHenry Ave Suite M	Modesto	CA	United States of America
705	www.communitycarecollege.edu	Community Care College	9186100027	4242 South Sheridan	Tulsa	OK	United States of America
706	www.concorde.edu	Concorde Career College	8187668151	12412 Victory Boulevard	North Hollywood	CA	United States of America
707	www.concordia-ny.edu	Concordia College	9143379300	171 White Plains Rd	Bronxville	NY	United States of America
708	www.concordia.edu	Concordia University at Austin	5124862000	3400 I-35 North	Austin	TX	United States of America
709	www.concordiaselma.edu	Concordia College Alabama	3348745700	1804 Green Street	Selma	AL	United States of America
710	www.connecticutcollege.edu	Connecticut College	8604471911	270 Mohegan Ave	New London	CT	United States of America
711	www.converse.edu	Converse College	8645969051	580 E Main St	Spartanburg	SC	United States of America
712	www.cooley.edu	Thomas M. Cooley Law School	5173715140	300 S Capitol Ave	Lansing	MI	United States of America
713	www.cooper.edu	Cooper Union for the Advancement of Science and Art	2123534000	30 Cooper Square	New York	NY	United States of America
714	www.coppin.edu	Coppin State University	4109513000	2500 West North Avenue	Baltimore	MD	United States of America
715	www.corban.edu	Corban University	5035818600	5000 Deer Park Drive SE	Salem	OR	United States of America
716	www.corcoran.edu	Corcoran College of Art and Design	2026391800	500 17th St NW	Washington	DC	United States of America
717	www.cord.edu	Concordia College	2182994100	901 S. 8th St.	Moorhead	MN	United States of America
718	www.cornell.edu	Cornell University	6072552000	300 Day Hall	Ithaca	NY	United States of America
719	www.cornellcollege.edu	Cornell College	3198954000	600 First St. SW	Mount Vernon	IA	United States of America
720	www.cornerstone.edu	Cornerstone University	6169495300	1001 E Beltline Ave NE	Grand Rapids	MI	United States of America
721	www.corning-cc.edu	Corning Community College	6079629011	1 Academic Dr	Corning	NY	United States of America
722	www.cornish.edu	Cornish College of the Arts	2063231400	1000 Lenora Street	Seattle	WA	United States of America
723	www.cortland.edu	SUNY College at Cortland	6077532011	PO Box 2000	Cortland	NY	United States of America
724	www.cosc.edu	Charter Oak State College	8608323800	55 Paul J Manafort Dr	New Britain	CT	United States of America
725	www.cotc.edu	Central Ohio Technical College	7403661351	1179 University Drive	Newark	OH	United States of America
726	www.cottey.edu	Cottey College	4176678181	1000 W Austin	Nevada	MO	United States of America
727	www.covenant.edu	Covenant College	7068201560	14049 Scenic Highway	Lookout Mountain	GA	United States of America
728	www.covenantseminary.edu	Covenant Theological Seminary	3144344044	12330 Conway Rd.	St. Louis	MO	United States of America
729	www.coxcollege.edu	Cox College	4172693401	1423 N. Jefferson Ave.	Springfield	MO	United States of America
730	www.coyneamerican.edu	Coyne American Institute Inc	7739352520	330 North Green Street	Chicago	IL	United States of America
731	www.cpcc.edu	Central Piedmont Community College	7043302722	1201 Elizabeth Avenue	Charlotte	NC	United States of America
732	www.cptc.edu	Clover Park Technical College	2535895678	4500 Steilacoom Blvd SW	Lakewood	WA	United States of America
733	www.craftonhills.edu	Crafton Hills College	9097942161	11711 Sand Canyon Road	Yucaipa	CA	United States of America
734	www.cravencc.edu	Craven Community College	2526384131	800 College Ct	New Bern	NC	United States of America
735	www.crc.losrios.edu	Cosumnes River College	9166887344	8401 Center Pky	Sacramento	CA	United States of America
736	www.crcds.edu	Colgate Rochester Crozer Divinity School	5852711320	1100 S Goodman St	Rochester	NY	United States of America
737	www.creighton.edu	Creighton University	4022802700	2500 California Plaza	Omaha	NE	United States of America
738	www.crestmontcollege.edu	Salvation Army College for Officer Training at Crestmont		30840 Hawthorne Blvd.	Rancho Palos Verdes	CA	United States of America
739	www.criswell.edu	The Criswell College	2148215433	4010 Gaston Ave.	Dallas	TX	United States of America
740	www.crk.umn.edu	University of Minnesota - Crookston	2182816510	2900 University Ave	Crookston	MN	United States of America
741	www.crossroads.edu	Crossroads Bible College	3173528736	601 N Shortridge Rd	Indianapolis	IN	United States of America
742	www.crossroadscollege.edu	Crossroads College	5072884563	920 Mayowood Rd SW	Rochester	MN	United States of America
743	www.crowder.edu	Crowder College	4174513223	601 Laclede Ave	Neosho	MO	United States of America
744	www.crowleysridgecollege.edu	Crowley's Ridge College	8702366901	100 College Dr	Paragould	AR	United States of America
745	www.crown.edu	Crown College	9524464100	8700 College View Drive	Saint Bonifacius	MN	United States of America
746	www.crowncollege.edu	Crown College	2535313123	8739 S Hosmer	Tacoma	WA	United States of America
747	www.crumpttc.edu	Tennessee College of Applied Technology - Crump	7316323393	3070 Highway 64 West	Crump	TN	United States of America
748	www.csb.edu	Consolidated School of Business	7177649550	1605 Clugston Rd	York	PA	United States of America
749	www.csbsju.edu	College of Saint Benedict	3203635011	37 S College Ave	Saint Joseph	MN	United States of America
750	www.csc.edu	Chadron State College	3084326000	1000 Main St	Chadron	NE	United States of America
751	www.cse.edu	College of Saint Elizabeth	9732904000	2 Convent Rd	Morristown	NJ	United States of America
752	www.csf.edu	Santa Fe University of Art and Design	5054736011	1600 St. Michael's Drive	Santa Fe	NM	United States of America
753	www.cshl.edu	Cold Spring Harbor Laboratory	5163676890	One Bungtown Road	Cold Spring Harbor	NY	United States of America
754	www.csi.cuny.edu	College of Staten Island of the City University of New York	7189822000	2800 Victory Blvd	Staten Island	NY	United States of America
755	www.csi.edu	College of Southern Idaho	2087339554	315 Falls Ave.	Twin Falls	ID	United States of America
756	www.csj.edu	College of St Joseph	8027735900	71 Clement Road	Rutland	VT	United States of America
757	www.csld.edu	Conway School of Landscape Design	4133694044	332 South Deerfield Rd	Conway	MA	United States of America
758	www.csmd.edu	College of Southern Maryland	3019342251	8730 Mitchell Rd	La Plata	MD	United States of America
759	www.csn.edu	College of Southern Nevada	7026514000	6375 West Charleston Boulevard	Las Vegas	NV	United States of America
760	www.csopp.edu	Chicago School of Professional Psychology	3123296600	325 North Wells Street	Chicago	IL	United States of America
761	www.css.edu	College of Saint Scholastica	2187236000	1200 Kenwood Ave.	Duluth	MN	United States of America
762	www.cst.edu	Claremont School of Theology	9094472500	1325 N College Ave	Claremont	CA	United States of America
763	www.cstm.edu	The College of Saints John Fisher and Thomas More	8179238459	3020 Lubbock	Fort Worth	TX	United States of America
764	www.csu.edu	Chicago State University	7739952000	9501 South King Drive	Chicago	IL	United States of America
765	www.csubak.edu	California State University - Bakersfield	6616642011	9001 Stockdale Hwy	Bakersfield	CA	United States of America
766	www.csuchico.edu	California State University - Chico	5308986116	400 West First Street	Chico	CA	United States of America
767	www.csuci.edu	California State University - Channel Islands	8054378400	One University Dr	Camarillo	CA	United States of America
768	www.csudh.edu	California State University - Dominguez Hills	3102433300	1000 E Victoria St	Carson	CA	United States of America
769	www.csueastbay.edu	California State University - East Bay	5108853000	25800 Carlos Bee Blvd	Hayward	CA	United States of America
770	www.csufresno.edu	California State University - Fresno	5592784240	5241 N Maple Ave	Fresno	CA	United States of America
771	www.csulb.edu	California State University - Long Beach	5629854111	1250 Bellflower Blvd	Long Beach	CA	United States of America
772	www.csum.edu	California Maritime Academy	7076541000	200 Maritime Academy Dr	Vallejo	CA	United States of America
773	www.csumb.edu	California State University - Monterey Bay	8315823330	100 Campus Ctr	Seaside	CA	United States of America
774	www.csun.edu	California State University - Northridge	8186771200	18111 Nordhoff St	Northridge	CA	United States of America
775	www.csuniv.edu	Charleston Southern University	8438637000	9200 University Blvd	Charleston	SC	United States of America
776	www.csuohio.edu	Cleveland State University	2166872000	2121 Euclid Avenue	Cleveland	OH	United States of America
777	www.csupomona.edu	California State Polytechnic University - Pomona	9098697659	3801 W Temple Ave	Pomona	CA	United States of America
778	www.csus.edu	California State University - Sacramento	9162786011	6000 J St	Sacramento	CA	United States of America
779	www.csusb.edu	California State University - San Bernardino	9098805000	5500 University Pky	San Bernardino	CA	United States of America
780	www.csusm.edu	California State University - San Marcos	7607504000	333 S Twin Oaks Valley Rd	San Marcos	CA	United States of America
781	www.csustan.edu	California State University - Stanislaus	2096673122	801 W Monte Vista	Turlock	CA	United States of America
782	www.ctcd.edu	Central Texas College	2545267161	6200 West Central Texas Expressway	Killeen	TX	United States of America
783	www.cts.edu	Christian Theological Seminary	3179241331	1000 W 42nd St	Indianapolis	IN	United States of America
784	www.ctschicago.edu	Chicago Theological Seminary	7737525757	1407 E. 60th Street	Chicago	IL	United States of America
785	www.ctsfw.edu	Concordia Theological Seminary	2604522100	6600 N Clinton St	Fort Wayne	IN	United States of America
786	www.ctsnet.edu	Columbia Theological Seminary	4043788821	701 Columbia Drive	Decatur	GA	United States of America
787	www.ctu.edu	Catholic Theological Union	7733248000	5401 South Cornell Avenue	Chicago	IL	United States of America
788	www.cu-portland.edu	Concordia University	5032889371	2811 NE Holman Street	Portland	OR	United States of America
789	www.cuaa.edu	Concordia University	7349957300	4090 Geddes Rd.	Ann Arbor	MI	United States of America
790	www.cuchicago.edu	Concordia University Chicago	7087718300	7400 Augusta	River Forest	IL	United States of America
791	www.cudenver.edu	University of Colorado Denver	3035562400		Denver	CO	United States of America
792	www.cui.edu	Concordia University	9498548002	1530 Concordia West	Irvine	CA	United States of America
793	www.culinary.edu	Culinary Institute of America	8454529600	1946 Campus Drive	Hyde Park	NY	United States of America
794	www.culinaryacademy.edu	Culinary Academy of Long Island	5163644344	125 Michael Drive	Syosset	NY	United States of America
795	www.culver.edu	Culver-Stockton College	5732886000	1 College Hill	Canton	MO	United States of America
796	www.cumberland.edu	Cumberland University	6154442562	One Cumberland Square	Lebanon	TN	United States of America
797	www.curry.edu	Curry College	6173330500	1071 Blue Hill Ave	Milton	MA	United States of America
798	www.curtis.edu	Curtis Institute of Music	2158935252	1726 Locust St	Philadelphia	PA	United States of America
799	www.cuw.edu	Concordia University Wisconsin	2622435700	12800 N. Lake Shore Dr.	Mequon	WI	United States of America
800	www.cv.edu	Chattahoochee Valley Community College	3342914900	2602 College Dr	Phenix City	AL	United States of America
801	www.cva.edu	College of Visual Arts	6512243416	344 Summit Ave.	St. Paul	MN	United States of America
802	www.cvcc.edu	Catawba Valley Community College	8283277000	2550 Hwy 70 SE	Hickory	NC	United States of America
803	www.cvcc.vccs.edu	Central Virginia Community College	4348327600	3506 Wards Rd	Lynchburg	VA	United States of America
804	www.cvtc.edu	Chippewa Valley Technical College	7158336200	620 W Clairemont Ave	Eau Claire	WI	United States of America
805	www.cw.edu	The College of Westchester	9149484442	325 Central Park Ave	White Plains	NY	United States of America
806	www.cwc.edu	Central Wyoming College	3078552000	2660 Peck Avenue	Riverton	WY	United States of America
807	www.cwsl.edu	California Western School of Law	6195257073	225 Cedar St	San Diego	CA	United States of America
808	www.cwu.edu	Central Washington University	5099631111	400 East University Way	Ellensburg	WA	United States of America
809	www.cypresscollege.edu	Cypress College	7144847000	9200 Valley View	Cypress	CA	United States of America
810	www.d.umn.edu	University of Minnesota - Duluth	2187268000	515 Darland Administration Bldg.	Duluth	MN	United States of America
811	www.dacc.edu	Danville Area Community College	2174433222	2000 E. Main St.	Danville	IL	United States of America
812	www.daemen.edu	Daemen College	7168393600	4380 Main St	Amherst	NY	United States of America
813	www.dallas.edu	Dallas Christian College	9722413371	2700 Christian Pkwy	Dallas	TX	United States of America
814	www.dallasinstitute.edu	Dallas Institute of Funeral Service	2143885466	3909 S Buckner Blvd	Dallas	TX	United States of America
815	www.daltonstate.edu	Dalton State College	7062724436	650 College Drive	Dalton	GA	United States of America
816	www.dana.edu	Dana College	4024269000	2848 College Dr	Blair	NE	United States of America
817	www.dartmouth.edu	Dartmouth College	6036461110		Hanover	NH	United States of America
818	www.darton.edu	Darton State College	2294306000	2400 Gillionville Rd	Albany	GA	United States of America
819	www.davenport.edu	Davenport University	6164513511	6191 Kraft Avenue S.E.	Grand Rapids	MI	United States of America
820	www.davidsonccc.edu	Davidson County Community College	3362498186	297 Davidson Community College Rd	Thomasville	NC	United States of America
821	www.daviscollege.edu	Davis College	4194732700	4747 Monroe St	Toledo	OH	United States of America
822	www.davisny.edu	Davis College	6077291581	400 Riverside Drive	Johnson City	NY	United States of America
823	www.daytonastate.edu	Daytona State College	3862543000	1200 W. International Speedway Blvd.	Daytona Beach	FL	United States of America
824	www.dbq.edu	University of Dubuque	5635893000	2000 University Ave	Dubuque	IA	United States of America
825	www.dbu.edu	Dallas Baptist University	2143337100	3000 Mountain Creek Parkway	Dallas	TX	United States of America
826	www.dbumn.edu	Duluth Business University	2187224000	4724 Mike Colalillo Drive	Dultuh	MN	United States of America
827	www.dc.edu	Dominican College of Blauvelt	8453597800	470 Western Hwy	Orangeburg	NY	United States of America
828	www.dc3.edu	Dodge City Community College	6202251321	2501 N 14th Ave	Dodge City	KS	United States of America
829	www.dcad.edu	Delaware College of Art and Design	3026228000	600 N Market St	Wilmington	DE	United States of America
830	www.dcc.edu	Delgado Community College	5044834114	615 City Park Ave	New Orleans	LA	United States of America
831	www.dcc.vccs.edu	Danville Community College	4347972222	1008 S Main St	Danville	VA	United States of America
832	www.dccc.edu	Delaware County Community College	6103595000	901 S Media Line Rd	Media	PA	United States of America
833	www.dci.edu	DCI Career Institute	7247280260	366 Beaver Valley Mall	Monaca	PA	United States of America
834	www.dctc.mnscu.edu	Dakota County Technical College	6514238000	1300  145th Street East	Rosemount	MN	United States of America
835	www.dean.edu	Dean College	5085411900	99 Main Street	Franklin	MA	United States of America
836	www.deanza.edu	De Anza College	4088645678	21250 Stevens Creek Blvd.	Cupertino	CA	United States of America
837	www.defiance.edu	Defiance College	4197844010	701 N. Clinton St.	Defiance	OH	United States of America
838	www.dekalbtech.edu	Georgia Piedmont Technical College	4042979522	495 N Indian Creek Dr	Clarkston	GA	United States of America
839	www.delhi.edu	SUNY College of Technology at Delhi	6077464000	2 Main Street	Delhi	NY	United States of America
840	www.delmar.edu	Del Mar College	3616981255	101 Baldwin Blvd.	Corpus Christi	TX	United States of America
841	www.delta.edu	Delta College	9896869000	1961 Delta Road	University Center	MI	United States of America
842	www.deltacollege.edu	San Joaquin Delta College	2099545051	5151 Pacific Ave	Stockton	CA	United States of America
843	www.deltastate.edu	Delta State University	6628464000	1003 West Sunflower Road	Cleveland	MS	United States of America
844	www.deltatech.edu	Delta School of Business and Technology	3374395765	517 Broad St	Lake Charles	LA	United States of America
845	www.delval.edu	Delaware Valley College	2153451500	700 E Butler Ave	Doylestown	PA	United States of America
846	www.denison.edu	Denison University	7405870810	100 West College Rd	Granville	OH	United States of America
847	www.denmarktech.edu	Denmark Technical College	8037935149	500 Solomon Blatt Blvd	Denmark	SC	United States of America
848	www.denverschoolofnursing.edu	Denver School of Nursing		1401 19th Street	Denver	CO	United States of America
849	www.denverseminary.edu	Denver Seminary	3037612482	6399 S. Santa Fe Drive	Littleton	CO	United States of America
850	www.depaul.edu	DePaul University	3123628000	1 East Jackson Blvd.	Chicago	IL	United States of America
851	www.depauw.edu	DePauw University	7656584800	313 S Locust St	Greencastle	IN	United States of America
852	www.desales.edu	DeSales University	6102821100	2755 Station Avenue	Center Valley	PA	United States of America
853	www.desu.edu	Delaware State University	3028576060	1200 N. Dupont Highway	Dover	DE	United States of America
854	www.devry.edu	DeVry University	6305717700	One Tower Lane	Oakbrook Terrace	IL	United States of America
855	www.dewv.edu	Davis & Elkins College	3046371900	100 Campus Dr	Elkins	WV	United States of America
856	www.dickinson.edu	Dickinson College	7172435121	College and Louther Streets	Carlisle	PA	United States of America
857	www.digipen.edu	DigiPen Institute of Technology	4255580299	5001-150th Ave NE	Redmond	WA	United States of America
858	www.dillard.edu	Dillard University	5042838822	2601 Gentilly Blvd	New Orleans	LA	United States of America
859	www.dist.maricopa.edu	Maricopa Community College System Office	4807318000	2411 W 14th St	Tempe	AZ	United States of America
860	www.dixie.edu	Dixie State College of Utah	4356527500	225 S 700 E	Saint George	UT	United States of America
861	www.dmacc.edu	Des Moines Area Community College	5159646241	2006 S. Ankeny Blvd.	Ankeny	IA	United States of America
862	www.dmu.edu	Des Moines University - Osteopathic Medical Center	5152711400	3200 Grand Ave.	Des Moines	IA	United States of America
863	www.doane.edu	Doane College	4028262161	1014 Boswell Avenue	Crete	NE	United States of America
864	www.dom.edu	Dominican University	7083662490	7900 W Division St	River Forest	IL	United States of America
865	www.dominican.edu	Dominican University of California	4154574440	50 Acacia Ave	San Rafael	CA	United States of America
866	www.dordt.edu	Dordt College	7127226000	498 4th Ave NE	Sioux Center	IA	United States of America
867	www.dowling.edu	Dowling College	6312443000	Idle Hour Blvd	Oakdale	NY	United States of America
868	www.downstate.edu	SUNY Downstate Medical Center		450 Clarkson Avenue	Brooklyn	NY	United States of America
869	www.drake.edu	Drake University	5152712011	2507 University Ave	Des Moines	IA	United States of America
870	www.drakestate.edu	J.F. Drake State Community and Technical College	2565398161	3421 Meridian St North	Huntsville	AL	United States of America
871	www.drew.edu	Drew University	9734083000	36 Madison Ave	Madison	NJ	United States of America
872	www.drexel.edu	Drexel University	2158952000	3141 Chestnut St	Philadelphia	PA	United States of America
873	www.drury.edu	Drury University	4178737879	900 N. Benton Ave.	Springfield	MO	United States of America
874	www.dscc.edu	Dyersburg State Community College	7312863200	1510 Lake Road	Dyersburg	TN	United States of America
875	www.dsl.psu.edu	Dickinson School of Law	7172405000	150 South College St	Carlisle	PA	United States of America
876	www.dslcc.edu	Dabney S Lancaster Community College	5408632815	1000 Dabney Drive	Clifton Forge	VA	United States of America
877	www.dspt.edu	Dominican School of Philosophy and Theology	5108492030	2301 Vine Street	Berkeley	CA	United States of America
878	www.dsu.edu	Dakota State University	6052565111	820 N. Washington Ave.	Madison	SD	United States of America
879	www.dtcc.edu	Delaware Technical and Community College - Terry	3028571000	100 Campus Drive	Dover	DE	United States of America
880	www.dts.edu	Dallas Theological Seminary	2148243094	3909 Swiss Ave	Dallas	TX	United States of America
881	www.du.edu	University of Denver	3038712000	2199 S. University Blvd	Denver	CO	United States of America
882	www.duke.edu	Duke University	9196842813	103 Allen Bldg	Durham	NC	United States of America
883	www.dula.edu	Dongguk University - Los Angeles	2134870110	440 Shatto Pl	Los Angeles	CA	United States of America
884	www.dunlap-stone.edu	Dunlap-Stone University	8004748013	11225 N. 28th Drive Suite B201	Phoenix	AZ	United States of America
885	www.dunwoody.edu	Dunwoody College of Technology	6123745800	818 Dunwoody Blvd	Minneapolis	MN	United States of America
886	www.duq.edu	Duquesne University	4123966000	Administration Bldg 600 Forbes Ave	Pittsburgh	PA	United States of America
887	www.durhamtech.edu	Durham Technical Community College	9196863300	1637 Lawson St	Durham	NC	United States of America
888	www.dwc.edu	Daniel Webster College	6035776000	20 University Dr	Nashua	NH	United States of America
889	www.dwci.edu	Divine Word College	5638763353	102 Jacoby Dr SW	Epworth	IA	United States of America
890	www.dwu.edu	Dakota Wesleyan University	6059952600	1200 W University Ave	Mitchell	SD	United States of America
891	www.dyc.edu	D'Youville College	7168298000	320 Porter Ave	Buffalo	NY	United States of America
892	www.eac.edu	Eastern Arizona College	9284288322	615 N. Stadium Ave.	Thatcher	AZ	United States of America
893	www.earlham.edu	Earlham College	7659831200	801 National Rd West	Richmond	IN	United States of America
894	www.eastcentral.edu	East Central College	6365835193	1964 Prairie Dell Road	Union	MO	United States of America
895	www.eastcentraltech.edu	East Central Technical College	2294682000	667 Perry House Rd	Fitzgerald	GA	United States of America
896	www.eastern.edu	Eastern University	6103415800	1300 Eagle Rd	Saint Davids	PA	United States of America
897	www.Eastern.wvnet.edu	Eastern West Virginia Community and Technical College	3044348000	1929 State Road 55	Moorefield	WV	United States of America
898	www.easternct.edu	Eastern Connecticut State University	8604655000	83 Windham St	Willimantic	CT	United States of America
899	www.eastms.edu	East Mississippi Community College	6624765000	1512 Kemper Street	Scooba	MS	United States of America
900	www.eastwest.edu	East-West University	3129390111	816 S Michigan Ave	Chicago	IL	United States of America
901	www.ebts.edu	Palmer Theological Seminary of Eastern University	6108965000	588 N. Gulph Road	King of Prussia	PA	United States of America
902	www.ec.edu	Emmanuel College	7062457226	181 Spring Street	Franklin Springs	GA	United States of America
903	www.ecc.edu	Erie Community College	7168422770	121 Ellicott St	Buffalo	NY	United States of America
904	www.eccc.edu	East Central Community College	6016352111	275 West Broad Street	Decatur	MS	United States of America
905	www.eckerd.edu	Eckerd College	7278671166	4200 54th Ave S	Saint Petersburg	FL	United States of America
906	www.ecok.edu	East Central University	5803328000	1100 E. 14th Street	Ada	OK	United States of America
907	www.ecollege.edu	Ecclesia College	4792487236	9653 Nations Drive	Springdale	AR	United States of America
908	www.ecpi.edu	ECPI University	7576717171	5555 Greenwich Rd Ste 300	Virginia Beach	VA	United States of America
909	www.ecpitech.edu	ECPI Technical College	8043305533	800 Moorefield Pk Dr	Richmond	VA	United States of America
910	www.ecsu.edu	Elizabeth City State University	2523353400	1704 Weeksville Rd	Elizabeth City	NC	United States of America
911	www.ecu.edu	East Carolina University	2523286131	East 5th Street	Greenville	NC	United States of America
912	www.edcc.edu	Edmonds Community College	4256401459	20000 68th Ave W	Lynnwood	WA	United States of America
913	www.eden.edu	Eden Theological Seminary	3149182620	475 East Lockwood Avenue	St. Louis	MO	United States of America
914	www.edgecombe.edu	Edgecombe Community College	2528235166	2009 W Wilson St	Tarboro	NC	United States of America
915	www.edgewood.edu	Edgewood College	6086634861	1000 Edgewood College Drive	Madison	WI	United States of America
916	www.edinboro.edu	Edinboro University of Pennsylvania	8147322000	219 Meadville Street	Edinboro	PA	United States of America
917	www.edison.edu	Edison State College	2394899300	8099 College Pky SW	Fort Myers	FL	United States of America
918	www.edisonOHIO.edu	Edison State Community College	9377788600	1973 Edison Dr	Piqua	OH	United States of America
919	www.eds.edu	Episcopal Divinity School	6178683450	99 Brattle St	Cambridge	MA	United States of America
920	efc.dcccd.edu	Eastfield College	9728607002	3737 Motley Drive	Mesquite	TX	United States of America
921	www.ega.edu	East Georgia State College	4782892000	131 College Cir	Swainsboro	GA	United States of America
922	www.ehc.edu	Emory and Henry College	2769444121	One Garnand Drive	Emory	VA	United States of America
923	www.ei.edu	Elegance International	3238718318	1622 N. Highland Ave	Hollywood	CA	United States of America
924	www.eicc.edu	Eastern Iowa Community College District	5633363309	306 W River Dr	Davenport	IA	United States of America
925	www.einstein.edu	Albert Einstein Medical Center		5501 Old York Road	Philadelphia	PA	United States of America
926	www.einstein.yu.edu	Albert Einstein College of Medicine of Yeshiva University	7184302000	1300 Morris Park Avenue Bronx	Bronx	NY	United States of America
927	www.eitc.edu	Eastern Idaho Technical College	2085243000	1600 S 25th E	Idaho Falls	ID	United States of America
928	www.eiu.edu	Eastern Illinois University	2175815000	600 Lincoln Avenue	Charleston	IL	United States of America
929	www.eku.edu	Eastern Kentucky University	8596221000	521 Lancaster Ave	Richmond	KY	United States of America
930	www.elac.edu	East Los Angeles College	3232658650	1301 Ave Cesar Chavez	Monterey Park	CA	United States of America
931	www.elcamino.edu	El Camino College	3105323670	16007 Crenshaw Blvd	Torrance	CA	United States of America
932	www.elcentrocollege.edu	El Centro College	2148602037	801 Main	Dallas	TX	United States of America
1211	www.hendrix.edu	Hendrix College	5013296811	1600 Washington Ave	Conway	AR	United States of America
933	www.elearn.byu.edu	Brigham Young  University Independent Study	8009148931	120 Morris Center	Provo	UT	United States of America
934	www.elgin.edu	Elgin Community College	8476971000	1700 Spartan Drive	Elgin	IL	United States of America
935	www.elizabethtown.kctcs.edu	Elizabethtown Community and Technical College	2707692371	600 College Street Rd	Elizabethtown	KY	United States of America
936	www.ellis.edu	John Hancock University	8004055844	One Mid America Plaza Suite 130	Oakbrook Terrace	IL	United States of America
937	www.elmhurst.edu	Elmhurst College	6302794100	190 Prospect Ave	Elmhurst	IL	United States of America
938	www.elmira.edu	Elmira College	6077351800	One Park Place	Elmira	NY	United States of America
939	www.elms.edu	College of Our Lady of the Elms	4135942761	291 Springfield St	Chicopee	MA	United States of America
940	www.elon.edu	Elon University	3362782000	100 Campus Drive	Elon	NC	United States of America
941	www.els.edu	ELS Language Centers		400 Alexander Park	Princeton	NJ	United States of America
942	www.emc.maricopa.edu	Maricopa Community Colleges - Estrella Mountain Community College	6239358000	3000 North Dysart Road	Avondale	AZ	United States of America
943	www.emcc.edu	Eastern Maine Community College	2079744600	354 Hogan Road	Bangor	ME	United States of America
944	www.emerson.edu	Emerson College	6178248500	120 Boylston Street	Boston	MA	United States of America
945	www.emich.edu	Eastern Michigan University	3134871849	202 Welch	Ypsilanti	MI	United States of America
946	www.emmanuel.edu	Emmanuel College	6172779320	400 The Fenway	Boston	MA	United States of America
947	www.emmaus.edu	Emmaus Bible College	5635888000	2570 Asbury Rd	Dubuque	IA	United States of America
948	www.emory.edu	Emory University	4047276123	201 Dowman Drive	Atlanta	GA	United States of America
949	www.empcol.edu	Empire College	7075464000	3035 Cleveland Ave	Santa Rosa	CA	United States of America
950	www.empire.edu	Empire Beauty School - Pottsville	8002233271	396 Pottsville/St. Claire Highway	Pottsville	PA	United States of America
951	www.emporia.edu	Emporia State University	6203411200	1200 Commercial Street	Emporia	KS	United States of America
952	www.emu.edu	Eastern Mennonite University	5404324000	1200 Park Rd	Harrisonburg	VA	United States of America
953	www.enc.edu	Eastern Nazarene College	6177453000	23 E Elm Ave	Quincy	MA	United States of America
954	www.endicott.edu	Endicott College	9789270585	376 Hale St	Beverly	MA	United States of America
955	www.enmu.edu	Eastern New Mexico University	5055622467	1500 S. Ave. K	Portales	NM	United States of America
956	www.eosc.edu	Eastern Oklahoma State College	9184652361	1301 W. Main	Wilburton	OK	United States of America
957	www.eou.edu	Eastern Oregon University	5419623672	One University Boulevard	La Grande	OR	United States of America
958	www.epcc.edu	El Paso Community College	9158312000	919 Hunter Drive	El Paso	TX	United States of America
959	www.epic.edu	EPIC Bible College	9163484689	4330 Auburn Boulevard	Sacramento	CA	United States of America
960	www.erau.edu	Embry-Riddle Aeronautical University - Daytona Beach	8002223728	600 S Clyde Morris Blvd	Daytona Beach	FL	United States of America
961	www.ErieIT.edu	Erie Institute of Technology Inc	8148689900	940 Millcreek Mall	Erie	PA	United States of America
962	www.erikson.edu	Erikson Institute	3127552250	451 North LaSalle Street	Chicago	IL	United States of America
963	www.erskine.edu	Erskine College	8643792131	2 Washington St	Due West	SC	United States of America
964	www.es.vccs.edu	Eastern Shore Community College	7577891789	29300 Lankford Hwy	Melfa	VA	United States of America
965	www.esc.edu	SUNY Empire State College	5185872100	1 Union Ave	Saratoga Springs	NY	United States of America
966	www.escc.edu	Enterprise State Community College	3343472623	600 Plaza Drive	Enterprise	AL	United States of America
967	www.esf.edu	SUNY College of Environmental Science and Forestry	3154706500	One Forestry Dr	Syracuse	NY	United States of America
968	www.esr.edu	Emmanuel Christian Seminary	4239261186	One Walker Dr	Johnson City	TN	United States of America
969	www.essex.edu	Essex County College	9738773000	303 University Ave	Newark	NJ	United States of America
970	www.esu.edu	East Stroudsburg University of Pennsylvania	5704223211	200 Prospect St	East Stroudsburg	PA	United States of America
971	www.etbu.edu	East Texas Baptist University	9039357963	1209 N Grove	Marshall	TX	United States of America
972	www.etown.edu	Elizabethtown College	7173611000	One Alpha Dr	Elizabethtown	PA	United States of America
973	www.etseminary.edu	Ecumenical Theological Seminary	3138315200	2930 Woodward Ave	Detroit	MI	United States of America
974	www.etsu.edu	East Tennessee State University	4234391000	807 University Pky	Johnson City	TN	United States of America
975	www.eucon.edu	EUCON International College	6702343203	P.O Box 500087 CK	Saipan	MP	United States of America
976	www.evangel.edu	Evangel University	4178652811	1111 N Glenstone	Springfield	MO	United States of America
977	www.evangelical.edu	Evangelical Theological Seminary	7178665775	121 S College St	Myerstown	PA	United States of America
978	www.evansville.edu	University of Evansville	8124792468	1800 Lincoln Avenue	Evansville	IN	United States of America
979	www.evc.edu	Evergreen Valley College	4082747900	3095 Yerba Buena Rd	San Jose	CA	United States of America
980	www.everest.edu	Everest Institute - Grand Rapids	6163648464	1750 Woodworth St NE	Grand Rapids	MI	United States of America
981	www.everettcc.edu	Everett Community College	4253889557	2000 Tower Street	Everett	WA	United States of America
982	www.evergreen.edu	The Evergreen State College	3608676000	2700 Evergreen Pkwy NW	Olympia	WA	United States of America
983	www.evms.edu	Eastern Virginia Medical School	7574468422	825 Fairfax Avenue	Norfolk	VA	United States of America
984	www.ewc.edu	Edward Waters College	9044708000	1658 Kings Rd	Jacksonville	FL	United States of America
985	www.ewu.edu	Eastern Washington University	5093596200	526 5th Street	Cheney	WA	United States of America
986	www.excelsior.edu	Excelsior College	5184648500	7 Columbia Cir	Albany	NY	United States of America
987	www.expression.edu	Ex'pression College for Digital Arts		6601 Shellmound St	Emeryville	CA	United States of America
988	www.fairfield.edu	Fairfield University	2032544000	1073 N Benson Rd	Fairfield	CT	United States of America
989	www.fairmontstate.edu	Fairmont State University	3043674000	1201 Locust Ave	Fairmont	WV	United States of America
990	www.faith.edu	Faith Baptist Bible College and Theological Seminary	5159640601	1900 NW 4th St	Ankeny	IA	United States of America
991	www.faithseminary.edu	Faith Evangelical College & Seminary	2537522020	3504 N Pearl St	Tacoma	WA	United States of America
992	www.famu.edu	Florida Agricultural and Mechanical University	8505993000	1668 South Martin Luther King Jr. Boulevard	Tallahassee	FL	United States of America
993	www.farmingdale.edu	SUNY at Farmingdale	5164202000	2350 Broadhollow Road	Farmingdale	NY	United States of America
994	www.fau.edu	Florida Atlantic University	5612973000	777 Glades Rd	Boca Raton	FL	United States of America
995	www.faulkner.edu	Faulkner University	3342725820	5345 Atlanta Hwy	Montgomery	AL	United States of America
996	www.faulknerstate.edu	James H Faulkner State Community College	2515802100	1900 US Hwy 31 S	Bay Minette	AL	United States of America
997	www.faytechcc.edu	Fayetteville Technical Community College	9106788400	2201 Hull Rd	Fayetteville	NC	United States of America
998	www.fbcc.bia.edu	Fort Berthold Community College	7016274738	220 8th Ave. N	New Town	ND	United States of America
999	www.fbcc.edu	Fort Belknap College	4063532607	Hwys 2 & 66	Harlem	MT	United States of America
1000	www.fcc.edu	Florida Christian College	4078478966	1011 Bill Beck Blvd	Kissimmee	FL	United States of America
1001	www.fcim.edu	Florida College of Integrative Medicine	4078888689	7100 Lake Ellenor Drive	Orlando	FL	United States of America
1002	www.fcsl.edu	Florida Coastal School of Law	9046807700	8787 Baypine Road	Jacksonville	FL	United States of America
1003	www.fdtc.edu	Florence-Darlington Technical College	8436618324	2715 W. Lucas Street	Florence	SC	United States of America
1004	www.fdu.edu	Fairleigh Dickinson University	2016922000	1000 River Road	Teaneck	NJ	United States of America
1005	www.fei.edu	Florida Education Institute	3052639990	5818 SW 8th St	Miami	FL	United States of America
1006	www.felician.edu	Felician College	2015596000	262 S Main St	Lodi	NJ	United States of America
1007	www.ferris.edu	Ferris State University	2315912000	1201 S. State Street	Big Rapids	MI	United States of America
1008	www.ferrum.edu	Ferrum College	5403652121	215 Ferrum Mountain Road	Ferrum	VA	United States of America
1009	www.fgcu.edu	Florida Gulf Coast University	2395901000	10501 FGCU Blvd South	Fort Myers	FL	United States of America
1010	www.fhchs.edu	Adventist University of Health Sciences	4073037742	671 Winyah Drive	Orlando	FL	United States of America
1011	www.fhsu.edu	Fort Hays State University	7856284000	600 Park Street	Hays	KS	United States of America
1012	www.fhtc.edu	Flint Hills Technical College	6203434600	3301 W. 18th Ave.	Emporia	KS	United States of America
1013	www.fhu.edu	Freed-Hardeman University	7319896000	158 E Main St	Henderson	TN	United States of America
1014	www.fielding.edu	Fielding Graduate University	8056871099	2112 Santa Barbara St	Santa Barbara	CA	United States of America
1015	www.findlay.edu	The University of Findlay	4194228313	1000 N Main St	Findlay	OH	United States of America
1016	www.finlandia.edu	Finlandia University	9064825300	601 Quincy St	Hancock	MI	United States of America
1017	www.fisher.edu	Fisher College	6172368800	118 Beacon St	Boston	MA	United States of America
1018	www.fisk.edu	Fisk University	6153298500	1000 17th Ave N	Nashville	TN	United States of America
1019	www.fit.edu	Florida Institute of Technology-Melbourne	3216748000	150 West University Boulevard	Melbourne	FL	United States of America
1020	www.fitnyc.edu	Fashion Institute of Technology	2122177999	Seventh Avenue At 27th Street	New York	NY	United States of America
1021	www.fiu.edu	Florida International University	3053482000	11200 SW 8th Street	Miami	FL	United States of America
1022	www.fkcc.edu	Florida Keys Community College	3052969081	5901 College Road	Key West	FL	United States of America
1023	www.flagler.edu	Flagler College	9048296481	74 King Street	Saint Augustine	FL	United States of America
1024	www.flc.losrios.edu	Folsom Lake College	9166086572	10 College Parkway	Folsom	CA	United States of America
1025	www.flcc.edu	Finger Lakes Community College	5853943500	3325 Marvin Sands Drive	Canandaigua	NY	United States of America
1026	www.flet.edu	Universidad FLET		13024 Southwest 120th Street	Miami	FL	United States of America
1027	www.flintrivertech.edu	Flint River Technical College	7066466144	1533 Hwy 19 S	Thomaston	GA	United States of America
1028	www.floridacollege.edu	Florida College	8139885131	119 N Glen Arven Ave	Temple Terrace	FL	United States of America
1029	www.flsouthern.edu	Florida Southern College	8636804111	111 Lake Hollingsworth Drive	Lakeland	FL	United States of America
1030	www.fmarion.edu	Francis Marion University	8436611362	4822 East Palmetto Street	Florence	SC	United States of America
1031	www.fmcc.edu	Fulton-Montgomery Community College	5187624651	2805 State Hwy 67	Johnstown	NY	United States of America
1032	www.fmu.edu	Everest University - Pinellas	7277252688	2471 McMullen Booth Road	Clearwater	FL	United States of America
1033	www.fmuniv.edu	Florida Memorial University	3056263600	15800 NW 42 Ave	Miami Gardens	FL	United States of America
1034	www.fnu.edu	Florida National University	3058213333	4425 West 20 Avenue	Hialeah	FL	United States of America
1035	www.focushope.edu	Focus:  HOPE Machinist Training Institute	3134945500	1200 Oakman Boulevard	Detroit	MI	United States of America
1036	www.fontbonne.edu	Fontbonne University	3148623456	6800 Wydown Blvd	St. Louis	MO	United States of America
1037	www.foothill.edu	Foothill College	6509497777	12345 El Monte Rd	Los Altos Hills	CA	United States of America
1038	www.fordham.edu	Fordham University	7188171000	441 E Fordham Rd	Bronx	NY	United States of America
1039	www.forest.edu	Forest Institute of Professional Psychology	4178233477	2885 W. Battlefield	Springfield	MO	United States of America
1040	www.forrestcollege.edu	Forrest College	8642257653	601 East River Street	Anderson	SC	United States of America
1041	www.forsythtech.edu	Forsyth Technical Community College	3367230371	2100 Silas Creek Pky	Winston Salem	NC	United States of America
1042	www.fortlewis.edu	Fort Lewis College	9702477010	1000 Rim Drive	Durango	CO	United States of America
1043	www.fortscott.edu	Fort Scott Community College	6202232700	2108 S Horton	Fort Scott	KS	United States of America
1044	www.fountainheadcollege.edu	Fountainhead College of Technology	8656889422	3203 Tazewell Pke	Knoxville	TN	United States of America
1045	www.foxcollege.edu	Fox College Inc	7086367700	4201 W 93rd St	Oak Lawn	IL	United States of America
1046	www.fpc.edu	Franklin Pierce University	6038994000	20 College Rd	Rindge	NH	United States of America
1047	www.fpcc.edu	Fort Peck Community College	4067686300	605 Indian Street	Poplar	MT	United States of America
1048	www.fpctx.edu	Frank Phillips College	8062745311	1301 W. Roosevelt St.	Borger	TX	United States of America
1049	www.framingham.edu	Framingham State University	5086201220	100 State St	Framingham	MA	United States of America
1050	www.francis.edu	Saint Francis University	8144723000	PO Box 600	Loretto	PA	United States of America
1051	www.franciscan.edu	Franciscan University of Steubenville	7402833771	1235 University Blvd	Steubenville	OH	United States of America
1052	www.franklin.edu	Franklin University	6147974700	201 S Grant Ave	Columbus	OH	United States of America
1053	www.franklincollege.edu	Franklin College	3177388000	101 Branigin Blvd	Franklin	IN	United States of America
1054	www.frc.edu	Feather River College	5302830202	570 Golden Eagle Ave	Quincy	CA	United States of America
1055	www.frederick.edu	Frederick Community College	3018462400	7932 Opossumtown Pike	Frederick	MD	United States of America
1056	www.fredonia.edu	SUNY at Fredonia	7166733111	280 Central Ave	Fredonia	NY	United States of America
1057	www.fresno.edu	Fresno Pacific University	5594532000	1717 S. Chestnut Ave.	Fresno	CA	United States of America
1058	www.friends.edu	Friends University	3162955000	2100 W. University Ave.	Wichita	KS	United States of America
1059	www.frontrange.edu	Front Range Community College	3034668811	3645 W 112th Ave	Westminster	CO	United States of America
1060	www.frostburg.edu	Frostburg State University	3016874000	101 Braddock Road	Frostburg	MD	United States of America
1061	www.fscj.edu	Florida State College at Jacksonville	9046323000	501 W State St	Jacksonville	FL	United States of America
1062	www.fsu.edu	Florida State University	8506442525	211 Westcott Bldg	Tallahassee	FL	United States of America
1063	www.ftc.edu	Five Towns College	6316562157	305 North Service Road	Dix Hills	NY	United States of America
1064	www.ftcc.edu	L.E. Fletcher Technical Community College	9858573655	310 St. Charles Street	Houma	LA	United States of America
1065	www.fullcoll.edu	Fullerton College	7149927000	321 E Chapman Avenue	Fullerton	CA	United States of America
1066	www.fuller.edu	Fuller Theological Seminary	6265845200	135 N Oakland Ave	Pasadena	CA	United States of America
1067	www.fullerton.edu	California State University - Fullerton	7142782011	800 N State College Blvd	Fullerton	CA	United States of America
1068	www.furman.edu	Furman University	8642942000	3300 Poinsett Highway	Greenville	SC	United States of America
1069	www.fvcc.edu	Flathead Valley Community College	4067563822	777 Grandview Dr	Kalispell	MT	United States of America
1070	www.fvsu.edu	Fort Valley State University	4788256315	1005 State University Dr	Fort Valley	GA	United States of America
1071	www.fvtc.edu	Fox Valley Technical College	9207355600	1825 N Bluemound Dr	Appleton	WI	United States of America
1072	www.fwbbc.edu	Welch College	6158445000	3606 West End Ave	Nashville	TN	United States of America
1073	www.gadsdenstate.edu	Gadsden State Community College	2565498200	1001 George Wallace Dr	Gadsden	AL	United States of America
1074	www.gannon.edu	Gannon University	8148717000	109 W Sixth St	Erie	PA	United States of America
1075	www.gardner-webb.edu	Gardner-Webb University	7044062361	110 South Main Street	Boiling Springs	NC	United States of America
1076	www.garrett.edu	Garrett-Evangelical Theological Seminary	8478663900	2121 Sheridan Rd	Evanston	IL	United States of America
1077	www.garrettcollege.edu	Garrett College	3013873000	687 Mosser Rd	McHenry	MD	United States of America
1078	www.gateway.kctcs.edu	Gateway Community and Technical College	8594414500	1025 Amsterdam Rd	Covington	KY	United States of America
1079	www.gavilan.edu	Gavilan College	4088471400	5055 Santa Teresa Blvd	Gilroy	CA	United States of America
1080	www.gbc.edu	Goldey-Beacom College	3022256265	4701 Limestone Rd	Wilmington	DE	United States of America
1081	www.gbcnv.edu	Great Basin College	7757388493	1500 College Pky	Elko	NV	United States of America
1082	www.gbcol.edu	Grace Bible College	6165382330	1011 Aldon SW	Grand Rapids	MI	United States of America
1083	www.gbs.edu	God's Bible School and College	5137217944	1810 Young Street	Cincinnati	OH	United States of America
1084	www.gc.cuny.edu	The Graduate School and University Center of the City University of New York	2128177000	365 Fifth Ave	New York	NY	United States of America
1085	www.gc.edu	Galveston College	4099441220	4015 Ave Q	Galveston	TX	United States of America
1086	www.gc.maricopa.edu	Maricopa Community Colleges - Glendale Community College	6238453000	6000 W Olive Ave	Glendale	AZ	United States of America
1087	www.gc.peachnet.edu	Gainesville State College	7707183639	3820 Mundy Mill Rd	Oakwood	GA	United States of America
1088	www.gcc.edu	Grove City College	7244582000	100 Campus Dr	Grove City	PA	United States of America
1089	www.gcc.mass.edu	Greenfield Community College	4137751000	One College Dr	Greenfield	MA	United States of America
1090	www.gcccks.edu	Garden City Community College	6202767611	801 Campus Dr	Garden City	KS	United States of America
1091	www.gccnj.edu	Gloucester County College	8564685000	1400 Tanyard Road	Sewell	NJ	United States of America
1092	www.gcs.ambassador.edu	Grace Communion Seminary	6266502306	2011 E. Financial Way	Glendora	CA	United States of America
1093	www.gcsu.edu	Georgia College and State University	4784452770	231 W Hancock Street	Milledgeville	GA	United States of America
1094	www.gcu.edu	Grand Canyon University	6025892500	3300 W Camelback Rd	Phoenix	AZ	United States of America
1095	www.gcuniv.edu	Georgia Christian University	7702790507	6789 Peachtree Industrial Blvd.	Atlanta	GA	United States of America
1096	www.gdn.edu	Gordon State College	7703585000	419 College Dr	Barnesville	GA	United States of America
1097	www.genesee.edu	Genesee Community College	5853430055	One College Rd	Batavia	NY	United States of America
1098	www.geneseo.edu	SUNY College at Geneseo	5852455211	1 College Circle	Geneseo	NY	United States of America
1099	www.geneva.edu	Geneva College	7248465100	3200 College Ave	Beaver Falls	PA	United States of America
1100	www.georgefox.edu	George Fox University	5035388383	414 N Meridian St	Newberg	OR	United States of America
1101	www.georgetown.edu	Georgetown University	2026870100	37th and O St NW	Washington	DC	United States of America
1102	www.georgetowncollege.edu	Georgetown College	5028638000	400 East College Street	Georgetown	KY	United States of America
1103	www.georgian.edu	Georgian Court University	7323642200	900 Lakewood Ave	Lakewood	NJ	United States of America
1104	www.georgiasouthern.edu	Georgia Southern University	9126815611	Hwy 301 S	Statesboro	GA	United States of America
1105	www.germanna.edu	Germanna Community College	5407273000	2130 Germanna Highway	Locust Grove	VA	United States of America
1106	www.ggbts.edu	Golden Gate Baptist Theological Seminary	4153801300	201 Seminary Drive	Mill Valley	CA	United States of America
1107	www.ggc.edu	Georgia Gwinnett College	6784075000	1000 University Center Lane	Lawrenceville	GA	United States of America
1108	www.ggu.edu	Golden Gate University-San Francisco	4154427000	536 Mission Street	San Francisco	CA	United States of America
1109	www.ghc.edu	Grays Harbor College	3605329020	1620 Edward P Smith Dr	Aberdeen	WA	United States of America
1110	www.gia.edu	Gemological Institute of America	7606034000	5345 Armada Dr	Carlsbad	CA	United States of America
1111	www.gial.edu	Graduate Institute of Applied Linguistics	9727087340	7500 West Camp Wisdom Road	Dallas	TX	United States of America
1112	www.glcc.edu	Great Lakes Christian College	5173210242	6211 W Willow Hwy	Lansing	MI	United States of America
1113	www.glendale.edu	Glendale Community College	8182401000	1500 N Verdugo Rd	Glendale	CA	United States of America
1114	www.glenville.edu	Glenville State College	3044627361	200 High Street	Glenville	WV	United States of America
1115	www.glit.edu	Great Lakes Institute of Technology	8148646666	5100 Peach St	Erie	PA	United States of America
1116	www.globaluniversity.edu	Global University		1211 South Glenstone Avenue	Springfield	MO	United States of America
1117	www.globecollege.edu	Globe University	6517305100	8089 Globe Drive	Woodbury	MN	United States of America
1118	www.gmc.edu	Gwynedd Mercy College	2156467300	1325 Sumneytown Pike	Gwynedd Valley	PA	United States of America
1119	www.gmu.edu	George Mason University	7039931000	4400 University Dr	Fairfax	VA	United States of America
1120	www.gntc.edu	Georgia Northwestern Technical College - Floyd County Campus	7062956927	One Maurice Culberson Dr	Rome	GA	United States of America
1121	www.gobbc.edu	Baptist Bible College	4172686060	628 E Kearney	Springfield	MO	United States of America
1122	www.goddard.edu	Goddard College	8024548311	123 Pitkin Road	Plainfield	VT	United States of America
1123	www.gogebic.edu	Gogebic Community College	9069324231	E 4946 Jackson Rd	Ironwood	MI	United States of America
1124	www.golfcollege.edu	Professional Golfers Career College	8008774380	26109 Ynez Road	Temecula	CA	United States of America
1125	www.gonzaga.edu	Gonzaga University	5093284220	E 502 Boone Ave	Spokane	WA	United States of America
1126	www.gordon.edu	Gordon College	9789272300	255 Grapevine Rd	Wenham	MA	United States of America
1127	www.gordonconwell.edu	Gordon-Conwell Theological Seminary	9784687111	130 Essex St	South Hamilton	MA	United States of America
1128	www.goshen.edu	Goshen College	5745357000	1700 S Main St	Goshen	IN	United States of America
1129	www.gotoltc.edu	Lakeshore Technical College	9204584183	1290 North Ave	Cleveland	WI	United States of America
1130	www.goucher.edu	Goucher College	4103376000	1021 Dulaney Valley Road	Baltimore	MD	United States of America
1131	www.govst.edu	Governors State University	7085345000	1 University Parkway	University Park	IL	United States of America
1132	www.gpc.edu	Georgia Perimeter College	4042445090	3251 Panthersville Rd	Decatur	GA	United States of America
1133	www.grace.edu	Grace College and Seminary	5743725100	200 Seminary Dr.	Winona Lake	IN	United States of America
1134	www.graceland.edu	Graceland University	6417845000	1 University Place	Lamoni	IA	United States of America
1135	www.GraceUniversity.edu	Grace University	4024492800	1311 S 9th St	Omaha	NE	United States of America
1136	www.gram.edu	Grambling State University	3182473811	403 Main Street	Grambling	LA	United States of America
1137	www.grantham.edu	Grantham University	8165955759	7200 NW 86th St	Kansas City	MO	United States of America
1138	www.gratz.edu	Gratz College	2156357300	7605 Old York Rd	Melrose Park	PA	United States of America
1139	www.grayson.edu	Grayson College	9034656030	6101 Grayson Drive	Denison	TX	United States of America
1140	www.grcc.edu	Grand Rapids Community College	6162344000	143 Bostwick Ave NE	Grand Rapids	MI	United States of America
1141	www.greenmtn.edu	Green Mountain College	8022878000	One College Cir	Poultney	VT	United States of America
1142	www.greenriver.edu	Green River Community College	2538339111	12401 SE 320th St	Auburn	WA	United States of America
1143	www.greensborocollege.edu	Greensboro College	3362727102	815 W Market St	Greensboro	NC	United States of America
1144	www.greenville.edu	Greenville College	6186642800	315 E. College Ave	Greenville	IL	United States of America
1145	www.griffintech.edu	Griffin Technical College	7702287348	501 Varsity Rd	Griffin	GA	United States of America
1146	www.grinnell.edu	Grinnell College	6412694000	1121 Park Street	Grinnell	IA	United States of America
1147	www.gsu.edu	Georgia State University	4046512000	33 Gilmer St SE	Atlanta	GA	United States of America
1148	www.gsw.edu	Georgia Southwestern State University	2299281279	800 Georgia Southwestern State University Dr.	Americus	GA	United States of America
1149	www.gtc.edu	Gateway Technical College	2625642200	3520 30th Ave	Kenosha	WI	United States of America
1150	www.gtcc.edu	Guilford Technical Community College	3363344822	601 High Point Rd	Jamestown	NC	United States of America
1151	www.guamcc.edu	Guam Community College	6717355500	Sesame Street	Mangilao	GU	United States of America
1152	www.guilford.edu	Guilford College	3363162000	5800 W Friendly Ave	Greensboro	NC	United States of America
1153	www.gulfcoast.edu	Gulf Coast State College	8507691551	5230 W Hwy 98	Panama City	FL	United States of America
1154	www.guptoncollege.edu	John A Gupton College	6153273927	1616 Church St	Nashville	TN	United States of America
1155	www.gutenberg.edu	Gutenberg College	5416835141	1883 University Street	Eugene	OR	United States of America
1156	www.gvltec.edu	Greenville Technical College	8642508111	506 S Pleasantburg Dr	Greenville	SC	United States of America
1157	www.gvsu.edu	Grand Valley State University	6163312020	1 Campus Dr	Allendale	MI	United States of America
1158	gwc.cccd.edu	Golden West College	7148927711	15744 Golden West	Huntington Beach	CA	United States of America
1159	www.gwc.maricopa.edu	Maricopa Community Colleges - Gateway Community College	6023925000	108 N. 40th Street	Phoenix	AZ	United States of America
1160	www.gwctc.commnet.edu	Gateway Community College	2032852000	60 Sargent Dr	New Haven	CT	United States of America
1161	www.gwinnetttech.edu	Gwinnett Technical College	7709627580	5150 Sugarloaf Parkway	Lawrenceville	GA	United States of America
1162	www.hacc.edu	Harrisburg Area Community College - Harrisburg	7177802300	One HACC Drive	Harrisburg	PA	United States of America
1163	www.hadley.edu	Hadley School for the Blind	8003234238	700 Elm Street	Winnetka	IL	United States of America
1164	www.hagerstowncc.edu	Hagerstown Community College	3017902800	11400 Robinwood Dr	Hagerstown	MD	United States of America
1165	www.halifaxcc.edu	Halifax Community College	2525364221	100 College Drive	Weldon	NC	United States of America
1166	www.hallmark.edu	Hallmark Institute of Photography	4138632478	241 Millers Falls Rd	Turners Falls	MA	United States of America
1167	www.hamilton.edu	Hamilton College	3158594011	198 College Hill Rd	Clinton	NY	United States of America
1168	www.hamline.edu	Hamline University	6515232800	1536 Hewitt Avenue	Saint Paul	MN	United States of America
1169	www.hampshire.edu	Hampshire College	4135494600	893 West St	Amherst	MA	United States of America
1170	www.hamptonu.edu	Hampton University	7577275000	100 East Queen Street	Hampton	VA	United States of America
1171	www.hancockcollege.edu	Allan Hancock College	8059226966	800 S College Dr	Santa Maria	CA	United States of America
1172	www.hanover.edu	Hanover College	8128667000	359 E. LaGrange Road	Hanover	IN	United States of America
1173	www.harborcareercollege.edu	Harbor Career College	3239361624	4201 Wilshire Blvd.	Los Angeles	CA	United States of America
1174	www.harcum.edu	Harcum College	6105254100	750 Montgomery Ave	Bryn Mawr	PA	United States of America
1175	www.harding.edu	Harding University	5012794000	915 E. Market Ave.	Searcy	AR	United States of America
1176	www.harford.edu	Harford Community College	4108364000	401 Thomas Run Rd	Bel Air	MD	United States of America
1177	www.harid.edu	Harid Conservatory	5619972677	2285 Potomac Road	Boca Raton	FL	United States of America
1178	www.harlingen.tstc.edu	Texas State Technical College - Harlingen	9563644000	1902 North Loop 499	Harlingen	TX	United States of America
1179	www.harpercollege.edu	William Rainey Harper College	8479256000	1200 W Algonquin Rd	Palatine	IL	United States of America
1180	www.HarrisburgU.edu	Harrisburg University of Science and Technology	7179015152	326 Market Street	Harrisburg	PA	United States of America
1181	www.harrison.edu	Harrison College - Indianapolis	3172645656	550 East Washington Street	Indianapolis	IN	United States of America
1182	www.hartford.edu	University of Hartford	8607684100	200 Bloomfield Ave	West Hartford	CT	United States of America
1183	www.hartnell.edu	Hartnell College	8317556700	156 Homestead Ave	Salinas	CA	United States of America
1184	www.hartsem.edu	Hartford Seminary	8605099500	77 Sherman St	Hartford	CT	United States of America
1185	www.hartwick.edu	Hartwick College	6074314000	One Hartwick Drive	Oneonta	NY	United States of America
1186	www.harvard.edu	Harvard University	6174951000	Massachusetts Hall	Cambridge	MA	United States of America
1187	www.haskell.edu	Haskell Indian Nations University	7857498404	155 Indian Ave	Lawrence	KS	United States of America
1188	www.hastings.edu	Hastings College	4024632402	710 N Turner Ave	Hastings	NE	United States of America
1189	www.haverford.edu	Haverford College	6108961000	370 Lancaster Ave	Haverford	PA	United States of America
1190	www.hawcc.hawaii.edu	Hawaii Community College	8089747611	200 W Kawili St	Hilo	HI	United States of America
1191	www.haywood.edu	Haywood Community College	8286272821	185 Freedlander Drive	Clyde	NC	United States of America
1192	www.hazard.kctcs.edu	Hazard Community and Technical College	6064365721	One Community College Dr.	Hazard	KY	United States of America
1193	www.hbc1.edu	Huntsville Bible College	2565390834	904 Oakwood Ave NW	Huntsville	AL	United States of America
1194	www.hbu.edu	Houston Baptist University	2816493000	7502 Fondren Rd	Houston	TX	United States of America
1195	www.hc.edu	Hillsdale Free Will Baptist College	4059129000	3701 S I-35 Service Road	Moore	OK	United States of America
1196	www.hcc-nd.edu	Holy Cross College	5742398400	54515 State Road 933 North	Notre Dame	IN	United States of America
1197	www.hcc.mass.edu	Holyoke Community College	4135522700	303 Homestead Ave	Holyoke	MA	United States of America
1198	www.hcc.mnscu.edu	Hibbing Community College	2182627200	1515 E. 25th St.	Hibbing	MN	United States of America
1199	www.hccc.edu	Hudson County Community College	2017147100	70 Sip Avenue	Jersey City	NJ	United States of America
1200	www.hccfl.edu	Hillsborough Community College	8132537000	39 Columbia Drive	Tampa	FL	United States of America
1201	www.hccs.edu	Houston Community College System	7137182000	3100 Main Street	Houston	TX	United States of America
1202	www.hchc.edu	Hellenic College	6177313500	50 Goddard Ave	Brookline	MA	United States of America
1203	www.hci.edu	Harrison Career Institute - Deptford	8563842888	1450 Clements Bridge Rd	Deptford	NJ	United States of America
1204	www.hctc.commnet.edu	Housatonic Community College	2033325000	900 Lafayette Blvd	Bridgeport	CT	United States of America
1205	www.hcu.edu	Heritage Christian University	2567666610	3625 Helton Dr	Florence	AL	United States of America
1206	www.healingoasis.edu	Healing Oasis Wellness Center	2628981680	2555 Wisconsin Street	Sturtevant	WI	United States of America
1207	www.heartland.edu	Heartland Community College	3092688000	1500 West Raab Road	Normal	IL	United States of America
1208	www.hebrewcollege.edu	Hebrew College	6175598600	160 Herrick Road	Newton Centre	MA	United States of America
1209	www.heidelberg.edu	Heidelberg University	4194482000	310 E Market St	Tiffin	OH	United States of America
1210	www.helenefuld.edu	Helene Fuld College of Nursing	2124232700	26 East 120th Street	New York	NY	United States of America
1212	www.hennepintech.edu	Hennepin Technical College	9529951300	9000 Brooklyn Blvd	Brooklyn Park	MN	United States of America
1213	www.henrycogswell.edu	Henry Cogswell College	8664114221	3002 Colby Avenue	Everett	WA	United States of America
1214	www.heritage.edu	Heritage University	5098658500	3240 Fort Rd	Toppenish	WA	United States of America
1215	www.herkimer.edu	Herkimer County Community College	3158660300	100 Reservoir Road	Herkimer	NY	United States of America
1216	www.herzing.edu	Herzing University		525 N. 6th Street	Milwaukee	WI	United States of America
1217	www.hesser.edu	Hesser College	6036686660	3 Sundial Ave	Manchester	NH	United States of America
1218	www.hesston.edu	Hesston College	6203274221	301 South Main	Hesston	KS	United States of America
1219	www.hfcc.edu	Henry Ford Community College	3138459615	5101 Evergreen Rd.	Dearborn	MI	United States of America
1220	www.hgst.edu	Houston Graduate School of Theology	7139429505	4300-C West Bellfort	Houston	TX	United States of America
1221	www.hgtc.edu	Horry-Georgetown Technical College	8433473186	2050 Highway 501 East	Conway	SC	United States of America
1222	www.highland.edu	Highland Community College	8152356121	2998 W Pearl City Rd	Freeport	IL	United States of America
1223	www.highlandcc.edu	Highland Community College	7854426000	606 W Main	Highland	KS	United States of America
1224	www.highline.edu	Highline Community College	2068783710	2400 S 240th St	Des Moines	WA	United States of America
1225	www.highpoint.edu	High Point University	3368419000	833 Montlieu Ave	High Point	NC	United States of America
1226	www.hilbert.edu	Hilbert College	7166497900	5200 S Park Ave	Hamburg	NY	United States of America
1227	www.hillcollege.edu	Hill College	2545822555	112 Lamar	Hillsboro	TX	United States of America
1228	www.hilo.hawaii.edu	University of Hawaii at Hilo	8089747311	200 W Kawili St	Hilo	HI	United States of America
1229	www.hindscc.edu	Hinds Community College	6018575261	501 E Main St	Raymond	MS	United States of America
1230	www.hiu.edu	Hope International University	7148793901	2500 E Nutwood Ave	Fullerton	CA	United States of America
1231	www.hiwassee.edu	Hiwassee College	4234422001	225 Hiwassee College Drive	Madisonville	TN	United States of America
1232	www.hlg.edu	Hannibal-LaGrange University	5732213675	2800 Palmyra Rd	Hannibal	MO	United States of America
1233	www.hmc.edu	Harvey Mudd College	9096218000	301 Platt Blvd.	Claremont	CA	United States of America
1234	www.hmu.edu	Harrison Middleton University	8772486724	1105 East Broadway	Tempe	AZ	United States of America
1235	www.hnu.edu	Holy Names University	5104361000	3500 Mountain Blvd	Oakland	CA	United States of America
1236	www.hocking.edu	Hocking College	7407533591	3301 Hocking Pky	Nelsonville	OH	United States of America
1237	www.hodges.edu	Hodges University	2395131122	2655 Northbrooke Drive	Naples	FL	United States of America
1238	www.hofstra.edu	Hofstra University	5164636600	100 Hofstra University	Hempstead	NY	United States of America
1239	www.hollins.edu	Hollins University	5403626000	7916 Williamson Rd NW	Roanoke	VA	United States of America
1240	www.holmescc.edu	Holmes Community College	6624722312	#1 Hill St	Goodman	MS	United States of America
1241	www.holyapostles.edu	Holy Apostles College and Seminary	8606323010	33 Prospect Hill Rd	Cromwell	CT	United States of America
1242	www.holycross.edu	College of the Holy Cross	5087932011	One College Street	Worcester	MA	United States of America
1243	www.holyfamily.edu	Holy Family University	2156377700	9801 Frankford Avenue	Philadelphia	PA	United States of America
1244	www.honolulu.hawaii.edu	Honolulu Community College	8088459211	874 Dillingham Blvd	Honolulu	HI	United States of America
1245	www.hood.edu	Hood College	3016633131	401 Rosemont Ave	Frederick	MD	United States of America
1246	www.hoodseminary.edu	Hood Theological Seminary	7046367611	1810 Lutheran Synod Drive	Salisbury	NC	United States of America
1247	www.hope.edu	Hope College	6163957000	141 E 12th St	Holland	MI	United States of America
1248	www.hopkinsville.kctcs.edu	Hopkinsville Community College	2708863921	720 North Dr	Hopkinsville	KY	United States of America
1249	www.hostos.cuny.edu	Hostos Community College of the City University of New York	7185184444	500 Grand Concourse	Bronx	NY	United States of America
1250	www.houghton.edu	Houghton College	5855679200	1 Willard Ave	Houghton	NY	United States of America
1251	www.houseoftutors.edu	House of Tutors Learning Centers USA		2400 Pearl Street	Austin	TX	United States of America
1252	www.howard.edu	Howard University	2028066100	2400 Sixth St NW	Washington	DC	United States of America
1253	www.howardcc.edu	Howard Community College	4107724800	10901 Little Patuxent Pkwy	Columbia	MD	United States of America
1254	www.howardcollege.edu	Howard College	4322645000	1001 Birdwell Lane	Big Spring	TX	United States of America
1255	www.hpu.edu	Hawaii Pacific University	8085440200	1164 Bishop St.	Honolulu	HI	United States of America
1256	www.hputx.edu	Howard Payne University	3256462502	1000 Fisk Ave	Brownwood	TX	United States of America
1257	www.hsbc.edu	Hobe Sound Bible College	7725465534	11298 SE Gomez Avenue	Hobe Sound	FL	United States of America
1258	www.hsc.unt.edu	University of North Texas Health Science Center at Fort Worth	8177352000	3500 Camp Bowie Blvd	Forth Worth	TX	United States of America
1259	www.hssu.edu	Harris-Stowe State University	3143403366	3026 Laclede Ave	St. Louis	MO	United States of America
1260	www.hsu.edu	Henderson State University	8702305000	1100 Henderson St	Arkadelphia	AR	United States of America
1261	www.hsutx.edu	Hardin-Simmons University	3256701000	2200 Hickory	Abilene	TX	United States of America
1262	www.hti.edu	Hawaii Technology Institute	8085272700	629 Pohukaina St	Honolulu	HI	United States of America
1263	www.hts.edu	Holy Trinity Orthodox Seminary	3158580945	Robert Road and Route 167	Jordanville	NY	United States of America
1264	www.htu.edu	Huston-Tillotson University	5125053000	900 Chicon St	Austin	TX	United States of America
1265	www.huc.edu	Hebrew Union College - Jewish Institute of Religion - New York	2126745300	One West 4th Street	New York	NY	United States of America
1266	www.hult.edu	Hult International Business School	6177461990	One Education Street	Cambridge	MA	United States of America
1267	www.humboldt.edu	Humboldt State University	7078263011	1 Harpst Street	Arcata	CA	United States of America
1268	www.humphreys.edu	Humphreys College - Stockton	2094780800	6650 Inglewood Avenue	Stockton	CA	United States of America
1269	www.hunter.cuny.edu	Hunter College of the City University of New York	2127724000	695 Park Ave	New York	NY	United States of America
1270	www.huntingdon.edu	Huntingdon College	3348334222	1500 East Fairview Avenue	Montgomery	AL	United States of America
1271	www.huntington.edu	Huntington University	2603566000	2303 College Ave	Huntington	IN	United States of America
1272	www.huntingtonjuniorcollege.edu	Huntington Junior College	3046977550	900 Fifth Ave	Huntington	WV	United States of America
1273	www.hussianart.edu	Hussian School of Art	2159810900	111 Independence Mall East	Philadelphia	PA	United States of America
1274	www.husson.edu	Husson University	2079417000	One College Circle	Bangor	ME	United States of America
1275	www.hutchcc.edu	Hutchinson Community College	6206653500	1300 N Plum St	Hutchinson	KS	United States of America
1276	www.hvcc.edu	Hudson Valley Community College	5186294822	80 Vandenburgh Ave	Troy	NY	United States of America
1277	www.hws.edu	Hobart & William Smith Colleges	3157813000	337 Pulteney Street	Geneva	NY	United States of America
1278	www.hypnosis.edu	Hypnosis Motivation Institute	8006824434	18607 Ventura Blvd Ste 310	Tarzana	CA	United States of America
1279	www.iaia.edu	Institute of American Indian and Alaska Native Culture and Arts Development	5054242300	83 Avan Nu Po Road	Santa Fe	NM	United States of America
1280	www.iastate.edu	Iowa State University	5152945836	1750 Beardshear Hall	Ames	IA	United States of America
1281	www.iavalley.edu	Iowa Valley Community College - Marshalltown Community College	6417527106	3700 S Center St	Marshalltown	IA	United States of America
1282	www.ibcschools.edu	Harrison College - Muncie	7652888681	411 West  Riggin Road	Muncie	IN	United States of America
1283	www.ic.edu	Illinois College	2172453000	1101 W College Ave	Jacksonville	IL	United States of America
1284	www.icc.edu	Illinois Central College	3096945011	One College Drive	East Peoria	IL	United States of America
1285	www.iccms.edu	Itawamba Community College	6018628000	602 West Hill Street	Fulton	MS	United States of America
1286	www.icseminary.edu	Seminary of the Immaculate Conception	6314230483	440 W Neck Rd	Huntington	NY	United States of America
1287	www.ict-ils.edu	Interactive College of Technology	7702162960	5303 New Peachtree Rd	Chamblee	GA	United States of America
1288	www.idc.edu	Institute of Design and Construction	7188553661	141 Willoughby St	Brooklyn	NY	United States of America
1289	www.idti.edu	Island Drafting and Technical Institute	6316918733	128 Broadway Rte 110	Amityville	NY	United States of America
1290	www.iecc.edu	Illinois Eastern Community Colleges	6183932982	233 E Chestnut St	Olney	IL	United States of America
1291	www.iglobal.edu	IGlobal University		7700 Little River Turnpike Suite #600	Annandale	VA	United States of America
1292	www.iia.edu	International Institute of the Americas	6022426265	6049 N 43rd Ave	Phoenix	AZ	United States of America
1293	www.iit.edu	Illinois Institute of Technology	3125673000	3300 S Federal St	Chicago	IL	United States of America
1294	www.ilia.aii.edu	The Illinois Institute of Art-Schaumburg	8476193450	1000 Plaza Drive	Schaumburg	IL	United States of America
1295	www.iliff.edu	Iliff School of Theology	3037441287	2201 S University Blvd	Denver	CO	United States of America
1296	www.immaculata.edu	Immaculata University	6106474400	1145 King Rd	Immaculata	PA	United States of America
1297	www.impacu.edu	IMPAC University	9416397512	900 West Marion Avenue	Punta Gorda	FL	United States of America
1298	www.imperial.edu	Imperial Valley College	7603528320	380 E. Aten Road	Imperial	CA	United States of America
1299	www.indianatech.edu	Indiana Institute of Technology	2604225561	1600 E Washington Blvd	Fort Wayne	IN	United States of America
1300	www.indwes.edu	Indiana Wesleyan University	7656746901	4201 S Washington St	Marion	IN	United States of America
1301	www.indycc.edu	Independence Community College	6203314100	1057 West College Avenue	Independence	KS	United States of America
1302	www.inste.edu	INSTE Bible College		2302 SW Third Street	Ankeny	IA	United States of America
1303	www.international.edu	Jones International University	8008115663	9697 East Mineral Avenue	Centennial	CO	United States of America
1304	www.inverhills.edu	Inver Hills Community College	6514508500	2500 80th Street East	Inver Grove Heights	MN	United States of America
1305	www.iona.edu	Iona College	9146332000	715 North Ave	New Rochelle	NY	United States of America
1306	www.ipfw.edu	Indiana University-Purdue University Fort Wayne	2604816100	2101 E. Coliseum Blvd.	Fort Wayne	IN	United States of America
1307	www.ipr.edu	Institute of Production and Recording	6123751900	312 Washington Avenue North	Minneapolis	MN	United States of America
1308	www.ipsciences.edu	The Institute for the Psychological Sciences	7034161441	2001 Jefferson Davis Highway	Arlington	VA	United States of America
1309	www.ipst.edu	Institute of Paper Science and Technology	4048945700	500 10th Street NW	Atlanta	GA	United States of America
1310	www.irsc.edu	Indian River State College	7724624722	3209 Virginia Ave	Fort Pierce	FL	United States of America
1311	www.isothermal.edu	Isothermal Community College	8282863636	286 ICC Loop Road	Spindale	NC	United States of America
1312	www.issaonline.edu	International Sports Sciences Association	8008924772	1015 Mark Avenue	Carpinteria	CA	United States of America
1313	www.isu.edu	Idaho State University	2082823620	921 S 7th Ave	Pocatello	ID	United States of America
1314	www.itc.edu	Interdenominational Theological Center	4045277700	700 Martin Luther King Jr Dr	Atlanta	GA	United States of America
1315	www.itech.edu	Immokalee Technical Center	2393779900	508 North 9th Street	Immokalee	FL	United States of America
1316	www.ithaca.edu	Ithaca College	6072743011	953 Danby Rd	Ithaca	NY	United States of America
1317	www.iticollege.edu	ITI Technical College	2257524233	13944 Airline Hwy	Baton Rouge	LA	United States of America
1318	www.itp.edu	Institute of Transpersonal Psychology	6504934430	1069 East Meadow Cr	Palo Alto	CA	United States of America
1319	www.itsla.edu	International Theological Seminary	6264480023	3215-3225 N. Tyler Avenue	El Monte	CA	United States of America
1320	www.itt-tech.edu	ITT Technical Institute - Indianapolis	3178758640	9511 Angola Ct	Indianapolis	IN	United States of America
2695	www.thomas.edu	Thomas College	2078591111	180 W River Rd	Waterville	ME	United States of America
1321	www.itu.edu	International Technological University	4085569010	355 W San Fernando Street	San Jose	CA	United States of America
1322	www.iu.edu	Indiana University Kokomo	7654532000	2300 S. Washington St.	Kokomo	IN	United States of America
1323	www.iue.edu	Indiana University East	7659738200	2325 Chester Blvd.	Richmond	IN	United States of America
1324	www.iup.edu	Indiana University of Pennsylvania	7243572100	1011 South Drive	Indiana	PA	United States of America
1325	www.iupui.edu	Indiana University-Purdue University Indianapolis	3172745555	355 N. Lansing	Indianapolis	IN	United States of America
1326	www.ivc.edu	Irvine Valley College	9494515100	5500 Irvine Center Drive	Irvine	CA	United States of America
1327	www.ivcampus.sdsu.edu	San Diego State University-Imperial Valley Campus	7607685500	720 Heber Ave	Calexico	CA	United States of America
1328	www.ivcc.edu	Illinois Valley Community College	8152242720	815 N Orlando Smith Ave	Oglesby	IL	United States of America
1329	www.ivytech.edu/	Ivy Tech Community College of Indiana	3179214882	50 W. Fall Creek Parkway N. Drive	Indianapolis	IN	United States of America
1330	www.iwc.edu	Iowa Wesleyan College	3193858021	601 N Main Street	Mount Pleasant	IA	United States of America
1331	www.iwp.edu	The Institute of World Politics	2024622101	1521 16th St NW	Washington	DC	United States of America
1332	www.iwu.edu	Illinois Wesleyan University	3095561000	1312 Park Street	Bloomington	IL	United States of America
1333	www.jacksonville-college.edu	Jacksonville College-Main Campus	9035862518	105 B J Albritton Dr	Jacksonville	TX	United States of America
1334	www.jalc.edu	John A Logan College	6189853741	700 Logan College Road	Carterville	IL	United States of America
1335	www.jamessprunt.edu	James Sprunt Community College	9102962400	133 James Sprunt Drive	Kenansville	NC	United States of America
1336	www.jamestownbusinesscollege.edu	Jamestown Business College	7166645100	7 Fairmount Avenue	Jamestown	NY	United States of America
1337	www.jarvis.edu	Jarvis Christian College	9037695700	Hwy 80 E	Hawkins	TX	United States of America
1338	www.jbc.edu	Johnson University	8655734517	7900 Johnson Drive	Knoxville	TN	United States of America
1339	www.jbu.edu	John Brown University	4795249500	2000 W University St	Siloam Springs	AR	United States of America
1340	www.jc.edu	University of Jamestown	7012523467	6000 College Lane	Jamestown	ND	United States of America
1341	www.jcc.edu	Eastern Gateway Community College	7402645591	4000 Sunset Blvd	Steubenville	OH	United States of America
1342	www.jchs.edu	Jefferson College of Health Sciences	5409858483	920 S Jefferson St	Roanoke	VA	United States of America
1343	www.jcjc.edu	Jones County Junior College	6014774000	900 S Court St	Ellisville	MS	United States of America
1344	www.jcsu.edu	Johnson C Smith University	7043781000	100 Beatties Ford Rd	Charlotte	NC	United States of America
1345	www.jcu.edu	John Carroll University	2163971886	20700 North Park Blvd.	University Heights	OH	United States of America
1346	www.jdcc.edu	Jefferson Davis Community College	2518674832	220 Alco Dr	Brewton	AL	United States of America
1347	www.jefferson.edu	Thomas Jefferson University	2159556000	1020 Walnut Street	Philadelphia	PA	United States of America
1348	www.jefferson.kctcs.edu	Jefferson Community and Technical College	5022135333	109 E Broadway	Louisville	KY	United States of America
1349	www.jessup.edu	William Jessup University	9165772200	333 Sunset Blvd.	Rocklin	CA	United States of America
1350	www.jewell.edu	William Jewell College	8167817700	500 College Hill	Liberty	MO	United States of America
1351	www.jfku.edu	John F Kennedy University	9259693300	100 Ellinwood Way	Pleasant Hill	CA	United States of America
1352	www.jhu.edu	Johns Hopkins University	4105168000	3400 N Charles St	Baltimore	MD	United States of America
1353	www.jjay.cuny.edu	John Jay College of Criminal Justice of the City University of New York	2122378000	899 Tenth Ave	New York	NY	United States of America
1354	www.jjc.edu	Joliet Junior College	8157299020	1215 Houbolt Rd	Joliet	IL	United States of America
1355	www.jmu.edu	James Madison University	5405686211	800 South Main Street	Harrisonburg	VA	United States of America
1356	www.johnson.edu	Johnson College	7173426404	3427 N Main Ave	Scranton	PA	United States of America
1357	www.johnstoncc.edu	Johnston Community College	9199343051	245 College Road	Smithfield	NC	United States of America
1358	www.jscc.edu	Jackson State Community College	7314243520	2046 North Parkway	Jackson	TN	United States of America
1359	www.jsu.edu	Jacksonville State University	2567825781	700 Pelham Road North	Jacksonville	AL	United States of America
1360	www.jsums.edu	Jackson State University	6019792121	1440 J R Lynch St	Jackson	MS	United States of America
1361	www.jtc.kctcs.edu	Jefferson Technical College	5022134100	727 W Chestnut St	Louisville	KY	United States of America
1362	www.jtcc.edu	John Tyler Community College	8047964000	13101 Jefferson Davis Hwy	Chester	VA	United States of America
1363	www.jtsa.edu	Jewish Theological Seminary of America	2126788000	3080 Broadway	New York	NY	United States of America
1364	www.ju.edu	Jacksonville University	9042568000	2800 University Blvd N	Jacksonville	FL	United States of America
1365	www.judson.edu	Judson College	3346835100	302 Bibb St	Marion	AL	United States of America
1366	www.JudsonU.edu	Judson University	8476281154	1151 N State St	Elgin	IL	United States of America
1367	www.juilliard.edu	The Juilliard School	2127995000	60 Lincoln Center Plaza	New York	NY	United States of America
1368	www.jungtao.edu	Jung Tao School of Classical Chinese Medicine	8282974181	207 Dale Adams Road	Sugar Grove	NC	United States of America
1369	www.juniata.edu	Juniata College	8146413000	1700 Moore St	Huntingdon	PA	United States of America
1370	www.jwcc.edu	John Wood Community College	2172246500	1301 S 48th Street	Quincy	IL	United States of America
1371	www.jwu.edu	Johnson & Wales University	4015981000	8 Abbott Park Place	Providence	RI	United States of America
1372	www.k-state.edu	Kansas State University	7855325942	110 Anderson Hall	Manhattan	KS	United States of America
1373	www.kankakee.edu	Kankakee Community College	8158028500	100 College Drive	Kankakee	IL	United States of America
1374	www.kaplan.edu	Kaplan College - Riverside	9517817400	4040 Vine Street	Riverside	CA	United States of America
1375	www.kaskaskia.edu	Kaskaskia College	6185453000	27210 College Rd	Centralia	IL	United States of America
1376	www.kauai.hawaii.edu	Kauai Community College	8082458311	3-1901 Kaumualii Hwy	Lihue	HI	United States of America
1377	www.kcai.edu	Kansas City Art Institute	8164724852	4415 Warwick Boulevard	Kansas City	MO	United States of America
1378	www.kcc.edu	Kentucky Christian University	6064743000	100 Academic Pky	Grayson	KY	United States of America
1379	www.kcc.hawaii.edu	Kapiolani Community College	8087349555	4303 Diamond Head Rd	Honolulu	HI	United States of America
1380	www.kckcc.edu	Kansas City Kansas Community College	9133341100	7250 State Ave	Kansas City	KS	United States of America
1381	www.kcumb.edu	Kansas City University of Medicine and Biosciences	8162832000	1750 Independence Ave	Kansas City	MO	United States of America
1382	www.kean.edu	Kean University	9087375326	1000 Morris Ave	Union	NJ	United States of America
1383	www.keene.edu	Keene State College	6033521909	229 Main Street	Keene	NH	United States of America
1384	www.keisercareer.edu	Southeastern College	3058205003	17395 N.W. 59th Avenue	Miami Lakes	FL	United States of America
1385	www.keiseruniversity.edu	Keiser University	9547764456	1500 NW 49th St.	Fort Lauderdale	FL	United States of America
1386	www.kellogg.edu	Kellogg Community College	2699653931	450 North Ave	Battle Creek	MI	United States of America
1387	www.kendall.edu	Kendall College	3127522000	900 N. North Branch St.	Chicago	IL	United States of America
1388	www.kennesaw.edu	Kennesaw State University	7704236000	1000 Chastain Rd    Mail Box  0110	Kennesaw	GA	United States of America
1389	www.kent.edu	Kent State University	3306723000	P.O. Box 5190	Kent	OH	United States of America
1390	www.kenyon.edu	Kenyon College	7404275000	106 College-Park Street	Gambier	OH	United States of America
1391	www.keuka.edu	Keuka College	3152795000	141 Central Avenue	Keuka Park	NY	United States of America
1392	www.keystone.edu	Keystone College	5709458000	One College Green	La Plume	PA	United States of America
1393	www.kgi.edu	Keck Graduate Institute	9096077855	535 Watson Dr	Claremont	CA	United States of America
1394	www.kilgore.edu	Kilgore College	9039848531	1100 Broadway	Kilgore	TX	United States of America
1395	www.king.edu	King University	4239681187	1350 King College Rd	Bristol	TN	United States of America
1396	www.kings.edu	King's College	5702085900	133 N River St	Wilkes Barre	PA	United States of America
1397	www.kingsborough.edu	Kingsborough Community College of the City University of New York	7183685000	2001 Oriental Blvd	Brooklyn	NY	United States of America
1398	www.kirkwood.edu	Kirkwood Community College	3193985411	6301 Kirkwood Blvd SW	Cedar Rapids	IA	United States of America
1399	www.kirtland.edu	Kirtland Community College	9892755000	10775 N Saint Helen Road	Roscommon	MI	United States of America
1400	www.kishwaukeecollege.edu	Kishwaukee College	8158252086	21193 Malta Rd	Malta	IL	United States of America
1401	www.kmbc.edu	Kentucky Mountain Bible College	6066935000	855 Hwy 541	Vancleve	KY	United States of America
1402	www.knox.edu	Knox College	3093417000	2 East South Street	Galesburg	IL	United States of America
1403	www.knoxseminary.edu	Knox Theological Seminary	9547710376	5554 North Federal Highway	Fort Lauderdale	FL	United States of America
1404	www.kona.edu	Kona University	8087915050	75-6099 Kuakini Highway	Kailua-Kona	HI	United States of America
1405	www.ksi.edu	Knowledge Systems Institute	8476793135	3420 Main St	Skokie	IL	United States of America
1406	www.ku.edu	University of Kansas	7858642700	230 Strong Hall 1450 Jayhawk Blvd.	Lawrence	KS	United States of America
1407	www.kutztown.edu	Kutztown University of Pennsylvania	6106834000	15200 Kutztown Rd	Kutztown	PA	United States of America
1408	www.kuyper.edu	Kuyper College	6162223000	3333 East Beltline N.E.	Grand Rapids	MI	United States of America
1409	www.kvcc.edu	Kalamazoo Valley Community College	2694884100	6767 West O Ave	Kalamazoo	MI	United States of America
1410	www.kvcc.me.edu	Kennebec Valley Community College	2074535000	92 Western Ave	Fairfield	ME	United States of America
1411	www.kwc.edu	Kentucky Wesleyan College	2709263111	3000 Frederica St	Owensboro	KY	United States of America
1412	www.kwu.edu	Kansas Wesleyan University	8008741154	100 E. Claflin Ave.	Salina	KS	United States of America
1413	www.kysu.edu	Kentucky State University	5025976000	400 East Main Street	Frankfort	KY	United States of America
1414	www.kzoo.edu	Kalamazoo College	2693377000	1200 Academy St	Kalamazoo	MI	United States of America
1415	www.labette.edu	Labette Community College	6204216700	200 South 14th Street	Parsons	KS	United States of America
1416	www.laboure.edu	Caritas Laboure College	6172968300	2120 Dorchester Ave	Boston	MA	United States of America
1417	www.lacitycollege.edu	Los Angeles City College	3239534000	855 N Vermont Ave	Los Angeles	CA	United States of America
1418	www.lackawanna.edu	Lackawanna College	5709617810	501 Vine St	Scranton	PA	United States of America
1419	www.lacollege.edu	Louisiana College	3184877011	1140 College Dr	Pineville	LA	United States of America
1420	www.ladelta.edu	Louisiana Delta Community College	3183423700	4014 LaSalle Street	Monroe	LA	United States of America
1421	www.lafayette.edu	Lafayette College	6103305000	High St	Easton	PA	United States of America
1422	www.lagcc.cuny.edu	LaGuardia Community College of the City University of New York	7184825000	31-10 Thomson Ave	Long Island City	NY	United States of America
1423	www.lagrange.edu	LaGrange College	7068808000	601 Broad St.	Lagrange	GA	United States of America
1424	www.lagunacollege.edu	Laguna College of Art and Design	9493766000	2222 Laguna Canyon Rd	Laguna Beach	CA	United States of America
1425	www.lahc.edu	Los Angeles Harbor College	3102334000	1111 Figueroa Place	Wilmington	CA	United States of America
1426	www.lakeareatech.edu	Lake Area Technical Institute	6058825284	230 11th St NE	Watertown	SD	United States of America
1427	www.lakecitycc.edu	Florida Gateway College	3867541822	149 SE College Place	Lake City	FL	United States of America
1428	www.lakeforest.edu	Lake Forest College	8472343100	555 N Sheridan Road	Lake Forest	IL	United States of America
1429	www.LakeForestMBA.edu	Lake Forest Graduate School of Management	8472345005	1905 W. Field Court	Lake Forest	IL	United States of America
1430	www.lakelandcc.edu	Lakeland Community College	4405257000	7700 Clocktower Dr	Kirtland	OH	United States of America
1431	www.lakelandcollege.edu	Lake Land College	2172345253	5001 Lake Land Blvd	Mattoon	IL	United States of America
1432	www.lakeside.edu	Lakeside School of Massage Therapy	4143724345	1726 N. First Street	Milwaukee	WI	United States of America
1433	www.lakeviewcol.edu	Lakeview College of Nursing	2174435238	903 N Logan Ave	Danville	IL	United States of America
1434	www.lamar.edu	Lamar University	4098807011	4400 MLK	Beaumont	TX	United States of America
1435	www.lamarcc.edu	Lamar Community College	7193362248	2401 S Main St	Lamar	CO	United States of America
1436	www.lambuth.edu	Lambuth University	7314252500	705 Lambuth Boulevard	Jackson	TN	United States of America
1437	www.lamission.edu	Los Angeles Mission College	8183647600	13356 Eldridge Avenue	Sylmar	CA	United States of America
1438	www.lamusicacademy.edu	Los Angeles Music Academy	6265688850	370 South Fair Oaks Avenue	Pasadena	CA	United States of America
1439	www.lancastergeneralcollege.edu	Lancaster General College of Nursing & Health Sciences	7175444912	410 North Lime Street	Lancaster	PA	United States of America
1440	www.lancasterseminary.edu	Lancaster Theological Seminary	7172908701	555 W James St	Lancaster	PA	United States of America
1441	www.lander.edu	Lander University	8643888000	320 Stanley Avenue	Greenwood	SC	United States of America
1442	www.landingschool.edu	Landing School of Boat Building and Design	2079857976	286 River Rd	Arundel	ME	United States of America
1443	www.landmark.edu	Landmark College	8023874767	River Rd South	Putney	VT	United States of America
1444	www.lanecc.edu	Lane Community College	5414633000	4000 East 30th Avenue	Eugene	OR	United States of America
1445	www.lanecollege.edu	Lane College	7314267500	545 Lane Ave	Jackson	TN	United States of America
1446	www.laniertech.edu	Lanier Technical College	7705316300	2990 Landrum Education Dr	Oakwood	GA	United States of America
1447	www.laroche.edu	La Roche College	4123679300	9000 Babcock Blvd	Pittsburgh	PA	United States of America
1448	www.lasalle.edu	La Salle University	2159511000	1900 W Olney Ave	Philadelphia	PA	United States of America
1449	www.lasc.edu	Los Angeles Southwest College	3232415225	1600 W Imperial Hwy.	Los Angeles	CA	United States of America
1450	www.lasell.edu	Lasell College	6172432000	1844 Commonwealth Ave	Newton	MA	United States of America
1451	www.lasierra.edu	La Sierra University	9517852000	4500 Riverwalk Parkway	Riverside	CA	United States of America
1452	www.lassencollege.edu	Lassen Community College	5302576181	Hwy 139	Susanville	CA	United States of America
1453	www.latech.edu	Louisiana Tech University	3182572000	305 Wisteria	Ruston	LA	United States of America
1454	www.lattc.edu	Los Angeles Trade Technical College	2137637000	400 W Washington Blvd	Los Angeles	CA	United States of America
1455	www.laurelbusiness.edu	Laurel Business Institute	7244394900	11 East Penn St	Uniontown	PA	United States of America
1456	www.laureluniversity.edu	Laurel University	3368892262	2314 N Centennial Street	High Point	NC	United States of America
1457	www.law.cuny.edu	CUNY School of Law at Queens College	7183404200	65-21 Main St	Flushing	NY	United States of America
1458	www.law.msu.edu	Michigan State University College of Law	5174326800	368 Law College Bldg	East Lansing	MI	United States of America
1459	www.law.udc.edu	University of the District of Columbia David A Clarke School of Law	2022747400	4200 Connecticut Ave NW	Washington	DC	United States of America
1460	www.Lawrence.edu	Lawrence University	9208327000	PO Box 599	Appleton	WI	United States of America
1461	www.lawtonschool.edu	Lawton Career Institute - Warren	5867777344	13877 E. Eight Mile Road	Warren	MI	United States of America
1462	www.lbc.edu	Lancaster Bible College	7175697071	901 Eden Road	Lancaster	PA	United States of America
1463	www.lbcc.edu	Long Beach City College	5629384206	4901 E. Carson St.	Long Beach	CA	United States of America
1464	www.lbs.edu	Lutheran Brethren Seminary	2187393375	815 W. Vernon Ave	Fergus Falls	MN	United States of America
1465	www.lc.edu	Lewis and Clark Community College	6184683411	5800 Godfrey Rd	Godfrey	IL	United States of America
1466	www.lcc.ctc.edu	Lower Columbia College	3604422000	1600 Maple	Longview	WA	United States of America
1467	www.lcc.hawaii.edu	Leeward Community College	8084550011	96-045 Ala Ike	Pearl City	HI	United States of America
1468	www.lccc.edu	Lehigh Carbon Community College	6107992121	4525 Education Park Dr	Schnecksville	PA	United States of America
1469	www.lccc.wy.edu	Laramie County Community College	3077785222	1400 E College Dr	Cheyenne	WY	United States of America
1470	www.lccs.edu	Lincoln Christian University	2177323168	100 Campus View Drive	Lincoln	IL	United States of America
1471	www.lclark.edu	Lewis & Clark College	5037687000	0615 S W Palatine Hill Rd	Portland	OR	United States of America
1472	www.lco-college.edu	Lac Courte Oreilles Ojibwa Community College	7156344790	13466 W Trepania Rd	Hayward	WI	United States of America
1473	www.lcsc.edu	Lewis-Clark State College	2087925272	500 8th Ave	Lewiston	ID	United States of America
1474	www.lcu.edu	Lubbock Christian University	8067968800	5601 19th Street	Lubbock	TX	United States of America
1475	www.ldsbc.edu	LDS Business College	8015248100	411 E South Temple	Salt Lake City	UT	United States of America
1476	www.lebanoncollege.edu	Lebanon College	6034482445	15 Hanover Street	Lebanon	NH	United States of America
1477	www.lec.edu	Lake Erie College	4403757000	391 W Washington St	Painesville	OH	United States of America
1478	www.lecom.edu	Lake Erie College of Osteopathic Medicine	8148666641	1858 W Grandview Blvd	Erie	PA	United States of America
1479	www.lee.edu	Lee College	2814275611	511 S Whiting	Baytown	TX	United States of America
1480	www.leeuniversity.edu	Lee University	4236148000	1120 N Ocoee St	Cleveland	TN	United States of America
1481	www.lehigh.edu	Lehigh University	6107583000	27 Memorial Dr W	Bethlehem	PA	United States of America
1482	www.lemoyne.edu	Le Moyne College	3154454100	1419 Salt Springs Rd	Syracuse	NY	United States of America
1483	www.lenoircc.edu	Lenoir Community College	2525276223	231 Highway 58 South	Kinston	NC	United States of America
1484	www.lesley.edu	Lesley University	6178689600	29 Everett St	Cambridge	MA	United States of America
1485	www.letu.edu	LeTourneau University	9032333000	2100 S Mobberly Ave	Longview	TX	United States of America
1486	www.lewiscollege.edu	Lewis College of Business	3138626300	17370 Meyers Rd	Detroit	MI	United States of America
1487	www.lewisu.edu	Lewis University	8158380500	One University Parkway	Romeoville	IL	United States of America
1488	www.lexingtoncollege.edu	Lexington College	3122266294	310 South Peoria	Chicago	IL	United States of America
1489	www.lextheo.edu	Lexington Theological Seminary	8592520361	631 S Limestone	Lexington	KY	United States of America
1490	www.lf.vccs.edu	Lord Fairfax Community College	5408687000	173 Skirmisher Lane	Middletown	VA	United States of America
1491	www.lhup.edu	Lock Haven University of Pennsylvania	5708932011	401 N Fairview St	Lock Haven	PA	United States of America
1492	www.liberty.edu	Liberty University	4345822000	1971 University Blvd	Lynchburg	VA	United States of America
1493	www.life.edu	Life University	7704262600	1269 Barclay Circle	Marietta	GA	United States of America
1494	www.lifepacific.edu	Life Pacific College	9095995433	1100 W. Covina Blvd	San Dimas	CA	United States of America
1495	www.lifewest.edu	Life Chiropractic College-West	5107804500	25001 Industrial Blvd.	Hayward	CA	United States of America
1496	www.limcollege.edu	LIM College	2127521530	12 E 53rd St	New York	NY	United States of America
1497	www.limestone.edu	Limestone College	8644897151	1115 College Drive	Gaffney	SC	United States of America
1498	www.lincoln.edu	Lincoln University of Pennsylvania	6109328300	1570 Baltimore Pike	Lincoln University	PA	United States of America
1499	www.lincolncollege.edu	Lincoln College	2177323155	300 Keokuk St	Lincoln	IL	United States of America
1500	www.LincolnCollegeNE.edu	Lincoln College of New England	8606284751	2279 Mount Vernon Road	Southington	CT	United States of America
1501	www.lincolnuca.edu	Lincoln University	5106288010	401 15th Street	Oakland	CA	United States of America
1502	www.lindenwood.edu	Lindenwood University	6369492000	209 S. Kingshighway	St. Charles	MO	United States of America
1503	www.lindsey.edu	Lindsey Wilson College	2703842126	210 Lindsey Wilson St	Columbia	KY	United States of America
1504	www.lineman.edu	Northwest Lineman College - Oroville Campus	5305347260	2009 Challenger Avenue	Oroville	CA	United States of America
1505	www.linfield.edu	Linfield College	5038832200	900 SE Baker	McMinnville	OR	United States of America
1506	www.linfield.edu	Linfield College-Portland Campus	5034138481	2215 NW Northrup St	Portland	OR	United States of America
1507	www.linnbenton.edu	Linn-Benton Community College	5419174999	6500 Pacific Blvd SW	Albany	OR	United States of America
1508	www.linnstate.edu	Linn State Technical College	5738975000	One Technology Drive	Linn	MO	United States of America
1509	www.lipscomb.edu	Lipscomb University	6152691000	3901 Granny White Pike	Nashville	TN	United States of America
1510	www.lit.edu	Lamar Institute of Technology	4098808321	855 E Lavaca	Beaumont	TX	United States of America
1511	www.liu.edu	Long Island University - C W Post Campus	5162992900	720 Northern Blvd	Brookville	NY	United States of America
1512	www.livingstone.edu	Livingstone College	7042166000	701 W Monroe St	Salisbury	NC	United States of America
1513	www.llcc.edu	Lincoln Land Community College	2177862200	5250 Shepherd Rd	Springfield	IL	United States of America
1514	www.llu.edu	Loma Linda University	9095581000	11234 Anderson St.	Loma Linda	CA	United States of America
1515	www.lmc.edu	Lees-McRae College	8288985241	191 Main Street	Banner Elk	NC	United States of America
1516	www.lmu.edu	Loyola Marymount University	3103382700	One LMU Drive	Los Angeles	CA	United States of America
1517	www.lmunet.edu	Lincoln Memorial University	4238693611	6965 Cumberland Gap Pky	Harrogate	TN	United States of America
1518	www.loc.edu	LeMoyne-Owen College	9017749090	807 Walker Ave	Memphis	TN	United States of America
1519	www.logan.edu	Logan University	6362272100	1851 Schoettler Rd.	Chesterfield	MO	United States of America
1520	www.logisticseducation.edu	Institute of Logistical Management	8004564600	315 West Broad Street	Burlington	NJ	United States of America
1521	www.logos-seminary.edu_1.htm	Logos Evangelical Seminary	6265715110	9358 Telstar Ave.	El Monte	CA	United States of America
1522	www.longwood.edu	Longwood University	4343952000	201 High St	Farmville	VA	United States of America
1523	www.longy.edu	Longy School of Music	6178760956	One Follen St	Cambridge	MA	United States of America
1524	www.lonmorris.edu	Lon Morris College	9035894000	800 College Ave	Jacksonville	TX	United States of America
1525	www.lorainccc.edu	Lorain County Community College	4403665222	1005 North Abbe Rd	Elyria	OH	United States of America
1526	www.loras.edu	Loras College	5635887100	1450 Alta Vista	Dubuque	IA	United States of America
1527	www.louisburg.edu	Louisburg College	9194962521	501 N. Main St.	Louisburg	NC	United States of America
1528	www.louisiana.edu	University of Louisiana at Lafayette	3774821000	104 University Cir	Lafayette	LA	United States of America
1529	www.louisville.edu	University of Louisville	5028525555	2301 S 3rd St	Louisville	KY	United States of America
1530	www.lourdes.edu	Lourdes University	4198853211	6832 Convent Blvd	Sylvania	OH	United States of America
1531	www.loyno.edu	Loyola University New Orleans	5048652011	6363 Saint Charles Ave	New Orleans	LA	United States of America
1532	www.loyola.edu	Loyola University Maryland	4106172000	4501 N Charles St	Baltimore	MD	United States of America
1533	www.lpts.edu	Louisville Presbyterian Theological Seminary	5028953411	1044 Alta Vista Rd	Louisville	KY	United States of America
1534	www.lr.edu	Lenoir-Rhyne University	8283281741	625 7th Avenue NE	Hickory	NC	United States of America
1535	www.lrsc.nodak.edu	Lake Region State College	7016621600	1801 College Dr N	Devils Lake	ND	United States of America
1536	www.lru.edu	Luther Rice University	7704841204	3038 Evans Mill Rd	Lithonia	GA	United States of America
1537	www.LSB.edu	Lansdale School of Business	2156995700	290 Wissahickon Avenue	North Wales	PA	United States of America
1538	www.lsc.mnscu.edu	Lake Superior College	8004322884	2101 Trinity Rd	Duluth	MN	United States of America
1539	www.lscc.edu	Lake-Sumter State College	3527873747	9501 US Hwy 441	Leesburg	FL	United States of America
1540	www.lsco.edu	Lamar State College - Orange	4098837750	410 Front St	Orange	TX	United States of America
1541	www.lssu.edu	Lake Superior State University	9066326841	650 W Easterday Ave	Sault Ste Marie	MI	United States of America
1542	www.lstc.edu	Lutheran School of Theology at Chicago	7732560700	1100 E 55th St	Chicago	IL	United States of America
1543	www.lsu.edu	Louisiana State University and Agricultural & Mechanical College	2255783202		Baton Rouge	LA	United States of America
1544	www.lsua.edu	Louisiana State University at Alexandria	3184453672	8100 Hwy 71 South	Alexandria	LA	United States of America
1545	www.lsue.edu	Louisiana State University - Eunice	3375501201	2048 Johnson Hwy	Eunice	LA	United States of America
1546	www.lsuhsc.edu	Louisiana State University Health Sciences Center at New Orleans	5045684808	433 Bolivar St	New Orleans	LA	United States of America
1547	www.lsus.edu	Louisiana State University - Shreveport	3187975000	One University Place	Shreveport	LA	United States of America
1548	www.ltc.edu	Louisiana Technical College - Delta-Ouachita Campus	3183976100	609 Vocational Parkway	West Monroe	LA	United States of America
1549	www.ltc.edu	Louisiana Technical College - Lafayette	3372625962	1101 Bertrand Drive	Lafayette	LA	United States of America
1550	www.ltcc.edu	Lake Tahoe Community College	5305414660	One College Drive	South Lake Tahoe	CA	United States of America
1551	www.ltsg.edu	Lutheran Theological Seminary at Gettysburg	7173346286	61 Seminary Ridge	Gettysburg	PA	United States of America
1552	www.ltsp.edu	Lutheran Theological Seminary at Philadelphia	2152484616	7301 Germantown Ave	Philadelphia	PA	United States of America
1553	www.ltss.edu	Lutheran Theological Southern Seminary	8037865150	4201 N Main St	Columbia	SC	United States of America
1554	www.ltu.edu	Lawrence Technological University	2482044000	21000 W Ten Mile Rd	Southfield	MI	United States of America
1555	www.luc.edu	Loyola University of Chicago	3129156000	820 N. Michigan Ave.	Chicago	IL	United States of America
1556	www.lunet.edu	Langston University	4054662231	102 Page Hall	Langston	OK	United States of America
1557	www.luther.edu	Luther College	5633872000	700 College Drive	Decorah	IA	United States of America
1558	www.luthersem.edu	Luther Seminary	6516413456	2481 Como Ave.	St. Paul	MN	United States of America
1559	www.luzerne.edu	Luzerne County Community College	5707400200	1333 South Prospect Street	Nanticoke	PA	United States of America
1560	www.lvc.edu	Lebanon Valley College	7178676100	101 N College Ave	Annville	PA	United States of America
1561	www.lwit.edu	Lorenzo Walker Institute of Technology	2393770906	3702 Estey Avenue	Naples	FL	United States of America
1562	www.lwtech.edu	Lake Washington Institute of Technology	4257398100	11605 132nd Avenue NE	Kirkland	WA	United States of America
1563	www.lycoming.edu	Lycoming College	5703214000	700 College Place	Williamsport	PA	United States of America
1564	www.lymeacademy.edu	Lyme Academy College of Fine Arts	8604345232	84 Lyme St	Old Lyme	CT	United States of America
1565	www.lynchburg.edu	Lynchburg College	4345448100	1501 Lakeside Dr	Lynchburg	VA	United States of America
1566	www.lynn.edu	Lynn University	5612377000	3601 N. Military Trail	Boca Raton	FL	United States of America
1567	www.lyon.edu	Lyon College	8707939813	2300 Highland Road	Batesville	AR	United States of America
1568	www.mac.edu	MacMurray College	2174797000	447 E. College Ave	Jacksonville	IL	United States of America
1569	www.macalester.edu	Macalester College	6516966000	1600 Grand Avenue	St. Paul	MN	United States of America
1570	www.macc.edu	Moberly Area Community College	6602634110	101 College Ave	Moberly	MO	United States of America
1571	www.maccormac.edu	MacCormac College	3129221884	29 E. Madison	Chicago	IL	United States of America
1572	www.macomb.edu	Macomb Community College	5864457999	14500 E Twelve Mile Rd	Warren	MI	United States of America
1573	www.maconstate.edu	Macon State College	4784712700	100 College Station Dr	Macon	GA	United States of America
1574	www.macu.edu	Mid-America Christian University	4056913800	3500 SW 119th St	Oklahoma City	OK	United States of America
1575	www.macuniversity.edu	Mid-Atlantic Christian University	2523342000	715 N Poindexter St	Elizabeth City	NC	United States of America
1576	www.madisonville.kctcs.edu	Madisonville Community College	2708212250	2000 College Drive	Madisonville	KY	United States of America
1577	www.madonna.edu	Madonna University	7344325300	36600 Schoolcraft Rd	Livonia	MI	United States of America
1578	www.magdalen.edu	Magdalen College	6034562656	511 Kearsarge Mtn Rd	Warner	NH	United States of America
1579	www.magnolia.edu	Magnolia Bible College	6622892896	822 S Huntington St	Kosciusko	MS	United States of America
1580	www.mainemaritime.edu	Maine Maritime Academy	2073262206	C3	Castine	ME	United States of America
1581	www.malone.edu	Malone University	3304718100	2600 Cleveland Ave. NW	Canton	OH	United States of America
1582	www.manchester.edu	Manchester University	2609825000	604 E. College Ave.	North Manchester	IN	United States of America
1583	www.manhattan.edu	Manhattan College	7188628000	Manhattan College Pky	Riverdale	NY	United States of America
1584	www.manor.edu	Manor College	2158852360	700 Fox Chase Rd	Jenkintown	PA	United States of America
1585	www.mansfield.edu	Mansfield University of Pennsylvania	5706624000	Academy Street	Mansfield	PA	United States of America
1586	www.mariacollege.edu	Maria College	5184383111	700 New Scotland Avenue	Albany	NY	United States of America
1587	www.marian.edu	Marian University	3179556000	3200 Cold Spring Rd	Indianapolis	IN	United States of America
1588	www.mariancollege.edu	Marian University	9209237600	45 S. National Ave.	Fond du Lac	WI	United States of America
1589	www.mariancourt.edu	Marian Court College	7815956768	35 Littles Point Rd	Swampscott	MA	United States of America
1590	www.mariccollege.edu	Kaplan College - San Diego	6192794500	9055 Balboa Avenue	San Diego	CA	United States of America
1591	www.marietta.edu	Marietta College	7403764643	215 Fifth Street	Marietta	OH	United States of America
1592	www.marionmilitary.edu	Marion Military Institute	3346832303	1101 Washington St	Marion	AL	United States of America
1593	www.marist.edu	Marist College	8455753000	3399 North Road	Poughkeepsie	NY	United States of America
1594	www.maritime.edu	Massachusetts Maritime Academy	5088305000	101 Academy Dr	Buzzards Bay	MA	United States of America
1595	www.marlboro.edu	Marlboro College	8022574333	2582 South Rd	Marlboro	VT	United States of America
1596	www.marshall.edu	Marshall University	3046963212	1 John Marshall Dr	Huntington	WV	United States of America
1597	www.marshall.edu	Mountwest Community and Technical College	3046963212	2205 Fifth Street Rd.	Huntington	WV	United States of America
1598	www.marshall.edu/	Marshall University School of Pharmacy	3046967302	One John Marshall Drive	Huntington	WV	United States of America
1599	www.martin.cc.edu	Martin Community College	2527921521	1161 Kehukee Pk Rd	Williamston	NC	United States of America
1600	www.martinmethodist.edu	Martin Methodist College	9313639804	433 West Madison Street	Pulaski	TN	United States of America
1601	www.marygrove.edu	Marygrove College	3139271200	8425 W McNichols Rd	Detroit	MI	United States of America
1602	www.marylhurst.edu	Marylhurst University	5036368141	17600 Pacific Hwy - Hwy 43	Marylhurst	OR	United States of America
1603	www.marymount.edu	Marymount University	7035225600	2807 N Glebe Rd	Arlington	VA	United States of America
1604	www.marymountpv.edu	Marymount College University	3103775501	30800 Palos Verdes Dr. East	Rancho Palos Verdes	CA	United States of America
1605	www.marymt.edu	Marymount College of Fordham University	9146313200	100 Marymount Ave	Tarrytown	NY	United States of America
1606	www.maryville.edu	Maryville University of Saint Louis	8006279855	650 Maryville University Drive	Saint Louis	MO	United States of America
1607	www.maryvillecollege.edu	Maryville College	8659818000	502 E Lamar Alexander Pky	Maryville	TN	United States of America
1608	www.marywood.edu	Marywood University	5703486211	2300 Adams Ave	Scranton	PA	United States of America
1609	www.massart.edu	Massachusetts College of Art and Design	6178797000	621 Huntington Ave	Boston	MA	United States of America
1610	www.massasoit.mass.edu	Massasoit Community College	5085889100	One Massasoit Boulevard	Brockton	MA	United States of America
1611	www.massbay.edu	Massachusetts Bay Community College	7812393000	50 Oakland St	Wellesley Hills	MA	United States of America
1612	www.masters.edu	The Master's College and Seminary	6612593540	21726 Placerita Canyon Road	Santa Clarita	CA	United States of America
1613	www.matc.edu	Milwaukee Area Technical College	4142976370	700 W State St	Milwaukee	WI	United States of America
1614	www.mauicc.hawaii.edu	University of Hawaii Maui College	8089843500	310 Kaahumanu Ave	Kahului	HI	United States of America
1615	www.mayland.edu	Mayland Community College	8287657351	200 Mayland Drive	Spruce Pine	NC	United States of America
1616	www.maysville.kctcs.edu	Maysville Community and Technical College	6067597141	1755 U.S. 68	Maysville	KY	United States of America
1617	www.mayvillestate.edu	Mayville State University	7017882301	330 Third St NE	Mayville	ND	United States of America
1618	www.mbc.edu	Mary Baldwin College	5408877000	101 East Frederick Street	Staunton	VA	United States of America
1619	www.mbseminary.edu	Mennonite Brethren Biblical Seminary	5592518628	4824 E Butler	Fresno	CA	United States of America
1620	www.mbts.edu	Midwestern Baptist Theological Seminary	8164143700	5001 N. Oak Trafficway	Kansas City	MO	United States of America
1621	www.mc.edu	Mississippi College	6019253000	200 South Capitol Street	Clinton	MS	United States of America
1622	www.mc.maricopa.edu	Maricopa Community Colleges - Mesa Community College	6024617000	1833 W Southern Ave	Mesa	AZ	United States of America
1623	www.mc.vanderbilt.edu	Vanderbilt University Medical Center		1161 21st Avenue South	Nashville	TN	United States of America
1624	www.mc3.edu	Montgomery County Community College	2156416300	340 Dekalb Pike	Blue Bell	PA	United States of America
1625	www.mca.edu	Memphis College of Art	9012725100	1930 Poplar Ave	Memphis	TN	United States of America
1626	www.mcc.edu	Charles Stewart Mott Community College	8107620200	1401 E. Court St.	Flint	MI	United States of America
1627	www.mccc.edu	Mercer County Community College	6095864800	1200 Old Trenton Road	West Windsor	NJ	United States of America
1628	www.mcckc.edu	Metropolitan Community College - Kansas City	8167591050	3200 Broadway	Kansas City	MO	United States of America
1629	www.mccks.edu	Manhattan Christian College	7855393571	1415 Anderson Ave	Manhattan	KS	United States of America
1630	www.mccn.edu	Mount Carmel College of Nursing	6142345800	127 So.  Davis Ave	Columbus	OH	United States of America
1631	www.mccneb.edu	Metropolitan Community College	4024572400	North 30th Street and Fort Street	Omaha	NE	United States of America
1632	www.mccormick.edu	McCormick Theological Seminary	7739476300	5460 S. University	Chicago	IL	United States of America
1633	www.mcdaniel.edu	McDaniel College	4108487000	2 College Hill	Westminster	MD	United States of America
1634	www.mcdowelltech.edu	McDowell Technical Community College	8286526021	54 College Drive	Marion	NC	United States of America
1635	www.mcg.edu	Georgia Health Sciences University	7067210211	1120 Fifteenth Street	Augusta	GA	United States of America
1636	www.mchenry.edu	McHenry County College	8154553700	8900 US Hwy 14	Crystal Lake	IL	United States of America
1637	www.mchs.edu	Mercy College of Health Sciences	5156433180	928 Sixth Ave	Des Moines	IA	United States of America
1638	www.mcidenver.edu	Montessori Casa International	3035237590	7551 East Academy Boulevard	Denver	CO	United States of America
1639	www.McIntoshcollege.edu	McIntosh College	6037421234	23 Cataract Ave	Dover	NH	United States of America
1640	www.mckendree.edu	McKendree University	6185374481	701 College Rd	Lebanon	IL	United States of America
1641	www.mckinleycollege.edu	McKinley College	9702074550	2001 Lowe Street	Fort Collins	CO	United States of America
1642	www.mcla.edu	Massachusetts College of Liberal Arts	4136625000	375 Church St	North Adams	MA	United States of America
1643	www.mclennan.edu	McLennan Community College	2542998000	1400 College Dr	Waco	TX	United States of America
1644	www.mcm.edu	McMurry University	3257933800	S 14th and Sayles Blvd	Abilene	TX	United States of America
1645	www.mcnallysmith.edu	McNally Smith College of Music	6512910177	19 Exchange Street East	Saint Paul	MN	United States of America
1646	www.mcneese.edu	McNeese State University	3374755000	4205 Ryan Street	Lake Charles	LA	United States of America
1647	www.mcpherson.edu	McPherson College	6202410731	1600 E Euclid	McPherson	KS	United States of America
1648	www.mcphs.edu	Massachusetts College of Pharmacy & Health Sciences	6177322800	179 Longwood Ave	Boston	MA	United States of America
1649	www.mcw.edu	Medical College of Wisconsin	4144568296	8701 Watertown Plank Rd	Milwaukee	WI	United States of America
1650	www.mdc.edu	Miami Dade College	3052378888	300 NE 2nd Ave	Miami	FL	United States of America
1651	www.mdc.edu	New World School of the Arts		25 NE Second Street	Miami	FL	United States of America
1652	www.meadville.edu	Meadville-Lombard Theological School	7732563000	610 S. Michigan Avenue	Chicago	IL	United States of America
1653	www.mec.cuny.edu	Medgar Evers College of the City University of New York	7182704900	1650 Bedford Ave	Brooklyn	NY	United States of America
1654	www.meca.edu	Maine College of Art	2077753052	97 Spring St	Portland	ME	United States of America
1655	www.mecc.edu	Mountain Empire Community College	2765232400	3441 Mountain Empire Road	Big Stone Gap	VA	United States of America
1656	www.mecr.edu	Montessori Education Center of the Rockies	3034943002	4745 Walnut Street	Boulder	CO	United States of America
1657	www.medaille.edu	Medaille College	7168843281	18 Agassiz Circle	Buffalo	NY	United States of America
1658	www.medcentral.edu	MedCentral College of Nursing	4195202600	335 Glessner Ave	Mansfield	OH	United States of America
1659	www.medianschool.edu	Vet Tech Institute	4123917021	125 Seventh St	Pittsburgh	PA	United States of America
1660	www.medical.edu	MedSpa Careers Institute	7578732423	1001 Omni Blvd	Newport News	VA	United States of America
1661	www.medicine.uiowa.edu	University of Iowa Hospital and Clinics		200 Hawkins Drive	Iowa City	IA	United States of America
1662	www.medixschool.edu	Medix School - West	4109078110	6901 Security Boulevard	Baltimore	MD	United States of America
1663	www.medvance.edu	Fortis College - Baton Rouge	2252481015	9255 Interline Avenue	Baton Rouge	LA	United States of America
1664	www.memphis.edu	University of Memphis	9016782000	341 Administration Building	Memphis	TN	United States of America
1665	www.memphisseminary.edu	Memphis Theological Seminary	9014588232	168 East Parkway South	Memphis	TN	United States of America
1666	www.MendocinoCollege.edu	Mendocino College	7074683000	1000 Hensley Creek Road	Ukiah	CA	United States of America
1667	www.menlo.edu	Menlo College	8005563656	1000 El Camino Real	Atherton	CA	United States of America
1668	www.menominee.edu	College of Menominee Nation	7157995600	N172 State Highway 47&55	Keshena	WI	United States of America
1669	www.mercer.edu	Mercer University	4783012700	1400 Coleman Avenue	Macon	GA	United States of America
1670	www.mercy.edu	Mercy College - Dobbs Ferry	9146934500	555 Broadway	Dobbs Ferry	NY	United States of America
1671	www.mercycollege.edu	Mercy College of Ohio	4192511279	2221 Madison Avenue	Toledo	OH	United States of America
1672	www.mercyhurst.edu	Mercyhurst University	8148242000	501 E 38th St	Erie	PA	United States of America
1673	www.meredith.edu	Meredith College	9197608600	3800 Hillsborough St	Raleigh	NC	United States of America
1674	www.meridiancc.edu	Meridian Community College	6014838241	910 Hwy 19 N	Meridian	MS	United States of America
1675	www.merritt.edu	Merritt College	5105314911	12500 Campus Dr	Oakland	CA	United States of America
1676	www.mesalands.edu	Mesalands Community College	5054614413	911 S Tenth Street	Tucumcari	NM	United States of America
1677	www.messengercollege.edu	Messenger College	4176247070	400 S. Industrial Boulevard	Euless	TX	United States of America
1678	www.messiah.edu	Messiah College	7177662511	One College Ave	Grantham	PA	United States of America
1679	www.methodist.edu	Methodist College	9106307000	5400 Ramsey St	Fayetteville	NC	United States of America
1680	www.methodistcollege.edu	Nebraska Methodist College of Nursing and Allied Health	4023904863	720 N. 87th Street	Omaha	NE	United States of America
1681	www.metropolitan.edu	Metropolitan College of New York	8003384465	75 Varick St	New York	NY	United States of America
1682	www.metrostate.edu	Metropolitan State University	6517931212	700 E Seventh St	Saint Paul	MN	United States of America
1683	www.mgc.edu	Middle Georgia College	4789346221	1100 Second St SE	Cochran	GA	United States of America
1684	www.mgccc.edu	Mississippi Gulf Coast Community College	6019285211	51 Main Street	Perkinston	MS	United States of America
1685	www.mghihp.edu	MGH Institute of Health Professions	6177263140	36 1st Avenue	Boston	MA	United States of America
1686	www.mhc.edu	Mars Hill University	8286891307	100 Athletic St	Mars Hill	NC	United States of America
1687	www.mhcc.edu	Mt. Hood Community College	5034916422	26000 SE Stark Street	Gresham	OR	United States of America
1688	www.mhgs.edu	The Seattle School of Theology and Psychology	2068766100	2501 Elliot Avenue	Seattle	WA	United States of America
1689	www.mi.edu	Musicians Institute	3238601143	6752 Hollywood Boulevard	Hollywood	CA	United States of America
1690	www.miad.edu	Milwaukee Institute of Art Design	4142767889	273 E Erie St	Milwaukee	WI	United States of America
1691	www.miami.edu	University of Miami	3052842211	University Station	Coral Gables	FL	United States of America
1692	www.mica.edu	Maryland Institute College of Art	4106699200	1300 Mount Royal Ave	Baltimore	MD	United States of America
1693	www.mid-america.edu	Mid-America College of Funeral Service	8122888878	3111 Hamburg Pke	Jeffersonville	IN	United States of America
1694	www.midamerica.edu	Mid-America Reformed Seminary	2198642400	229 Seminary Drive	Dyer	IN	United States of America
1695	www.midcontinent.edu	Mid-Continent University	2702478521	99 Powell Rd E	Mayfield	KY	United States of America
1696	www.middlebury.edu	Middlebury College	8024435000	Old Chapel	Middlebury	VT	United States of America
1697	www.middlegatech.edu	Middle Georgia Technical College	4789886800	80 Cohen Walker Dr	Warner Robins	GA	United States of America
1698	www.middlesex.mass.edu	Middlesex Community College - Bedford	9786563200	591 Springs Road	Bedford	MA	United States of America
1699	www.middlesexcc.edu	Middlesex County College	7325486000	2600 Woodbridge Avenue	Edison	NJ	United States of America
1700	www.midland.edu	Midland College	4326854500	3600 N Garfield	Midland	TX	United States of America
1701	www.midlandstech.edu	Midlands Technical College	8037388324	1260 Lexington Drive	West Columbia	SC	United States of America
1702	www.midmich.edu	Mid Michigan Community College	5173866622	1375 S Clare Ave	Harrison	MI	United States of America
1703	www.midsouthcc.edu	Mid-South Community College	8707336722	2000 W.  Broadway	West Memphis	AR	United States of America
1704	www.midstate.edu	Midstate College	3096924092	411 W Northmoor Road	Peoria	IL	United States of America
1705	www.midway.edu	Midway College	8598464421	512 E. Stephens St	Midway	KY	United States of America
1706	www.midwest.edu	Midwest University	6363274645	851 Parr Rd	Wentzville	MO	United States of America
1707	www.midwestern.edu	Midwestern University	6309694400	555 31st Street	Downers Grove	IL	United States of America
1708	www.midwesttech.edu	Midwest Technical Institute - East Peoria	8005048882	280 Highpoint Lane	East Peoria	IL	United States of America
1709	www.midwifery.edu	Midwives College of Utah	8666802756	1174 E 2700 S Suite 2	Salt Lake City	UT	United States of America
1710	www.milaninstitute.edu	Milan Institute - San Antonio	2106475100	6804 Ingram Road	San Antonio	TX	United States of America
1711	www.mildred-elley.edu	Mildred Elley	5187860855	855 Central Avenue	Albany	NY	United States of America
1712	www.miles.edu	Miles College	2059291000	5500 Myron Massey Blvd	Fairfield	AL	United States of America
1713	www.milescc.edu	Miles Community College	8005419281	2715 Dickinson	Miles City	MT	United States of America
1714	www.millercollege.edu	Robert B. Miller College	2696608021	450 North Avenue	Battle Creek	MI	United States of America
1715	www.millersville.edu	Millersville University of Pennsylvania	7178723024	20 Dilworth Rd	Millersville	PA	United States of America
1716	www.milligan.edu	Milligan College	4234618700	1 Blowers Boulevard	Milligan College	TN	United States of America
1717	www.millikin.edu	Millikin University	2174246211	1184 W Main St	Decatur	IL	United States of America
1718	www.mills.edu	Mills College	5104302255	5000 MacArthur Blvd	Oakland	CA	United States of America
1719	www.millsaps.edu	Millsaps College	6019741000	1701 N State St	Jackson	MS	United States of America
1720	www.milwaukeeballetschool.edu	Milwaukee Ballet School	4149022218	504 West National Avenue	Milwaukee	WI	United States of America
1721	www.mines.edu	Colorado School of Mines	3032733200	1500 Illinois St	Golden	CO	United States of America
1722	www.minnesota.edu	Minnesota State Community and Technical College	2187397500	1414 College Way	Fergus Falls	MN	United States of America
1723	www.minotstateu.edu	Minot State University	7018583000	500 University Ave W	Minot	ND	United States of America
1724	www.miracosta.edu	Miracosta College	7607572121	One Barnard Dr	Oceanside	CA	United States of America
1725	www.misericordia.edu	Misericordia University	5706746400	301 Lake St	Dallas	PA	United States of America
1726	www.mispp.edu	Michigan School of Professional Psychology	2484761122	26811 Orchard Lake Rd.	Farmington Hills	MI	United States of America
1727	www.missouri.edu	University of Missouri - Columbia	5738822121	105 Jesse Hall	Columbia	MO	United States of America
1728	www.missouristate.edu	Missouri State University	4178365000	901 S National	Springfield	MO	United States of America
1729	www.missouriwestern.edu	Missouri Western State University	8162714200	4525 Downs Dr	Saint Joseph	MO	United States of America
1730	www.mitchell.cc.edu	Mitchell Community College	7048783200	500 W Broad Street	Statesville	NC	United States of America
1731	www.mitchell.edu	Mitchell College	8607015000	437 Pequot Ave	New London	CT	United States of America
1732	www.mji.edu	Michigan Jewish Institute	2484146900	6890 West Maple Road	West Bloomfield	MI	United States of America
1733	www.mlatc.edu	Mountainland Applied Technology	8018637662	2301 West Ashton Road	Lehi	UT	United States of America
1734	www.mlc-wels.edu	Martin Luther College	5073548221	1995 Luther Court	New Ulm	MN	United States of America
1735	www.MLC.edu	Midland University	4027215480	900 N. Clarkson	Fremont	NE	United States of America
1736	www.mmc.edu	Meharry Medical College	6153276111	1005 Dr. D.B. Todd Blvd.	Nashville	TN	United States of America
1737	www.mmm.edu	Marymount Manhattan College	2125170400	221 E 71st St	New York	NY	United States of America
1738	www.mnstate.edu	Minnesota State University - Moorhead	2184774000	1104 7th Ave S	Moorhead	MN	United States of America
1739	www.mnsu.edu	Minnesota State University - Mankato	5073896767	228 Wiecking Center	Mankato	MN	United States of America
1740	www.mnu.edu	MidAmerica Nazarene University	9137823750	2030 E College Way	Olathe	KS	United States of America
1741	www.mnwest.edu	Minnesota West Community and Technical College	3205644511	1593 11th Ave	Granite Falls	MN	United States of America
1742	www.mobap.edu	Missouri Baptist University	3144341115	One College Park Dr	Saint Louis	MO	United States of America
1743	www.moc.edu	University of Mount Olive	9196582502	634 Henderson St	Mount Olive	NC	United States of America
1744	www.mohave.edu	Mohave Community College	9287574331	1971 Jagerson Ave	Kingman	AZ	United States of America
1745	www.molloy.edu	Molloy College	5166785000	1000 Hempstead Ave	Rockville Centre	NY	United States of America
1746	www.monm.edu	Monmouth College	3094572345	700 E Broadway	Monmouth	IL	United States of America
1747	www.monmouth.edu	Monmouth University	7325713400	400 Cedar Ave	West Long Branch	NJ	United States of America
1748	www.monroecc.edu	Monroe Community College	5852922000	1000 E Henrietta Rd	Rochester	NY	United States of America
1749	www.MONROECCC.edu	Monroe County Community College	7342427300	1555 South  Raisinville Road	Monroe	MI	United States of America
1750	www.monroecollege.edu	Monroe College	7189336700	2501 Jerome Avenue	Bronx	NY	United States of America
1751	www.montana.edu	Montana State University - Bozeman	4069940211	P.O. Box 172420	Bozeman	MT	United States of America
1752	www.montanabiblecollege.edu	Montana Bible College	4065863585	3625 S 19th Ave	Bozeman	MT	United States of America
1753	www.montcalm.edu	Montcalm Community College	9893282111	2800 College Dr	Sidney	MI	United States of America
1754	www.montclair.edu	Montclair State University	9736554000	1 Normal Avenue - 855 Valley Road	Montclair	NJ	United States of America
1755	www.montevallo.edu	University of Montevallo	2056656155	Station 6001	Montevallo	AL	United States of America
1756	www.montgomery.edu	Montgomery Community College	9105766222	1011 Page St	Troy	NC	United States of America
1757	www.montgomerycollege.edu	Montgomery College	3012795000	51 Mannakee Street	Rockville	MD	United States of America
1758	www.montreat.edu	Montreat College	8286698011	310 Gaither Cir	Montreat	NC	United States of America
1759	www.montserrat.edu	Montserrat College of Art	9789228222	23 Essex St	Beverly	MA	United States of America
1760	www.moody.edu	Moody Bible Institute	3123294000	820 N LaSalle Blvd	Chicago	IL	United States of America
1761	www.moore.edu	Moore College of Art and Design	2155684515	20th and the Parkway	Philadelphia	PA	United States of America
1762	www.moorparkcollege.edu	Moorpark College	8053781400	7075 Campus Rd	Moorpark	CA	United States of America
1763	www.morainepark.edu	Moraine Park Technical College	9209228611	235 N National Ave	Fond Du Lac	WI	United States of America
1764	www.morainevalley.edu	Moraine Valley Community College	7089744300	9000 W. College Parkway	Palos Hills	IL	United States of America
1765	www.moravian.edu	Moravian College	6108611300	1200 Main St	Bethlehem	PA	United States of America
1766	www.moreheadstate.edu	Morehead State University	6067832221	150 University Blvd	Morehead	KY	United States of America
1767	www.morehouse.edu	Morehouse College	4046812800	830 Westview Dr SW	Atlanta	GA	United States of America
1768	www.morgan.edu	Morgan State University	4438853333	1700 East Cold Spring Lane	Baltimore	MD	United States of America
1769	www.morningside.edu	Morningside College	7122745000	1501 Morningside Ave	Sioux City	IA	United States of America
1770	www.morris.edu	Morris College	8039343200	100 West College St	Sumter	SC	United States of America
1771	www.morrisville.edu	SUNY College of Agriculture & Technology at Morrisville	3156846000	P.O.  Box 901	Morrisville	NY	United States of America
1772	www.morton.edu	Morton College	7086568000	3801 S Central Ave	Cicero	IL	United States of America
1773	www.motech.edu	Missouri Tech	3145693600	1690 Country Club Drive	St. Charles	MO	United States of America
1774	www.mountainstate.edu	Mountain State University	3042537351	410 Neville Street PO Box 9003	Beckley	WV	United States of America
1775	www.mountida.edu	Mount Ida College	6179284500	777 Dedham Street	Newton	MA	United States of America
1776	www.mountsaintvincent.edu	College of Mount Saint Vincent	7184053200	6301 Riverdale Ave	Bronx	NY	United States of America
1777	www.mountunion.edu	University of Mount Union	8009926682	1972 Clark Ave.	Alliance	OH	United States of America
1778	www.moval.edu	Missouri Valley College	6608314000	500 E College St	Marshall	MO	United States of America
1779	www.mpc.edu	Monterey Peninsula College	8316464000	980 Fremont St	Monterey	CA	United States of America
1780	www.mpcc.edu	Mid-Plains Community College - South Campus	8006584308	601 West State Farm Road	North Platte	NE	United States of America
1781	www.mr.mnscu.edu	Mesabi Range College	2187413095	1001 Chestnut St W	Virginia	MN	United States of America
1782	www.mrs.umn.edu	University of Minnesota - Morris	3205892211	600 East 4th Street	Morris	MN	United States of America
1783	www.ms.nhctc.edu	New Hampshire Community Technical College - Manchester	6037721194	1066 Front Street	Manchester	NH	United States of America
1784	www.msbbcs.edu	Maple Springs Baptist Bible College and Seminary	3017363631	4130 Belt Road	Capital Heights	MD	United States of America
1785	www.msbcollege.edu	Minnesota School of Business	6128612000	1401 W 76 St	Richfield	MN	United States of America
1786	www.mscc.edu	Motlow State Community College	9313931500	6015 Ledford Mill Road	Tullahoma	TN	United States of America
1787	www.mscd.edu	Metropolitan State University of Denver	3035563876	PO Box 173362	Denver	CO	United States of America
1788	www.mscok.edu	Murray State College	5803712371	One Murray Campus	Tishomingo	OK	United States of America
1789	www.msdelta.edu	Mississippi Delta Community College	6622466322	Hwy 3 and Cherry St	Moorhead	MS	United States of America
1790	www.msj.edu	College of Mount St. Joseph	5132444200	5701 Delhi Rd	Cincinnati	OH	United States of America
1791	www.msjc.edu	Mt San Jacinto College	9514876752	1499 N State St	San Jacinto	CA	United States of America
1792	www.mslaw.edu	Massachusetts School of Law	9786810800	500 Federal St Woodland Park	Andover	MA	United States of America
1793	www.msm.edu	Morehouse School of Medicine	4047521500	720 Westview Dr SW	Atlanta	GA	United States of America
1794	www.msmary.edu	Mount St Mary's University	3014476122	16300 Old Emmitsburg Rd	Emmitsburg	MD	United States of America
1795	www.msmc.edu	Mount Saint Mary College	8455610800	330 Powell Avenue	Newburgh	NY	United States of America
1796	www.msmc.la.edu	Mount St. Mary's College	3109544000	12001 Chalon Road	Los Angeles	CA	United States of America
1797	www.msmnyc.edu	Manhattan School of Music	2127492802	120 Claremont Ave	New York	NY	United States of America
1798	www.msoe.edu	Milwaukee School of Engineering	4142777300	1025 N Broadway	Milwaukee	WI	United States of America
1799	www.mspp.edu	Massachusetts School of Professional Psychology	6173276777	1 Wells Avenue	Newton	MA	United States of America
1800	www.mssm.edu	Mount Sinai School of Medicine	2122416691	1 Gustave L Levy Place	New York	NY	United States of America
1801	www.msstate.edu	Mississippi State University	6623252323	610 Allen Hall	Mississippi State	MS	United States of America
1802	www.mssu.edu	Missouri Southern State University	4176259300	3950 E Newman Rd	Joplin	MO	United States of America
1803	www.mst.edu	Missouri University of Science and Technology	5733414111	1870 Miner Circle	Rolla	MO	United States of America
1804	www.mstc.edu	Mid-State Technical College	7154225300	500 32nd St N	Wisconsin Rapids	WI	United States of America
1805	www.msu.edu	Michigan State University	5173551855	450 Administration Bldg.	East Lansing	MI	United States of America
1806	www.msubillings.edu	Montana State University - Billings	4066572011	1500 University Drive	Billings	MT	United States of America
1807	www.msugf.edu	Montana State University - Great Falls College of Technology	4067714300	2100 16th Ave S	Great Falls	MT	United States of America
1808	www.msun.edu	Montana State University - Northern	4062653700	P.O.Box 7751	Havre	MT	United States of America
1809	www.mtaloy.edu	Mount Aloysius College	8148864131	7373 Admiral Peary Highway	Cresson	PA	United States of America
1810	www.mtangel.edu	Mount Angel Seminary	5038453951	1 Abbey Dr	Saint Benedict	OR	United States of America
1811	www.mtc.edu	Marion Technical College	7403894636	1467 Mt. Vernon Ave.	Marion	OH	United States of America
1812	www.mtech.edu	Montana Tech of the University of Montana	4064964101	1300 W Park St	Butte	MT	United States of America
1813	www.mtholyoke.edu	Mount Holyoke College	4135382000	50 College Street	South Hadley	MA	United States of America
1814	www.MTI.edu	MTI College of Business and Technology	7139747181	7277 Regency Sq Blvd	Houston	TX	United States of America
1815	www.mti.edu	MTI College of Business and Technology	2813333363	11420 East Frwy	Houston	TX	United States of America
1816	www.mticollege.edu	MTI College	9163391500	5221 Madison Ave	Sacramento	CA	United States of America
1817	www.mtiweb.edu	Cortiva Institute - Boston	6175761300	103 Morse Street	Watertown	MA	United States of America
1818	www.mtmary.edu	Mount Mary University	4142584810	2900 N. Menomonee River Pky	Milwaukee	WI	United States of America
1819	www.mtmc.edu	Mount Marty College	8006584552	1105 W. 8th Street	Yankton	SD	United States of America
1820	www.mtmercy.edu	Mount Mercy University	3193638213	1330 Elmhurst Dr NE	Cedar Rapids	IA	United States of America
1821	www.mts.edu	Moody Theological Seminary and Graduate School - Michigan	7342079581	41550 E Ann Arbor Trail	Plymouth	MI	United States of America
1822	www.mtsa.edu	Middle Tennessee School of Anesthesia Inc	6158686503	315 Hospital Drive	Madison	TN	United States of America
1823	www.mtsac.edu	Mt San Antonio College	9095945611	1100 N Grand Ave	Walnut	CA	United States of America
1824	www.mtsierra.edu	Mt Sierra College	6268732144	101 E Huntington Dr	Monrovia	CA	United States of America
1825	www.mtso.edu	Methodist Theological School in Ohio	7403631146	3081 Columbus Pike	Delaware	OH	United States of America
1826	www.mtsu.edu	Middle Tennessee State University	6158982300	1301 East Main Street	Murfreesboro	TN	United States of America
1827	www.mtti.edu	MotoRing Technical Training Institute (MTTI)	4014344840	1241 Fall River Avenue	Seekonk	MA	United States of America
1828	www.mtu.edu	Michigan Technological University	9064871885	1400 Townsend Drive	Houghton	MI	United States of America
1829	www.muhlenberg.edu	Muhlenberg College	4846643100	2400 Chew Street	Allentown	PA	United States of America
1830	www.multnomah.edu	Multnomah University	5032550332	8435 NE Glisan St	Portland	OR	United States of America
1831	www.mum.edu	Maharishi University of Management	5154727000	1000 N 4th St	Fairfield	IA	United States of America
1832	www.muohio.edu	Miami University	5135291809	501 East High St	Oxford	OH	United States of America
1833	www.murraystate.edu	Murray State University	2707623011	218 Wells Hall	Murray	KY	United States of America
1834	www.musc.edu	Medical University of South Carolina	8437922300	171 Ashley Ave	Charleston	SC	United States of America
1835	www.muskegoncc.edu	Muskegon Community College	6167739131	221 S Quarterline Rd	Muskegon	MI	United States of America
1836	www.muskingum.edu	Muskingum University	7408268114	163 Stormont Street	New Concord	OH	United States of America
1837	www.muw.edu	Mississippi University for Women	6623294750	1100 College Street	Columbus	MS	United States of America
1838	mvc.dcccd.edu	Mountain View College	2148608680	4849 West Illinois Avenue	Dallas	TX	United States of America
1839	www.mvcc.edu	Mohawk Valley Community College	3157925400	1101 Sherman Drive	Utica	NY	United States of America
1840	www.mville.edu	Manhattanville College	9146942200	2900 Purchase Street	Purchase	NY	United States of America
1841	www.mvnu.edu	Mount Vernon Nazarene University	7403926868	800 Martinsburg Rd	Mount Vernon	OH	United States of America
1842	www.mvsu.edu	Mississippi Valley State University	6622549041	14000 Highway 82 West	Itta Bena	MS	United States of America
1843	www.mwsu.edu	Midwestern State University	9403974000	3410 Taft Blvd	Wichita Falls	TX	United States of America
1844	www.mxcc.commnet.edu	Middlesex Community College - Middletown	8603435701	100 Training Hill Road	Middletown	CT	United States of America
1845	www.mybrcc.edu	Baton Rouge Community College	2252168000	5310 Florida Blvd	Baton Rouge	LA	United States of America
1846	www.naa.edu	National Aviation Academy A & P School	7275312080	6225 Ulmerton Road	Clearwater	FL	United States of America
1847	www.nacc.edu	Northeast Alabama Community College	2056384418	138 Alabama Highway 35	Rainsville	AL	United States of America
1848	www.naropa.edu	Naropa University	3034440202	2130 Arapahoe Ave	Boulder	CO	United States of America
1849	www.nashcc.edu	Nash Community College	2524434011	522 N. Old Carriage Road	Rocky Mount	NC	United States of America
1850	www.nashotah.edu	Nashotah House	2626466500	2777 Mission Rd	Nashotah	WI	United States of America
1851	www.national.edu	National American University - Rapid City	6053944800	321 Kansas City Street	Rapid City	SD	United States of America
1852	www.natpoly.edu	National Polytechnic College of Science	3108342501	272 S Fries Ave l  Los Angeles Harbor	Wilmington	CA	United States of America
1853	www.nau.edu	Northern Arizona University	9285239011	P.O. Box 4092	Flagstaff	AZ	United States of America
1854	www.navarrocollege.edu	Navarro College	9038746501	3200 W 7th Avenue	Corsicana	TX	United States of America
1855	www.naz.edu	Nazareth College of Rochester	5853892525	4245 East Ave	Rochester	NY	United States of America
1856	www.nbc.edu	Nazarene Bible College	7198845000	1111 Academy Park Loop	Colorado Springs	CO	United States of America
1857	www.nbs.edu	Northwest Baptist Seminary	2537596104	4301 N Stevens	Tacoma	WA	United States of America
1858	www.nbts.edu	New Brunswick Theological Seminary	7322475241	17 Seminary Place	New Brunswick	NJ	United States of America
1859	www.nca.edu	Northwest College of Art	3607799993	16301 Creative Dr NE	Poulsbo	WA	United States of America
1860	www.ncat.edu	North Carolina A & T State University	3363347500	1601 East Market Street	Greensboro	NC	United States of America
1861	www.ncbt.edu	American National University - Salem	5409861800	1813 E Main St	Salem	VA	United States of America
1862	www.ncc.commnet.edu	Norwalk Community College	2038577060	188 Richards Avenue	Norwalk	CT	United States of America
1863	www.ncc.edu	Nassau Community College	5162227355	1 Education Dr	Garden City	NY	United States of America
1864	www.nccc.edu	North Country Community College	5188912915	23 Santanoni Avenue	Saranac Lake	NY	United States of America
1865	www.nccu.edu	North Carolina Central University	9195606100	1801 Fayetteville Street	Durham	NC	United States of America
1866	www.ncf.edu	New College of Florida	9413594269	5800 Bay Shore Road	Sarasota	FL	United States of America
1867	www.nci.edu	North Central Institute	9314319700	168 Jack Miller Blvd	Clarksville	TN	United States of America
1868	www.ncmissouri.edu	North Central Missouri College	6603593948	1301 Main St	Trenton	MO	United States of America
1869	www.ncnm.edu	National College of Natural Medicine	5034994343	049 SW Porter	Portland	OR	United States of America
1870	www.ncstatecollege.edu	North Central State College	4197554800	2441 Kenwood Circle	Mansfield	OH	United States of America
1871	www.ncsu.edu	North Carolina State University	9195152011	20 Watauga Club Drive	Raleigh	NC	United States of America
1872	www.nctc.edu	North Central Texas College	9406687731	1525 W California Street	Gainesville	TX	United States of America
1873	www.ncu.edu	Northcentral University	8883272877	505 W. Whipple St.	Prescott	AZ	United States of America
1874	www.ncwc.edu	North Carolina Wesleyan College	2529855100	3400 N Wesleyan Blvd	Rocky Mount	NC	United States of America
1875	www.nd.edu	University of Notre Dame	5746315000	Main Building	Notre Dame	IN	United States of America
1876	www.ndic.edu	National Intelligence University		Defense Intelligence Analysis Center	Washington	DC	United States of America
1877	www.ndm.edu	Notre Dame of Maryland University	4104350100	4701 N Charles St	Baltimore	MD	United States of America
1878	www.ndnu.edu	Notre Dame de Namur University	6505083500	1500 Ralston Ave	Belmont	CA	United States of America
1879	www.nds.edu	Notre Dame Seminary	5048667426	2901 South Carrollton Ave	New Orleans	LA	United States of America
1880	www.ndscs.edu	North Dakota State College of Science	7016712403	800 N 6th St	Wahpeton	ND	United States of America
1881	www.ndsu.nodak.edu	North Dakota State University - Main Campus	7012318011	1301  12th Avenue North	Fargo	ND	United States of America
1882	www.ndu.edu	National Defense University	2026854700	300 5th Avenue	Fort McNair	DC	United States of America
1883	www.ne-optometry.edu	New England College of Optometry	6172662030	424 Beacon St	Boston	MA	United States of America
1884	www.nebrwesleyan.edu	Nebraska Wesleyan University	4024662371	5000 St Paul Ave	Lincoln	NE	United States of America
1885	www.nec.edu	New England College	6034282211	24 Bridge St	Henniker	NH	United States of America
1886	www.necc.mass.edu	Northern Essex Community College	9785563000	100 Elliott Street	Haverhill	MA	United States of America
1887	www.neci.edu	New England Culinary Institute	8022236324	56 College Street	Montpelier	VT	United States of America
1888	www.necmusic.edu	The New England Conservatory of Music	6175851100	290 Huntington Ave	Boston	MA	United States of America
1889	www.neia.artinstitutes.edu	The New England Institute of Art	6177391700	10 Brookline Place West	Brookline	MA	United States of America
1890	www.neit.edu	New England Institute of Technology	4014677744	One New England Boulevard	East Greenwich	RI	United States of America
1891	www.neiu.edu	Northeastern Illinois University	7735834050	5500 N Saint Louis Ave	Chicago	IL	United States of America
1892	www.nemcc.edu	Northeast Mississippi Community College	6627287751	101 Cunningham Boulevard	Booneville	MS	United States of America
1893	www.neoam.edu	Northeastern Oklahoma A&M College	9185428441	200 I St NE	Miami	OK	United States of America
1894	www.neosho.edu	Neosho County Community College	6204312820	800 W 14th St	Chanute	KS	United States of America
1895	www.neoucom.edu	Northeastern Ohio Universities College of Medicine	3303252511	4209 State Route 44	Rootstown	OH	United States of America
1896	www.nes.edu	Northeastern Seminary at Roberts Wesleyan College	5855946000	2265 Westside Dr	Rochester	NY	United States of America
1897	www.nesa.edu	New England School of Acupuncture Inc	6179261788	150 California Street	Newton	MA	United States of America
1898	www.nescom.edu	New England School of Communications	2079417176	1 College Circle	Bangor	ME	United States of America
1899	www.nesl.edu	New England School of Law	6174510010	154 Stuart St	Boston	MA	United States of America
1900	www.netc.edu	Northeastern Technical College	8439216900	1201 Chesterfield Hwy.	Cheraw	SC	United States of America
1901	www.neumann.edu	Neumann University	6104590905	One Neumann Drive	Aston	PA	United States of America
1902	www.newberry.edu	Newberry College	8032765010	2100 College St	Newberry	SC	United States of America
1903	www.newbury.edu	Newbury College-Brookline	6177307000	129 Fisher Ave	Brookline	MA	United States of America
1904	www.newcollege.edu	New College of California	4154373400	777 Valencia St.	San Francisco	CA	United States of America
1905	www.newhaven.edu	University of New Haven	2039327000	300 Boston Post Road	West Haven	CT	United States of America
1906	www.newhope.edu	New Hope Christian College	5414851780	2155 Bailey Hill Rd	Eugene	OR	United States of America
1907	www.newmanu.edu	Newman University	3169424291	3100 McCormick Ave	Wichita	KS	United States of America
1908	www.newpaltz.edu	SUNY College at New Paltz	8452572121	1 Hawk Drive	New Paltz	NY	United States of America
1909	www.newschool.edu	The New School	2122295600	66 W 12th Street	New York	NY	United States of America
1910	www.newschoolarch.edu	NewSchool of Architecture and Design	6192354100	1249 F St	San Diego	CA	United States of America
1911	www.nfcc.edu	North Florida Community College	9049732288	325 NW Turner Davis Dr	Madison	FL	United States of America
1912	www.ngs.edu	National Graduate School of Quality Management	8008382580	186 Jones Road	Falmouth	MA	United States of America
1913	www.ngu.edu	North Greenville University	8649777000	7801 N. Tigerville Road	Tigerville	SC	United States of America
1914	www.nhcc.mnscu.edu	North Hennepin Community College	7634240702	7411 85th Ave N	Brooklyn Park	MN	United States of America
1915	www.nhctc.edu	New Hamsphire Community Technical College-Berlin	6035243207	2020 Riverside Road	Berlin	NH	United States of America
1916	www.nhia.edu	New Hampshire Institute of Art	6038362542	148 Concord Street	Manchester	NH	United States of America
1917	www.nhmccd.edu	Lone Star College System	8328136500	5000 Research Forest Drive	The Woodlands	TX	United States of America
1918	www.nhti.edu	New Hampshire Technical Institute	6032716484	31 College Drive	Concord	NH	United States of America
1919	www.nhu.edu	The National Hispanic University	4082546900	14271 Story Rd	San Jose	CA	United States of America
1920	www.ni.edu	Northland International University	7153246900	W10085 Pike Plains Road	Dunbar	WI	United States of America
1921	www.niacc.edu	North Iowa Area Community College	6414231264	500 College Dr	Mason City	IA	United States of America
1922	www.niagara.edu	Niagara University	7162851212		Niagara University	NY	United States of America
1923	www.niagaracc.suny.edu	Niagara County Community College	7166146222	3111 Saunders Settlement Road	Sanborn	NY	United States of America
1924	www.nic.edu	North Idaho College	2087693300	1000 W Garden Avenue	Coeur D'alene	ID	United States of America
1925	www.nicc.edu	Northeast Iowa Community College	5635623263	1625 Hwy 150	Calmar	IA	United States of America
2806	www.uh.edu	University of Houston	7137431000	4800 Calhoun Rd.	Houston	TX	United States of America
1926	www.nicholls.edu	Nicholls State University	8776424655	University Station  La Hwy 1	Thibodaux	LA	United States of America
1927	www.nicoletcollege.edu	Nicolet Area Technical College	7153654410	P.O. Box 518	Rhinelander	WI	United States of America
1928	www.niu.edu	Northern Illinois University	8008923050	1425 West Lincoln Highway	Dekalb	IL	United States of America
1929	www.njc.edu	Northeastern Junior College	9705216600	100 College Avenue	Sterling	CO	United States of America
1930	www.njcu.edu	New Jersey City University	2012002000	2039 Kennedy Blvd	Jersey City	NJ	United States of America
1931	www.njit.edu	New Jersey Institute of Technology	9735963000	University Heights	Newark	NJ	United States of America
1932	www.nku.edu	Northern Kentucky University	8595725100	University Dr	Highland Heights	KY	United States of America
1933	www.nl.edu	National Louis University	8474751100	122 S Michigan Ave	Chicago	IL	United States of America
1934	www.nlc.edu	National Labor College	3014316400	8455 Colesville Road	Silver Spring	MD	United States of America
1935	www.nmcc.edu	Northern Maine Community College	2077682700	33 Edgemont Drive	Presque Isle	ME	United States of America
1936	www.nmcnet.edu	Northern Marianas College	6702345498	As Terlaje Campus	Saipan	MP	United States of America
1937	www.nmhu.edu	New Mexico Highlands University	5054257511	University Ave	Las Vegas	NM	United States of America
1938	www.nmjc.edu	New Mexico Junior College	5053924510	5317 Lovington Hwy	Hobbs	NM	United States of America
1939	www.nmmi.edu	New Mexico Military Institute	5056226250	101 W.  College Blvd.	Roswell	NM	United States of America
1940	www.nmsu.edu	New Mexico State University	5056460111	P.O. Box 30001	Las Cruces	NM	United States of America
1941	www.nmt.edu	New Mexico Institute of Mining and Technology	8004288324	801 Leroy Place	Socorro	NM	United States of America
1942	www.nmu.edu	Northern Michigan University	9062271000	1401 Presque Isle	Marquette	MI	United States of America
1943	www.nnu.edu	Northwest Nazarene University	2084678011	623 Holly St	Nampa	ID	United States of America
1944	www.nobts.edu	New Orleans Baptist Theological Seminary	5042824455	3939 Gentilly Blvd	New Orleans	LA	United States of America
1945	www.normandale.mnscu.edu	Normandale Community College	9524878200	9700 France Ave S	Bloomington	MN	United States of America
1946	www.north-ok.edu	Northern Oklahoma College	5806286200	1220 E Grand Ave	Tonkawa	OK	United States of America
1947	www.northampton.edu	Northampton County Area Community College	6108615300	3835 Green Pond Rd	Bethlehem	PA	United States of America
1948	www.northark.edu	North Arkansas College	8703913200	1515 Pioneer Dr	Harrison	AR	United States of America
1949	www.northcentral.edu	North Central University	6123434400	910 Elliot Ave	Minneapolis	MN	United States of America
1950	www.northeastern.edu	Northeastern University	6173732000	360 Huntington Ave	Boston	MA	United States of America
1951	www.northeaststate.edu	Northeast State Technical Community College	4233233191	2425 Hwy 75	Blountville	TN	United States of America
1952	www.northern.edu	Northern State University	6056263011	1200 S Jay St	Aberdeen	SD	United States of America
1953	www.northgatech.edu	North Georgia Technical College	7067547700	1500 Highway 197 North	Clarkesville	GA	United States of America
1954	www.northgeorgia.edu	North Georgia College & State University	7068641400	82 College Circle	Dahlonega	GA	United States of America
1955	www.northlakecollege.edu	North Lake College	9722733000	5001 N MacArthur Blvd	Irving	TX	United States of America
1956	www.northland.edu	Northland College	7156821699	1411 Ellis Avenue	Ashland	WI	United States of America
1957	www.northlandcollege.edu	Northland Community and Technical College	2186810701	1101 Hwy # 1 East	Thief River Falls	MN	United States of America
1958	www.northmetrotech.edu	North Metro Technical College	7709754000	5198 Ross Rd	Acworth	GA	United States of America
1959	www.northpark.edu	North Park University	7732446200	3225 W Foster Ave	Chicago	IL	United States of America
1960	www.northseattle.edu	North Seattle Community College	2065273600	9600 College Way North	Seattle	WA	United States of America
1961	www.northshore.edu	North Shore Community College	5087624000	1 Ferncroft Rd	Danvers	MA	United States of America
1962	www.northwestchristian.edu	Northwest Christian University	5413431641	828 East 11th Avenue	Eugene	OR	United States of America
1963	www.northwestcollege.edu	Northwest College	3077546000	231 W 6th St	Powell	WY	United States of America
1964	www.northwestern.edu	Northwestern University	3124913741	633 Clark St	Evanston	IL	United States of America
1965	www.northwestms.edu	Northwest Mississippi Community College	6625623200	4975 Highway 51 North	Senatobia	MS	United States of America
1966	www.northweststate.edu	Northwest State Community College	4192675511	22600 State Route 34	Archbold	OH	United States of America
1967	www.northwestu.edu	Northwest University	4258228266	5520 108th Ave NE	Kirkland	WA	United States of America
1968	www.northwood.edu	Northwood University	9898374200	4000 Whiting Dr	Midland	MI	United States of America
1969	www.norwich.edu	Norwich University	8024852000	158 Harmon Drive	Northfield	VT	United States of America
1970	www.notredamecollege.edu	Notre Dame College	2163811680	4545 College Rd	Cleveland	OH	United States of America
1971	www.nova.edu	Nova Southeastern University	9542627300	3301 College Ave	Fort Lauderdale	FL	United States of America
1972	www.npc.edu	Northland Pioneer College	9285247600	103 N. First Ave	Holbrook	AZ	United States of America
1973	www.npcc.edu	National Park Community College	5017679314	101 College Dr	Hot Springs	AR	United States of America
1974	www.npu.edu	Northwestern Polytechnic University	5106575913	47671 Westinghouse Drive	Fremont	CA	United States of America
1975	www.nr.edu	New River Community College	5406743600	5251 College Drive	Dublin	VA	United States of America
1976	www.nsa.edu	New Saint Andrews College	2088821566	405 S. Main Street	Moscow	ID	United States of America
1977	www.nsc.nevada.edu	Nevada State College at Henderson	7029922000	1125 Nevada State Drive	Henderson	NV	United States of America
1978	www.nscc.edu	Nashville State Community College	6153533333	120 White Bridge Rd	Nashville	TN	United States of America
1979	www.nsu.edu	Norfolk State University	7578238600	700 Park Ave	Norfolk	VA	United States of America
2968	www.vassar.edu	Vassar College	8454377000	124 Raymond Ave	Poughkeepsie	NY	United States of America
1980	www.nsula.edu	Northwestern State University of Louisiana	3183576361	140 Central Avenue	Natchitoches	LA	United States of America
1981	www.nsuok.edu	Northeastern State University	9184565511	600 N Grand	Tahlequah	OK	United States of America
1982	www.ntc.edu	Northcentral Technical College	7156753331	1000 West Campus Dr	Wausau	WI	United States of America
1983	www.ntcc.edu	Northeast Texas Community College	9035721911	2886 Fm 1735	Mount Pleasant	TX	United States of America
1984	www.ntcmn.edu	Northwest Technical College	2187554270	905 Grant Avenue SE	Bemidji	MN	United States of America
1985	www.nti.edu	Northwest Technical Institute	9529440080	950 Blue Gentian Road	Eagan	MN	United States of America
1986	www.nts.edu	Nazarene Theological Seminary	8163336254	1700 E Meyer Blvd	Kansas City	MO	United States of America
1987	www.ntts.edu	National Tractor Trailer School Inc	3154512430	4650 Buckley Rd	Liverpool	NY	United States of America
1988	www.ntu.edu	National Technological University	8005829976	155 Fifth Avenue South	Minneapolis	MN	United States of America
1989	www.nu.edu	National University	8586428000	11255 North Torrey Pines Road	La Jolla	CA	United States of America
1990	www.nuhs.edu	National University of Health Sciences	6308896604	200 E Roosevelt Rd	Lombard	IL	United States of America
1991	www.nunez.edu	Nunez Community College	5046802240	3710 Paris Rd	Chalmette	LA	United States of America
1992	www.nvcc.commnet.edu	Naugatuck Valley Community College	2035758040	750 Chase Parkway	Waterbury	CT	United States of America
1993	www.nvcc.edu	Northern Virginia Community College	7033233000	4001 Wakefield Chapel Rd	Annandale	VA	United States of America
1994	www.nvgc.vt.edu	Virginia Tech University Falls Church		7054 Haycock Rd. Room 202F	Falls Church	VA	United States of America
1995	www.nwacc.edu	NorthWest Arkansas Community College	4796369222	One College Dr	Bentonville	AR	United States of America
1996	www.nwc.edu	University of Northwestern - St. Paul	6516315100	3003 Snelling Ave N	Saint Paul	MN	United States of America
1997	www.nwcc.commnet.edu	Northwestern Connecticut Community College	8607386300	Park Pl E	Winsted	CT	United States of America
1998	www.nwciowa.edu	Northwestern College	7127077000	101 Seventh St SW	Orange City	IA	United States of America
1999	www.nwhealth.edu	Northwestern Health Sciences University	6128884777	2501 W 84th St	Bloomington	MN	United States of America
2000	www.nwic.edu	Northwest Indian College	3606762772	2522 Kwina Rd	Bellingham	WA	United States of America
2001	www.nwicc.edu	Northwest Iowa Community College	7123245061	603 W Park St	Sheldon	IA	United States of America
2002	www.nwmissouri.edu	Northwest Missouri State University	6605621212	800 University Drive	Maryville	MO	United States of America
2003	www.nwosu.edu	Northwestern Oklahoma State University	5803271700	709 Oklahoma Blvd	Alva	OK	United States of America
2004	www.nws.edu	New World Symphony	3056733330	541 Lincoln Road	Miami Beach	FL	United States of America
2005	www.nwscc.edu	Northwest-Shoals Community College - Muscle Shoals	2563315200	800 George Wallace Blvd	Muscle Shoals	AL	United States of America
2006	www.nwtc.edu	Northeast Wisconsin Technical College	9204985400	2740 W Mason St	Green Bay	WI	United States of America
2007	www.nyaa.edu	New York Academy of Art	2129660300	111 Franklin St	New York	NY	United States of America
2008	www.nyack.edu	Nyack College	8453581710	1 South Boulevard	Nyack	NY	United States of America
2009	www.nycc.edu	New York Chiropractic College	3155683000	2360 State Route 89	Seneca Falls	NY	United States of America
2010	www.nycollege.edu	New York College of Health Professions	5163640808	6801 Jericho Turnpike	Syosset	NY	United States of America
2011	www.nycpm.edu	New York College of Podiatric Medicine	2124108000	1800 Park Ave	New York	NY	United States of America
2012	www.nyctcm.edu	New York College of Traditional Chinese Medicine	5167391545	155 First St	Mineola	NY	United States of America
2013	www.nyit.edu	New York Institute of Technology-Manhattan Campus	2122611500	1855 Broadway	New York	NY	United States of America
2014	www.nyls.edu	New York Law School	2124312100	57 Worth St	New York	NY	United States of America
2015	www.nymc.edu	New York Medical College	9145944000	Administration Building	Valhalla	NY	United States of America
2016	www.nysid.edu	New York School of Interior Design	2124721500	170 East 70th Street	New York	NY	United States of America
2017	www.nyts.edu	New York Theological Seminary	2128701211	475 Riverside Dr.  Ste 500	New York	NY	United States of America
2018	www.nyu.edu	New York University	2129981212	70 Washington Sq South	New York	NY	United States of America
2019	www.oak.edu	Oakland City University	8127494781	138 N Lucretia St	Oakland City	IN	United States of America
2020	www.oakhills.edu	Oak Hills Christian College	2187518670	1600 Oak Hills Rd SW	Bemidji	MN	United States of America
2021	www.oakland.edu	Oakland University	2483702100	204 Wilson Hall	Rochester	MI	United States of America
2022	www.oaklandcc.edu	Oakland Community College	2483412000	2480 Opdyke Rd	Bloomfield Hills	MI	United States of America
2023	www.oakton.edu	Oakton Community College	8476351600	1600 E Golf Rd.	Des Plaines	IL	United States of America
2024	www.oakwood.edu	Oakwood University	2567267000	7000 Adventist Blvd N.W.	Huntsville	AL	United States of America
2025	www.oberlin.edu	Oberlin College	4407758411	70 N Professor St	Oberlin	OH	United States of America
2026	www.obu.edu	Ouachita Baptist University	8702455000	410 Ouachita St	Arkadelphia	AR	United States of America
2027	www.oc.edu	Oklahoma Christian University	4054255000	P.O. Box 11000	Oklahoma City	OK	United States of America
2028	www.ocac.edu	Oregon College of Art and Craft	5032975544	8245 SW Barnes Rd	Portland	OR	United States of America
2029	www.cccd.edu	Orange Coast College	7144325072	2701 Fairview Road	Costa Mesa	CA	United States of America
2030	www.occ.edu	Ozark Christian College	4176242518	1111 N Main St	Joplin	MO	United States of America
2031	www.occc.edu	Oklahoma City Community College	4056821611	7777 S May Ave	Oklahoma City	OK	United States of America
2032	www.ocean.edu	Ocean County College	7322550326	College Drive	Toms River	NJ	United States of America
2033	www.ocm.edu	Ohio College of Massotherapy Inc	3306651084	225 Heritage Woods Dr	Akron	OH	United States of America
2034	www.ocom.edu	Oregon College of Oriental Medicine	5032533443	10525 SE Cherry Blossom Dr	Portland	OR	United States of America
2035	www.octech.edu	Orangeburg Calhoun Technical College	8035360311	3250 Saint Matthews Rd	Orangeburg	SC	United States of America
2036	www.odessa.edu	Odessa College	4323356400	201 W University	Odessa	TX	United States of America
2037	www.odu.edu	Old Dominion University	7576833000	5115 Hampton Blvd	Norfolk	VA	United States of America
2038	www.ogeecheetech.edu	Ogeechee Technical College	9126815500	One Joe Kennedy Blvd	Statesboro	GA	United States of America
2039	www.oglethorpe.edu	Oglethorpe University	4042611441	4484 Peachtree Rd NE	Atlanta	GA	United States of America
2040	www.ohio.edu	Ohio University - Main Campus	7405931000		Athens	OH	United States of America
2041	www.ohiochristian.edu	Ohio Christian University	7404748896	1476 Lancaster Pike	Circleville	OH	United States of America
2042	www.ohiodominican.edu	Ohio Dominican University	6142532741	1216 Sunbury Rd	Columbus	OH	United States of America
2043	www.ohlone.edu	Ohlone College	5106596000	43600 Mission Blvd	Fremont	CA	United States of America
2044	www.ohsu.edu	Oregon Health & Science University	5034947800	3181 SW Sam Jackson Park Rd	Portland	OR	United States of America
2045	www.oit.edu	Oregon Institute of Technology	5418851900	3201 Campus Drive	Klamath Falls	OR	United States of America
2046	www.okbu.edu	Oklahoma Baptist University	4052752850	500 W University	Shawnee	OK	United States of America
2047	www.okcu.edu	Oklahoma City University	4055215000	2501 N Blackwelder	Oklahoma City	OK	United States of America
2048	www.okwu.edu	Oklahoma Wesleyan University	9183336151	2201 Silver Lake Rd	Bartlesville	OK	United States of America
2049	www.olc.edu	Oglala Lakota College	6054556000	490 Piya Wiconi Road	Kyle	SD	United States of America
2050	www.olemiss.edu	University of Mississippi Main Campus	6629157211		University	MS	United States of America
2051	www.olhcc.edu	Our Lady of Holy Cross College	5043947744	4123 Woodland Dr	New Orleans	LA	United States of America
2052	www.olin.edu	Franklin W. Olin College of Engineering	7812922300	Olin Way	Needham	MA	United States of America
2053	www.olivet.edu	Olivet Nazarene University	8159395011	One University Avenue	Bourbonnais	IL	United States of America
2054	www.olivetcollege.edu	Olivet College	2697497000	320 South Main Street	Olivet	MI	United States of America
2055	www.olivetuniversity.edu	Olivet University	4153710002	250 4th St	San Francisco	CA	United States of America
2056	www.ollusa.edu	Our Lady of the Lake University	2104346711	411 SW 24th St	San Antonio	TX	United States of America
2057	www.ololcollege.edu	Our Lady of the Lake College	2257681700	5414 Brittany Drive	Baton Rouge	LA	United States of America
2058	www.olympic.edu	Olympic College	3607926050	1600 Chester Avenue	Bremerton	WA	United States of America
2059	www.omorecollege.edu	O'More College of Design	6157944254	423 S Margin St	Franklin	TN	United States of America
2060	www.oneonta.edu	SUNY College at Oneonta	6074363500	Ravine Parkway	Oneonta	NY	United States of America
2061	www.onu.edu	Ohio Northern University	4197722000	525 Main St	Ada	OH	United States of America
2062	www.opsu.edu	Oklahoma Panhandle State University	5803492611	323 Eagle Ave	Goodwell	OK	United States of America
2063	www.orleanstech.edu	Orleans Technical Institute	2157284400	2770 Red Lion Road	Philadelphia	PA	United States of America
2064	www.oseda.missouri.edu/	Nichols Career Center	5736593100	605 Union Street	Jefferson City	MO	United States of America
2065	www.ost.edu	Oblate School of Theology	2103411366	285 Oblate Dr	San Antonio	TX	United States of America
2066	www.osu.edu	Ohio State University	6142926446	190 N. Oval Mall	Columbus	OH	United States of America
2067	www.osuit.edu	Oklahoma State University Institute of Technology - Okmulgee	9182934678	1801 E 4th St	Okmulgee	OK	United States of America
2068	www.osuokc.edu	Oklahoma State University - Oklahoma City	4059474421	900 N Portland	Oklahoma City	OK	United States of America
2069	www.oswego.edu	SUNY College at Oswego	3153122500	7060 State Route 104	Oswego	NY	United States of America
2070	www.otc.edu	Ozarks Technical Community College	4178957000	1001 E. Chestnut Expressway	Springfield	MO	United States of America
2071	www.otcweb.edu	Ouachita Technical College	5013375000	One College Cir	Malvern	AR	United States of America
2072	www.oti-okc.edu	Brookline College - Oklahoma City	4058429400	9801 Broadway Extension	Oklahoma City	OK	United States of America
2073	www.otis.edu	Otis College of Art and Design	8005276847	9045 Lincoln Blvd	Los Angeles	CA	United States of America
2074	www.ottawa.edu	Ottawa University	7852425200	1001 South Cedar	Ottawa	KS	United States of America
2075	www.otterbein.edu	Otterbein University	6148903000	One Otterbein College	Westerville	OH	United States of America
2076	www.ovc.edu	Ohio Valley University	3048656000	#1 Campus View Drive	Vienna	WV	United States of America
2077	www.owc.edu	Okaloosa-Walton College	8506785111	100 College Blvd	Niceville	FL	United States of America
2078	www.owens.edu	Owens Community College	5676617000	30335 Oregon Rd	Perrysburg	OH	United States of America
2079	www.owensboro.kctcs.edu	Owensboro Community and Technical College	2706864400	4800 New Hartford Rd	Owensboro	KY	United States of America
2080	www.owu.edu	Ohio Wesleyan University	7403682000	61 S Sandusky Street	Delaware	OH	United States of America
2081	www.oxnardcollege.edu	Oxnard College	8059865800	4000 S Rose Ave	Oxnard	CA	United States of America
2082	www.oxy.edu	Occidental College	3232592500	1600 Campus Rd	Los Angeles	CA	United States of America
2083	www.ozarka.edu	Ozarka College	8703687371	218 College Dr	Melbourne	AR	United States of America
2084	www.ozarks.edu	University of the Ozarks	4799791000	415 N College Ave	Clarksville	AR	United States of America
2085	www.pa.lamar.edu	Lamar State College - Port Arthur	4099846342	1500 Proctor St	Port Arthur	TX	United States of America
2086	www.pace.edu	Pace University - New York	2123461200	1 Pace Plaza	New York	NY	United States of America
2087	www.pacific.edu	University of the Pacific	2099462011	3601 Pacific Ave	Stockton	CA	United States of America
2088	www.pacifica.edu	Pacifica Graduate Institute	8059693626	249 Lambert Rd	Carpinteria	CA	United States of America
2089	www.PacificCollege.edu	Pacific College of Oriental Medicine	8007290941	7445 Mission Valley Rd Ste 105	San Diego	CA	United States of America
2090	www.pacificcollege.edu	Pacific College of Oriental Medicine - New York	8007293468	915 Broadway 3rd Fl	New York	NY	United States of America
2091	www.pacificoaks.edu	Pacific Oaks College	6263971300	5 Westmoreland Pl	Pasadena	CA	United States of America
2092	www.pacificu.edu	Pacific University	5033521111	2043 College Way	Forest Grove	OR	United States of America
2093	www.paducahtech.edu	Daymar College - Paducah	2704449676	509 South 30th Street	Paducah	KY	United States of America
2094	www.pagunsmith.edu	Pennsylvania Gunsmith School	4127661812	812 Ohio River Blvd	Pittsburgh	PA	United States of America
2095	www.paiercollegeofart.edu	Paier College of Art Inc	2032873031	20 Gorham Ave	Hamden	CT	United States of America
2096	www.paine.edu	Paine College	7068218200	1235 15th St	Augusta	GA	United States of America
2097	www.palau.edu	Palau Community College	6804882471	Medalaii	Koror	PW	United States of America
2098	www.palmer.edu	Palmer College of Chiropractic-West	4089446000	90 E Tasman Dr	San Jose	CA	United States of America
2099	www.paloaltou.edu	Palo Alto University	8008186136	1791 Arastadero Road	Palo Alto	CA	United States of America
2100	www.paloverde.edu	Palo Verde College	7609215500	One College Drive	Blythe	CA	United States of America
2101	www.pamlicocc.edu	Pamlico Community College	2522491851	5049 Hwy 306 South	Grantsboro	NC	United States of America
2102	www.panola.edu	Panola College	9036932000	1109 W Panola St	Carthage	TX	United States of America
2103	www.park.edu	Park University	8167412000	8700 NW River Park Dr	Parkville	MO	United States of America
2104	www.parkercc.edu	Parker University	9724386932	2500 Walnut Hill Lane	Dallas	TX	United States of America
2105	www.parkland.edu	Parkland College	2173512200	2400 W Bradley Ave	Champaign	IL	United States of America
2106	www.parsons.newschool.edu	Parsons the New School for Design	2122298950	66 Fifth Avenue	New York	NY	United States of America
2107	www.pasadena.edu	Pasadena City College	6265857123	1570 E Colorado Blvd	Pasadena	CA	United States of America
2108	www.passhe.edu	Pennsylvania State System of Higher Education-Central Office	7177204000	2986 N 2nd St Dixon Univ Ctr	Harrisburg	PA	United States of America
2109	www.patten.edu	Patten University	5102618500	2433 Coolidge Ave	Oakland	CA	United States of America
2110	www.paulsmiths.edu	Paul Smiths College of Arts and Science	5183276000	PO Box 265	Paul Smiths	NY	United States of America
2111	www.pba.edu	Palm Beach Atlantic University - West Palm Beach	5618032000	901 S. Flagler Drive	West Palm Beach	FL	United States of America
2112	www.pbc.edu	Piedmont Baptist College and Graduate School	3367258344	420 S. Broad Street	Winston Salem	NC	United States of America
2113	www.pbcc.edu	Palm Beach State College	5619677222	4200 Congress Ave	Lake Worth	FL	United States of America
2114	www.pbu.edu	Cairn University	2157525800	200 Manor Ave	Langhorne	PA	United States of America
2115	www.pc.ctc.edu	Peninsula College	3604529277	1502 E Lauridsen Blvd	Port Angeles	WA	United States of America
2116	www.pc.edu	University of Pikeville	6062185250	147 Sycamore Street	Pikeville	KY	United States of America
2117	www.pcad.edu	Pennsylvania College of Art and Design	7173967833	204 N Prince St	Lancaster	PA	United States of America
2118	www.pcc.edu	Portland Community College	5032446111	12000 SW 49th Avenue	Portland	OR	United States of America
2119	www.pccc.edu	Passaic County Community College	9736846800	One College Blvd	Paterson	NJ	United States of America
2120	www.pccua.edu	Phillips Community College of the University of Arkansas	8703386474	1000 Campus Dr	Helena	AR	United States of America
2121	www.pct.edu	Pennsylvania College of Technology	5703263761	One College Ave	Williamsport	PA	United States of America
2122	www.pdc.edu	Paul D Camp Community College	7575696700	100 N College Dr	Franklin	VA	United States of America
2123	www.pdx.edu	Portland State University	5037254433	724 SW Harrison	Portland	OR	United States of America
2124	www.peace.edu	William Peace University	9195082000	15 E Peace St	Raleigh	NC	United States of America
2125	www.peirce.edu	Peirce College	8776709190	1420 Pine Street	Philadelphia	PA	United States of America
2126	www.pennfoster.edu	Penn Foster Career School	5703427701	925 Oak Street	Scranton	PA	United States of America
2127	www.pennfostercollege.edu	Penn Foster College	4809476644	14300 N. Northsight Boulevard Suite 120	Scottsdale	AZ	United States of America
2128	www.pepperdine.edu	Pepperdine University	3105064000	24255 Pacific Coast Hwy	Malibu	CA	United States of America
2129	www.peralta.edu	College of Alameda	5107482299	555 Ralph Appezzato Memorial Parkway	Alameda	CA	United States of America
2130	www.perrytech.edu	Perry Technical Institute	5094530374	2011 W Washington Ave.	Yakima	WA	United States of America
2131	www.peru.edu	Peru State College	4028723815	600 Hoyt Street	Peru	NE	United States of America
2132	www.pfeiffer.edu	Pfeiffer University	7044631360	48380 US Highway 52N	Misenheimer	NC	United States of America
2133	www.pgcc.edu	Prince George's Community College	3013366000	301 Largo Road	Largo	MD	United States of America
2134	www.ph.vccs.edu	Patrick Henry Community College	2766560311	645 Patriot Avenue	Martinsville	VA	United States of America
2135	www.phc.edu	Patrick Henry College	5403381776	One Patrick Henry Circle	Purcellville	VA	United States of America
2136	www.phcc.edu	Pasco-Hernando State College	7278472727	10230 Ridge Road	New Port Richey	FL	United States of America
2137	www.philander.edu	Philander Smith College	5013759845	One Trudie Kibbe Reed Drive	Little Rock	AR	United States of America
2138	www.philau.edu	Philadelphia University	2159512700	School House Lane and Henry Avenue	Philadelphia	PA	United States of America
2139	www.phoenix.edu	University of Phoenix	4808047600	1625 Fountainhead Parkway	Tempe	AZ	United States of America
2140	www.pia.edu	Pittsburgh Institute of Aeronautics	4123462100	5 Allegheny County Airport	West Mifflin	PA	United States of America
2141	www.piaschools.edu	Pacific International Academy		17600 Pacific Highway 43	Marylhurst	OR	United States of America
2142	www.pibc.edu	Pacific Islands University	6717341812	172 Kinney's Road	Mangilao	GU	United States of America
2143	www.pic.edu	Palomar Institute of Cosmetology	7607447900	355 Via Vera Cruz Ste 3	San Marcos	CA	United States of America
2144	www.piedmont.edu	Piedmont College	7067783000	165 Central Ave	Demorest	GA	United States of America
2145	www.piedmontcc.edu	Piedmont Community College	3365991181	1715 College Dr	Roxboro	NC	United States of America
2146	www.pierce.ctc.edu	Pierce College at Puyallup	2538408400	1601 39th Ave SE	Puyallup	WA	United States of America
2147	www.piercelaw.edu	Franklin Pierce Law Center	6032281541	Two White St	Concord	NH	United States of America
2148	www.pierpont.edu	Pierpont Community and Technical College	3043674692	1201 Locust Ave	Fairmont	WV	United States of America
2149	www.pillsbury.edu	Pillsbury Baptist Bible College	5074512710	315 S Grove	Owatonna	MN	United States of America
2150	www.pima.edu	Pima Community College	5202064500	2202 W Anklam Rd	Tucson	AZ	United States of America
2151	www.pims.edu	Pittsburgh Institute of Mortuary Science Inc	4123628500	5808 Baum Blvd	Pittsburgh	PA	United States of America
2152	www.pinetech.edu	Pine Technical College	3206295100	900 4th St. SE	Pine City	MN	United States of America
2153	www.pit.edu	Pennsylvania Institute of Technology	6105657900	800 Manchester Ave	Media	PA	United States of America
2154	www.pitc.edu	PITC Institute	2155765650	137 S Easton Rd	Glenside	PA	United States of America
2155	www.pitt.edu	University of Pittsburgh - Main Campus	4126244141	4200 Fifth Ave	Pittsburgh	PA	United States of America
2156	www.pittcc.edu	Pitt Community College	2523214200	1986 Pitt Tech Road	Winterville	NC	United States of America
2157	www.pittstate.edu	Pittsburg State University	6202317000	1701 S Broadway	Pittsburg	KS	United States of America
2158	www.pitzer.edu	Pitzer College	9096218243	1050 North Mills Avenue	Claremont	CA	United States of America
2159	www.pjc.edu	Pensacola State College	8504841000	1000 College Blvd	Pensacola	FL	United States of America
2160	www.platt.edu	Platt College-San Diego	6192650107	6250 El Cajon Blvd	San Diego	CA	United States of America
2161	www.plattcollege.edu	Platt College-Newport Beach	9498514991	7755 Center Ave	Huntington Beach	CA	United States of America
2162	www.plattcolorado.edu	Platt College	3033695151	3100 S Parker Rd	Aurora	CO	United States of America
2163	www.plattsburgh.edu	SUNY College at Plattsburgh	5185642000	101 Broad Street	Plattsburgh	NY	United States of America
2164	www.plazacollege.edu	Plaza College	7187791430	118-35 Queens Boulevard	Forest Hills	NY	United States of America
2165	www.plu.edu	Pacific Lutheran University	2535316900	1010 122nd St So	Tacoma	WA	United States of America
2166	www.plymouth.edu	Plymouth State University	6035355000	17 High Street	Plymouth	NH	United States of America
2167	www.pmc.edu	Pine Manor College	6177317000	400 Heath St	Chestnut Hill	MA	United States of America
2168	www.pmi.edu	Pima Medical Institute - Albuquerque	5058811314	8601 Golf Course Road NW	Albuquerque	NM	United States of America
2169	www.pnc.edu	Purdue University - North Central	2197855200	1401 S US Hwy 421	Westville	IN	United States of America
2170	www.pnca.edu	Pacific Northwest College of Art	5032264391	1241 NW Johnson	Portland	OR	United States of America
2171	www.pointloma.edu	Point Loma Nazarene University	6198492200	3900 Lomaland Dr	San Diego	CA	United States of America
2172	www.pointpark.edu	Point Park University	4123914100	201 Wood St	Pittsburgh	PA	United States of America
2173	www.polaris.edu	Polaris Career Center	4408917750	7285 Old Oak Blvd	Middleburg Heights	OH	United States of America
2174	www.polk.edu	Polk State College	8632971000	999 Avenue H NE	Winter Haven	FL	United States of America
2175	www.poly.edu	Polytechnic Institute of New York University	7182603100	Six Metrotech Ctr	Brooklyn	NY	United States of America
2176	www.polylanguages.edu	POLY Languages Institute		2900 E. Colorado Blvd.	Pasadena	CA	United States of America
2177	www.post.edu	Post University	2035964500	800 Country Club Rd	Waterbury	CT	United States of America
2178	www.potsdam.edu	SUNY - Potsdam	3152672000	44 Pierrepont Ave	Potsdam	NY	United States of America
2179	www.ppcc.edu	Pikes Peak Community College	7195767711	5675 S Academy Blvd	Colorado Springs	CO	United States of America
2180	www.pqc.edu	Paul Quinn College	2143761000	3837 Simpson Stuart Rd	Dallas	TX	United States of America
2181	www.prairiestate.edu	Prairie State College	7087093500	202 South Halsted Street	Chicago Heights	IL	United States of America
2182	www.pratt.edu	Pratt Institute-Main	7186363600	200 Willoughby Ave	Brooklyn	NY	United States of America
2183	www.prattcc.edu	Pratt Community College	6206725641	348 NE Sr 61	Pratt	KS	United States of America
2184	www.prbc-hawaii.edu	Pacific Rim Bible College	8088531040	290 Sand Island Access Road	Honolulu	HI	United States of America
2185	www.prcc.edu	Pearl River Community College	6014031000	101 Highway 11N	Poplarville	MS	United States of America
2186	www.premierecollege.edu	Premiere Career College	6268142080	12901 Ramona Blvd	Irwindale	CA	United States of America
2187	www.presby.edu	Presbyterian College	8648332820	503 S Broad St	Clinton	SC	United States of America
2188	www.prescott.edu	Prescott College	9287782090	220 Grove Ave	Prescott	AZ	United States of America
2189	www.presentation.edu	Presentation College	6052251634	1500 N Main	Aberdeen	SD	United States of America
2190	www.prgs.edu	Pardee Rand Graduate School of Policy Studies	3103930411	1776 Main St	Santa Monica	CA	United States of America
2191	www.prin.edu	Principia College	6183742131	1 Maybeck Place	Elsah	IL	United States of America
2192	www.princeton.edu	Princeton University	6092583000	One Nassau Hall	Princeton	NJ	United States of America
2193	www.providence.edu	Providence College	4018651000	River Ave and Eaton St	Providence	RI	United States of America
2194	www.pscc.edu	Puget Sound Christian College	4257758686	2610 Wetmore Ave	Everett	WA	United States of America
2195	www.psr.edu	Pacific School of Religion	5108480528	1798 Scenic Ave	Berkeley	CA	United States of America
2196	www.pstcc.edu	Pellissippi State Community College	8656946400	10915 Hardin Valley Road	Knoxville	TN	United States of America
2197	www.psu.edu	Pennsylvania State University - Penn State Main Campus	8148654700	201 Old Main	University Park	PA	United States of America
2198	www.ptc.edu	Piedmont Technical College	8649418324	620 North Emerald Road	Greenwood	SC	United States of America
2199	www.pts.edu	Pittsburgh Theological Seminary	4123625610	616 N Highland Ave	Pittsburgh	PA	United States of America
2200	www.ptsem.edu	Princeton Theological Seminary	6099218300	64 Mercer St	Princeton	NJ	United States of America
2201	www.ptseminary.edu	Pentecostal Theological Seminary	4234781131	900 Walker St NE	Cleveland	TN	United States of America
2202	www.ptstulsa.edu	Phillips Theological Seminary	9186108303	901 N Mingo Rd	Tulsa	OK	United States of America
2203	www.puc.edu	Pacific Union College	7079656311	One Angwin Ave	Angwin	CA	United States of America
2204	www.pueblocc.edu	Pueblo Community College	7195493200	900 West Orman Avenue	Pueblo	CO	United States of America
2205	www.pulaskitech.edu	Pulaski Technical College	5018122200	3000 West Scenic Drive	North Little Rock	AR	United States of America
2206	www.purchase.edu	SUNY College at Purchase	9142516000	735 Anderson Hill Road	Purchase	NY	United States of America
2207	www.purdue.edu	Purdue University	7654944600	Hovde Hall of Administration	West Lafayette	IN	United States of America
2208	www.pvamu.edu	Prairie View A & M University	9368573111	P.O. Box 519	Prairie View	TX	United States of America
2209	www.pvcc.edu	Piedmont Virginia Community College	4349773900	501 College Drive	Charlottesville	VA	United States of America
2210	www.pwscc.edu	Prince William Sound Community College	9078341632	303 Lowe Street	Valdez	AK	United States of America
2211	www.qc.cuny.edu	Queens College of the City University of New York	7189975000	65 30 Kissena Blvd	Flushing	NY	United States of America
2212	www.qcc.cuny.edu	Queensborough Community College of the City University of New York	7186316262	222-05 56th Ave	Bayside	NY	United States of America
2213	www.qcc.mass.edu	Quinsigamond Community College	5088532300	670 W Boylston St	Worcester	MA	United States of America
2214	www.queens.edu	Queens University of Charlotte	7043372200	1900 Selwyn Ave	Charlotte	NC	United States of America
2215	www.quest.edu	Quest Career College	4408865544	6248 Pearl Rd	Parma Heights	OH	United States of America
2216	www.quincy.edu	Quincy University	2172228020	1800 College Ave	Quincy	IL	United States of America
2217	www.quincycollege.edu	Quincy College	8006981700	1250 Hancock Street	Quincy	MA	United States of America
2218	www.quinnipiac.edu	Quinnipiac University	2035828200	275 Mount Carmel Ave	Hamden	CT	United States of America
2219	www.qvctc.commnet.edu	Quinebaug Valley Community College	8607741164	742 Upper Maple St	Danielson	CT	United States of America
2220	www.racc.edu	Reading Area Community College	6103724721	10 S Second St	Reading	PA	United States of America
2221	www.radford.edu	Radford University	5408315000	East Main Street	Radford	VA	United States of America
2222	www.ramapo.edu	Ramapo College of New Jersey	2016847500	505 Ramapo Valley Rd	Mahwah	NJ	United States of America
2223	www.randolph.edu	Randolph Community College	3366330200	629 Industrial Pk Ave	Asheboro	NC	United States of America
2224	www.randolphcollege.edu	Randolph-Macon Woman's College	4349478000	2500 Rivermont Ave	Lynchburg	VA	United States of America
2225	www.rangercollege.edu	Ranger College	2546473234	1100 College Circle	Ranger	TX	United States of America
2226	www.ranken.edu	Ranken Technical College	3143710236	4431 Finney Ave	Saint Louis	MO	United States of America
2227	www.rappahannock.edu	Rappahannock Community College	8047586700	12745 College Drive	Glenns	VA	United States of America
2228	www.raritanval.edu	Raritan Valley Community College	9085261200	111 Lamington Road	North Branch	NJ	United States of America
2229	www.rbc.edu	Richard Bland College	8048626100	11301 Johnson Rd	Petersburg	VA	United States of America
2230	www.rc.edu	Rochester College	2482182000	800 W Avon Rd	Rochester Hills	MI	United States of America
2231	www.rcc.edu	Norco College		2001 Third Street	Norco	CA	United States of America
2232	www.rcc.edu	Riverside City College	9512228000	4800 Magnolia Ave	Riverside	CA	United States of America
2233	www.rctc.edu	Rochester Community and Technical College	5072857210	851 30th Ave SE	Rochester	MN	United States of America
2234	www.redlands.edu	University of Redlands	9097932121	1200 E. Colton Ave	Redlands	CA	United States of America
2235	www.redlandscc.edu	Redlands Community College	4052622552	1300 S Country Club Rd	El Reno	OK	United States of America
2236	www.redwoods.edu	College of the Redwoods	7074764100	7351 Tompkins Hill Rd	Eureka	CA	United States of America
2237	www.reed.edu	Reed College	5037711112	3203 SE Woodstock Boulevard	Portland	OR	United States of America
2238	www.reedleycollege.edu	Reedley College	5596383641	995 N Reed Ave	Reedley	CA	United States of America
2239	www.regent.edu	Regent University	7572264127	1000 Regent University Dr	Virginia Beach	VA	United States of America
2240	www.region2.ltc.edu	Capital Area Technical College	2253599204	3250 North Acadian Thruway East	Baton Rouge	LA	United States of America
2241	www.region6.ltc.edu	Central Louisiana Technical Community College - Alexandria	3184875439	4311 South MacArthur Drive	Alexandria	LA	United States of America
2242	www.regis.edu	Regis University	3034584100	3333 Regis Blvd	Denver	CO	United States of America
2243	www.regiscollege.edu	Regis College	7817687000	235 Wellesley St	Weston	MA	United States of America
2244	www.reinhardt.edu	Reinhardt University	7707205600	7300 Reinhardt College Circle	Waleska	GA	United States of America
2245	www.remingtoncollege.edu	Remington College - Tempe Campus	4808341000	875 W Elliot Rd #126	Tempe	AZ	United States of America
2246	www.remingtoncollege.edu	Remington College - San Diego	6196868600	123 Camino de La Reina Ste 100 N	San Diego	CA	United States of America
2247	www.researchcollege.edu	Research College of Nursing	8162764700	2525 E. Meyer Boulevard	Kansas City	MO	United States of America
2248	www.reynolds.edu	J Sargeant Reynolds Community College	8043713000	1651 E Parham Road	Richmond	VA	United States of America
2249	www.rhodes.edu	Rhodes College	9018433000	2000 North Parkway	Memphis	TN	United States of America
2250	www.RhodesState.edu	James A Rhodes State College	4192211112	4240 Campus Dr	Lima	OH	United States of America
2251	www.ric.edu	Rhode Island College	4014568000	600 Mount Pleasant Ave	Providence	RI	United States of America
2252	www.rice.edu	Rice University	7133480000	6100 S Main	Houston	TX	United States of America
2253	www.richland.edu	Richland Community College	2178757200	One College Pk	Decatur	IL	United States of America
2254	www.richmond.edu	University of Richmond	8042898000	28 Westhampton Way	Richmond	VA	United States of America
2255	www.richmondcc.edu	Richmond Community College	9105827000	1042 W Hamlet Ave	Hamlet	NC	United States of America
2256	www.rider.edu	Rider University	6098965000	2083 Lawrenceville Road	Lawrenceville	NJ	United States of America
2257	www.ridgewater.edu	Ridgewater College	8007221151	2101 15th Ave NW	Willmar	MN	United States of America
2258	www.ridley.edu	Ridley-Lowell Business and Technical Institute - New London	8604437441	470 Bank St	New London	CT	United States of America
2259	www.Ringling.edu	Ringling College of Art and Design	8002557695	2700 North Tamiami Tr	Sarasota	FL	United States of America
2260	www.rio.edu	University of Rio Grande	7402457206	218 N College Ave	Rio Grande	OH	United States of America
2261	www.riogrande.edu	Rio Grande Bible Institute	9563808100	4300 S US Highway 281	Edinburg	TX	United States of America
2262	www.riohondo.edu	Rio Hondo College	5626920921	3600 Workman Mill Rd	Whittier	CA	United States of America
2263	www.ripon.edu	Ripon College	9207488115	300 Seward St	Ripon	WI	United States of America
2264	www.risd.edu	Rhode Island School of Design	4014546100	2 College St	Providence	RI	United States of America
2265	www.rit.edu	Rochester Institute of Technology	5854752411	1 Lomb Memorial Dr	Rochester	NY	United States of America
2266	www.riverland.edu	Riverland Community College	5074330600	1900 8th Ave NW	Austin	MN	United States of America
2267	www.riverside.edu	Riverside School of Health Careers	7572402200	316 Main Street	Newport News	VA	United States of America
2268	www.rivier.edu	Rivier University	6038881311	420 South Main St	Nashua	NH	United States of America
2269	rlc.dcccd.edu	Richland College	9722386106	12800 Abrams Rd	Dallas	TX	United States of America
2270	www.rmc.edu	Randolph-Macon College	8047527200	204 Henry Street	Ashland	VA	United States of America
2271	www.rmcad.edu	Rocky Mountain College of Art and Design	3037536046	1600 Pierce St	Denver	CO	United States of America
2272	www.rmcc.edu	Rich Mountain Community College	4793947622	1100 College Dr	Mena	AR	United States of America
2273	www.rmu.edu	Robert Morris University	4122628200	6001 University Boulevard	Moon Township	PA	United States of America
2274	www.rmuohp.edu	Rocky Mountain University of Health Professions		1662 West 820 North	Provo	UT	United States of America
2275	www.roanestate.edu	Roane State Community College	4233543000	276 Patton Lane	Harriman	TN	United States of America
2276	www.roanoke.edu	Roanoke College	5403752500	221 College Ln	Salem	VA	United States of America
2277	www.roanokechowen.edu	Roanoke-Chowan Community College	2528621200	109 Community College Rd	Ahoskie	NC	United States of America
2278	www.robertmorris.edu	Robert Morris University - Illinois	3129356800	401 S State Street	Chicago	IL	United States of America
2279	www.roberts.edu	Roberts Wesleyan College	5855946000	2301 Westside Drive	Rochester	NY	United States of America
2280	www.robeson.edu	Robeson Community College	9106185680	5160 Fayetteville Rd	Lumberton	NC	United States of America
2281	www.rochester.edu	University of Rochester	5852752121	Wallis Hall	Rochester	NY	United States of America
2282	www.rockefeller.edu	Rockefeller University	2123278000	1230 York Ave Box 177	New York	NY	United States of America
2283	www.rockford.edu	Rockford University	8152264000	5050 E State St	Rockford	IL	United States of America
2284	www.rockhurst.edu	Rockhurst University	8165014000	1100 Rockhurst Rd	Kansas City	MO	United States of America
2285	www.rockies.edu	University of the Rockies	7194420505	555 E Pikes Peak Ave #108	Colorado Springs	CO	United States of America
2286	www.rockinghamcc.edu	Rockingham Community College	3363424261	Hwy 65w County Home Rd	Wentworth	NC	United States of America
2287	www.rockvalleycollege.edu	Rock Valley College	8159217821	3301 N Mulford Rd	Rockford	IL	United States of America
2288	www.rocky.edu	Rocky Mountain College	4066571000	1511 Poly Drive	Billings	MT	United States of America
2289	www.roguecc.edu	Rogue Community College	5419567500	3345 Redwood Highway	Grants Pass	OR	United States of America
2290	www.rollins.edu	Rollins College	4076462000	1000 Holt Ave	Winter Park	FL	United States of America
2291	www.roosevelt.edu	Roosevelt University	3123413500	430 S Michigan Ave	Chicago	IL	United States of America
2292	www.rosalindfranklin.edu	Rosalind Franklin University of Medicine and Science	8475783000	3333 Green Bay Rd	North Chicago	IL	United States of America
2293	www.rose-hulman.edu	Rose-Hulman Institute of Technology	8128771511	5500 Wabash Avenue	Terre Haute	IN	United States of America
2294	www.rose.edu	Rose State College	4057337311	6420 S E 15th	Midwest City	OK	United States of America
2295	www.rosedale.edu	Rosedale Bible College	7408571311	2270 Rosedale Rd	Irwin	OH	United States of America
2296	www.rosemont.edu	Rosemont College	6105270200	1400 Montgomery Ave	Rosemont	PA	United States of America
2297	www.roswell.enmu.edu	Eastern New Mexico University - Roswell	5056247000	52 University Blvd.	Roswell	NM	United States of America
2298	www.rowan.edu	Rowan University	8562564000	201 Mullica Hill Road	Glassboro	NJ	United States of America
2299	www.rowancabarrus.edu	Rowan-Cabarrus Community College	7046370760	1333 Jake Alexander Blvd	Salisbury	NC	United States of America
2300	www.rpcc.edu	River Parishes Community College	2256758270	7384 John Leblanc Blvd	Sorrento	LA	United States of America
2301	www.rpi.edu	Rensselaer Polytechnic Institute	5182766000	110 8th St	Troy	NY	United States of America
2302	www.rpts.edu	Reformed Presbyterian Theological Seminary	4127318690	7418 Penn Ave	Pittsburgh	PA	United States of America
2303	www.rrc.edu	Reconstructionist Rabbinical College	2155760800	1299 Church Rd	Wyncote	PA	United States of America
2304	www.rrcc.cccoes.edu	Red Rocks Community College	3039146600	13300 W Sixth Ave	Lakewood	CO	United States of America
2305	www.rrcc.mnscu.edu	Rainy River Community College	2182857722	1501 Hwy 71	International Falls	MN	United States of America
2306	www.rsu.edu	Rogers State University	9183437777	1701 W Will Rogers Blvd	Claremore	OK	United States of America
2307	www.rtc.edu	Renton Technical College	4252352352	3000 NE Fourth Street	Renton	WA	United States of America
2308	www.rts.edu	Reformed Theological Seminary	6019231600	5422 Clinton Blvd.	Jackson	MS	United States of America
2309	www.rustcollege.edu	Rust College	6012528000	150 Rust Ave	Holly Springs	MS	United States of America
2310	www.rwc.uc.edu	University of Cincinnati Blue Ash College	5137455600	9555 Plainfield Rd	Blue Ash	OH	United States of America
2311	www.rwu.edu	Roger Williams University	4012531040	One Old Ferry Rd	Bristol	RI	United States of America
2312	www.sac.edu	Santa Ana College	7145646000	1530 W. 17th Street	Santa Ana	CA	United States of America
2313	www.sacredheart.edu	Sacred Heart University	2033717999	5151 Park Ave	Fairfield	CT	United States of America
2314	www.sagchip.edu	Saginaw Chippewa Tribal College	9897754123	2274 Enterprise Dr	Mount Pleasant	MI	United States of America
2315	www.sage.edu	The Sage Colleges	5182442000	45 Ferry St	Troy	NY	United States of America
2316	www.sagu.edu	Southwestern Assemblies of God University	8889374010	1200 Sycamore	Waxahachie	TX	United States of America
2317	www.saintjoe.edu	Saint Josephs College	2198666000	US Highway 231	Rensselaer	IN	United States of America
2318	www.saintleo.edu	Saint Leo University	3525888200	33701 State Road 52	Saint Leo	FL	United States of America
2319	www.saintmarys.edu	Saint Mary's College	5742844602	132 Le Mans Hall Indiana Rt. 933	Notre Dame	IN	United States of America
2320	www.saintmeinrad.edu	Saint Meinrad School of Theology	8123576611	200 Hill Drive	Saint Meinrad	IN	United States of America
2321	www.saintpaul.edu	Saint Paul College - A Community and Technical College	6518461600	235 Marshall Ave	Saint Paul	MN	United States of America
2322	www.saintpauls.edu	Saint Paul's College	4348483111	115 College Drive	Lawrenceville	VA	United States of America
2323	www.salem.edu	Salem College	3367212600	601 S Church St	Winston Salem	NC	United States of America
2324	www.salemcc.edu	Salem Community College	8562992100	460 Hollywood Ave	Carneys Point	NJ	United States of America
2325	www.salemstate.edu	Salem State University	9785426000	352 Lafayette St	Salem	MA	United States of America
2326	www.salemu.edu	Salem International University	3047825389	223 W Main St	Salem	WV	United States of America
2327	www.salinatech.edu	Salina Area Technical College	7853093100	2562 Centennial Road	Salina	KS	United States of America
2328	www.salisbury.edu	Salisbury University	4105436000	1101 Camden Ave	Salisbury	MD	United States of America
2329	www.salus.edu	Salus University	2157801400	8360 Old York Road	Elkins Park	PA	United States of America
2330	www.salve.edu	Salve Regina University	4018476650	100 Ochre Point Avenue	Newport	RI	United States of America
2331	www.samford.edu	Samford University	2057262011	800 Lakeshore Drive	Birmingham	AL	United States of America
2332	www.sampsoncc.edu	Sampson Community College	9105928081	1801 Sunset Avenut	Clinton	NC	United States of America
2333	www.samuelmerritt.edu	Samuel Merritt University	5108696511	370 Hawthorne Ave	Oakland	CA	United States of America
2334	www.sandburg.edu	Carl Sandburg College	3093458501	2400 Tom L. Wilson Boulevard	Galesburg	IL	United States of America
2335	www.sandhills.edu	Sandhills Community College	9106926185	3395 Airport Rd	Pinehurst	NC	United States of America
2336	www.sandiego.edu	University of San Diego	6192604600	5998 Alcala Park	San Diego	CA	United States of America
2337	www.sanjuan.edu	San Juan Adult Education	9169717421	3738 Walnut Avenue	Carmichael	CA	United States of America
2338	www.santarosa.edu	Santa Rosa Junior College	7075274011	1501 Mendocino Avenue	Santa Rosa	CA	United States of America
2339	www.sapc.edu	St. Andrews Presbyterian College	9102775000	1700 Dogwood Mile	Laurinburg	NC	United States of America
2340	www.sau.edu	Saint Ambrose University	5633336000	518 W. Locust St.	Davenport	IA	United States of America
2341	www.sautech.edu	Southern Arkansas University Tech	8705744500	P.O. Box 3499	Camden	AR	United States of America
2342	www.savannahstate.edu	Savannah State University	9123562186	3219 College Avenue	Savannah	GA	United States of America
2343	www.savannahtech.edu	Savannah Technical College	9123516362	5717 White Bluff Rd	Savannah	GA	United States of America
2344	www.saybrook.edu	Saybrook University	4154339200	747 Front Street	San Francisco	CA	United States of America
2345	www.sbc.edu	Sweet Briar College	4343816100	134 Chapel Drive	Sweet Briar	VA	United States of America
2346	www.sbcc.edu	Santa Barbara City College	8059650581	721 Cliff Dr	Santa Barbara	CA	United States of America
2347	www.sbts.edu	The Southern Baptist Theological Seminary	5028974011	2825 Lexington Rd	Louisville	KY	United States of America
2348	www.sbu.edu	St. Bonaventure University	7163752000	3261 West State Road	St. Bonaventure	NY	United States of America
2349	www.sbuniv.edu	Southwest Baptist University	8005265859	1600 University Ave	Bolivar	MO	United States of America
2350	www.sc.edu	University of South Carolina - Columbia	8037777000	Osborne Administration Building	Columbia	SC	United States of America
2351	www.sc4.edu	St Clair County Community College	8109843881	323 Erie	Port Huron	MI	United States of America
2352	www.scad.edu	Savannah College of Art and Design	9125255000	342 Bull St	Savannah	GA	United States of America
2353	www.scc.losrios.edu	Sacramento City College	9165582111	3835 Freeport Blvd	Sacramento	CA	United States of America
2354	www.scc.spokane.edu	Spokane Community College	5095337000	1810 North Greene Street	Spokane	WA	United States of America
2355	www.sccc.edu	Seward County Community College	6206241951	1801 N. Kansas Ave.	Liberal	KS	United States of America
2356	www.sccd.ctc.edu	Seattle Vocational Institute	2065874950	2120 S Jackson	Seattle	WA	United States of America
2357	www.scciowa.edu	Southeastern Community College	3197522731	1500 West Agency Road	West Burlington	IA	United States of America
2358	www.sccky.edu	Saint Catharine College	8593365082	2735 Bardstown Rd	Saint Catharine	KY	United States of America
2359	www.sccnc.edu	Southeastern Community College	9106427141	4564 Chadbourn Hwy	Whiteville	NC	United States of America
2360	www.scco.edu	Southern California College of Optometry	7144497450	2575 Yorba Linda Blvd	Fullerton	CA	United States of America
2361	www.sccollege.edu	Santiago Canyon College	7146284900	8045 E Chapman	Orange	CA	United States of America
2362	www.sccsc.edu	Spartanburg Technical College	8645913600	Business I85	Spartanburg	SC	United States of America
2363	www.schiller.edu	Schiller International University	7277365082	8560 Ulmerton Road	Largo	FL	United States of America
2364	www.schoolcraft.edu	Schoolcraft College	7344624400	18600 Haggerty Road	Livonia	MI	United States of America
2365	www.schoolofvisualarts.edu	School of Visual Arts	2125922000	209 E 23rd St	New York	NY	United States of America
2366	www.schreiner.edu	Schreiner University	8308965411	2100 Memorial Blvd	Kerrville	TX	United States of America
2367	www.sci.edu	Springfield College in Illinois	2175251420	1500 N Fifth St	Springfield	IL	United States of America
2368	www.sciarc.edu	Southern California Institute of Architecture	2136132200	960 E. 3rd Street	Los Angeles	CA	United States of America
2369	www.sckans.edu	Southwestern College	6202296000	100 College St	Winfield	KS	United States of America
2370	www.scnm.edu	Southwest College of Naturopathic Medicine & Health Sciences	4808589100	2140 E Broadway Rd	Tempe	AZ	United States of America
2371	www.sco.edu	Southern College of Optometry	9017223200	1245 Madison Ave	Memphis	TN	United States of America
2372	www.scranton.edu	University of Scranton	5709417400	800 Linden Street	Scranton	PA	United States of America
2373	www.scripps.edu	Scripps Research Institute		10550 N Torrey Pines Rd	La Jolla	CA	United States of America
2374	www.scs.edu	Saint Charles Borromeo Seminary-Overbrook	6106673394	100 East Wynnewood Road	Wynnewood	PA	United States of America
2375	www.scsu.edu	South Carolina State University	8035367000	300 College St NE	Orangeburg	SC	United States of America
2376	www.sctc.edu	Saint Cloud Technical College	3203085000	1540 Northway Drive	Saint Cloud	MN	United States of America
2377	www.sctc.mnscu.edu	South Central College	5073897200	1920 Lee Blvd	North Mankato	MN	United States of America
2378	www.sctd.edu	Sullivan College of Technology and Design	5024566509	3901 Atkinson Square Dr	Louisville	KY	United States of America
2379	www.sctoday.edu	Stautzenberger College	4198660261	1796 Indian Wood Circle	Maumee	OH	United States of America
2380	www.scu.edu	Santa Clara University	4085544000	500 El Camino Real	Santa Clara	CA	United States of America
2381	www.scuhs.edu	Southern California University of Health Sciences	5629478755	16200 E Amber Valley Dr	Whittier	CA	United States of America
2382	www.sdc.edu	Sojourner-Douglass College	4102760306	500 N Caroline St	Baltimore	MD	United States of America
2383	www.sdcity.edu	San Diego City College	6193883400	1313 Park Boulevard	San Diego	CA	United States of America
2384	www.sdsmt.edu	South Dakota School of Mines and Technology	6053942511	501 E Saint Joseph St	Rapid City	SD	United States of America
2385	www.sdsu.edu	San Diego State University	6195945000	5500 Campanile Dr	San Diego	CA	United States of America
2386	www.se-massage.edu	Southeastern College	9044489499	6700 South Point Parkway	Jacksonville	FL	United States of America
2387	www.seabury.edu	Seabury-Western Theological Seminary	8473289300	2122 Sheridan Rd	Evanston	IL	United States of America
2388	www.seark.edu	Southeast Arkansas College	8705435900	1900 Hazel	Pine Bluff	AR	United States of America
2389	www.seattleu.edu	Seattle University	2062966000	900 Broadway	Seattle	WA	United States of America
2390	www.sebc.edu	Southeastern Bible College	2059709200	2545 Valleydale Road	Birmingham	AL	United States of America
2391	www.sebts.edu	Southeastern Baptist Theological Seminary	9195563101	120 South Wingate	Wake Forest	NC	United States of America
2392	www.secc.kctcs.edu	Southeast Kentucky Community and Technical College	6065892145	700 College Rd	Cumberland	KY	United States of America
2393	www.secon.edu	St. Elizabeth College of Nursing	3157988144	2215 Genesee Street	Utica	NY	United States of America
2394	www.selu.edu	Southeastern Louisiana University	9855492000	548 Western Ave.	Hammond	LA	United States of America
2395	www.seminary.edu	Northern Baptist Theological Seminary	6306202128	660 E Butterfield Rd	Lombard	IL	United States of America
2396	www.seminolestate.edu	Seminole State College of Florida	4073284722	100 Weldon Blvd	Sanford	FL	United States of America
2397	www.ses.edu	Southern Evangelical Seminary	7048475600	3000 Tilley Morris Road	Matthews	NC	United States of America
2398	www.setonhill.edu	Seton Hill University	7248342200	Seton Hill Dr	Greensburg	PA	United States of America
2399	www.sewanee.edu	The University of the South	9315981000	735 University Avenue	Sewanee	TN	United States of America
2400	www.sf.edu	University of Saint Francis - Fort Wayne	2194343100	2701 Spring St	Fort Wayne	IN	United States of America
2401	www.sfai.edu	San Francisco Art Institute	4157717020	800 Chestnut St	San Francisco	CA	United States of America
2402	www.sfasu.edu	Stephen F Austin State University	9364682011	1936 North St	Nacogdoches	TX	United States of America
2403	www.sfbc.edu	South Florida Bible College	9544268652	747 S Federal Hwy	Deerfield Beach	FL	United States of America
2404	www.sfc.edu	St. Francis College	7185222300	180 Remsen Street	Brooklyn Heights	NY	United States of America
2405	www.sfcm.edu	San Francisco Conservatory of Music	4155648086	50 Oak Street	San Francisco	CA	United States of America
2406	www.sfcollege.edu	Santa Fe College	3523955000	3000 NW 83rd St	Gainesville	FL	United States of America
2407	www.sfmccon.edu	Saint Francis Medical Center College of Nursing	3096552086	511 NE Greenleaf St	Peoria	IL	United States of America
2408	www.sfs.edu	Saint Francis Seminary	4147476400	3257 S Lake Dr	Saint Francis	WI	United States of America
2409	www.sfseminary.edu	Sioux Falls Seminary	6053366588	2100 S. Summit Avenus	Sioux Falls	SD	United States of America
2410	www.sfsu.edu	San Francisco State University	4153382411	1600 Holloway Ave	San Francisco	CA	United States of America
2411	www.sft.edu	New York Conservatory for Dramatic Arts	8886450030	39 West 19th Street	New York	NY	United States of America
2412	www.sga.edu	South Georgia College	9123894220	100 W College Pk Dr	Douglas	GA	United States of America
2413	www.shasta.edu	Shasta Bible College & Graduate School	5302214275	2951 Goodwater Ave.	Redding	CA	United States of America
2414	www.shastacollege.edu	Shasta College	5302254600	11555 Old Oregon Trail	Redding	CA	United States of America
2415	www.shawneecc.edu	Shawnee Community College	6186343200	8364 Shawnee College Rd	Ullin	IL	United States of America
2416	www.shawuniversity.edu	Shaw University	9195468200	118 East South Street	Raleigh	NC	United States of America
2417	www.shc.edu	Spring Hill College	2513804000	4000 Dauphin St	Mobile	AL	United States of America
2418	www.sheffield.edu	New York Institute of Art and Design	2126617270	211 East 43rd Street	New York	NY	United States of America
2419	www.sheltonstate.edu	Shelton State Community College	2053912347	9500 Old Greensboro Rd	Tuscaloosa	AL	United States of America
2420	www.sheridan.edu	Northern Wyoming Community College District - Sheridan College	3076746446	3059 S Coffeen Ave	Sheridan	WY	United States of America
2421	www.sherman.edu	Sherman College of Chiropractic	8645788770	2020 Springfield Rd	Spartanburg	SC	United States of America
2422	www.shimer.edu	Shimer College	3122353500	3424 South State Street	Chicago	IL	United States of America
2423	www.ship.edu	Shippensburg University of Pennsylvania	7174777447	1871 Old Main Drive	Shippensburg	PA	United States of America
2424	www.shoreline.edu	Shoreline Community College	2065464101	16101 Greenwood Ave N	Shoreline	WA	United States of America
2425	www.shorter.edu	Shorter University	7062912121	315 Shorter Ave	Rome	GA	United States of America
2426	www.shst.edu	Sacred Heart School of Theology	4144258300	7335 S Hwy 100	Hales Corners	WI	United States of America
2427	www.shsu.edu	Sam Houston State University	9362941111	1803 Ave I	Huntsville	TX	United States of America
2428	www.shu.edu	Seton Hall University	9737619000	400 S Orange Ave	South Orange	NJ	United States of America
2429	www.sic.edu	Southeastern Illinois College	6182525400	3575 College Road	Harrisburg	IL	United States of America
2430	www.siegalcollege.edu	Siegal College of Judaic Studies	2164644050	26500 Shaker Blvd	Beachwood	OH	United States of America
2431	www.siena.edu	Siena College	5187832300	515 Loudon Rd	Loudonville	NY	United States of America
2432	www.sienaheights.edu	Siena Heights University	5172630731	E 1247 Siena Heights Dr	Adrian	MI	United States of America
2433	www.sierracollege.edu	Sierra College	9166243333	5000 Rocklin Road	Rocklin	CA	United States of America
2434	www.sierranevada.edu	Sierra Nevada College	7758311314	999 Tahoe Blvd.	Incline Village	NV	United States of America
2435	www.siliconvalley.edu	Silicon Valley College-Emeryville	5106010133	1400 65th Street	Emeryville	CA	United States of America
2436	www.simmons.edu	Simmons College	6175212000	300 the Fenway	Boston	MA	United States of America
2437	www.simmonscollegeky.edu	Simmons College of Kentucky	5027761443	1018 South 7th Street	Louisville	KY	United States of America
2438	www.simons-rock.edu	Simons Rock College of Bard	4135280771	84 Alford Rd	Great Barrington	MA	United States of America
2439	www.simpson.edu	Simpson College	5159616251	701 North C St	Indianola	IA	United States of America
2440	www.simpsonuniversity.edu	Simpson University	5302245600	2211 College View Drive	Redding	CA	United States of America
2441	www.sinclair.edu	Sinclair Community College	9375123000	444 W. Third St.	Dayton	OH	United States of America
2442	www.sintegleska.edu	Sinte Gleska University	6058565871	E. Highway 18	Mission	SD	United States of America
2443	www.siom.edu	Seattle Institute of Oriental Medicine	2065174541	444 NE Ravenna Blvd. Suite 101	Seattle	WA	United States of America
2444	www.sipi.bia.edu	Southwestern Indian Polytechnic Institute	5053462347	9169 Coors Rd NW	Albuquerque	NM	United States of America
2445	www.siskiyous.edu	College of the Siskiyous	5309385555	800 College Ave	Weed	CA	United States of America
2446	www.sit.edu	School for International Training	8022577751	Kipling Rd	Brattleboro	VT	United States of America
2447	www.sitanka.edu	SI TANKA UNIVERSITY-HURON CAMPUS	6053528721	333 9TH ST SW	HURON	SD	United States of America
2448	www.sittingbull.edu	Sitting Bull College	7018543861	1341 92nd Street	Fort Yates	ND	United States of America
2449	www.siuc.edu	Southern Illinois University Carbondale	6184532121	Anthony Hall 116	Carbondale	IL	United States of America
2450	www.siue.edu	Southern Illinois University Edwardsville	6186502475	Campus Box 1151	Edwardsville	IL	United States of America
2451	www.sj-alaska.edu	Sheldon Jackson College	9077475220	801 Lincoln Street	Sitka	AK	United States of America
2452	www.sjasc.edu	Saint Joseph Seminary College	9858672232	75376 River Road	St. Benedict	LA	United States of America
2453	www.sjbtc.edu	San Juan Basin Technical College	9705658457	33057 Highway 160	Mancos	CO	United States of America
2454	www.sjc.edu	University of Saint Joseph	8602324571	1678 Asylum Ave	West Hartford	CT	United States of America
2455	www.sjcd.edu	San Jacinto College District	2819986100	4624 Fairmont Pkwy	Pasadena	TX	United States of America
2456	www.sjcl.edu	San Joaquin College of Law	2093232100	901 Fifth St	Clovis	CA	United States of America
2457	www.sjcme.edu	Saint Joseph's College of Maine	2078926766	278 White's Bridge Road	Standish	ME	United States of America
2458	www.sjcsf.edu	St. John's College	5059846000	1160 Camino Cruz Blanca	Santa Fe	NM	United States of America
2459	www.sjfc.edu	Saint John Fisher College	5853858000	3690 East Ave	Rochester	NY	United States of America
2460	www.sjrcc.edu	St. Johns River State College	3863124200	5001 Saint Johns Ave	Palatka	FL	United States of America
2461	www.sjs.edu	Saint John's Seminary	6172542610	127 Lake St	Brighton	MA	United States of America
2462	www.sjsu.edu	San Jose State University	4089241000	1 Washington Sq	San Jose	CA	United States of America
2463	www.sju.edu	Saint Joseph's University	6106601000	5600 City Avenue	Philadelphia	PA	United States of America
2464	www.sjvc.edu	San Joaquin Valley College	5596512500	8400 W Mineral King Ave	Visalia	CA	United States of America
2465	www.skagit.edu	Skagit Valley College	3604167600	2405 E. College Way	Mount Vernon	WA	United States of America
2466	www.skc.edu	Salish Kootenai College	4062754800	52000 Highway 93	Pablo	MT	United States of America
2467	www.skidmore.edu	Skidmore College	5185805000	815 N Broadway	Saratoga Springs	NY	United States of America
2468	www.sksm.edu	Starr King School for Ministry	5108456232	2441 Le Conte Ave	Berkeley	CA	United States of America
2469	www.sl.edu	Silver Lake College	9206846691	2406 S Alverno Rd	Manitowoc	WI	United States of America
2470	www.slc.edu	Sarah Lawrence College	9143370700	One Meadway	Bronxville	NY	United States of America
2471	www.slcc.edu	Salt Lake Community College	8019574333	4600 South Redwood Road	Salt Lake City	UT	United States of America
2472	www.slcconline.edu	Saint Louis Christian College	3148376777	1360 Grandview Dr	Florissant	MO	United States of America
2473	www.slu.edu	Saint Louis University-Main Campus	3149772222	221 N Grand Blvd	Saint Louis	MO	United States of America
2474	www.smc.edu	Santa Monica College	3104344000	1900 Pico Blvd	Santa Monica	CA	United States of America
2475	www.smcc.edu	Southwest Mississippi Community College	6012762000	1156 College Drive	Summit	MS	United States of America
2476	www.smccME.edu	Southern Maine Community College	2077415500	2 Fort Road	South Portland	ME	United States of America
2477	www.smcm.edu	St. Mary's College of Maryland	2408952000	18952 E. Fisher Rd	Saint Mary's City	MD	United States of America
2478	www.smcollege.edu	Southern Methodist College	8035347826	541 Broughton St	Orangeburg	SC	United States of America
2479	www.smcsc.edu	Spartanburg Methodist College	8645874117	1000 Powell Mill Road	Spartanburg	SC	United States of America
2480	www.smcvt.edu	Saint Michaels College	8026542000	One Winooski Park	Colchester	VT	United States of America
2481	www.smfa.edu	School of the Museum of Fine Arts - Boston	6172676100	230 The Fenway	Boston	MA	United States of America
2482	www.smith.edu	Smith College	4135842700	Elm St	Northampton	MA	United States of America
2483	www.smsu.edu	Southwest Minnesota State University	5075377021	1501 State Street	Marshall	MN	United States of America
2484	www.smu.edu	Southern Methodist University	2147682000	6425 Boaz St	Dallas	TX	United States of America
2485	www.smumn.edu	Saint Mary's University of Minnesota	5074571600	700 Terrace Heights	Winona	MN	United States of America
2486	www.smwc.edu	Saint Mary-of-the-Woods College	8125355151	St Hwy 150	Saint Mary-Of-The-Woods	IN	United States of America
2487	www.snc.edu	Saint Norbert College	9204033181	100 Grant St	De Pere	WI	United States of America
2488	www.snead.edu	Snead State Community College	2565935120	220 North Walnut Street	Boaz	AL	United States of America
2489	www.snhu.edu	Southern New Hampshire University	6036682211	2500 N River Rd	Manchester	NH	United States of America
2490	www.snow.edu	Snow College	4352837000	150 E College Ave	Ephraim	UT	United States of America
2491	www.socalsem.edu	Southern California Seminary	6194429841	2075 E. Madison Avenue	El Cajon	CA	United States of America
2492	www.socc.edu	Southwestern Oregon Community College	5418882525	1988 Newmark Ave	Coos Bay	OR	United States of America
2493	www.soka.edu	Soka University of America	9494804000	1 University Drive	Aliso Viejo	CA	United States of America
2494	www.solano.edu	Solano Community College	7078647000	4000 Suisun Valley Rd	Fairfield	CA	United States of America
2495	www.solex.edu	Solex College	8472299595	350 East Dundee Road	Wheeling	IL	United States of America
2496	www.somerset.edu	Pillar College	7323561595	10 College Way	Zarephath	NJ	United States of America
2497	www.somerset.kctcs.edu	LAUREL TECHNICAL COLLEGE		235 S LAUREL RD	LONDON	KY	United States of America
2498	www.somerset.kctcs.edu	Somerset Community College	8776299722	808 Monticello Street	Somerset	KY	United States of America
2499	www.sonoma.edu	Sonoma State University	7076642880	1801 E Cotati Ave	Rohnert Park	CA	United States of America
2500	www.sou.edu	Southern Oregon University	5415527672	1250 Siskiyou Blvd	Ashland	OR	United States of America
2501	www.southark.edu	South Arkansas Community College	8708628131	300 S West Ave	El Dorado	AR	United States of America
2502	www.southbaylo.edu	South Baylo University	7145331495	1126 N Brookhurst St	Anaheim	CA	United States of America
2503	www.southcollegetn.edu	South College	8652511800	3904 Lonas Road	Knoxville	TN	United States of America
2504	www.southeast.edu	Southeast Community College Area	4024713333	301 S. 68th Street Place	Lincoln	NE	United States of America
2505	www.southeasternbaptist.edu	Southeastern Baptist College	6014266346	4229 Hwy 15 N	Laurel	MS	United States of America
2506	www.southeasterntech.edu	Southeastern Technical College	9125383100	3001 E First St	Vidalia	GA	United States of America
2507	www.southeastmn.edu	Minnesota State College-Southeast Technical	5074532700	1250 Homer Rd	Winona	MN	United States of America
2508	www.southern.edu	Southern Adventist University	4232362000	4881 Taylor Cir	Collegedale	TN	United States of America
2509	www.southernct.edu	Southern Connecticut State University	2033925200	501 Crescent Street	New Haven	CT	United States of America
2510	www.southernvirginia.edu	Southern Virginia University	5402618400	One University Hill Drive	Buena Vista	VA	United States of America
2511	www.southernwv.edu	Southern West Virginia Community and Technical College	3047927098	Dempsey Branch Road	Mount Gay	WV	United States of America
2512	www.southflorida.edu	South Florida State College	8634536661	600 W College Dr	Avon Park	FL	United States of America
2513	www.southgatech.edu	South Georgia Technical College	2299312394	900 South Georgia Tech Parkway	Americus	GA	United States of America
2514	www.southhills.edu	South Hills School of Business and Technology - State College	8142347755	480 Waupelani Drive	State College	PA	United States of America
2515	www.southlouisiana.edu	South Louisiana Community College	3379843684	320 Devalcourt Street	Lafayette	LA	United States of America
2516	www.southmountaincc.edu	Maricopa Community Colleges - South Mountain Community College		7050 South 24th Street	Phoenix	AZ	United States of America
2517	www.southseattle.edu	South Seattle Community College	2067645300	6000 16th Ave SW	Seattle	WA	United States of America
2518	www.southside.edu	Southside Virginia Community College	4349491000	109 Campus Dr	Alberta	VA	United States of America
2519	www.southsuburbancollege.edu	South Suburban College of Cook County	7085962000	15800 South State Street	South Holland	IL	United States of America
2520	www.southtexascollege.edu	South Texas College	9566188311	3201 W Pecan	McAllen	TX	United States of America
2521	www.southuniversity.edu	South University-Savannah	9122018000	709 Mall Blvd	Savannah	GA	United States of America
2522	www.southwest.edu	Southwest University	8004335923	2200 Veterans Memorial Boulevard	Kenner	LA	United States of America
2523	www.southwest.tn.edu	Southwest Tennessee Community College	9013335000	737 Union Avenue	Memphis	TN	United States of America
2524	www.southwestcc.edu	Southwestern Community College	8285864091	447 College Dr	Sylva	NC	United States of America
2525	www.southwestern.edu	Southwestern University	5128636511	1001 University Ave	Georgetown	TX	United States of America
2526	www.southwestgatech.edu	Southwest Georgia Technical College	2292255060	15689 US Hwy 19 N	Thomasville	GA	United States of America
2527	www.sowela.edu	Sowela Technical Community College	3374912698	3820 Senator J. Bennett Johnston Ave	Lake Charles	LA	United States of America
2528	www.spalding.edu	Spalding University	5025859911	845 South Third Street	Louisville	KY	United States of America
2529	www.spartan.edu	Spartan College of Aeronautics and Technology	9188366886	8820 E Pine St	Tulsa	OK	United States of America
2530	www.spc.edu	Saint Peter's University	2019159000	2641 Kennedy Blvd	Jersey City	NJ	United States of America
2531	www.spcc.edu	South Piedmont Community College	7042727635	680 Highway 74 West	Polkton	NC	United States of America
2532	www.spcollege.edu	St. Petersburg College	7273413781	14025 58th Street North	Clearwater	FL	United States of America
2533	www.spelman.edu	Spelman College	4046813643	350 Spelman Ln SW	Atlanta	GA	United States of America
2534	www.spencerian.edu	Spencerian College - Louisville	5024471000	4627 Dixie Hwy	Louisville	KY	United States of America
2535	www.spertus.edu	Spertus Institute for Jewish Learning and Leadership	3123221700	610 S. Michigan Ave.	Chicago	IL	United States of America
2536	www.spokane.wsu.edu	Washington State University - Spokane	5093587500	310 N Riverpoint Blvd	Spokane	WA	United States of America
2537	www.spokanefalls.edu	Spokane Falls Community College	5095333500	3410 W Fort Geo Wright Dr	Spokane	WA	United States of America
2538	www.springfieldcollege.edu	Springfield College	4137483116	263 Alden St	Springfield	MA	United States of America
2539	www.spscc.ctc.edu	South Puget Sound Community College	3605965241	2011 Mottman Rd SW	Olympia	WA	United States of America
2540	www.spst.edu	Saint Paul School of Theology	8164839600	13720 Roe Avenue	Leawood	KS	United States of America
2541	www.spsu.edu	Southern Polytechnic State University	6789157778	1100 S. Marietta Parkway	Marietta	GA	United States of America
2542	www.sptseminary.edu	St Petersburg Theological Seminary	7273990276	10830 Navajo Dr	St. Petersburg	FL	United States of America
2543	www.spu.edu	Seattle Pacific University	2062812000	3307 3rd Ave W	Seattle	WA	United States of America
2544	www.src.edu	Spoon River College	3096474645	23235 North County 22	Canton	IL	United States of America
2545	www.sru.edu	Slippery Rock University of Pennsylvania	7247389000	1 Morrow Way	Slippery Rock	PA	United States of America
2546	www.sscc.edu	Southern State Community College	9373933431	100 Hobart Dr	Hillsboro	OH	United States of America
2547	www.sscok.edu	Seminole State College	4053829950	2701 Boren Blvd	Seminole	OK	United States of America
2548	www.ssw.edu	Seminary of the Southwest	5124724133	501 E. 32nd	Austin	TX	United States of America
2549	www.st-aug.edu	Saint Augustine's University	9195164000	1315 Oakwood Avenue	Raleigh	NC	United States of America
2550	www.stac.edu	St. Thomas Aquinas College	8453984000	125 Rte 340	Sparkill	NY	United States of America
2551	www.stanford.edu	Stanford University Residency in Clinical Psychology		450 Serra Mall	Stanford	CA	United States of America
2552	www.stanly.edu	Stanly Community College	7049820121	141 College Dr	Albemarle	NC	United States of America
2553	www.starkstate.edu	Stark State College	3304946170	6200 Frank Ave NW	North Canton	OH	United States of America
2554	www.staugustinecollege.edu	Saint Augustine College	7738788756	1333-45 W Argyle	Chicago	IL	United States of America
2555	www.stbernards.edu	St. Bernard's School of Theology and Ministry	5852713657	120 French Road	Rochester	NY	United States of America
2556	www.stcc.edu	Springfield Technical Community College	4137817822	1 Armory Sq	Springfield	MA	United States of America
2557	www.stchas.edu	St Charles Community College	6369228420	4601 Mid Rivers Mall Dr	Cottleville	MO	United States of America
2558	www.stcl.edu	South Texas College of Law	7136598040	1303 San Jacinto St	Houston	TX	United States of America
2559	www.stcloudstate.edu	Saint Cloud State University	3203080121	720 Fourth Ave. South	Saint Cloud	MN	United States of America
2560	www.stedwards.edu	St. Edward's University	5124488400	3001 S Congress Ave	Austin	TX	United States of America
2561	www.stephens.edu	Stephens College	5734422211	1200 E Broadway	Columbia	MO	United States of America
2562	www.sterling.edu	Sterling College	6202782173	125 W. Cooper	Sterling	KS	United States of America
2563	www.sterlingcollege.edu	Sterling College	8025867711	16 Sterling Drive	Craftsbury Common	VT	United States of America
2564	www.stetson.edu	Stetson University	3868227000	421 N Woodland Blvd	DeLand	FL	United States of America
2565	www.stevens-tech.edu	Stevens Institute of Technology	2012165100	Castle Point On Hudson	Hoboken	NJ	United States of America
2566	www.stevenscollege.edu	Thaddeus Stevens College of Technology	7172997730	750 E King St	Lancaster	PA	United States of America
2567	www.stevenson.edu	Stevenson University	4104867000	1525 Greenspring Valley Rd	Stevenson	MD	United States of America
2568	www.stfrancis.edu	University of St. Francis	8157403360	500 N Wilcox St	Joliet	IL	United States of America
2569	www.stgregorys.edu	Saint Gregory's University	4058785100	1900 W MacArthur	Shawnee	OK	United States of America
2570	www.stgregoryseminary.edu	Saint Gregory the Great Seminary		800 Fletcher Road	Seward	NE	United States of America
2571	www.stillman.edu	Stillman College	2053494240	3601 Stillman Boulevard	Tuscaloosa	AL	United States of America
2572	www.stjohns.edu	St. John's University - New York	7189906161	8000 Utopia Parkway	Queens	NY	United States of America
2573	www.stjohnscollege.edu	St. John's College	4102632371	60 College Avenue	Annapolis	MD	United States of America
2574	www.stjohnsem.edu	Saint Johns Seminary	8054822755	5012 Seminary Rd	Camarillo	CA	United States of America
2575	www.stkate.edu	St. Catherine University	6516906000	2004 Randolph Ave.	St. Paul	MN	United States of America
2576	www.stlawu.edu	St. Lawrence University	3152295011	23 Romoda Drive	Canton	NY	United States of America
2577	www.stlcc.edu	Saint Louis Community College	3145395000	300 S Broadway	St Louis	MO	United States of America
2578	www.stlcop.edu	St Louis College of Pharmacy	3144468312	4588 Parkview Pl	Saint Louis	MO	United States of America
2579	www.stlukescollege.edu	St. Luke's College	7122793149	2720 Stone Park Blvd	Sioux City	IA	United States of America
2580	www.stmartin.edu	Saint Martin's University	3604914700	5300 Pacific Ave SE	Lacey	WA	United States of America
2581	www.stmary.edu	University of Saint Mary	9136825151	4100 S 4th St Trafficway	Leavenworth	KS	United States of America
2582	www.stmarys-ca.edu	Saint Mary's College of California	9256314000	1928 Saint Marys Road	Moraga	CA	United States of America
2583	www.stmarys.edu	St. Mary's Seminary & University	4108644000	5400 Roland Ave	Baltimore	MD	United States of America
2584	www.stmarysem.edu	Saint Mary Seminary and Graduate School of Theology	4409437600	28700 Euclid Ave	Wickliffe	OH	United States of America
2585	www.stmarytx.edu	St. Mary's University	2104363011	One Camino Santa Maria	San Antonio	TX	United States of America
2586	www.stockton.edu	The Richard Stockton College of New Jersey	6096521776	101 Vera King Farris Dr.	Galloway	NJ	United States of America
2587	www.stolaf.edu	St. Olaf College	5076462222	1520 St Olaf Ave	Northfield	MN	United States of America
2588	www.stonechild.edu	Stone Child College	4063954313	Upper Bonneau Road	Box Elder	MT	United States of America
2589	www.stonehill.edu	Stonehill College	5085651000	320 Washington Street	Easton	MA	United States of America
2590	www.stots.edu	St Tikhon's Orthodox Theological Seminary	5709374411	St Tikhons Rd	South Canaan	PA	United States of America
2591	www.stratford.edu	Stratford University	8004440804	7777 Leesburg Pike	Falls Church	VA	United States of America
2592	www.strayer.edu	Strayer University	2024082400	1133 15th St NW	Washington	DC	United States of America
2593	www.stritch.edu	Cardinal Stritch University	4144104000	6801 N Yates Rd	Milwaukee	WI	United States of America
2594	www.strose.edu	The College of Saint Rose	5184545111	432 Western Ave	Albany	NY	United States of America
2595	www.stthom.edu	University of St. Thomas	7135227911	3800 Montrose Blvd	Houston	TX	United States of America
2596	www.stthomas.edu	University of Saint Thomas	6519625000	2115 Summit Ave	Saint Paul	MN	United States of America
2597	www.stu.edu	Saint Thomas University	3056256000	16401 NW 37th Ave	Miami Gardens	FL	United States of America
2598	www.stvincent.edu	Saint Vincent College	7245399761	300 Fraser Purchase Rd	Latrobe	PA	United States of America
2599	www.stvincentscollege.edu	St Vincent's College	2035765235	2800 Main St	Bridgeport	CT	United States of America
2600	www.stvt.edu	South Texas Vo-Tech Institute	9569691564	2419 E Haggar Ave	Weslaco	TX	United States of America
2601	www.su.edu	Shenandoah University	5406654500	1460 University Dr	Winchester	VA	United States of America
2602	www.subr.edu	Southern University and A & M College	2257714500	G. Leon Netterville Drive	Baton Rouge	LA	United States of America
2603	www.success.edu	Glendale Career College		1015 Grandview Avenue	Glendale	CA	United States of America
2604	www.suffolk.edu	Suffolk University	6175738000	8 Ashburton Pl Beacon Hill	Boston	MA	United States of America
2605	www.sullivan.edu	Sullivan University	5024566504	3101 Bardstown Rd	Louisville	KY	United States of America
2606	www.sullivan.suny.edu	Sullivan County Community College	8454345750	112 College Road	Loch Sheldrake	NY	United States of America
2607	www.sulross.edu	Sul Ross State University	9158378011	400 North Harrison	Alpine	TX	United States of America
2608	www.sum.edu	SUM Bible College & Theological Seminary - Main Campus	5105676174	735 105th Ave	Oakland	CA	United States of America
2609	www.suno.edu	Southern University at New Orleans	5042865000	6400 Press Dr	New Orleans	LA	United States of America
2610	www.sunstate.edu	Sunstate Academy	7275383827	2525 Drew St	Clearwater	FL	United States of America
2611	www.sunycgcc.edu	Columbia-Greene Community College	5188284181	4400 Rte 23	Hudson	NY	United States of America
2612	www.sunydutchess.edu	Dutchess Community College	8454318000	53 Pendell Rd	Poughkeepsie	NY	United States of America
2613	www.sunyit.edu	SUNY Institute of Technology at Utica - Rome	3157927100	Horatio Street	Utica	NY	United States of America
2614	www.sunyjcc.edu	Jamestown Community College	7166655220	525 Falconer St	Jamestown	NY	United States of America
2615	www.sunyjefferson.edu	Jefferson Community College	3157862200	1220 Coffeen St	Watertown	NY	United States of America
2616	www.sunymaritime.edu	SUNY Maritime College	7184097200	6 Pennyfield Ave	Bronx	NY	United States of America
2617	www.sunyocc.edu	Onondaga Community College	3154982622	4941 Onondaga Rd	Syracuse	NY	United States of America
2618	www.sunyopt.edu	SUNY College of Optometry	2127804900	33 West 42nd Street	New York	NY	United States of America
2619	www.sunyorange.edu	Orange County Community College	8453446222	115 South St	Middletown	NY	United States of America
2620	www.sunyrockland.edu	Rockland Community College	8455744000	145 College Rd	Suffern	NY	United States of America
2621	www.sunysb.edu	SUNY at Stony Brook	6316326000	Nicolls Road	Stony Brook	NY	United States of America
2622	www.sunysccc.edu	Schenectady County Community College	5183811200	78 Washington Avenue	Schenectady	NY	United States of America
2623	www.sunysuffolk.edu	Suffolk County Community College	6314514110	533 College Road	Selden	NY	United States of America
2624	www.sunyulster.edu	Ulster County Community College	8456875000	Cottekill Road	Stone Ridge	NY	United States of America
2625	www.sunywcc.edu	SUNY Westchester Community College	9147856600	75 Grasslands Road	Valhalla	NY	United States of America
2626	www.surry.edu	Surry Community College	3363863204	630 S. Main St.	Dobson	NC	United States of America
2627	www.suscc.edu	Southern Union State Community College	2563952211	750 Roberts St	Wadley	AL	United States of America
2628	www.susla.edu	Southern University at Shreveport	3186743300	3050 Martin Luther King Dr	Shreveport	LA	United States of America
2629	www.susqu.edu	Susquehanna University	5703740101	514 University Ave	Selinsgrove	PA	United States of America
2630	www.sussex.edu	Sussex County Community College	9733002100	One College Hill	Newton	NJ	United States of America
2631	www.suu.edu	Southern Utah University	4355867700	351 West University Blvd	Cedar City	UT	United States of America
2632	www.svc.edu	Southern Vermont College	8024425427	982 Mansion Drive	Bennington	VT	United States of America
2633	www.svcc.edu	Sauk Valley Community College	8152885511	173 Illinois Rt 2	Dixon	IL	United States of America
2634	www.svdp.edu	Saint Vincent de Paul Regional Seminary	5617324424	10701 S Military Tr	Boynton Beach	FL	United States of America
2635	www.svots.edu	Saint Vladimirs Orthodox Theological Seminary	9149618313	575 Scarsdale Rd	Crestwood	NY	United States of America
2636	www.svsu.edu	Saginaw Valley State University	9899644000	7400 Bay Rd	University Center	MI	United States of America
2637	www.sw.edu	Southwest Virginia Community College	2769642555	369 College Road	Richlands	VA	United States of America
2638	www.swainsborotech.edu	Swainsboro Technical College	4782892200	346 Kite Rd	Swainsboro	GA	United States of America
2639	www.swarthmore.edu	Swarthmore College	6103288000	500 College Ave	Swarthmore	PA	United States of America
2640	www.swau.edu	Southwestern Adventist University	8176453921	100 W Hillcrest	Keene	TX	United States of America
2641	www.swbts.edu	Southwestern Baptist Theological Seminary	8179231921	2001 West Seminary Drive	Fort Worth	TX	United States of America
2642	www.swc.edu	Southwestern College	5054715756	3960 ABC San Felipe	Santa Fe	NM	United States of America
2643	www.swcaz.edu	Arizona Christian University	6024895300	2625 E. Cactus Road	Phoenix	AZ	United States of America
2644	www.swcc.edu	Southwestern Christian College	9725243341	200 Bowser Circle	Terrell	TX	United States of America
2645	www.swcu.edu	Southwestern Christian University	4057897661	7210 NW 39th Expressway	Bethany	OK	United States of America
2646	www.swfc.edu	Southern Technical College at Fort Myers	2399394766	1685 Medical Lane	Fort Myers	FL	United States of America
2647	www.swic.edu	Southwestern Illinois College	6182352700	2500 Carlyle Ave	Belleville	IL	United States of America
2648	www.swlaw.edu	Southwestern Law School	2137386700	3050 Wilshire Boulevard	Los Angeles	CA	United States of America
2649	www.swmich.edu	Southwestern Michigan College	2697821000	58900 Cherry Grove Rd	Dowagiac	MI	United States of America
2650	www.swosu.edu	Southwestern Oklahoma State University	5807726611	100 Campus Dr	Weatherford	OK	United States of America
2651	www.swtc.edu	Southwest Wisconsin Technical College	6088223262	1800 Bronson Blvd	Fennimore	WI	United States of America
2652	www.swu.edu	Southern Wesleyan University	8646445000	907 Wesleyan Drive	Central	SC	United States of America
2653	www.t-bird.edu	Thunderbird School of Global Management	6029787000	15249 N 59th Ave	Glendale	AZ	United States of America
2654	www.tabor.edu	Tabor College	6209473121	400 S Jefferson	Hillsboro	KS	United States of America
2655	www.tacomacc.edu	Tacoma Community College	2535665000	6501 S 19th Street	Tacoma	WA	United States of America
2656	www.taftcollege.edu	Taft College	6617637700	29 Emmons Park Drive	Taft	CA	United States of America
2657	www.TaftU.edu	Taft Law School	8008824555	3700 South Susan Street Office 200	Santa Ana	CA	United States of America
2658	www.tai.edu	Maryland University of Integrative Health	4108889048	7750 Montpelier Road	Laurel	MD	United States of America
2659	www.talladega.edu	Talladega College	2563620206	627 W Battle St	Talladega	AL	United States of America
2660	www.tamiu.edu	Texas A & M International University	9563262001	5201 University Blvd	Laredo	TX	United States of America
2661	www.tamu-commerce.edu	Texas A & M University - Commerce	9038865081	2600 South Neal	Commerce	TX	United States of America
2662	www.tamu.edu	Texas A & M University	9798453211		College Station	TX	United States of America
2663	www.tamucc.edu	Texas A & M University - Corpus Christi	3618255700	6300 Ocean Dr.	Corpus Christi	TX	United States of America
2664	www.tamuk.edu	Texas A & M University - Kingsville	3615932111	955 University Blvd	Kingsville	TX	United States of America
2665	www.tamut.edu	Texas A & M University - Texarkana	9032233000	2600 N Robison Rd	Texarkana	TX	United States of America
2666	www.tarleton.edu	Tarleton State University	2549689000	1333 W. Washington	Stephenville	TX	United States of America
2667	www.taylor.edu	Taylor University	7659985134	236 W Reade Ave	Upland	IN	United States of America
2668	www.taylorcollege.edu	Taylor College	3522454119	5190 SE 125th Street	Belleview	FL	United States of America
2669	www.tbc.edu	Trinity Baptist College	9045962414	800 Hammond Blvd	Jacksonville	FL	United States of America
2670	www.tc.edu	Teachers College at Columbia University	2126783000	525 W 120th Street	New York	NY	United States of America
2671	www.TC3.edu	Tompkins-Cortland Community College	6078448211	170 North Street	Dryden	NY	United States of America
2672	www.tcatdickson.edu	Tennessee College of Applied Technology - Dickson	6154416220	740 Hwy 46	Dickson	TN	United States of America
2673	www.tcc.edu	Tidewater Community College	7578221122	500 East Main Street	Norfolk	VA	United States of America
2674	www.tcc.fl.edu	Tallahassee Community College	8502016200	444 Appleyard Dr	Tallahassee	FL	United States of America
2675	www.tccd.edu	Tarrant County College District	8175155100	1500 Houston St	Fort Worth	TX	United States of America
2676	www.tcl.edu	Technical College of the Lowcountry	8435258324	921 Ribaut Road	Beaufort	SC	United States of America
2677	www.tcnj.edu	The College of New Jersey	6097711855	2000 Pennington Road	Ewing	NJ	United States of America
2678	www.tctc.edu	Tri-County Technical College	8646461500	7900 U.S. Hwy 76	Pendleton	SC	United States of America
2679	www.tcu.edu	Texas Christian University	8172577000	2800 S University Dr	Fort Worth	TX	United States of America
2680	www.temple.edu	Temple University	2152047000	1801 North Broad Street	Philadelphia	PA	United States of America
2681	www.templebaptist.edu	Ohio Mid-Western College	5138513800	10765 Reading Road	Cincinnati	OH	United States of America
2682	www.templebaptistseminary.edu	Temple Baptist Seminary	4234934221	1906  Union Avenue	Chattanooga	TN	United States of America
2683	www.templejc.edu	Temple College	2542988282	2600 S 1st St	Temple	TX	United States of America
2684	www.tennessee.edu	University of Tennessee	8659741000	527 Andy Holt Tower	Knoxville	TN	United States of America
2685	www.terra.edu	Terra State Community College	4193348400	2830 Napoleon Rd	Fremont	OH	United States of America
2686	www.tesc.edu	Thomas Edison State College	6099841100	101 W State St	Trenton	NJ	United States of America
2687	www.tesm.edu	Trinity Episcopal School for Ministry	7242663838	311 Eleventh St	Ambridge	PA	United States of America
2688	www.teu.edu	Teacher Education University	8005231578	1079 West Morse Boulevard Suite B	Winter Park	FL	United States of America
2689	www.texarkanacollege.edu	Texarkana College	9038384541	2500 N Robison Rd	Texarkana	TX	United States of America
2690	www.texascollege.edu	Texas College	9035938311	2404 N. Grand Avenue	Tyler	TX	United States of America
2691	www.tfc.edu	Toccoa Falls College	7068866831	107 North Chapel Drive	Toccoa Falls	GA	United States of America
2692	www.the-bac.edu	Boston Architectural Center	6172625000	320 Newbury St	Boston	MA	United States of America
2693	www.theaileyschool.edu	The Ailey School	2124059510	405 West 55th Street	New York	NY	United States of America
2694	www.thiel.edu	Thiel College	7245892000	75 College Ave	Greenville	PA	United States of America
2696	www.thomasaquinas.edu	Thomas Aquinas College	8055254417	10000 N Ojai Rd	Santa Paula	CA	United States of America
2697	www.thomasmore.edu	Thomas More College	8593415800	333 Thomas More Parkway	Crestview Hills	KY	United States of America
2698	www.thomasmorecollege.edu	Thomas More College of Liberal Arts	6038808308	6 Manchester St	Merrimack	NH	United States of America
2699	www.thomasu.edu	Thomas University	2292261621	1501 Millpond Rd	Thomasville	GA	United States of America
2700	www.thompson.edu	Kaplan Career Institute - Harrisburg	7175644112	5650 Derry Street	Harrisburg	PA	United States of America
2701	www.tiffin.edu	Tiffin University	4194476442	155 Miami Street	Tiffin	OH	United States of America
2702	www.tiu.edu	Trinity International University	8479458800	2065 Half Day Rd	Deerfield	IL	United States of America
2703	www.tjc.edu	Tyler Junior College	9035102200	1400 East Fifth Street	Tyler	TX	United States of America
2704	www.tjsl.edu	Thomas Jefferson School of Law	6192979700	2121 San Diego Ave	San Diego	CA	United States of America
2705	www.tlc.edu	Trinity Lutheran College	4253920400	4221 - 228th Ave SE	Issaquah	WA	United States of America
2706	www.tlsohio.edu	Trinity Lutheran Seminary	6142354136	2199 E Main St	Columbus	OH	United States of America
2707	www.tlu.edu	Texas Lutheran University	8303728000	1000 W. Court St	Seguin	TX	United States of America
2708	www.tm.edu	Turtle Mountain Community College	7014777862	P.O. Box 340	Belcourt	ND	United States of America
2709	www.tmcc.edu	Truckee Meadows Community College	7756737000	7000 Dandini Blvd	Reno	NV	United States of America
2710	www.tncc.edu	Thomas Nelson Community College	7578252700	99 Thomas Nelson Drive	Hampton	VA	United States of America
2711	www.tnstate.edu	Tennessee State University	6159635111	3500 John A. Merritt Blvd	Nashville	TN	United States of America
2712	www.tntech.edu	Tennessee Technological University	9313723223	1 William L. Jones Drive	Cookeville	TN	United States of America
2713	www.tntemple.edu	Tennessee Temple University	4234934100	1815 Union Ave	Chattanooga	TN	United States of America
2714	www.tokai.edu	Hawaii Tokai International College		2241 Kapiolani Blvd.	Honolulu	HI	United States of America
2715	www.tougaloo.edu	Tougaloo College	6019777700	500 W County Line Rd	Tougaloo	MS	United States of America
2716	www.touro.edu	Touro College	2124630400	27-33 W 23rd St	New York	NY	United States of America
2717	www.towson.edu	Towson University	4107042000	8000 York Rd	Towson	MD	United States of America
2718	www.transy.edu	Transylvania University	8592338300	300 N Broadway	Lexington	KY	United States of America
2719	www.trcc.commnet.edu	Three Rivers Community College	8608232800	7 Mahan Dr	Norwich	CT	United States of America
2720	www.trcc.edu	Three Rivers Community College	5738409600	2080 Three Rivers Blvd	Poplar Bluff	MO	United States of America
2721	www.trenholmstate.edu	H Councill Trenholm State Technical College	3344204295	1225 Air Base Blvd	Montgomery	AL	United States of America
2722	www.trevecca.edu	Trevecca Nazarene University	6152481200	333 Murfreesboro Rd	Nashville	TN	United States of America
2723	www.tri-c.edu	Cuyahoga Community College	8009548742	700 Carnegie Ave	Cleveland	OH	United States of America
2724	www.triangle-tech.edu	Triangle Tech Inc-Erie	8144536016	2000 Liberty St	Erie	PA	United States of America
2725	www.tricountycc.edu	Tri-County Community College	8288376810	21 Campus Circle	Murphy	NC	United States of America
2726	www.tridenttech.edu	Trident Technical College	8435746111	7000 Rivers Avenue	Charleston	SC	United States of America
2727	www.Trincoll.edu	Trinity College	8602972000	300 Summit St	Hartford	CT	United States of America
2728	www.trine.edu	Trine University	2606654100	1 University Ave	Angola	IN	United States of America
2729	www.trinidadstate.edu	Trinidad State Junior College	7198465011	600 Prospect St	Trinidad	CO	United States of America
2730	www.trinity.edu	Trinity University	2109997011	One Trinity Place	San Antonio	TX	United States of America
2731	www.trinitybiblecollege.edu	Trinity Bible College	8888222329	50 Sixth Avenue South	Ellendale	ND	United States of America
2732	www.trinitycollegeqc.edu	Trinity College of Nursing and Health Sciences	3097797700	2122 - 25th Avenue	Rock Island	IL	United States of America
2733	www.trinitydc.edu	Trinity Washington University	2028849000	125 Michigan Ave NE	Washington	DC	United States of America
2734	www.triton.edu	Triton College	7084560300	2000 5th Ave	River Grove	IL	United States of America
2735	www.trnty.edu	Trinity Christian College	7085973000	6601 W College Dr	Palos Heights	IL	United States of America
2736	www.trocaire.edu	Trocaire College	7168261200	360 Choate Ave	Buffalo	NY	United States of America
2737	www.troy.edu	Troy University	3346703100	University Avenue	Troy	AL	United States of America
2738	www.truett.edu	Truett-McConnell College	7068652134	100 Alumni Dr	Cleveland	GA	United States of America
2739	www.truman.edu	Truman State University	6607854000	100 E Normal	Kirksville	MO	United States of America
2740	www.tsb.edu	Texas School of Business Inc	2814438900	711 East Airtex Drive	Houston	TX	United States of America
2741	www.tsbc.edu	Tri-State Bible College	7403772520	506 Margaret St	South Point	OH	United States of America
2742	www.tsbi.edu	Fortis Institute - Erie	8148387673	5757 West 26th Street	Erie	PA	United States of America
2743	www.TSCA.edu	Tri-State College of Acupuncture	2122422255	80 Eighth Ave Rm 400	New York	NY	United States of America
2744	www.tsu.edu	Texas Southern University	7133137011	3100 Cleburne St	Houston	TX	United States of America
2745	www.ttcmcminnville.edu	Tennessee College of Applied Technology - McMinnville	9314735587	241 Vo-Tech Drive	McMinnville	TN	United States of America
2746	www.ttcpulaski.edu	Tennessee College of Applied Technology - Pulaski	9314244014	PO Box 614 1233 E. College Street	Pulaski	TN	United States of America
2747	www.ttu.edu	Texas Tech University	8067422011	2500 Broadway	Lubbock	TX	United States of America
2748	www.tui.edu	Union Institute & University	8004863116	440 E McMillan St	Cincinnati	OH	United States of America
2749	www.tulane.edu	Tulane University	5048655000	6823 Saint Charles Ave	New Orleans	LA	United States of America
2750	www.tulsacc.edu	Tulsa Community College	9185957000	6111 E Skelly Dr	Tulsa	OK	United States of America
2751	www.tusculum.edu	Tusculum College	4236367300	60 Shiloh Road	Greeneville	TN	United States of America
2752	www.tvcc.edu	Trinity Valley Community College	9036756200	100 Cardinal Drive	Athens	TX	United States of America
2753	www.twcnet.edu	Tennessee Wesleyan College	4237457504	204 East College Street	Athens	TN	United States of America
2754	www.twu.edu	Texas Woman's University	9408982000	304 Administration Dr	Denton	TX	United States of America
2755	www.txchiro.edu	Texas Chiropractic College	2814871170	5912 Spencer Hwy	Pasadena	TX	United States of America
2756	www.txstate.edu	Texas State University	5122452111	601 University Dr	San Marcos	TX	United States of America
2757	www.txwes.edu	Texas Wesleyan University	8175314444	1201 Wesleyan St	Fort Worth	TX	United States of America
2758	www.ua.edu	The University of Alabama	2053486010	739 University Boulevard	Tuscaloosa	AL	United States of America
2759	www.uaa.alaska.edu	University of Alaska Anchorage	9077861480	3211 Providence Drive	Anchorage	AK	United States of America
2760	www.uab.edu	University of Alabama at Birmingham	2059344011	1530 3rd Avenue South	Birmingham	AL	United States of America
2761	www.uaccb.edu	University of Arkansas Community College-Batesville	8707937581	2005 White Drive	Batesville	AR	United States of America
2762	www.uacch.edu	University of Arkansas Community College-Hope	8707228206	2500 S Main	Hope	AR	United States of America
2763	www.uaccm.edu	University of Arkansas Community College-Morrilton	5019772000	1537 University Blvd.	Morrilton	AR	United States of America
2764	www.uaf.edu	University of Alaska Fairbanks	9074747211	Signers' Hall	Fairbanks	AK	United States of America
2765	www.uafortsmith.edu	University of Arkansas-Fort Smith	4797887004	5210 Grand Ave P.O. Box 3649	Fort Smith	AR	United States of America
2766	www.uah.edu	University of Alabama in Huntsville	2568246120	301 Sparkman Dr	Huntsville	AL	United States of America
2767	www.uakron.edu	University of Akron	3309727111	302 Buchtel Common	Akron	OH	United States of America
2768	www.ualr.edu	University of Arkansas at Little Rock	5015693000	2801 S University Ave	Little Rock	AR	United States of America
2769	www.uamont.edu	University of Arkansas at Monticello	8703676811	Highway 425 South	Monticello	AR	United States of America
2770	www.uams.edu	University of Arkansas for Medical Sciences	5016865454	4301 W Markham	Little Rock	AR	United States of America
2771	www.uapb.edu	University of Arkansas at Pine Bluff	8705758000	1200 N University Mail Slot 4789	Pine Bluff	AR	United States of America
2772	www.uarts.edu	The University of the Arts	2157176000	320 S Broad St	Philadelphia	PA	United States of America
2773	www.uas.alaska.edu	University of Alaska Southeast	9074656457	11120 Glacier Highway	Juneau	AK	United States of America
2774	www.uat.edu	University of Advancing Technology	6023838255	2625 W Baseline Rd	Tempe	AZ	United States of America
2775	www.uav.edu	University of Antelope Valley	6617261911	44055 North Sierra Highway	Lancaster	CA	United States of America
2776	www.ubalt.edu	University of Baltimore	4108374200	1420 N. Charles Street	Baltimore	MD	United States of America
2777	www.uc.edu	University of Cincinnati - Main Campus	5135566000	P.O. Box 210063	Cincinnati	OH	United States of America
2778	www.uca.edu	University of Central Arkansas	5014505000	201 Donaghey Ave	Conway	AR	United States of America
2779	www.ucc.edu	Union County College	9087097000	1033 Springfield Ave	Cranford	NJ	United States of America
2780	www.uccs.edu	University of Colorado at Colorado Springs	7192623000	1420 Austin Bluffs Parkway	Colorado Springs	CO	United States of America
2781	www.ucdavis.edu	University of California - Davis	5307521011	One Shields Avenue	Davis	CA	United States of America
2782	www.ucf.edu	University of Central Florida	4078232000	4000 Central Florida Blvd	Orlando	FL	United States of America
2783	www.uchastings.edu	University of California Hastings College of Law	4155654600	200 McAllister St	San Francisco	CA	United States of America
2784	www.uchc.edu	The University of Connecticut School of Medicine and Dentistry	8606792000	263 Farmington Ave	Farmington	CT	United States of America
2785	www.uci.edu	University of California - Irvine	9498245011	510 Aldrich Hall	Irvine	CA	United States of America
2786	www.ucla.edu	University of California - Los Angeles	3108254321	405 Hilgard Ave	Los Angeles	CA	United States of America
2787	www.ucmo.edu	University of Central Missouri	6605434112	116 W. South Street	Warrensburg	MO	United States of America
2788	www.uco.edu	University of Central Oklahoma	4059742000	100 N. University Dr.	Edmond	OK	United States of America
2789	www.ucollege.edu	Union College	4024882331	3800 S 48th	Lincoln	NE	United States of America
2790	www.uconn.edu	University of Connecticut	8604862000	352 Mansfield Rd.	Storrs	CT	United States of America
2791	www.ucsb.edu	University of California - Santa Barbara	8058938000	UC Santa Barbara	Santa Barbara	CA	United States of America
2792	www.ucsc.edu/	University of California - Santa Cruz	8314590111	1156 High St	Santa Cruz	CA	United States of America
2793	www.ucsd.edu	University of California - San Diego	8585342230	9500 Gilman Dr	La Jolla	CA	United States of America
2794	www.ucsf.edu	University of California - San Francisco	4154769000	500 Parnassus Ave	San Francisco	CA	United States of America
2795	www.ucumberlands.edu	University of the Cumberlands	6065492200	6191 College Station Drive	Williamsburg	KY	United States of America
2796	www.udallas.edu	University of Dallas	9727215000	1845 E Northgate	Irving	TX	United States of America
2797	www.udayton.edu	University of Dayton	9372291000	300 College Pk	Dayton	OH	United States of America
2798	www.udc.edu	University of the District of Columbia	2022745000	4200 Connecticut Ave NW	Washington	DC	United States of America
2799	www.udel.edu	University of Delaware	3028312000	104 Hullihen Hall	Newark	DE	United States of America
2800	www.udmercy.edu	University of Detroit Mercy	3139931000	4001 W McNichols Rd	Detroit	MI	United States of America
2801	www.uewm.edu	University of East West Medicine		595 Lawrence Expressway	Sunnyvale	CA	United States of America
2802	www.ufl.edu	University of Florida	3523923261	355 Tigert Hall	Gainesville	FL	United States of America
2803	www.uftl.edu	University of Fort Lauderdale	9544867728	4093 N.W. 16th Street	Lauderhill	FL	United States of America
2804	www.uga.edu	University of Georgia	7065423000	456 East Broad Street	Athens	GA	United States of America
2805	www.ugf.edu	University of Great Falls	4067618210	1301 Twentieth St S	Great Falls	MT	United States of America
2807	www.uhcl.edu	University of Houston-Clear Lake	2812837600	2700 Bay Area Blvd	Houston	TX	United States of America
2808	www.uhd.edu	University of Houston-Downtown	7132218000	1 Main St	Houston	TX	United States of America
2809	www.uhv.edu	University of Houston-Victoria	3615704848	3007 N. Ben Wilson	Victoria	TX	United States of America
2810	www.uic.edu	University of Illinois at Chicago	3124133350	601 S. Morgan St. ; M/C 102	Chicago	IL	United States of America
2811	www.uidaho.edu	University of Idaho	2088856111	875 Perimeter Drive	Moscow	ID	United States of America
2812	www.uiowa.edu	University of Iowa	3193353500	101 Jessup Hall	Iowa City	IA	United States of America
2813	www.uis.edu	University of Illinois at Springfield	2172066600	One University Plaza	Springfield	IL	United States of America
2814	www.uiu.edu	Upper Iowa University	5634255200	605 Washington St	Fayette	IA	United States of America
2815	www.uiuc.edu	University of Illinois at Urbana-Champaign	2173331000	601 E John Street	Champaign	IL	United States of America
2816	www.uiw.edu	University of the Incarnate Word	2108296000	4301 Broadway	San Antonio	TX	United States of America
2817	www.uj.edu	American Jewish University	3104769777	15600 Mulholland Dr	Los Angeles	CA	United States of America
2818	www.uky.edu	University of Kentucky	6062579000	101 Main Building	Lexington	KY	United States of America
2819	www.uky.edu/	Lexington Community College	8592574872	Cooper Dr	Lexington	KY	United States of America
2820	www.ulm.edu	University of Louisiana at Monroe	3183421000	700 University Avenue	Monroe	LA	United States of America
2821	www.ultrasound.edu	Cardiac & Vascular Institute of Ultrasound	2514331600	2936 North McVay Drive	Mobile	AL	United States of America
2822	www.ulv.edu	University of La Verne	9095933511	1950 Third St	La Verne	CA	United States of America
2823	www.uma.maine.edu	University of Maine at Augusta	2076213146	46 University Dr	Augusta	ME	United States of America
2824	www.umary.edu	University of Mary	7012557500	7500 University Dr	Bismarck	ND	United States of America
2825	www.umaryland.edu	University of Maryland - Baltimore	4107063100	522 West Lombard Street	Baltimore	MD	United States of America
2826	www.umass.edu	University of Massachusetts Amherst	4135450111	181 Presidents Drive	Amherst	MA	United States of America
2827	www.umassd.edu	University of Massachusetts - Dartmouth	5089998000	285 Old Westport Rd	North Dartmouth	MA	United States of America
2828	www.umassmed.edu	University of Massachusetts - Worcester	5088561542	55 Lake Avenue North	Worcester	MA	United States of America
2829	www.umb.edu	University of Massachusetts - Boston	6172876000	100 Morrissey Blvd	Boston	MA	United States of America
2830	www.umbc.edu	University of Maryland - Baltimore County	4104551000	1000 Hilltop Circle	Baltimore	MD	United States of America
2831	www.umc.edu	University of Mississippi Medical Center	6019841000	2500 North State Street	Jackson	MS	United States of America
2832	www.umd.edu	University of Maryland - College Park	3014051000	Main Administration Building	College Park	MD	United States of America
2833	www.umd.umich.edu	University of Michigan - Dearborn	3135935000	4901 Evergreen Rd	Dearborn	MI	United States of America
2834	www.umes.edu	University of Maryland - Eastern Shore	4106512200	11868 Academic Oval	Princess Anne	MD	United States of America
2835	www.umf.maine.edu	University of Maine at Farmington	2077787000	224 Main St	Farmington	ME	United States of America
2836	www.umfk.maine.edu	University of Maine at Fort Kent	2078347500	23 University Drive	Fort Kent	ME	United States of America
2837	www.umflint.edu	University of Michigan - Flint	8107623000	303 E Kearsley	Flint	MI	United States of America
2838	www.umhb.edu	University of Mary Hardin-Baylor	8007278642	900 College St	Belton	TX	United States of America
2839	www.umhelena.edu	University of Montana - Helena College of Technology	4064446800	1115 N Roberts Street	Helena	MT	United States of America
2840	www.umich.edu	University of Michigan - Ann Arbor	7347641817	2074 Fleming Administration Building	Ann Arbor	MI	United States of America
2841	www.umkc.edu	University of Missouri - Kansas City	8162351000	5100 Rockhill Rd	Kansas City	MO	United States of America
2842	www.umm.maine.edu	University of Maine at Machias	2072551200	9 O'Brien Ave	Machias	ME	United States of America
2843	www.umobile.edu	University of Mobile	2516755990	5735 College Parkway Drive	Mobile	AL	United States of America
2844	www.umpi.maine.edu	University of Maine at Presque Isle	2077689400	181 Main St	Presque Isle	ME	United States of America
2845	www.umpqua.edu	Umpqua Community College	5414404600	1140 College Rd.	Roseburg	OR	United States of America
2846	www.umsl.edu	University of Missouri - St Louis	3145165000	One University Boulevard	Saint Louis	MO	United States of America
2847	www.umt.edu	The University of Montana	4062430211	32 Campus Drive	Missoula	MT	United States of America
2848	www.umuc.edu	University of Maryland - University College	3019857000	3501 University Blvd East	Adelphi	MD	United States of America
2849	www.umw.edu	University of Mary Washington	5406541000	1301 College Ave	Fredericksburg	VA	United States of America
2850	www.umwestern.edu	The University of Montana - Western	4066837011	710 S Atlantic	Dillon	MT	United States of America
2851	www.una.edu	University of North Alabama	2567654100	One Harrison Plaza	Florence	AL	United States of America
2852	www.unc.edu	University of North Carolina at Chapel Hill	9199622211	103 South Bldg Campus Box 9100	Chapel Hill	NC	United States of America
2853	www.unca.edu	University of North Carolina at Asheville	8282516600	One University Hts	Asheville	NC	United States of America
2854	www.uncc.edu	University of North Carolina at Charlotte	7046872000	9201 University City Blvd	Charlotte	NC	United States of America
2855	www.uncfsu.edu	Fayetteville State University	9106721111	1200 Murchison Rd	Fayetteville	NC	United States of America
2856	www.uncg.edu	University of North Carolina at Greensboro	3363345000	1000 Spring Garden St	Greensboro	NC	United States of America
2857	www.unco.edu	University of Northern Colorado	9703511890	501 20th St.	Greeley	CO	United States of America
2858	www.uncp.edu	University of North Carolina at Pembroke	9105216000	One University Drive	Pembroke	NC	United States of America
2859	www.uncsa.edu	North Carolina School of the Arts	3367703399	1533 South Main St.	Winston-Salem	NC	United States of America
2860	www.uncw.edu	University of North Carolina - Wilmington	9109623000	601 South College Road	Wilmington	NC	United States of America
2861	www.und.edu	University of North Dakota	8002255863	264 Centennial Drive Stop 8193	Grand Forks	ND	United States of America
2862	www.unf.edu	University of North Florida	9046201000	1 UNF Drive	Jacksonville	FL	United States of America
2863	www.uni.edu	University of Northern Iowa	3192732311	1222 W 27th St	Cedar Falls	IA	United States of America
2864	www.unilatina.edu	Unilatina International College	9546074344	3130 Commerce Parkway	Miramar	FL	United States of America
2865	www.union.edu	Union College	5183886000	807 Union Street	Schenectady	NY	United States of America
2866	www.uniongraduatecollege.edu	Union Graduate College	5186319844	80 Nott Terrace	Schenectady	NY	United States of America
2867	www.unionky.edu	Union College	6065464151	310 College St	Barbourville	KY	United States of America
2868	www.united.edu	United Theological Seminary	9372785817	4501 Denlinger Rd.	Dayton	OH	United States of America
2869	www.unity.edu	Unity College	2079483131	90 Quaker Hill Road	Unity	ME	United States of America
2870	www.unk.edu	University of Nebraska at Kearney	3088658441	905 W 25th St	Kearney	NE	United States of America
2871	www.unl.edu	University of Nebraska - Lincoln	4024727211	201 Canfield Administration Bldg. 14th & R Street	Lincoln	NE	United States of America
2872	www.unm.edu	University of New Mexico-Main Campus	5052770111		Albuquerque	NM	United States of America
2873	www.unmc.edu	University of Nebraska Medical Center	4025594200	986605 Nebraska Medical Center	Omaha	NE	United States of America
2874	www.uno.edu	University of New Orleans	5042806000	2000 Lakeshore Drive	New Orleans	LA	United States of America
2875	www.unoh.edu	University of Northwestern Ohio	4192273141	1441 N Cable Rd	Lima	OH	United States of America
2876	www.unomaha.edu	University of Nebraska at Omaha	4025542800	6001 Dodge St	Omaha	NE	United States of America
2877	www.unr.edu	University of Nevada - Reno	7757841110	1664 North Virginia Street	Reno	NV	United States of America
2878	www.unt.edu	University of North Texas	9405652000	1155 Union Circle #311277	Denton	TX	United States of America
2879	www.unva.edu	University of Northern Virginia	7033920771	10021 Balls Ford Road	Manassas	VA	United States of America
2880	www.uofa.edu	University of Atlanta	7703688877	6685 Peachtree Industrial Boulevard	Atlanta	GA	United States of America
2881	www.uog.edu	University of Guam	6717352990	J.U. Torres Drive	Mangilao	GU	United States of America
2882	www.uoregon.edu	University of Oregon	5413463014	110 Johnson Hall	Eugene	OR	United States of America
2883	www.up.edu	University of Portland	5039437911	5000 N Willamette Blvd	Portland	OR	United States of America
2884	www.upb.pitt.edu	University of Pittsburgh - Bradford	8143627500	300 Campus Drive	Bradford	PA	United States of America
2885	www.upenn.edu	University of Pennsylvania	2158985000	3451 Walnut Street	Philadelphia	PA	United States of America
2886	www.upj.pitt.edu	University of Pittsburgh - Johnstown	8142697000	450 Schoolhouse Rd	Johnstown	PA	United States of America
2887	www.upmc.edu	University of Pittsburgh Medical Center - Shadyside School of Nursing	4126232950	5230 Centre Ave	Pittsburgh	PA	United States of America
2888	www.upmc.edu	University of Pittsburgh Medical Center - Health System	4126473528	200 Lothrop St	Pittsburgh	PA	United States of America
2889	www.upmc.edu	UPMC Presbyterian Shadyside Dietetic Internship	4126232114	5230 Centre Avenue	Pittsburgh	PA	United States of America
2890	www.uprs.edu	University of Philosophical Research	8005484062	3910 Los Feliz Boulevard	Los Angeles	CA	United States of America
2891	www.ups.edu	University of Puget Sound	2538793100	1500 N Warner	Tacoma	WA	United States of America
2892	www.upsem.edu	Union Presbyterian Seminary	8043550671	3401 Brook Rd	Richmond	VA	United States of America
2893	www.upstate.edu	SUNY  Upstate Medical University	3154645540	750 E Adams St	Syracuse	NY	United States of America
2894	www.upt.pitt.edu	University of Pittsburgh - Titusville	8148274400	504 E Main St	Titusville	PA	United States of America
2895	www.urbana.edu	Urbana University	9374841301	579 College Way	Urbana	OH	United States of America
2896	www.urbancollege.edu	Urban College of Boston	6172924723	178 Tremont St 7th Fl	Boston	MA	United States of America
2897	www.ursinus.edu	Ursinus College	6104093000	601 E. Main St	Collegeville	PA	United States of America
2898	www.ursuline.edu	Ursuline College	4404494200	2550 Lander Rd	Pepper Pike	OH	United States of America
2899	www.usa.edu	University of St. Augustine for Health Sciences		One University Boulevard	St. Augustine	FL	United States of America
2900	www.usao.edu	University of Science and Arts of Oklahoma	4052243140	1727 West Alabama	Chickasha	OK	United States of America
2901	www.usc.edu	University of Southern California	2137402311	University Park	Los Angeles	CA	United States of America
2902	www.usca.edu	University of South Carolina - Aiken	8036486851	471 University Pkwy	Aiken	SC	United States of America
2903	www.uscareerinstitute.edu	U.S. Career Institute	8003477899	2001 Lowe Street	Fort Collins	CO	United States of America
2904	www.uscb.edu	University of South Carolina - Beaufort	8035214100	1 University Boulevard	Bluffton	SC	United States of America
2905	www.uscny.edu	Utica School of Commerce	3157332307	201 Bleecker St	Utica	NY	United States of America
2906	www.uscupstate.edu	University of South Carolina - Upstate	8645035000	800 University Way	Spartanburg	SC	United States of America
2907	www.usf.edu	University of South Florida	8139742011	4202 East Fowler Ave	Tampa	FL	United States of America
2908	www.usfca.edu	University of San Francisco	4154225555	2130 Fulton St	San Francisco	CA	United States of America
2909	www.usi.edu	University of Southern Indiana	8124648600	8600 University Blvd	Evansville	IN	United States of America
2910	www.usm.edu	University of Southern Mississippi	6012661000	118 College Drive # 0001	Hattiesburg	MS	United States of America
2911	www.usm.maine.edu	University of Southern Maine	2077804141	96 Falmouth St	Portland	ME	United States of America
2912	www.usma.edu	United States Military Academy	8459384200	Institutional Research/Analysis Branch	West  Point	NY	United States of America
2913	www.usml.edu	University of Saint Mary of the Lake Mundelein Seminary	8475666401	1000 E Maple Ave	Mundelein	IL	United States of America
2914	www.usn.edu	Roseman University of Health Sciences		11 Sunset  Way	Henderson	NV	United States of America
2915	www.usna.edu	United States Naval Academy	4102931000	121 Blake Road	Annapolis	MD	United States of America
2916	www.usouthal.edu	University of South Alabama	3344606101	307 N University Blvd	Mobile	AL	United States of America
2917	www.usp.edu	University of the Sciences	2155968800	600 S 43rd St	Philadelphia	PA	United States of America
2918	www.ussa.edu	United States Sports Academy	2516263303	One Academy Dr	Daphne	AL	United States of America
2919	www.usu.edu	Utah State University	4357971000	Old Main Hill	Logan	UT	United States of America
2920	www.usw.edu	University of the Southwest	5053926565	6610 Lovington Hwy	Hobbs	NM	United States of America
2921	www.ut.edu	The University of Tampa	8132533333	401 W Kennedy Blvd	Tampa	FL	United States of America
2922	www.uta.edu	The University of Texas at Arlington	8172722011	701 S. Nedderman Dr.	Arlington	TX	United States of America
2923	www.utah.edu	University of Utah	8015817200	201 Presidents Circle	Salt Lake City	UT	United States of America
2924	www.utahcollege.edu	Broadview University - West Jordan	8013044224	1902 W 7800 S	West Jordan	UT	United States of America
2925	www.utb.edu	The University of Texas at Brownsville and Texas Southmost College	9565448200	80 Fort Brown	Brownsville	TX	United States of America
2926	www.utc.edu	The University of Tennessee - Chattanooga	4234254111	615 McCallie Ave	Chattanooga	TN	United States of America
2927	www.utdallas.edu	The University of Texas at Dallas	9728832111	800 West Campbell  Rd	Richardson	TX	United States of America
2928	www.utep.edu	The University of Texas at El Paso	9157475000	500 W. University Ave	El Paso	TX	United States of America
2929	www.utexas.edu	University of Texas at Austin	5124713434	1 University Station	Austin	TX	United States of America
2930	www.uthscsa.edu	The University of Texas Health Science - San Antonio	2105672621	7703 Floyd Curl Dr	San Antonio	TX	United States of America
2931	www.utica.edu	Utica College	3157923111	1600 Burrstone Rd	Utica	NY	United States of America
2932	www.utm.edu	The University of Tennessee - Martin	7318817000	University Street	Martin	TN	United States of America
2933	www.utmb.edu	The University of Texas Medical Branch	4097721011	301 University Blvd	Galveston	TX	United States of America
2934	www.utoledo.edu	University of Toledo	4195304636	2801 W Bancroft	Toledo	OH	United States of America
2935	www.utpa.edu	The University of Texas - Pan American	9563812011	1201 W University Dr	Edinburg	TX	United States of America
2936	www.utpb.edu	The University of Texas of the Permian Basin	4325522020	4901 E University	Odessa	TX	United States of America
2937	www.uts.edu	Unification Theological Seminary	8457523000	30 Seminary Drive	Barrytown	NY	United States of America
2938	www.utsa.edu	The University of Texas at San Antonio	2104584011	One UTSA Circle	San Antonio	TX	United States of America
2939	www.utsnyc.edu	Union Theological Seminary	2126627100	3041 Broadway	New York	NY	United States of America
2940	www.utsouthwestern.edu	University of Texas Southwestern Medical Center	2146483606	5323 Harry Hines Blvd	Dallas	TX	United States of America
2941	www.uttyler.edu	The University of Texas at Tyler	9035667000	3900 University Blvd	Tyler	TX	United States of America
2942	www.utulsa.edu	University of Tulsa	9186312305	800 South Tucker Drive	Tulsa	OK	United States of America
2943	www.uu.edu	Union University	7316681818	1050 Union University Dr	Jackson	TN	United States of America
2944	www.uvawise.edu	The University of Virginia's College at Wise	2763280100	1 College Avenue	Wise	VA	United States of America
2945	www.uvi.edu	University of the Virgin Islands	3407769200	2 John Brewers Bay	Charlotte Amalie	VI	United States of America
2946	www.uvm.edu	University of Vermont	8026563131	85 S Prospect St	Burlington	VT	United States of America
2947	www.uvu.edu	Utah Valley University	8018638000	800 W University Parkway	Orem	UT	United States of America
2948	www.uwa.edu	University of West Alabama	2056523400	205 North Washington Street	Livingston	AL	United States of America
2949	www.uwc.edu	University of Wisconsin Colleges	6082621783	780 Regent St	Madison	WI	United States of America
2950	www.uwec.edu	University of Wisconsin - Eau Claire	7158362637	105 Garfield Avenue	Eau Claire	WI	United States of America
2951	www.uwla.edu	The University of West Los Angeles	3103425200	9920 S. La Cienega Blvd. #404	Inglewood	CA	United States of America
2952	www.uwlax.edu	University of Wisconsin - La Crosse	6087858000	1725 State St	La Crosse	WI	United States of America
2953	www.uwm.edu	University of Wisconsin - Milwaukee	4142291122	PO Box 413	Milwaukee	WI	United States of America
2954	www.uwosh.edu	University of Wisconsin - Oshkosh	9204241234	800 Algoma Blvd	Oshkosh	WI	United States of America
2955	www.uwp.edu	University of Wisconsin - Parkside	2625952573	900 Wood Road Box 2000	Kenosha	WI	United States of America
2956	www.uwrf.edu	University of Wisconsin - River Falls	7154253913	410 S 3rd St	River Falls	WI	United States of America
2957	www.uwsp.edu	University of Wisconsin - Stevens Point	7153464301	2100 Main St	Stevens Point	WI	United States of America
2958	www.uwstout.edu	University of Wisconsin - Stout	7152321431	712 Broad Way Street	Menomonie	WI	United States of America
2959	www.uwsuper.edu	University of Wisconsin - Superior	7153948101	Belknap & Catlin	Superior	WI	United States of America
2960	www.uww.edu	University of Wisconsin - Whitewater	2624721234	800 W Main St	Whitewater	WI	United States of America
2961	www.uwyo.edu	University of Wyoming	3077661121	1000 E. University Ave.	Laramie	WY	United States of America
2962	www.valdosta.edu	Valdosta State University	9123335800	1500 N Patterson	Valdosta	GA	United States of America
2963	www.valleycollege.edu	San Bernardino Valley College	9093844401	701 South Mount Vernon Avenue	San Bernardino	CA	United States of America
2964	www.valpo.edu	Valparaiso University	2194645000	1700 Chapel Drive OP Kretzmann Hall	Valparaiso	IN	United States of America
2965	www.vanderbilt.edu	Vanderbilt University	6153227311	2101 West End Avenue	Nashville	TN	United States of America
2966	www.vandercook.edu	VanderCook College of Music	3122256288	3140 S. Federal St.	Chicago	IL	United States of America
2967	www.vanguard.edu	Vanguard University of Southern California	7145563610	55 Fair Dr	Costa Mesa	CA	United States of America
2969	www.vatterott-college.edu	Vatterott College - Quincy	8004385621	3609 North Marx Drive	Quincy	IL	United States of America
2970	www.vaughn.edu	Vaughn College of Aeronautics and Technology	7184296600	86-01 23rd Avenue	Flushing	NY	United States of America
2971	www.vbc.edu	Virginia Baptist College	5407855440	4105 Plank Road	Fredericksburg	VA	United States of America
2972	www.vc.edu	Virginia College - Birmingham	2058021200	488 Palisades Boulevard	Birmingham	AL	United States of America
2973	www.vcc.edu	Vermilion Community College	2183657200	1900 E Camp St	Ely	MN	United States of America
2974	www.vcsu.edu	Valley City State University	7018457990	101 SW College St.	Valley City	ND	United States of America
2975	www.vct.edu	Valley College - Martinsburg	3042630979	287 Aikens Ctr Edwin Miller Blvd	Martinsburg	WV	United States of America
2976	www.vcu.edu	Virginia Commonwealth University	8048280100	910 W Franklin St	Richmond	VA	United States of America
2977	www.vennard.edu	Vennard College	6416738391	2300 8th Ave E	University Park	IA	United States of America
2978	www.venturacollege.edu	Ventura College	8056546400	4667 Telegraph Rd	Ventura	CA	United States of America
2979	www.vermontcollege.edu	Vermont College of Fine Arts	8028280600	36 College Street	Montpelier	VT	United States of America
2980	www.vermontlaw.edu	Vermont Law School	8002271395	164 Chelsea St	South Royalton	VT	United States of America
2981	www.vernoncollege.edu	Vernon College	9405526291	4400 College Dr	Vernon	TX	United States of America
2982	www.vfcc.edu	Valley Forge Christian College	6109350450	1401 Charlestown Road	Phoenixville	PA	United States of America
2983	www.vfmac.edu	Valley Forge Military College	6109891203	1001 Eagle Rd Sorley House	Wayne	PA	United States of America
2984	www.vgcc.edu	Vance-Granville Community College	2524922061	PO Box 917 State Rd 1126	Henderson	NC	United States of America
2985	www.vhcc.edu	Virginia Highlands Community College	2767392400	100 VHCC Drive	Abingdon	VA	United States of America
2986	www.vic.edu	Virginia Intermont College	2766696101	1013 Moore Street	Bristol	VA	United States of America
2987	www.victoriacollege.edu	Victoria College	3615733291	2200 E Red River	Victoria	TX	United States of America
2988	www.victory.edu	Victory University	9013209700	255 North Highland	Memphis	TN	United States of America
2989	www.villa.edu	Villa Maria College Buffalo	7168960700	240 Pine Ridge Rd	Buffalo	NY	United States of America
2990	www.villanova.edu	Villanova University	6105194500	800 Lancaster Avenue	Villanova	PA	United States of America
2991	www.vinu.edu	Vincennes University	8128888888	1002 N First St	Vincennes	IN	United States of America
2992	www.virginia.edu	University of Virginia	4349240311	1707 University Avenue	Charlottesville	VA	United States of America
2993	www.virginiawestern.edu	Virginia Western Community College	5408577200	3095 Colonial Ave	Roanoke	VA	United States of America
2994	www.viterbo.edu	Viterbo University	6087963000	900 Viterbo Drive	La Crosse	WI	United States of America
2995	www.vmced.edu	Virginia Marti College of Art and Design	2162218584	11724 Detroit Avenue	Lakewood	OH	United States of America
2996	www.vmi.edu	Virginia Military Institute	5404647207		Lexington	VA	United States of America
2997	www.volstate.edu	Volunteer State Community College	6154528600	1480 Nashville Pike	Gallatin	TN	United States of America
2998	www.voorhees.edu	Voorhees College	8037933351	481 Porter Drive	Denmark	SC	United States of America
2999	www.vsu.edu	Virginia State University	8045245000	One Hayden Street	Petersburg	VA	United States of America
3000	www.vtc.edu	Vermont Technical College	8027281000	1 Main Street	Randolph Center	VT	United States of America
3001	www.vts.edu	Virginia Theological Seminary	7033706600	3737 Seminary Road	Alexandria	VA	United States of America
3002	www.vul.edu	Virginia University of Lynchburg	4345285276	2058 Garfield Ave	Lynchburg	VA	United States of America
3003	www.vuu.edu	Virginia Union University	8042575600	1500 N Lombardy St	Richmond	VA	United States of America
3004	www.vvc.edu	Victor Valley College	7602454271	18422 Bear Valley Rd	Victorville	CA	United States of America
3005	www.vwc.edu	Virginia Wesleyan College	7574553200	1584 Wesleyan Dr	Norfolk	VA	United States of America
3006	www.wabash.edu	Wabash College	7653616100	P.O. Box 352	Crawfordsville	IN	United States of America
3007	www.waco.tstc.edu	Texas State Technical College - Waco	2547993611	3801 Campus Dr	Waco	TX	United States of America
3008	www.wagner.edu	Wagner College	7183903100	One Campus Rd	Staten Island	NY	United States of America
3009	www.waketech.edu	Wake Technical Community College	9196623400	9101 Fayetteville Road	Raleigh	NC	United States of America
3010	www.waldenu.edu	Walden University	8009253368	155 Fifth Ave S	Minneapolis	MN	United States of America
3011	www.waldorf.edu	Waldorf College	6415852450	106 S Sixth St	Forest City	IA	United States of America
3012	www.wallace.edu	George C Wallace Community College - Dothan	3349833521	1141 Wallace Drive	Dothan	AL	United States of America
3013	www.wallacestate.edu	Wallace State Community College  - Hanceville	2563528000	801 Main St. P. O. Box 2000	Hanceville	AL	United States of America
3014	www.wallawalla.edu	Walla Walla University	5095272615	204 S College Ave	College Place	WA	United States of America
3015	www.walnuthillcollege.edu	The Restaurant School at Walnut Hill College	2152224200	4207 Walnut St	Philadelphia	PA	United States of America
3016	www.walsh.edu	Walsh University	3304997090	2020 East Maple St	North Canton	OH	United States of America
3017	www.walshcollege.edu	Walsh College of Accountancy and Business Administration	2486898282	3838 Livernois	Troy	MI	United States of America
3018	www.warner.edu	Warner University	8636381426	13895 Hwy 27	Lake Wales	FL	United States of America
3019	www.warnerpacific.edu	Warner Pacific College	5035171000	2219 SE 68th Ave	Portland	OR	United States of America
3020	www.warren-wilson.edu	Warren Wilson College	8282983325	701 Warren Wilson Rd	Swannanoa	NC	United States of America
3021	www.warren.edu	Warren County Community College	9088359222	475 Rte 57 W	Washington	NJ	United States of America
3022	www.wartburg.edu	Wartburg College	3193528200	100 Wartburg Blvd.	Waverly	IA	United States of America
3023	www.wartburgseminary.edu	Wartburg Theological Seminary	5635890200	333 Wartburg Place	Dubuque	IA	United States of America
3024	www.washburn.edu	Washburn University	7852311010	1700 SW College Avenue	Topeka	KS	United States of America
3025	www.washcoll.edu	Washington College	4107782800	300 Washington Ave	Chestertown	MD	United States of America
3026	www.washington.edu	University of Washington-Seattle Campus	2065432100	P.O. Box 351230	Seattle	WA	United States of America
3027	www.washjeff.edu	Washington & Jefferson College	7242224400	60 S Lincoln St	Washington	PA	United States of America
3028	www.watc.edu	Wichita Area Technical College	3166779282	301 South Grove	Wichita	KS	United States of America
3029	www.wau.edu	Washington Adventist University	3018914000	7600 Flower Ave	Takoma Park	MD	United States of America
3030	www.waubonsee.edu	Waubonsee Community College	6304667900	Rte 47 at Waubonsee Drive	Sugar Grove	IL	United States of America
3031	www.waycross.edu	Waycross College	9122856133	2001 S Georgia Pky	Waycross	GA	United States of America
3032	www.wayne.edu	Wayne State University	3135772424	656 West Kirby Street	Detroit	MI	United States of America
3033	www.wayne.uakron.edu	University of Akron - Wayne College	8002218308	1901 Smucker Rd	Orrville	OH	United States of America
3034	www.waynecc.edu	Wayne Community College	9197355151	3000 Wayne Memorial Dr	Goldsboro	NC	United States of America
3035	www.waynesburg.edu	Waynesburg University	7246278191	51 W College St	Waynesburg	PA	United States of America
3036	www.wbcoll.edu	Williams Baptist College	8708866741	60 W Fulbright Avenue	Walnut Ridge	AR	United States of America
3037	www.wbcs.edu	Washington Baptist University	7033335904	4300 Evergreen Lane	Annandale	VA	United States of America
3038	www.wbi.edu	Western Beauty Institute	8188949550	8700 Van Nuys Blvd	Panorama City	CA	United States of America
3039	www.wbs.edu	Wesley Biblical Seminary	6013668880	787 E. Northside Drive	Jackson	MS	United States of America
3040	www.wbu.edu	Wayland Baptist University	8062911000	1900 W 7th St.	Plainview	TX	United States of America
3041	www.wc.edu	Weatherford College	8175945471	225 College Park Drive	Weatherford	TX	United States of America
3042	www.wcc.vccs.edu	Wytheville Community College	2762234700	1000 E Main St	Wytheville	VA	United States of America
3043	www.wccc.me.edu	Washington County Community College	2074541000	One College Drive	Calais	ME	United States of America
3044	www.wcccd.edu	Wayne County Community College District	3134962600	801 W Fort St	Detroit	MI	United States of America
3045	www.wccnet.edu	Washtenaw Community College	7349733543	4800 E Huron River Dr	Ann Arbor	MI	United States of America
3046	www.wccs.edu	George Corley Wallace State Community College - Selma	3348769227	3000 Earl Goodwin Parkway	Selma	AL	United States of America
3047	www.wcjc.edu	Wharton County Junior College	9795324560	911 Boling Hwy	Wharton	TX	United States of America
3048	www.wcsu.edu	Western Connecticut State University	2038378200	181 White Street	Danbury	CT	United States of America
3049	www.wctc.edu	Waukesha County Technical College	2626915566	800 Main Street	Pewaukee	WI	United States of America
3050	www.wcu.edu	Western Carolina University	8282277211		Cullowhee	NC	United States of America
3051	www.wcupa.edu	West Chester University of Pennsylvania	6104361000	University Avenue and  High Street	West Chester	PA	United States of America
3052	www.wdt.edu	Western Dakota Technical Institute	6053944034	800 Mickelson Dr.	Rapid City	SD	United States of America
3053	www.webb-institute.edu	Webb Institute	5166712213	298 Crescent Beach Rd	Glen Cove	NY	United States of America
3054	www.webber.edu	Webber International University	8636381431	1201 N Scenic Hwy	Babson Park	FL	United States of America
3055	www.weber.edu	Weber State University	8016266000	3750 Harrison Blvd	Ogden	UT	United States of America
3056	www.webster.edu	Webster University	3149682660	470 E Lockwood Ave.	Saint Louis	MO	United States of America
3057	www.wellesley.edu	Wellesley College	7812831000	106 Central St	Wellesley	MA	United States of America
3058	www.wells.edu	Wells College	3153643266	170 State Rte 90	Aurora	NY	United States of America
3059	www.wesley.edu	Wesley College	3027362300	120 N State St	Dover	DE	United States of America
3060	www.wesleyancollege.edu	Wesleyan College	4784771110	4760 Forsyth Rd	Macon	GA	United States of America
3061	www.wesleycollege.edu	Wesley College	6018452265	111 Wesley Cir	Florence	MS	United States of America
3062	www.wesleyseminary.edu	Wesley Theological Seminary	2028858600	4500 Massachusetts Ave NW	Washington	DC	United States of America
3063	www.westcentraltech.edu	West Central Technical College	7705376000	176 Murphy Campus Blvd.	Waco	GA	United States of America
3064	www.westech.edu	Westech College	9099804474	3491 E. Concours Ave	Ontario	CA	United States of America
3065	www.western.edu	Western State College of Colorado	9709430120	600 N Adams	Gunnison	CO	United States of America
3066	www.westernsem.edu	Western Theological Seminary	6163928555	101 E 13th St	Holland	MI	United States of America
3067	www.westernseminary.edu	Western Seminary	5035171800	5511 SE Hawthorne Blvd	Portland	OR	United States of America
3068	www.westernu.edu	Western University of Health Sciences	9096236116	309 E 2nd St	Pomona	CA	United States of America
3069	www.westga.edu	University of West Georgia	6788395000	1601 Maple St	Carrollton	GA	United States of America
3070	www.westgatech.edu	West Georgia Technical College	7068454323	303 Fort Dr	LaGrange	GA	United States of America
3071	www.westkentucky.kctcs.edu	West Kentucky Community and Technical College	2705549200	4810 Alben Barkley Drive	Paducah	KY	United States of America
3072	www.westlawn.edu	Westlawn Institute of Marine Technology	2078536600	16 Deep Cove Road	Eastport	ME	United States of America
3073	www.westminster.edu	Westminster College	7249468761	North Market  Street	New Wilmington	PA	United States of America
3074	www.westminstercollege.edu	Westminster College	8014847651	1840 South 1300 East	Salt Lake City	UT	United States of America
3075	www.westmont.edu	Westmont College	8055656000	955 La Paz Rd	Santa Barbara	CA	United States of America
3076	www.westoahu.hawaii.edu	University of Hawaii - West Oahu	8084544700	96-129 Ala Ike	Pearl City	HI	United States of America
3077	www.westshore.edu	West Shore Community College	2318450824	3000 N Stiles Rd	Scottville	MI	United States of America
3078	www.westtexas.tstc.edu	Texas State Technical College - West Texas	3252357300	300 Homer K. Taylor Drive	Sweetwater	TX	United States of America
3079	www.westvalley.edu	West Valley College	4088672200	14000 Fruitvale Ave	Saratoga	CA	United States of America
3080	www.westwood.edu	Redstone College	8008883995	10851 W 120th Ave	Broomfield	CO	United States of America
3081	www.wfu.edu	Wake Forest University	3367585255	1834 Wake Forest Road	Winston Salem	NC	United States of America
3082	www.whatcom.ctc.edu	Whatcom Community College	3606762170	237 W Kellogg Rd	Bellingham	WA	United States of America
3083	www.wheaton.edu	Wheaton College	6307525000	501 College Ave	Wheaton	IL	United States of America
3084	www.wheatoncollege.edu	Wheaton College	5082857722	26 E Main St	Norton	MA	United States of America
3085	www.wheelock.edu	Wheelock College	6177345200	200 the Riverway	Boston	MA	United States of America
3086	www.whitman.edu	Whitman College	5095275111	345 Boyer Ave	Walla Walla	WA	United States of America
3087	www.whitworth.edu	Whitworth University	5097771000	300 W Hawthorne Rd	Spokane	WA	United States of America
3088	www.wichita.edu	Wichita State University	3169783456	1845 Fairmount	Wichita	KS	United States of America
3089	www.widener.edu	Widener University - Main Campus	6104994000	One University Place	Chester	PA	United States of America
3090	www.wilberforce.edu	Wilberforce University	9373762911	1055 N Bickett Rd	Wilberforce	OH	United States of America
3091	www.wileyc.edu	Wiley College	9039273300	711 Wiley Ave	Marshall	TX	United States of America
3092	www.wilkes.edu	Wilkes University	5704085000	84 West South Street	Wilkes-Barre	PA	United States of America
3093	www.wilkescc.edu	Wilkes Community College	3368386100	1328 South Collegiate Dr	Wilkesboro	NC	United States of America
3094	www.willamette.edu	Willamette University	5033706300	900 State St	Salem	OR	United States of America
3095	www.williams.edu	Williams College	4135973131	880 Main St	Williamstown	MA	United States of America
3096	www.williamson.edu	The Williamson Free School of Mechanical Trades	6105661776	106 S New Middletown Road	Media	PA	United States of America
3097	www.williamsoncc.edu	Williamson College	6157717821	200 Seaboard Lane	Franklin	TN	United States of America
3098	www.williamtyndale.edu	William Tyndale College	8004830707	35700 W Twelve Mile Road	Farmington Hills	MI	United States of America
3099	www.williamwoods.edu	William Woods University	5736422251	One University Avenue	Fulton	MO	United States of America
3100	www.wilmington.edu	Wilmington College	8003419318	251 Ludovic St	Wilmington	OH	United States of America
3101	www.wilmu.edu	Wilmington University	3023289401	320 Dupont Highway	New Castle	DE	United States of America
3102	www.wilson.edu	Wilson College	7172644141	1015 Philadelphia Ave	Chambersburg	PA	United States of America
3103	www.wiltech.edu	Williamsburg Technical College	8433554110	601 Martin Luther King Jr Ave	Kingstree	SC	United States of America
3104	www.windward.hawaii.edu	Windward Community College	8082357400	45-720 Keaahala Rd	Kaneohe	HI	United States of America
3105	www.winebrenner.edu	Winebrenner Theological Seminary	4194344200	950 North Main Street	Findlay	OH	United States of America
3106	www.wingate.edu	Wingate University	7042338000	220 North Camden Road	Wingate	NC	United States of America
3107	www.winner-institute.edu	Winner Institute of Arts & Sciences	7246462433	One Winner Place	Transfer	PA	United States of America
3108	www.winona.edu	Winona State University	5074575000	8th and Johnson St	Winona	MN	United States of America
3109	www.winthrop.edu	Winthrop University	8033232211	701 Oakland Avenue	Rock Hill	SC	United States of America
3110	www.wintu.edu	Western International University	6029432311	1601 W. Fountainhead Parkway	Tempe	AZ	United States of America
3111	www.wiregrass.edu	Wiregrass Georgia Technical College	2293332100	4089 Valtech Rd	Valdosta	GA	United States of America
3112	www.wisc.edu	University of Wisconsin - Madison	6082621234	500 Lincoln Dr	Madison	WI	United States of America
3113	www.witc.edu	Wisconsin Indianhead Technical College	7154682815	505 Pine Ridge Drive	Shell Lake	WI	United States of America
3114	www.wittenberg.edu	Wittenberg University	9373276231	Ward St at N Wittenberg Ave	Springfield	OH	United States of America
3115	www.wiu.edu	Western Illinois University	3092951414	1 University Circle	Macomb	IL	United States of America
3116	www.wju.edu	Wheeling Jesuit University	3042432000	316 Washington Ave	Wheeling	WV	United States of America
3117	www.wku.edu	Western Kentucky University	2707450111	1906 College Heights Blvd	Bowling Green	KY	United States of America
3118	www.WLAC.edu	West Los Angeles College	3102874200	9000 Overland Avenue	Culver City	CA	United States of America
3119	www.wlc.edu	Wisconsin Lutheran College	4144438800	8800 W Bluemound Rd	Milwaukee	WI	United States of America
3120	www.wlu.edu	Washington and Lee University	5404588400	204 West Washington Street	Lexington	VA	United States of America
3121	www.wm.edu	College of William and Mary	7572214000	P.O. Box 8795	Williamsburg	VA	United States of America
3122	www.wmcarey.edu	William Carey University	6013185051	498 Tuscan Ave	Hattiesburg	MS	United States of America
3123	www.wmich.edu	Western Michigan University	2693873530	1903 West Michigan Avenue	Kalamazoo	MI	United States of America
3124	www.wmitchell.edu	William Mitchell College of Law	6512279171	875 Summit Ave	Saint Paul	MN	United States of America
3125	www.wmpenn.edu	William Penn University	6416731001	201 Trueblood Ave	Oskaloosa	IA	United States of America
3126	www.wmu.edu	World Mission University	2133882322	500 S. Shatto Pl Ste 600	Los Angeles	CA	United States of America
3127	www.wnc.edu	Western Nevada College	7754453000	2201 West College Parkway	Carson City	NV	United States of America
3128	www.wnec.edu	Western New England College	4137823111	1215 Wilbraham Rd	Springfield	MA	United States of America
3129	www.wnmu.edu	Western New Mexico University	5055386336	1000 W. College Ave	Silver City	NM	United States of America
3130	www.wofford.edu	Wofford College	8645974000	429 N Church St	Spartanburg	SC	United States of America
3131	www.wolford.edu	Wolford College		4933 Tamiami Trail	Naples	FL	United States of America
3132	www.woodbury-college.edu	Woodbury College	8022290516	660 Elm St	Montpelier	VT	United States of America
3133	www.woodbury.edu	Woodbury University	8187670888	7500 Glenoaks Blvd	Burbank	CA	United States of America
3134	www.wooster.edu	The College of Wooster	3302632000	1189 Beall Avenue	Wooster	OH	United States of America
3135	www.worcester.edu	Worcester State University	5089298000	486 Chandler St	Worcester	MA	United States of America
3136	www.worwic.edu	Wor-Wic Community College	4103342800	32000 Campus Drive	Salisbury	MD	United States of America
3137	www.wosc.edu	Western Oklahoma State College	5804772000	2801 N Main St	Altus	OK	United States of America
3138	www.wou.edu	Western Oregon University	5038388000	345 N Monmouth Ave	Monmouth	OR	United States of America
3139	www.wp.smsu.edu	Missouri State University-West Plains	4172557255	128 Garfield Avenue	West Plains	MO	United States of America
3140	www.wpcc.edu	Western Piedmont Community College	8284386141	1001 Burkemont Ave	Morganton	NC	United States of America
3141	www.wpi.edu	Worcester Polytechnic Institute	5088315000	100 Institute Road	Worcester	MA	United States of America
3142	www.wpunj.edu	William Paterson University of New Jersey	9737202000	300 Pompton Rd	Wayne	NJ	United States of America
3143	www.wright.edu	Wright State University	9377753333	3640 Colonel Glenn Highway	Dayton	OH	United States of America
3144	www.wrightinst.edu	The Wright Institute	5108419230	2728 Durant Ave	Berkeley	CA	United States of America
3145	www.ws.edu	Walters State Community College	4235852600	500 S Davy Crockett Pky	Morristown	TN	United States of America
3146	www.wsc.edu	Wayne State College	4023757000	1111 Main St	Wayne	NE	United States of America
3147	www.wsc.ma.edu	Westfield State University	4135725300	577 Western Ave	Westfield	MA	United States of America
3148	www.wsc.nodak.edu	Williston State College	7017744200	1410 University Ave	Williston	ND	United States of America
3149	www.wscal.edu	Westminster Seminary California	7604808474	1725 Bear Valley Parkway	Escondido	CA	United States of America
3150	www.wscc.edu	Washington State Community College	7403748716	710 Colegate Dr	Marietta	OH	United States of America
3151	www.wscn.edu	Resurrection University	7087636530	1431 N. Claremont Avenue	Chicago	IL	United States of America
3152	www.wspp.edu	Wisconsin School of Professional Psychology	4144649777	9120 W Hampton Ave	Milwaukee	WI	United States of America
3153	www.wssu.edu	Winston-Salem State University	3367502000	601 Martin Luther King Jr Dr	Winston-Salem	NC	United States of America
3154	www.wsu.edu	Washington State University	5093353564	French Administration Building	Pullman	WA	United States of America
3155	www.wsulaw.edu	Western State University - College of Law	7147381000	1111 N State College Blvd	Fullerton	CA	United States of America
3156	www.wtamu.edu	West Texas A & M University	8066512000	2501 4th Ave	Canyon	TX	United States of America
3157	www.wtc.edu	Western Texas College	3255738511	6200 College Ave	Snyder	TX	United States of America
3158	www.wti.edu	Wichita Technical Institute	3169432241	2051 South Meridian	Wichita	KS	United States of America
3159	www.wts.edu	Westminster Theological Seminary	2158875511	2960 W Church Rd	Glenside	PA	United States of America
3160	www.wtu.edu	Washington Theological Union	2027268800	6896 Laurel St NW	Washington	DC	United States of America
3161	www.wustl.edu	Washington University in St Louis	3149355000	One Brookings Dr	Saint Louis	MO	United States of America
3162	www.wvbc.edu	West Virginia Business College - Wheeling	3042320361	1052 Main St	Wheeling	WV	United States of America
3163	www.wvc.edu	Wenatchee Valley College	5096826800	1300 Fifth St	Wenatchee	WA	United States of America
3164	www.wvjcmorgantown.edu	West Virginia Junior College - Morgantown	3042968282	148 Willey St	Morgantown	WV	United States of America
3165	www.wvncc.edu	West Virginia Northern Community College	3042335900	1704 Market St.	Wheeling	WV	United States of America
3166	www.wvsctc.edu	Kanawha Valley Community and Technical College	3047663118	2000 Union Carbide Drive	South Charleston	WV	United States of America
3167	www.wvsom.edu	West Virginia School of Osteopathic Medicine	3046456270	400 N Lee St	Lewisburg	WV	United States of America
3168	www.wvstateu.edu	West Virginia State University	3047663000	Rte 25	Institute	WV	United States of America
3169	www.wvu.edu	West Virginia University	3042930111	Presidents Office Box 6201	Morgantown	WV	United States of America
3170	www.wvup.edu	West Virginia University at Parkersburg	3044248000	300 Campus Dr	Parkersburg	WV	United States of America
3171	www.wvwc.edu	West Virginia Wesleyan College	3044738000	59 College Ave	Buckhannon	WV	United States of America
3172	www.wwc.edu	Walla Walla College		10345 SE Market Street	Portland	OR	United States of America
3173	www.wwcc.edu	Walla Walla Community College	5095222500	500 Tausick Way	Walla Walla	WA	United States of America
3174	www.wwcc.wy.edu	Western Wyoming Community College	3073821600	2500 College Dr	Rock Springs	WY	United States of America
3175	www.wwu.edu	Western Washington University	3606503430	516 High St	Bellingham	WA	United States of America
3176	www.lac.edu	LA College International	2133813333	3200 Wilshire Blvd. #400	Los Angeles	CA	United States of America
3177	www.wyotech.edu	WyoTech	3862550295	470 Destination Daytona Lane	Ormond Beach	FL	United States of America
3178	www.xavier.edu	Xavier University	5137453000	3800 Victory Parkway	Cincinnati	OH	United States of America
3179	www.xula.edu	Xavier University of Louisiana	5044867411	One Drexel Drive	New Orleans	LA	United States of America
3180	www.yale.edu	Berkeley Divinity School	2034329285	409 Prospect Street	New Haven	CT	United States of America
3181	www.ybi.edu	Yorktowne Business Institute	7178465000	West Seventh Avenue	York	PA	United States of America
3182	www.yccc.edu	York County Community College	2076469282	112 College Drive	Wells	ME	United States of America
3183	www.yccd.edu	Yuba College	5307416700	2088 N Beale Rd	Marysville	CA	United States of America
3184	www.ycm.edu	The Youngstown College of Massotherapy	3307551406	14 Highland Ave	Struthers	OH	United States of America
3185	www.ycp.edu	York College of Pennsylvania	7178467788	Country Club Rd	York	PA	United States of America
3186	www.yhc.edu	Young Harris College	7063793111	1 College Street	Young Harris	GA	United States of America
3187	www.york.cuny.edu	York College of the City University of New York	7182622000	94-20 Guy R Brewer Blvd	Jamaica	NY	United States of America
3188	www.york.edu	York College	4023635600	1125 E 8th St	York	NE	United States of America
3189	www.yosan.edu	Yo San University of Traditional Chinese Medicine	3105773000	13315 W. Washington Boulevard	Los Angeles	CA	United States of America
3190	www.ysu.edu	Youngstown State University	8774686978	One University Plaza	Youngstown	OH	United States of America
3191	www.yti.edu	York Technical Institute	7177571100	1405 Williams Rd	York	PA	United States of America
3192	www.yu.edu	Yeshiva University	2129605285	500 W 185th St	New York	NY	United States of America
3193	www.yvcc.edu	Yakima Valley Community College	5095744600	Sixteenth and Nob Hill Boulevard	Yakima	WA	United States of America
3194	www.zanestate.edu	Zane State College	7404542501	1555 Newark Rd	Zanesville	OH	United States of America
3195	www.zbc.edu	Northpoint Bible College	9784783400	320 S. Main Street	Haverhill	MA	United States of America
3196	www.davidson.edu	Davidson College	7048942000	102 N. Main Street	Davidson	NC	United States of America
3197	www.southplainscollege.edu	South Plains College	8068949611	1401 S. College Ave	Levelland	TX	United States of America
3198	deleted.edu	deleted					
\.


--
-- Name: schedule_school_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('schedule_school_id_seq', 3198, true);


--
-- Name: schedule_school_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY schedule_school
    ADD CONSTRAINT schedule_school_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

