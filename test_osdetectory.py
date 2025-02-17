import pytest
import os_detector

import sys

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

    expected_result = {
        'System Type': 'Linux',
        'Node Name': 'test_node',
        'Release': '5.4.0-42-generic',
        'Version': '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020',
        'Machine': 'x86_64',
        'Processor': 'x86_64'
    }

    result = os_detector.obtenir_sys_info()
    assert result == expected_result

@pytest.mark.skipif(sys.platform != "win32", reason="Le test ne fonctionne que sur Windows")
def test_get_windows_hardware_info(mocker):
    mock_check_output = mocker.patch('os_detector.subprocess.check_output')

    mock_check_output.side_effect = [
        "Name\nIntel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(), # Simule la sortie de la commande  pour le CPU
        "Capacity\n17179869184\n".encode()  # Simule la sortie de la commande pour la RAM (16 Go)
    ]

    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0 # 16 Go de RAM (17179869184 octets = 16 Go)        
    }

    result = os_detector.get_windows_hardware_info()
    assert result == expected_result
@pytest.mark.skipif(sys.platform != "linux", reason="Le test ne fonctionne que sur Linux")
def test_get_linux_hardware_info(mocker):
    mock_check_output = mocker.patch('os_detector.subprocess.check_output')

    mock_check_output.side_effect = [
        "Model name: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(), # Sortie pour le CPU
        "MemTotal: 16777216 kB\n".encode() # Sortie pour la RAM (16 Go)
    ]

    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0
    }

    result = os_detector.get_linux_hardware_info()
    assert result == expected_result

@pytest.mark.skipif(sys.platform != "darwin", reason="Le test ne fonctionne que sur macOS")
def test_get_macOS_hardware_info(mocker):
    mock_check_output = mocker.patch('os_detector.subprocess.check_output')

    mock_check_output.side_effect = [
        "Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz\n".encode(), # Sortie pour le CPU
        "17179869184\n".encode() # Sortie pour la RAM (16 Go)
    ]

    expected_result = {
        'CPU': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Total Memory (GB)': 16.0
    }

    result = os_detector.get_macOS_hardware_info()
    assert result == expected_result