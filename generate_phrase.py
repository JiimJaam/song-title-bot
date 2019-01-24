import random


def random_phrase():
    lines = open('phrases.txt').read().splitlines()
    myline = random.choice(lines)
    return myline


def random_noun():
    nouns = open('nouns.txt').read().splitlines()
    mynoun = random.choice(nouns)
    return mynoun


def pluralnoun(a):
    pn = a

    if pn[-1:] == "y":
        if pn == "Kennedy":
            pn = pn + "s"
            return pn
        if pn[-2:] == "ay" or pn[-2:] == "ey" or pn[-2:] == "iy" or pn[-2:] == "oy" or pn[-2] == "uy":
            pn = pn + "s"
            return pn
        else:
            pn = pn[:-1] + "ies"
            return pn
    if pn == "mouse":
        pn = "mice"
        return pn
    if pn == "woman":
        pn = "women"
        return pn
    if pn == "man":
        pn = "men"
        return pn
    if pn == "person":
        pn = "people"
        return pn
    if pn == "blood" or pn == "money" or pn == "meat" or pn == "police" or pn == "dead" or pn == "bread" or pn == "milk" or pn == "sheep" or pn == "scum":
        pn = pn
        return pn

    if pn[-1:] == "s" or pn[-1:] == "x" or pn[-2:] == "sh" or pn[-2:] == "ch":
        pn = pn + "es"
        return pn

    pn = pn + "s"
    return pn


def random_verb():
    verbs = open('verbs.txt').read().splitlines()
    myverb = random.choice(verbs)
    return myverb


def verb_ing():
    ing = random_verb()
    if ing != "reap" and ing != "sleep" and ing != "fight" and ing != "scream" and ing != "shoot" and ing != "start" and ing != "stomp" and ing != "burn" and ing != "weep" and ing != "disgust":
        if ing[-1:] == "t" or ing[-1:] == "p" or ing[-1:] == "g" or ing[-1:] == "m" or ing[-1:] == "n" or ing[-1:] == "z":
            ing = ing + ing[-1:] + "ing"
            return ing
    if ing[-1:] == "e":
        ing = ing[:-1] + "ing"
        return ing
    ing = ing + "ing"
    return ing


def verb_er():
    er = random_verb()
    if er != "reap" and er != "sleep" and er != "fight" and er != "scream" and er != "shoot" and er != "start" and er != "stomp" and er != "burn" and er != "weep" and er != "disgust":
        if er[-1:] == "t" or er[-1:] == "p" or er[-1:] == "g" or er[-1:] == "m" or er[-1:] == "n" or er[-1:] == "z":
            er = er + er[-1:] + "er"
            return er
    if er[-1:] == "y":
        if er[-2:] == "ay" or er[-2:] == "ey" or er[-2:] == "iy" or er[-2:] == "oy" or er[-2:] == "uy":
            er = er[:-1] + "ier"
            return er
        else:
            er = er + "er"
            return er
    if er[-1:] == "e":
        er = er + "r"
        return er
    er = er + "er"
    return er


def verb_s():
    pv = random_verb()
    if pv[-1:] == "s" or pv[-1:] == "x" or pv[-2:] == "sh" or pv[-2:] == "ch":
        pv = pv + "es"
        return pv
    if pv[-1:] == "y":
        if pv[-2:] == "ay" or pv[-2:] == "ey" or pv[-2:] == "iy" or pv[-2:] == "iy" or pv[-2:] == "oy" or pv[-2:] == "uy":
            pv = pv + "s"
            return pv
        else:
            pv = pv[:-1] + "ies"
            return pv
    pv = pv + "s"
    return pv


def verb_ed():
    ed = random_verb()
    if ed == "catch":
        ed = "caught"
        return ed
    if ed == "fly":
        ed = "flew"
        return ed
    if ed == "drive":
        ed = "drove"
        return ed
    if ed == "fight":
        ed = "fought"
        return ed
    if ed == "get":
        ed = "got"
        return ed
    if ed == "give":
        ed = "gave"
        return ed
    if ed == "know":
        ed = "knew"
        return ed
    if ed == "run":
        ed = "ran"
        return ed
    if ed == "shoot":
        ed = "shot"
        return ed
    if ed == "sleep":
        ed = "slept"
        return ed
    if ed == "cut" or ed == "hit" or ed == "shit":
        ed = ed
        return ed
    if ed != "reap" and ed != "sleep" and ed != "fight" and ed != "scream" and ed != "shoot" and ed != "start" and ed != "stomp" and ed != "burn" and ed != "weep" and ed != "disgust":
        if ed[-1:] == "t" or ed[-1:] == "p" or ed[-1:] == "g" or ed[-1:] == "m" or ed[-1:] == "n" or ed[-1:] == "z":
            ed = ed + ed[-1:] + "ed"
    if ed[-1:] == "y":
        if ed[-2:] == "ay" or ed[-2:] == "ey" or ed[-2:] == "iy" or ed[-2:] == "oy" or ed[-2:] == "uy":
            ed = ed[:-1] + "ied"
            return ed
        else:
            ed = ed + "ed"
            return ed
    if ed[-1:] == "e":
        ed = ed + "d"
        return ed
    ed = ed + "ed"
    return ed


def random_adjective():
    adjectives = open('adjectives.txt').read().splitlines()
    myadjective = random.choice(adjectives)
    return myadjective


def random_city():
    cities = open('cities.txt').read().splitlines()
    mycity = random.choice(cities)
    return mycity


def random_firstname():
    firstnames = open('first_names.txt').read().splitlines()
    myfirstname = random.choice(firstnames)
    return myfirstname


def random_lastname():
    lastnames = open('last_names.txt').read().splitlines()
    mylastname = random.choice(lastnames)
    return mylastname


def gen():
    phrase = random_phrase()
    phrase2 = ""
    while phrase2 != phrase:
        phrase2 = phrase
        phrase = phrase.replace("#noun#", random_noun().capitalize(), 1)
        phrase = phrase.replace("#noun.s#", pluralnoun(random_noun()).capitalize(), 1)
        phrase = phrase.replace("#verb#", random_verb().capitalize(), 1)
        phrase = phrase.replace("#verb.er#", verb_er().capitalize(), 1)
        phrase = phrase.replace("#verb.ers#", pluralnoun(verb_er()).capitalize(), 1)
        phrase = phrase.replace("#verb.ing#", verb_ing().capitalize(), 1)
        phrase = phrase.replace("#verb.ed#", verb_ed().capitalize(), 1)
        phrase = phrase.replace("#verb.s#", verb_s().capitalize(), 1)
        phrase = phrase.replace("#adjective#", random_adjective().capitalize(), 1)
        phrase = phrase.replace("#city#", random_city(), 1)
        phrase = phrase.replace("#firstname#", random_firstname(), 1)
        phrase = phrase.replace("#lastname#", random_lastname(), 1)
        phrase = phrase.replace("#number#", str(random.randint(1, 1000)), 1)
    print(phrase)
    return phrase


gen()
