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
    pluralnoun = a
    spec = False

    if pluralnoun[-1:] == "y":
        if pluralnoun[-2] != "a" and pluralnoun[-2] != "e" and pluralnoun[-2] != "i" and pluralnoun[-2] != "o" and pluralnoun[-2] != "u" and pluralnoun != "Kennedy":
            pluralnoun = pluralnoun[:-1] + "ie"

    else:
        if pluralnoun == "mouse":
            spec = True
            pluralnoun = "mice"
        elif pluralnoun == "woman":
            spec = True
            pluralnoun = "women"
        elif pluralnoun == "men":
            spec = True
            pluralnoun = "men"
        elif pluralnoun == "person":
            spec = True
            pluralnoun = "people"
            spec = True
        elif pluralnoun == "money" or pluralnoun == "meat" or pluralnoun == "police" or pluralnoun == "dead" or pluralnoun == "bread" or pluralnoun == "milk" or pluralnoun == "sheep":
            spec = True
            pluralnoun = pluralnoun

    if pluralnoun[-1:] == "s" or pluralnoun[-1:] == "x" or pluralnoun[-2:] == "sh" or pluralnoun[-2:] == "ch":
        pluralnoun = pluralnoun + "e"

    if spec == False:
        pluralnoun = pluralnoun + "s"
    return pluralnoun


def random_verb():
    verbs = open('verbs.txt').read().splitlines()
    myverb = random.choice(verbs)
    return myverb


def verb_ing():
    ing = random_verb()
    if ing != "reap":
        if ing[-1:] == "t" or ing[-1:] == "p" or ing[-1:] == "g" or ing[-1:] == "m" or ing[-1:] == "n" or ing[-1:] == "z":
            ing = ing + ing[-1:] + "ing"
    elif ing[-1:] == "e":
        ing = ing[:-1] + "ing"
    else:
        ing = ing + "ing"
    return ing


def verb_er():
    er = random_verb()
    if er != "reap" and er != "sleep" and er != "fight" and er != "scream" and er != "shoot" and er != "start" and er != "stomp":
        if er[-1:] == "t" or er[-1:] == "p" or er[-1:] == "g" or er[-1:] == "m" or er[-1:] == "n" or er[-1:] == "z":
            er = er + er[-1:]
    if er[-1:] == "e":
        er = er[:-1]
    er = er + "er"
    return er


def verb_ed():
    ed = random_verb()
    if ed == "catch":
        ed = "caught"
    elif ed == "fly":
        ed = "flew"
    elif ed == "drive":
        ed = "drove"
    elif ed == "fight":
        ed = "fought"
    elif ed == "get":
        ed = "got"
    elif ed == "give":
        ed = "gave"
    elif ed == "know":
        ed = "knew"
    elif ed == "run":
        ed = "ran"
    elif ed == "shoot":
        ed = "shot"
    elif ed == "sleep":
        ed = "slept"
    elif ed == "cut" or ed == "hit" or ed == "shit":
        ed = ed
    else:
        if ed != "reap" and ed != "sleep" and ed != "fight" and ed != "scream" and ed != "shoot" and ed != "start" and ed != "stomp":
            if ed[-1:] == "t" or ed[-1:] == "p" or ed[-1:] == "g" or ed[-1:] == "m" or ed[-1:] == "n" or ed[-1:] == "z":
                ed = ed + ed[-1:] + "ed"
        if ed[-1:] == "e":
            ed = ed[:-1]
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
    while(phrase2 != phrase):
        phrase2 = phrase
        phrase = phrase.replace("#noun#", random_noun().capitalize(), 1)
        phrase = phrase.replace("#noun.s#", pluralnoun(random_noun()).capitalize(), 1)
        phrase = phrase.replace("#verb#", random_verb().capitalize(), 1)
        phrase = phrase.replace("#verb.er#", verb_er().capitalize(), 1)
        phrase = phrase.replace("#verb.ers#", pluralnoun(verb_er()).capitalize(), 1)
        phrase = phrase.replace("#verb.ing#", verb_ing().capitalize(), 1)
        phrase = phrase.replace("#verb.ed#", verb_ed().capitalize(), 1)
        phrase = phrase.replace("#adjective#", random_adjective().capitalize(), 1)
        phrase = phrase.replace("#city#", random_city(), 1)
        phrase = phrase.replace("#firstname#", random_firstname(), 1)
        phrase = phrase.replace("#lastname#", random_lastname(), 1)
        phrase = phrase.replace("#number#", str(random.randint(1, 1000)), 1)
    print(phrase)
    return phrase
