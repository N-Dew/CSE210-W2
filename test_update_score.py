import pytest
from game import Game
import io

def test_high():
    
    #tests whether score adds points based on user entering 'h'
    game = Game()
    game.previous = 1
    game.selected = 2
    game.update_score("h")
    assert game.score == 400
    game.previous = 2
    game.selected = 1
    game.update_score("h")
    assert game.score == 325

def test_low():

    #tests whether score subtracts points based on user entering 'l'
    game = Game()
    game.previous = 2
    game.selected = 1
    game.update_score("l")
    assert game.score == 400
    game.previous = 1
    game.selected = 2
    game.update_score("l")
    assert game.score == 325


# Testing to make sure end/continue controls work "y" (yes) and "n" (no)
def test_do_updates(invalid):

    # test 'y' to continue game
    game = Game()
    invalid.setattr("sys.stdin", io.StringIO("1234\ny"))
    game.do_updates()
    assert game.is_playing == True

    # test 'n' to end game
    game = Game()
    invalid.setattr("sys.stdin", io.StringIO("asdf\nn"))
    game.do_updates()
    assert game.is_playing == False


pytest.main(["-v", "--tb=line", "-rN", __file__])
