import pytest
from unittest.mock import patch, Mock
import os_detector
import sys

# Test de la fonction obtenir_sys_info
@patch('platform.uname')
def test_obtenir_sys_info(mock_uname):
    MockUname = Mock()
    MockUname.system = 'Linux'
    MockUname.node = 'test_node'
    MockUname.release = '5.4.0-42-generic'
    MockUname.version = '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'
    MockUname.machine = 'x86_64'
    MockUname.processor = 'x86_64'
    mock_uname.return_value = MockUname

    expected_result = {
        'System Type' : 'Linux',
        'Node Name' : 'test_node',
        'Release' : '5.4.0-42-generic',
        'Version' : '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020',
        'Machine' : 'x86_64',
        'Processor': 'x86_64'
    }

    result = os_detector.obtenir_sys_info()
    assert result == expected_result

# Test de la fonction get_windows_hardware_info
@pytest.mark.skipif(sys.platform != "win32", reason="Le test ne fonctionne que sur Windows")
@patch('os_detector.subprocess.check_output')
def test_get_windows_hardware_info(mock_check_output):
    mock_check_output.side_effect = [
        "Name\nIntel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(),
        "Capacity\n17179869184\n".encode() # 16 GB
    ]

    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0
    }

    result = os_detector.get_windows_hardware_info()
    assert result == expected_result

# Test de la fonction get_linux_hardware_info
@pytest.mark.skipif(sys.platform != "linux", reason="Le test ne fonctionne que sur Linux")
@patch('os_detector.subprocess.check_output')
def test_get_linux_hardware_info(mock_check_output):
    mock_check_output.side_effect = [
        "Model name: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(),
        "MemTotal: 16777216 kB\n".encode() # 16 GB
    ]
    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0
    }
    result = os_detector.get_linux_hardware_info()
    assert result == expected_result

# Test de la fonction get_macOS_hardware_info
@pytest.mark.skipif(sys.platform != "darwin", reason="Le test ne fonctionne que sur macOS")
@patch('os_detector.subprocess.check_output')
def test_get_macOS_hardware_info(mock_check_output):
    mock_check_output.side_effect = [
        "Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(),
        "17179869184\n".encode() # 16 GB
    ]
    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0
    }
    result = os_detector.get_macOS_hardware_info()
    assert result == expected_result