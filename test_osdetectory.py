import pytest
import os_detector

def test_obtenir_sys_info(mocker):
    mock_uname = mocker.patch('platform.uname')

    mock_uname.return_value = mocker.Mock(
        system='Linux',
        node='test_node',
        release='5.4.0-42-generic',
        version='#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020',
        machine='x86_64',
        processor='x86_64'
    )