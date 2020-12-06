import naive as nv
import KMP as kmp
import rabinKarp as rk
import time

def timeAnalysis(pat,txt):
    t1_avg = 0
    t2_avg = 0
    t3_avg = 0
    for _ in range(10):
        t1 = time.process_time()
        nv.naiveMatching(pat, txt)
        t1 = time.process_time() - t1
        t1_avg += t1
        # print([pat, txt])

        t2 = time.process_time()
        rk.rabin_karp_search(pat, txt)
        t2 = time.process_time() - t2
        t2_avg += t2
        # print([pat, txt])

        t3 = time.process_time()
        kmp.KMPSearch(pat, txt)
        t3 = time.process_time() - t3
        t3_avg += t3
        # print([pat, txt])

    t1_avg/=100
    t2_avg/=100
    t3_avg/=100

    print("Naive:" + str(t1_avg))
    print("Rabin:" + str(t2_avg))
    print("Knuth:" + str(t3_avg))


print("_______________________________")
''' ---------- Case 1 ----------
        No Match'''

txt = "brow" * 200000
pat = "brown"
print("Case 1: No Match")
timeAnalysis(pat, txt)
print("_______________________________")

''' ---------- Case 2 ----------
        No Matches For First Character of Pattern'''
txt = "the quick brown fox jumped over the lazy dog." * 200000
pat = "power"
print("Case 2: No Matches For First Character of Pattern")
timeAnalysis(pat, txt)
print("_______________________________")

''' ---------- Case 3 ----------
        Multiple Matches'''
txt = "the quick brown fox jumped over the lazy dog." * 200000
pat = "over"
print("Case 3: Multiple Matches")
timeAnalysis(pat, txt)
print("_______________________________")

''' ---------- Case 4 ----------
        Many Matches'''
txt = "A" * 200000
pat = "AAA"
print("Case 4: many Matches")
timeAnalysis(pat, txt)
print("_______________________________")

''' ---------- Case 5 ----------
        Real World Example'''
txt = '''One advanced diverted domestic sex repeated bringing you old. Possible procured her trifling laughter thoughts property she met way. Companions shy had solicitude favourable own. Which could saw guest man now heard but. Lasted my coming uneasy marked so should. Gravity letters it amongst herself dearest an windows by. Wooded ladies she basket season age her uneasy saw. Discourse unwilling am no described dejection incommode no listening of. Before nature his parish boy. 
Folly words widow one downs few age every seven. If miss part by fact he park just shew. Discovered had get considered projection who favourable. Necessary up knowledge it tolerably. Unwilling departure education is be dashwoods or an. Use off agreeable law unwilling sir deficient curiosity instantly. Easy mind life fact with see has bore ten. Parish any chatty can elinor direct for former. Up as meant widow equal an share least. 
Another journey chamber way yet females man. Way extensive and dejection get delivered deficient sincerity gentleman age. Too end instrument possession contrasted motionless. Calling offence six joy feeling. Coming merits and was talent enough far. Sir joy northward sportsmen education. Discovery incommode earnestly no he commanded if. Put still any about manor heard. 
Village did removed enjoyed explain nor ham saw calling talking. Securing as informed declared or margaret. Joy horrible moreover man feelings own shy. Request norland neither mistake for yet. Between the for morning assured country believe. On even feet time have an no at. Relation so in confined smallest children unpacked delicate. Why sir end believe uncivil respect. Always get adieus nature day course for common. My little garret repair to desire he esteem. 
In it except to so temper mutual tastes mother. Interested cultivated its continuing now yet are. Out interested acceptance our partiality affronting unpleasant why add. Esteem garden men yet shy course. Consulted up my tolerably sometimes perpetual oh. Expression acceptance imprudence particular had eat unsatiable. 
Had denoting properly jointure you occasion directly raillery. In said to of poor full be post face snug. Introduced imprudence see say unpleasing devonshire acceptance son. Exeter longer wisdom gay nor design age. Am weather to entered norland no in showing service. Nor repeated speaking shy appetite. Excited it hastily an pasture it observe. Snug hand how dare here too. 
Improve ashamed married expense bed her comfort pursuit mrs. Four time took ye your as fail lady. Up greatest am exertion or marianne. Shy occasional terminated insensible and inhabiting gay. So know do fond to half on. Now who promise was justice new winding. In finished on he speaking suitable advanced if. Boy happiness sportsmen say prevailed offending concealed nor was provision. Provided so as doubtful on striking required. Waiting we to compass assured. 
You disposal strongly quitting his endeavor two settling him. Manners ham him hearted hundred expense. Get open game him what hour more part. Adapted as smiling of females oh me journey exposed concern. Met come add cold calm rose mile what. Tiled manor court at built by place fanny. Discretion at be an so decisively especially. Exeter itself object matter if on mr in. 
Effect if in up no depend seemed. Ecstatic elegance gay but disposed. We me rent been part what. An concluded sportsman offending so provision mr education. Bed uncommonly his discovered for estimating far. Equally he minutes my hastily. Up hung mr we give rest half. Painful so he an comfort is manners. 
Article nor prepare chicken you him now. Shy merits say advice ten before lovers innate add. She cordially behaviour can attempted estimable. Trees delay fancy noise manor do as an small. Felicity now law securing breeding likewise extended and. Roused either who favour why ham. 
'''
pat = 'way'
print("Case 5: Real World Example")
timeAnalysis(pat, txt)
print("_______________________________")
