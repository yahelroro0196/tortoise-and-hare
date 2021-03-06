import json

from animal_factory import factory
from competition.Round import Round
from config import RACERS_CONFIG_PATH
from constants import ORIGIN0_OFFSET

RACER_PROPERTIES = 'racer_properties'

TRACK_LENGTH = 'track_length'
RACERS = 'racers'
ANIMAL_TYPE = 'type'
RACERS_CONFIG = 'racers_config'
RACE_SETTINGS = 'race_settings'
ROUNDS = 'rounds'
RACER_NAME = 'name'


def initialize_rounds(race_settings: dict):
    return (
        _build_round(round_num, round_settings, _build_round_racers(round_settings))
        for round_num, round_settings in enumerate(race_settings.values())
    )


def load_race_settings() -> dict:
    with open(RACERS_CONFIG_PATH) as cfg_file:
        return json.load(cfg_file)


def unpack_round_settings(curr_round):
    return curr_round.racers, curr_round.track_length


def _build_round(round_num, round_settings: dict, racers):
    return Round(round_num + ORIGIN0_OFFSET, round_settings[TRACK_LENGTH], racers)


def _build_round_racers(round_settings: dict):
    racers_settings = round_settings[RACERS]
    racers = [_build_racer(racer_name, racers_settings) for racer_name in racers_settings]
    return racers


def _build_racer(racer_name: str, racers_settings: dict):
    racer_properties = racers_settings[racer_name]
    racer_type = racer_properties.pop(ANIMAL_TYPE)
    racer_properties[RACER_NAME] = racer_name
    return factory(racer_type, racer_properties)
