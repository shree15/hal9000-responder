"""onionlovers.py slackbot test"""
# pylint:disable=C0111

from hal9000.plugins import onionlove

def test_running(mocker):
    message = mocker.MagicMock()
    onionlove.react_onion(message)
    calls = [mocker.call('heart'), mocker.call('onion')]
    message.react.assert_has_calls(calls)
