from microCabrilloLog import convert_to_utc ,give_me_a_bool, collect_header_info, print_to_log, start_logging
import pytest
import mock #used to trick the input
import builtins # where input lives
import datetime

def test_give_me_a_bool():
    #test the input fuction for the give_me _boolFuction. 
    #mocks input of "Y"
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        assert give_me_a_bool("Filler Print Text") == True

    #mocks input of "N"
    with mock.patch.object(builtins, 'input', lambda _: 'N'):
        assert give_me_a_bool("Filler Print Text") == False
    
    

def test_conver_to_utc():
    assert convert_to_utc() == datetime.datetime.now(datetime.timezone.utc)
    

def main():
    test_give_me_a_bool()
    test_conver_to_utc()


pytest.main(["-v", "--tb=line", "-rN", __file__])



