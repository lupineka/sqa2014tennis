# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_p1_and_p2_start_a_match_to_num_sets(step, p1, p2, num):
    world.match = m.Match(p1, p2, num)


@step(u'When: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def when_g1_and_g2_start_a_match_to_g3_sets(step, g1, g2, g3):
    assert False, 'This step must be implemented'


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score() == score, "Got %s" % m.score()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_g1_won_the_g2_set_g3_g4(step, g1, g2, g3, g4):
    world.match.asignar(g1, g2, g3, g4)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_g1_won_the_g2_set_g3_g4(step, g1, g2, g3, g4):
    world.match.asignar(g1, g2, g3, g4)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, group1):
    assert world.match.score() == group1, "Got %s" % m.score()
