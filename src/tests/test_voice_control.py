import pytest
from controllers.voice_control import VoiceControl

def test_voice_commands():
    voice_control = VoiceControl()

    assert voice_control.execute_command("clique") is None
    assert voice_control.execute_command("scroll para cima") is None