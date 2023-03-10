from telebot import types
import sqlite3
import telebot
import os
import settings
import random
import requests
import json
import datetime

class Emoji(object):
    """This object represents an Emoji."""
    
    GRINNING_FACE_WITH_SMILING_EYES = b'\xF0\x9F\x98\x81'
    FACE_WITH_TEARS_OF_JOY = b'\xF0\x9F\x98\x82'
    SMILING_FACE_WITH_OPEN_MOUTH = b'\xF0\x9F\x98\x83'
    SMILING_FACE_WITH_OPEN_MOUTH_AND_SMILING_EYES = b'\xF0\x9F\x98\x84'
    SMILING_FACE_WITH_OPEN_MOUTH_AND_COLD_SWEAT = b'\xF0\x9F\x98\x85'
    SMILING_FACE_WITH_OPEN_MOUTH_AND_TIGHTLY_CLOSED_EYES = b'\xF0\x9F\x98\x86'
    WINKING_FACE = b'\xF0\x9F\x98\x89'
    SMILING_FACE_WITH_SMILING_EYES = b'\xF0\x9F\x98\x8A'
    FACE_SAVOURING_DELICIOUS_FOOD = b'\xF0\x9F\x98\x8B'
    RELIEVED_FACE = b'\xF0\x9F\x98\x8C'
    SMILING_FACE_WITH_HEART_SHAPED_EYES = b'\xF0\x9F\x98\x8D'
    SMIRKING_FACE = b'\xF0\x9F\x98\x8F'
    UNAMUSED_FACE = b'\xF0\x9F\x98\x92'
    FACE_WITH_COLD_SWEAT = b'\xF0\x9F\x98\x93'
    PENSIVE_FACE = b'\xF0\x9F\x98\x94'
    CONFOUNDED_FACE = b'\xF0\x9F\x98\x96'
    FACE_THROWING_A_KISS = b'\xF0\x9F\x98\x98'
    KISSING_FACE_WITH_CLOSED_EYES = b'\xF0\x9F\x98\x9A'
    FACE_WITH_STUCK_OUT_TONGUE_AND_WINKING_EYE = b'\xF0\x9F\x98\x9C'
    FACE_WITH_STUCK_OUT_TONGUE_AND_TIGHTLY_CLOSED_EYES = b'\xF0\x9F\x98\x9D'
    DISAPPOINTED_FACE = b'\xF0\x9F\x98\x9E'
    ANGRY_FACE = b'\xF0\x9F\x98\xA0'
    POUTING_FACE = b'\xF0\x9F\x98\xA1'
    CRYING_FACE = b'\xF0\x9F\x98\xA2'
    PERSEVERING_FACE = b'\xF0\x9F\x98\xA3'
    FACE_WITH_LOOK_OF_TRIUMPH = b'\xF0\x9F\x98\xA4'
    DISAPPOINTED_BUT_RELIEVED_FACE = b'\xF0\x9F\x98\xA5'
    FEARFUL_FACE = b'\xF0\x9F\x98\xA8'
    WEARY_FACE = b'\xF0\x9F\x98\xA9'
    SLEEPY_FACE = b'\xF0\x9F\x98\xAA'
    TIRED_FACE = b'\xF0\x9F\x98\xAB'
    LOUDLY_CRYING_FACE = b'\xF0\x9F\x98\xAD'
    FACE_WITH_OPEN_MOUTH_AND_COLD_SWEAT = b'\xF0\x9F\x98\xB0'
    FACE_SCREAMING_IN_FEAR = b'\xF0\x9F\x98\xB1'
    ASTONISHED_FACE = b'\xF0\x9F\x98\xB2'
    FLUSHED_FACE = b'\xF0\x9F\x98\xB3'
    DIZZY_FACE = b'\xF0\x9F\x98\xB5'
    FACE_WITH_MEDICAL_MASK = b'\xF0\x9F\x98\xB7'
    GRINNING_CAT_FACE_WITH_SMILING_EYES = b'\xF0\x9F\x98\xB8'
    CAT_FACE_WITH_TEARS_OF_JOY = b'\xF0\x9F\x98\xB9'
    SMILING_CAT_FACE_WITH_OPEN_MOUTH = b'\xF0\x9F\x98\xBA'
    SMILING_CAT_FACE_WITH_HEART_SHAPED_EYES = b'\xF0\x9F\x98\xBB'
    CAT_FACE_WITH_WRY_SMILE = b'\xF0\x9F\x98\xBC'
    KISSING_CAT_FACE_WITH_CLOSED_EYES = b'\xF0\x9F\x98\xBD'
    POUTING_CAT_FACE = b'\xF0\x9F\x98\xBE'
    CRYING_CAT_FACE = b'\xF0\x9F\x98\xBF'
    WEARY_CAT_FACE = b'\xF0\x9F\x99\x80'
    FACE_WITH_NO_GOOD_GESTURE = b'\xF0\x9F\x99\x85'
    FACE_WITH_OK_GESTURE = b'\xF0\x9F\x99\x86'
    PERSON_BOWING_DEEPLY = b'\xF0\x9F\x99\x87'
    SEE_NO_EVIL_MONKEY = b'\xF0\x9F\x99\x88'
    HEAR_NO_EVIL_MONKEY = b'\xF0\x9F\x99\x89'
    SPEAK_NO_EVIL_MONKEY = b'\xF0\x9F\x99\x8A'
    HAPPY_PERSON_RAISING_ONE_HAND = b'\xF0\x9F\x99\x8B'
    PERSON_RAISING_BOTH_HANDS_IN_CELEBRATION = b'\xF0\x9F\x99\x8C'
    PERSON_FROWNING = b'\xF0\x9F\x99\x8D'
    PERSON_WITH_POUTING_FACE = b'\xF0\x9F\x99\x8E'
    PERSON_WITH_FOLDED_HANDS = b'\xF0\x9F\x99\x8F'
    BLACK_SCISSORS = b'\xE2\x9C\x82'
    WHITE_HEAVY_CHECK_MARK = b'\xE2\x9C\x85'
    AIRPLANE = b'\xE2\x9C\x88'
    ENVELOPE = b'\xE2\x9C\x89'
    RAISED_FIST = b'\xE2\x9C\x8A'
    RAISED_HAND = b'\xE2\x9C\x8B'
    VICTORY_HAND = b'\xE2\x9C\x8C'
    PENCIL = b'\xE2\x9C\x8F'
    BLACK_NIB = b'\xE2\x9C\x92'
    HEAVY_CHECK_MARK = b'\xE2\x9C\x94'
    HEAVY_MULTIPLICATION_X = b'\xE2\x9C\x96'
    SPARKLES = b'\xE2\x9C\xA8'
    EIGHT_SPOKED_ASTERISK = b'\xE2\x9C\xB3'
    EIGHT_POINTED_BLACK_STAR = b'\xE2\x9C\xB4'
    SNOWFLAKE = b'\xE2\x9D\x84'
    SPARKLE = b'\xE2\x9D\x87'
    CROSS_MARK = b'\xE2\x9D\x8C'
    NEGATIVE_SQUARED_CROSS_MARK = b'\xE2\x9D\x8E'
    BLACK_QUESTION_MARK_ORNAMENT = b'\xE2\x9D\x93'
    WHITE_QUESTION_MARK_ORNAMENT = b'\xE2\x9D\x94'
    WHITE_EXCLAMATION_MARK_ORNAMENT = b'\xE2\x9D\x95'
    HEAVY_EXCLAMATION_MARK_SYMBOL = b'\xE2\x9D\x97'
    HEAVY_BLACK_HEART = b'\xE2\x9D\xA4'
    HEAVY_PLUS_SIGN = b'\xE2\x9E\x95'
    HEAVY_MINUS_SIGN = b'\xE2\x9E\x96'
    HEAVY_DIVISION_SIGN = b'\xE2\x9E\x97'
    BLACK_RIGHTWARDS_ARROW = b'\xE2\x9E\xA1'
    CURLY_LOOP = b'\xE2\x9E\xB0'
    ROCKET = b'\xF0\x9F\x9A\x80'
    RAILWAY_CAR = b'\xF0\x9F\x9A\x83'
    HIGH_SPEED_TRAIN = b'\xF0\x9F\x9A\x84'
    HIGH_SPEED_TRAIN_WITH_BULLET_NOSE = b'\xF0\x9F\x9A\x85'
    METRO = b'\xF0\x9F\x9A\x87'
    STATION = b'\xF0\x9F\x9A\x89'
    BUS = b'\xF0\x9F\x9A\x8C'
    BUS_STOP = b'\xF0\x9F\x9A\x8F'
    AMBULANCE = b'\xF0\x9F\x9A\x91'
    FIRE_ENGINE = b'\xF0\x9F\x9A\x92'
    POLICE_CAR = b'\xF0\x9F\x9A\x93'
    TAXI = b'\xF0\x9F\x9A\x95'
    AUTOMOBILE = b'\xF0\x9F\x9A\x97'
    RECREATIONAL_VEHICLE = b'\xF0\x9F\x9A\x99'
    DELIVERY_TRUCK = b'\xF0\x9F\x9A\x9A'
    SHIP = b'\xF0\x9F\x9A\xA2'
    SPEEDBOAT = b'\xF0\x9F\x9A\xA4'
    HORIZONTAL_TRAFFIC_LIGHT = b'\xF0\x9F\x9A\xA5'
    CONSTRUCTION_SIGN = b'\xF0\x9F\x9A\xA7'
    POLICE_CARS_REVOLVING_LIGHT = b'\xF0\x9F\x9A\xA8'
    TRIANGULAR_FLAG_ON_POST = b'\xF0\x9F\x9A\xA9'
    DOOR = b'\xF0\x9F\x9A\xAA'
    NO_ENTRY_SIGN = b'\xF0\x9F\x9A\xAB'
    SMOKING_SYMBOL = b'\xF0\x9F\x9A\xAC'
    NO_SMOKING_SYMBOL = b'\xF0\x9F\x9A\xAD'
    BICYCLE = b'\xF0\x9F\x9A\xB2'
    PEDESTRIAN = b'\xF0\x9F\x9A\xB6'
    MENS_SYMBOL = b'\xF0\x9F\x9A\xB9'
    WOMENS_SYMBOL = b'\xF0\x9F\x9A\xBA'
    RESTROOM = b'\xF0\x9F\x9A\xBB'
    BABY_SYMBOL = b'\xF0\x9F\x9A\xBC'
    TOILET = b'\xF0\x9F\x9A\xBD'
    WATER_CLOSET = b'\xF0\x9F\x9A\xBE'
    BATH = b'\xF0\x9F\x9B\x80'
    CIRCLED_LATIN_CAPITAL_LETTER_M = b'\xE2\x93\x82'
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_A = b'\xF0\x9F\x85\xB0'
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_B = b'\xF0\x9F\x85\xB1'
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_O = b'\xF0\x9F\x85\xBE'
    NEGATIVE_SQUARED_LATIN_CAPITAL_LETTER_P = b'\xF0\x9F\x85\xBF'
    NEGATIVE_SQUARED_AB = b'\xF0\x9F\x86\x8E'
    SQUARED_CL = b'\xF0\x9F\x86\x91'
    SQUARED_COOL = b'\xF0\x9F\x86\x92'
    SQUARED_FREE = b'\xF0\x9F\x86\x93'
    SQUARED_ID = b'\xF0\x9F\x86\x94'
    SQUARED_NEW = b'\xF0\x9F\x86\x95'
    SQUARED_NG = b'\xF0\x9F\x86\x96'
    SQUARED_OK = b'\xF0\x9F\x86\x97'
    SQUARED_SOS = b'\xF0\x9F\x86\x98'
    SQUARED_UP_WITH_EXCLAMATION_MARK = b'\xF0\x9F\x86\x99'
    SQUARED_VS = b'\xF0\x9F\x86\x9A'
    REGIONAL_INDICATOR_SYMBOL_LETTER_D_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_E\
        = b'\xF0\x9F\x87\xA9\xF0\x9F\x87\xAA'
    REGIONAL_INDICATOR_SYMBOL_LETTER_G_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_B\
        = b'\xF0\x9F\x87\xAC\xF0\x9F\x87\xA7'
    REGIONAL_INDICATOR_SYMBOL_LETTER_C_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_N\
        = b'\xF0\x9F\x87\xA8\xF0\x9F\x87\xB3'
    REGIONAL_INDICATOR_SYMBOL_LETTER_J_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_P\
        = b'\xF0\x9F\x87\xAF\xF0\x9F\x87\xB5'
    REGIONAL_INDICATOR_SYMBOL_LETTER_K_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_R\
        = b'\xF0\x9F\x87\xB0\xF0\x9F\x87\xB7'
    REGIONAL_INDICATOR_SYMBOL_LETTER_F_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_R\
        = b'\xF0\x9F\x87\xAB\xF0\x9F\x87\xB7'
    REGIONAL_INDICATOR_SYMBOL_LETTER_E_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_S\
        = b'\xF0\x9F\x87\xAA\xF0\x9F\x87\xB8'
    REGIONAL_INDICATOR_SYMBOL_LETTER_I_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_T\
        = b'\xF0\x9F\x87\xAE\xF0\x9F\x87\xB9'
    REGIONAL_INDICATOR_SYMBOL_LETTER_U_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_S\
        = b'\xF0\x9F\x87\xBA\xF0\x9F\x87\xB8'
    REGIONAL_INDICATOR_SYMBOL_LETTER_R_PLUS_REGIONAL_INDICATOR_SYMBOL_LETTER_U\
        = b'\xF0\x9F\x87\xB7\xF0\x9F\x87\xBA'
    SQUARED_KATAKANA_KOKO = b'\xF0\x9F\x88\x81'
    SQUARED_KATAKANA_SA = b'\xF0\x9F\x88\x82'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7121 = b'\xF0\x9F\x88\x9A'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6307 = b'\xF0\x9F\x88\xAF'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7981 = b'\xF0\x9F\x88\xB2'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7A7A = b'\xF0\x9F\x88\xB3'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_5408 = b'\xF0\x9F\x88\xB4'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6E80 = b'\xF0\x9F\x88\xB5'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6709 = b'\xF0\x9F\x88\xB6'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_6708 = b'\xF0\x9F\x88\xB7'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_7533 = b'\xF0\x9F\x88\xB8'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_5272 = b'\xF0\x9F\x88\xB9'
    SQUARED_CJK_UNIFIED_IDEOGRAPH_55B6 = b'\xF0\x9F\x88\xBA'
    CIRCLED_IDEOGRAPH_ADVANTAGE = b'\xF0\x9F\x89\x90'
    CIRCLED_IDEOGRAPH_ACCEPT = b'\xF0\x9F\x89\x91'
    COPYRIGHT_SIGN = b'\xC2\xA9'
    REGISTERED_SIGN = b'\xC2\xAE'
    DOUBLE_EXCLAMATION_MARK = b'\xE2\x80\xBC'
    EXCLAMATION_QUESTION_MARK = b'\xE2\x81\x89'
    DIGIT_EIGHT_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x38\xE2\x83\xA3'
    DIGIT_NINE_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x39\xE2\x83\xA3'
    DIGIT_SEVEN_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x37\xE2\x83\xA3'
    DIGIT_SIX_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x36\xE2\x83\xA3'
    DIGIT_ONE_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x31\xE2\x83\xA3'
    DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x30\xE2\x83\xA3'
    DIGIT_TWO_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x32\xE2\x83\xA3'
    DIGIT_THREE_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x33\xE2\x83\xA3'
    DIGIT_FIVE_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x35\xE2\x83\xA3'
    DIGIT_FOUR_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x34\xE2\x83\xA3'
    NUMBER_SIGN_PLUS_COMBINING_ENCLOSING_KEYCAP = b'\x23\xE2\x83\xA3'
    TRADE_MARK_SIGN = b'\xE2\x84\xA2'
    INFORMATION_SOURCE = b'\xE2\x84\xB9'
    LEFT_RIGHT_ARROW = b'\xE2\x86\x94'
    UP_DOWN_ARROW = b'\xE2\x86\x95'
    NORTH_WEST_ARROW = b'\xE2\x86\x96'
    NORTH_EAST_ARROW = b'\xE2\x86\x97'
    SOUTH_EAST_ARROW = b'\xE2\x86\x98'
    SOUTH_WEST_ARROW = b'\xE2\x86\x99'
    LEFTWARDS_ARROW_WITH_HOOK = b'\xE2\x86\xA9'
    RIGHTWARDS_ARROW_WITH_HOOK = b'\xE2\x86\xAA'
    WATCH = b'\xE2\x8C\x9A'
    HOURGLASS = b'\xE2\x8C\x9B'
    BLACK_RIGHT_POINTING_DOUBLE_TRIANGLE = b'\xE2\x8F\xA9'
    BLACK_LEFT_POINTING_DOUBLE_TRIANGLE = b'\xE2\x8F\xAA'
    BLACK_UP_POINTING_DOUBLE_TRIANGLE = b'\xE2\x8F\xAB'
    BLACK_DOWN_POINTING_DOUBLE_TRIANGLE = b'\xE2\x8F\xAC'
    ALARM_CLOCK = b'\xE2\x8F\xB0'
    HOURGLASS_WITH_FLOWING_SAND = b'\xE2\x8F\xB3'
    BLACK_SMALL_SQUARE = b'\xE2\x96\xAA'
    WHITE_SMALL_SQUARE = b'\xE2\x96\xAB'
    BLACK_RIGHT_POINTING_TRIANGLE = b'\xE2\x96\xB6'
    BLACK_LEFT_POINTING_TRIANGLE = b'\xE2\x97\x80'
    WHITE_MEDIUM_SQUARE = b'\xE2\x97\xBB'
    BLACK_MEDIUM_SQUARE = b'\xE2\x97\xBC'
    WHITE_MEDIUM_SMALL_SQUARE = b'\xE2\x97\xBD'
    BLACK_MEDIUM_SMALL_SQUARE = b'\xE2\x97\xBE'
    BLACK_SUN_WITH_RAYS = b'\xE2\x98\x80'
    CLOUD = b'\xE2\x98\x81'
    BLACK_TELEPHONE = b'\xE2\x98\x8E'
    BALLOT_BOX_WITH_CHECK = b'\xE2\x98\x91'
    UMBRELLA_WITH_RAIN_DROPS = b'\xE2\x98\x94'
    HOT_BEVERAGE = b'\xE2\x98\x95'
    WHITE_UP_POINTING_INDEX = b'\xE2\x98\x9D'
    WHITE_SMILING_FACE = b'\xE2\x98\xBA'
    ARIES = b'\xE2\x99\x88'
    TAURUS = b'\xE2\x99\x89'
    GEMINI = b'\xE2\x99\x8A'
    CANCER = b'\xE2\x99\x8B'
    LEO = b'\xE2\x99\x8C'
    VIRGO = b'\xE2\x99\x8D'
    LIBRA = b'\xE2\x99\x8E'
    SCORPIUS = b'\xE2\x99\x8F'
    SAGITTARIUS = b'\xE2\x99\x90'
    CAPRICORN = b'\xE2\x99\x91'
    AQUARIUS = b'\xE2\x99\x92'
    PISCES = b'\xE2\x99\x93'
    BLACK_SPADE_SUIT = b'\xE2\x99\xA0'
    BLACK_CLUB_SUIT = b'\xE2\x99\xA3'
    BLACK_HEART_SUIT = b'\xE2\x99\xA5'
    BLACK_DIAMOND_SUIT = b'\xE2\x99\xA6'
    HOT_SPRINGS = b'\xE2\x99\xA8'
    BLACK_UNIVERSAL_RECYCLING_SYMBOL = b'\xE2\x99\xBB'
    WHEELCHAIR_SYMBOL = b'\xE2\x99\xBF'
    ANCHOR = b'\xE2\x9A\x93'
    WARNING_SIGN = b'\xE2\x9A\xA0'
    HIGH_VOLTAGE_SIGN = b'\xE2\x9A\xA1'
    MEDIUM_WHITE_CIRCLE = b'\xE2\x9A\xAA'
    MEDIUM_BLACK_CIRCLE = b'\xE2\x9A\xAB'
    SOCCER_BALL = b'\xE2\x9A\xBD'
    BASEBALL = b'\xE2\x9A\xBE'
    SNOWMAN_WITHOUT_SNOW = b'\xE2\x9B\x84'
    SUN_BEHIND_CLOUD = b'\xE2\x9B\x85'
    OPHIUCHUS = b'\xE2\x9B\x8E'
    NO_ENTRY = b'\xE2\x9B\x94'
    CHURCH = b'\xE2\x9B\xAA'
    FOUNTAIN = b'\xE2\x9B\xB2'
    FLAG_IN_HOLE = b'\xE2\x9B\xB3'
    SAILBOAT = b'\xE2\x9B\xB5'
    TENT = b'\xE2\x9B\xBA'
    FUEL_PUMP = b'\xE2\x9B\xBD'
    ARROW_POINTING_RIGHTWARDS_THEN_CURVING_UPWARDS = b'\xE2\xA4\xB4'
    ARROW_POINTING_RIGHTWARDS_THEN_CURVING_DOWNWARDS = b'\xE2\xA4\xB5'
    LEFTWARDS_BLACK_ARROW = b'\xE2\xAC\x85'
    UPWARDS_BLACK_ARROW = b'\xE2\xAC\x86'
    DOWNWARDS_BLACK_ARROW = b'\xE2\xAC\x87'
    BLACK_LARGE_SQUARE = b'\xE2\xAC\x9B'
    WHITE_LARGE_SQUARE = b'\xE2\xAC\x9C'
    WHITE_MEDIUM_STAR = b'\xE2\xAD\x90'
    HEAVY_LARGE_CIRCLE = b'\xE2\xAD\x95'
    WAVY_DASH = b'\xE3\x80\xB0'
    PART_ALTERNATION_MARK = b'\xE3\x80\xBD'
    CIRCLED_IDEOGRAPH_CONGRATULATION = b'\xE3\x8A\x97'
    CIRCLED_IDEOGRAPH_SECRET = b'\xE3\x8A\x99'
    MAHJONG_TILE_RED_DRAGON = b'\xF0\x9F\x80\x84'
    PLAYING_CARD_BLACK_JOKER = b'\xF0\x9F\x83\x8F'
    CYCLONE = b'\xF0\x9F\x8C\x80'
    FOGGY = b'\xF0\x9F\x8C\x81'
    CLOSED_UMBRELLA = b'\xF0\x9F\x8C\x82'
    NIGHT_WITH_STARS = b'\xF0\x9F\x8C\x83'
    SUNRISE_OVER_MOUNTAINS = b'\xF0\x9F\x8C\x84'
    SUNRISE = b'\xF0\x9F\x8C\x85'
    CITYSCAPE_AT_DUSK = b'\xF0\x9F\x8C\x86'
    SUNSET_OVER_BUILDINGS = b'\xF0\x9F\x8C\x87'
    RAINBOW = b'\xF0\x9F\x8C\x88'
    BRIDGE_AT_NIGHT = b'\xF0\x9F\x8C\x89'
    WATER_WAVE = b'\xF0\x9F\x8C\x8A'
    VOLCANO = b'\xF0\x9F\x8C\x8B'
    MILKY_WAY = b'\xF0\x9F\x8C\x8C'
    EARTH_GLOBE_ASIA_AUSTRALIA = b'\xF0\x9F\x8C\x8F'
    NEW_MOON_SYMBOL = b'\xF0\x9F\x8C\x91'
    FIRST_QUARTER_MOON_SYMBOL = b'\xF0\x9F\x8C\x93'
    WAXING_GIBBOUS_MOON_SYMBOL = b'\xF0\x9F\x8C\x94'
    FULL_MOON_SYMBOL = b'\xF0\x9F\x8C\x95'
    CRESCENT_MOON = b'\xF0\x9F\x8C\x99'
    FIRST_QUARTER_MOON_WITH_FACE = b'\xF0\x9F\x8C\x9B'
    GLOWING_STAR = b'\xF0\x9F\x8C\x9F'
    SHOOTING_STAR = b'\xF0\x9F\x8C\xA0'
    CHESTNUT = b'\xF0\x9F\x8C\xB0'
    SEEDLING = b'\xF0\x9F\x8C\xB1'
    PALM_TREE = b'\xF0\x9F\x8C\xB4'
    CACTUS = b'\xF0\x9F\x8C\xB5'
    TULIP = b'\xF0\x9F\x8C\xB7'
    CHERRY_BLOSSOM = b'\xF0\x9F\x8C\xB8'
    ROSE = b'\xF0\x9F\x8C\xB9'
    HIBISCUS = b'\xF0\x9F\x8C\xBA'
    SUNFLOWER = b'\xF0\x9F\x8C\xBB'
    BLOSSOM = b'\xF0\x9F\x8C\xBC'
    EAR_OF_MAIZE = b'\xF0\x9F\x8C\xBD'
    EAR_OF_RICE = b'\xF0\x9F\x8C\xBE'
    HERB = b'\xF0\x9F\x8C\xBF'
    FOUR_LEAF_CLOVER = b'\xF0\x9F\x8D\x80'
    MAPLE_LEAF = b'\xF0\x9F\x8D\x81'
    FALLEN_LEAF = b'\xF0\x9F\x8D\x82'
    LEAF_FLUTTERING_IN_WIND = b'\xF0\x9F\x8D\x83'
    MUSHROOM = b'\xF0\x9F\x8D\x84'
    TOMATO = b'\xF0\x9F\x8D\x85'
    AUBERGINE = b'\xF0\x9F\x8D\x86'
    GRAPES = b'\xF0\x9F\x8D\x87'
    MELON = b'\xF0\x9F\x8D\x88'
    WATERMELON = b'\xF0\x9F\x8D\x89'
    TANGERINE = b'\xF0\x9F\x8D\x8A'
    BANANA = b'\xF0\x9F\x8D\x8C'
    PINEAPPLE = b'\xF0\x9F\x8D\x8D'
    RED_APPLE = b'\xF0\x9F\x8D\x8E'
    GREEN_APPLE = b'\xF0\x9F\x8D\x8F'
    PEACH = b'\xF0\x9F\x8D\x91'
    CHERRIES = b'\xF0\x9F\x8D\x92'
    STRAWBERRY = b'\xF0\x9F\x8D\x93'
    HAMBURGER = b'\xF0\x9F\x8D\x94'
    SLICE_OF_PIZZA = b'\xF0\x9F\x8D\x95'
    MEAT_ON_BONE = b'\xF0\x9F\x8D\x96'
    POULTRY_LEG = b'\xF0\x9F\x8D\x97'
    RICE_CRACKER = b'\xF0\x9F\x8D\x98'
    RICE_BALL = b'\xF0\x9F\x8D\x99'
    COOKED_RICE = b'\xF0\x9F\x8D\x9A'
    CURRY_AND_RICE = b'\xF0\x9F\x8D\x9B'
    STEAMING_BOWL = b'\xF0\x9F\x8D\x9C'
    SPAGHETTI = b'\xF0\x9F\x8D\x9D'
    BREAD = b'\xF0\x9F\x8D\x9E'
    FRENCH_FRIES = b'\xF0\x9F\x8D\x9F'
    ROASTED_SWEET_POTATO = b'\xF0\x9F\x8D\xA0'
    DANGO = b'\xF0\x9F\x8D\xA1'
    ODEN = b'\xF0\x9F\x8D\xA2'
    SUSHI = b'\xF0\x9F\x8D\xA3'
    FRIED_SHRIMP = b'\xF0\x9F\x8D\xA4'
    FISH_CAKE_WITH_SWIRL_DESIGN = b'\xF0\x9F\x8D\xA5'
    SOFT_ICE_CREAM = b'\xF0\x9F\x8D\xA6'
    SHAVED_ICE = b'\xF0\x9F\x8D\xA7'
    ICE_CREAM = b'\xF0\x9F\x8D\xA8'
    DOUGHNUT = b'\xF0\x9F\x8D\xA9'
    COOKIE = b'\xF0\x9F\x8D\xAA'
    CHOCOLATE_BAR = b'\xF0\x9F\x8D\xAB'
    CANDY = b'\xF0\x9F\x8D\xAC'
    LOLLIPOP = b'\xF0\x9F\x8D\xAD'
    CUSTARD = b'\xF0\x9F\x8D\xAE'
    HONEY_POT = b'\xF0\x9F\x8D\xAF'
    SHORTCAKE = b'\xF0\x9F\x8D\xB0'
    BENTO_BOX = b'\xF0\x9F\x8D\xB1'
    POT_OF_FOOD = b'\xF0\x9F\x8D\xB2'
    COOKING = b'\xF0\x9F\x8D\xB3'
    FORK_AND_KNIFE = b'\xF0\x9F\x8D\xB4'
    TEACUP_WITHOUT_HANDLE = b'\xF0\x9F\x8D\xB5'
    SAKE_BOTTLE_AND_CUP = b'\xF0\x9F\x8D\xB6'
    WINE_GLASS = b'\xF0\x9F\x8D\xB7'
    COCKTAIL_GLASS = b'\xF0\x9F\x8D\xB8'
    TROPICAL_DRINK = b'\xF0\x9F\x8D\xB9'
    BEER_MUG = b'\xF0\x9F\x8D\xBA'
    CLINKING_BEER_MUGS = b'\xF0\x9F\x8D\xBB'
    RIBBON = b'\xF0\x9F\x8E\x80'
    WRAPPED_PRESENT = b'\xF0\x9F\x8E\x81'
    BIRTHDAY_CAKE = b'\xF0\x9F\x8E\x82'
    JACK_O_LANTERN = b'\xF0\x9F\x8E\x83'
    CHRISTMAS_TREE = b'\xF0\x9F\x8E\x84'
    FATHER_CHRISTMAS = b'\xF0\x9F\x8E\x85'
    FIREWORKS = b'\xF0\x9F\x8E\x86'
    FIREWORK_SPARKLER = b'\xF0\x9F\x8E\x87'
    BALLOON = b'\xF0\x9F\x8E\x88'
    PARTY_POPPER = b'\xF0\x9F\x8E\x89'
    CONFETTI_BALL = b'\xF0\x9F\x8E\x8A'
    TANABATA_TREE = b'\xF0\x9F\x8E\x8B'
    CROSSED_FLAGS = b'\xF0\x9F\x8E\x8C'
    PINE_DECORATION = b'\xF0\x9F\x8E\x8D'
    JAPANESE_DOLLS = b'\xF0\x9F\x8E\x8E'
    CARP_STREAMER = b'\xF0\x9F\x8E\x8F'
    WIND_CHIME = b'\xF0\x9F\x8E\x90'
    MOON_VIEWING_CEREMONY = b'\xF0\x9F\x8E\x91'
    SCHOOL_SATCHEL = b'\xF0\x9F\x8E\x92'
    GRADUATION_CAP = b'\xF0\x9F\x8E\x93'
    CAROUSEL_HORSE = b'\xF0\x9F\x8E\xA0'
    FERRIS_WHEEL = b'\xF0\x9F\x8E\xA1'
    ROLLER_COASTER = b'\xF0\x9F\x8E\xA2'
    FISHING_POLE_AND_FISH = b'\xF0\x9F\x8E\xA3'
    MICROPHONE = b'\xF0\x9F\x8E\xA4'
    MOVIE_CAMERA = b'\xF0\x9F\x8E\xA5'
    CINEMA = b'\xF0\x9F\x8E\xA6'
    HEADPHONE = b'\xF0\x9F\x8E\xA7'
    ARTIST_PALETTE = b'\xF0\x9F\x8E\xA8'
    TOP_HAT = b'\xF0\x9F\x8E\xA9'
    CIRCUS_TENT = b'\xF0\x9F\x8E\xAA'
    TICKET = b'\xF0\x9F\x8E\xAB'
    CLAPPER_BOARD = b'\xF0\x9F\x8E\xAC'
    PERFORMING_ARTS = b'\xF0\x9F\x8E\xAD'
    VIDEO_GAME = b'\xF0\x9F\x8E\xAE'
    DIRECT_HIT = b'\xF0\x9F\x8E\xAF'
    SLOT_MACHINE = b'\xF0\x9F\x8E\xB0'
    BILLIARDS = b'\xF0\x9F\x8E\xB1'
    GAME_DIE = b'\xF0\x9F\x8E\xB2'
    BOWLING = b'\xF0\x9F\x8E\xB3'
    FLOWER_PLAYING_CARDS = b'\xF0\x9F\x8E\xB4'
    MUSICAL_NOTE = b'\xF0\x9F\x8E\xB5'
    MULTIPLE_MUSICAL_NOTES = b'\xF0\x9F\x8E\xB6'
    SAXOPHONE = b'\xF0\x9F\x8E\xB7'
    GUITAR = b'\xF0\x9F\x8E\xB8'
    MUSICAL_KEYBOARD = b'\xF0\x9F\x8E\xB9'
    TRUMPET = b'\xF0\x9F\x8E\xBA'
    VIOLIN = b'\xF0\x9F\x8E\xBB'
    MUSICAL_SCORE = b'\xF0\x9F\x8E\xBC'
    RUNNING_SHIRT_WITH_SASH = b'\xF0\x9F\x8E\xBD'
    TENNIS_RACQUET_AND_BALL = b'\xF0\x9F\x8E\xBE'
    SKI_AND_SKI_BOOT = b'\xF0\x9F\x8E\xBF'
    BASKETBALL_AND_HOOP = b'\xF0\x9F\x8F\x80'
    CHEQUERED_FLAG = b'\xF0\x9F\x8F\x81'
    SNOWBOARDER = b'\xF0\x9F\x8F\x82'
    RUNNER = b'\xF0\x9F\x8F\x83'
    SURFER = b'\xF0\x9F\x8F\x84'
    TROPHY = b'\xF0\x9F\x8F\x86'
    AMERICAN_FOOTBALL = b'\xF0\x9F\x8F\x88'
    SWIMMER = b'\xF0\x9F\x8F\x8A'
    HOUSE_BUILDING = b'\xF0\x9F\x8F\xA0'
    HOUSE_WITH_GARDEN = b'\xF0\x9F\x8F\xA1'
    OFFICE_BUILDING = b'\xF0\x9F\x8F\xA2'
    JAPANESE_POST_OFFICE = b'\xF0\x9F\x8F\xA3'
    HOSPITAL = b'\xF0\x9F\x8F\xA5'
    BANK = b'\xF0\x9F\x8F\xA6'
    AUTOMATED_TELLER_MACHINE = b'\xF0\x9F\x8F\xA7'
    HOTEL = b'\xF0\x9F\x8F\xA8'
    LOVE_HOTEL = b'\xF0\x9F\x8F\xA9'
    CONVENIENCE_STORE = b'\xF0\x9F\x8F\xAA'
    SCHOOL = b'\xF0\x9F\x8F\xAB'
    DEPARTMENT_STORE = b'\xF0\x9F\x8F\xAC'
    FACTORY = b'\xF0\x9F\x8F\xAD'
    IZAKAYA_LANTERN = b'\xF0\x9F\x8F\xAE'
    JAPANESE_CASTLE = b'\xF0\x9F\x8F\xAF'
    EUROPEAN_CASTLE = b'\xF0\x9F\x8F\xB0'
    SNAIL = b'\xF0\x9F\x90\x8C'
    SNAKE = b'\xF0\x9F\x90\x8D'
    HORSE = b'\xF0\x9F\x90\x8E'
    SHEEP = b'\xF0\x9F\x90\x91'
    MONKEY = b'\xF0\x9F\x90\x92'
    CHICKEN = b'\xF0\x9F\x90\x94'
    BOAR = b'\xF0\x9F\x90\x97'
    ELEPHANT = b'\xF0\x9F\x90\x98'
    OCTOPUS = b'\xF0\x9F\x90\x99'
    SPIRAL_SHELL = b'\xF0\x9F\x90\x9A'
    BUG = b'\xF0\x9F\x90\x9B'
    ANT = b'\xF0\x9F\x90\x9C'
    HONEYBEE = b'\xF0\x9F\x90\x9D'
    LADY_BEETLE = b'\xF0\x9F\x90\x9E'
    FISH = b'\xF0\x9F\x90\x9F'
    TROPICAL_FISH = b'\xF0\x9F\x90\xA0'
    BLOWFISH = b'\xF0\x9F\x90\xA1'
    TURTLE = b'\xF0\x9F\x90\xA2'
    HATCHING_CHICK = b'\xF0\x9F\x90\xA3'
    BABY_CHICK = b'\xF0\x9F\x90\xA4'
    FRONT_FACING_BABY_CHICK = b'\xF0\x9F\x90\xA5'
    BIRD = b'\xF0\x9F\x90\xA6'
    PENGUIN = b'\xF0\x9F\x90\xA7'
    KOALA = b'\xF0\x9F\x90\xA8'
    POODLE = b'\xF0\x9F\x90\xA9'
    BACTRIAN_CAMEL = b'\xF0\x9F\x90\xAB'
    DOLPHIN = b'\xF0\x9F\x90\xAC'
    MOUSE_FACE = b'\xF0\x9F\x90\xAD'
    COW_FACE = b'\xF0\x9F\x90\xAE'
    TIGER_FACE = b'\xF0\x9F\x90\xAF'
    RABBIT_FACE = b'\xF0\x9F\x90\xB0'
    CAT_FACE = b'\xF0\x9F\x90\xB1'
    DRAGON_FACE = b'\xF0\x9F\x90\xB2'
    SPOUTING_WHALE = b'\xF0\x9F\x90\xB3'
    HORSE_FACE = b'\xF0\x9F\x90\xB4'
    MONKEY_FACE = b'\xF0\x9F\x90\xB5'
    DOG_FACE = b'\xF0\x9F\x90\xB6'
    PIG_FACE = b'\xF0\x9F\x90\xB7'
    FROG_FACE = b'\xF0\x9F\x90\xB8'
    HAMSTER_FACE = b'\xF0\x9F\x90\xB9'
    WOLF_FACE = b'\xF0\x9F\x90\xBA'
    BEAR_FACE = b'\xF0\x9F\x90\xBB'
    PANDA_FACE = b'\xF0\x9F\x90\xBC'
    PIG_NOSE = b'\xF0\x9F\x90\xBD'
    PAW_PRINTS = b'\xF0\x9F\x90\xBE'
    EYES = b'\xF0\x9F\x91\x80'
    EAR = b'\xF0\x9F\x91\x82'
    NOSE = b'\xF0\x9F\x91\x83'
    MOUTH = b'\xF0\x9F\x91\x84'
    TONGUE = b'\xF0\x9F\x91\x85'
    WHITE_UP_POINTING_BACKHAND_INDEX = b'\xF0\x9F\x91\x86'
    WHITE_DOWN_POINTING_BACKHAND_INDEX = b'\xF0\x9F\x91\x87'
    WHITE_LEFT_POINTING_BACKHAND_INDEX = b'\xF0\x9F\x91\x88'
    WHITE_RIGHT_POINTING_BACKHAND_INDEX = b'\xF0\x9F\x91\x89'
    FISTED_HAND_SIGN = b'\xF0\x9F\x91\x8A'
    WAVING_HAND_SIGN = b'\xF0\x9F\x91\x8B'
    OK_HAND_SIGN = b'\xF0\x9F\x91\x8C'
    THUMBS_UP_SIGN = b'\xF0\x9F\x91\x8D'
    THUMBS_DOWN_SIGN = b'\xF0\x9F\x91\x8E'
    CLAPPING_HANDS_SIGN = b'\xF0\x9F\x91\x8F'
    OPEN_HANDS_SIGN = b'\xF0\x9F\x91\x90'
    CROWN = b'\xF0\x9F\x91\x91'
    WOMANS_HAT = b'\xF0\x9F\x91\x92'
    EYEGLASSES = b'\xF0\x9F\x91\x93'
    NECKTIE = b'\xF0\x9F\x91\x94'
    T_SHIRT = b'\xF0\x9F\x91\x95'
    JEANS = b'\xF0\x9F\x91\x96'
    DRESS = b'\xF0\x9F\x91\x97'
    KIMONO = b'\xF0\x9F\x91\x98'
    BIKINI = b'\xF0\x9F\x91\x99'
    WOMANS_CLOTHES = b'\xF0\x9F\x91\x9A'
    PURSE = b'\xF0\x9F\x91\x9B'
    HANDBAG = b'\xF0\x9F\x91\x9C'
    POUCH = b'\xF0\x9F\x91\x9D'
    MANS_SHOE = b'\xF0\x9F\x91\x9E'
    ATHLETIC_SHOE = b'\xF0\x9F\x91\x9F'
    HIGH_HEELED_SHOE = b'\xF0\x9F\x91\xA0'
    WOMANS_SANDAL = b'\xF0\x9F\x91\xA1'
    WOMANS_BOOTS = b'\xF0\x9F\x91\xA2'
    FOOTPRINTS = b'\xF0\x9F\x91\xA3'
    BUST_IN_SILHOUETTE = b'\xF0\x9F\x91\xA4'
    BOY = b'\xF0\x9F\x91\xA6'
    GIRL = b'\xF0\x9F\x91\xA7'
    MAN = b'\xF0\x9F\x91\xA8'
    WOMAN = b'\xF0\x9F\x91\xA9'
    FAMILY = b'\xF0\x9F\x91\xAA'
    MAN_AND_WOMAN_HOLDING_HANDS = b'\xF0\x9F\x91\xAB'
    POLICE_OFFICER = b'\xF0\x9F\x91\xAE'
    WOMAN_WITH_BUNNY_EARS = b'\xF0\x9F\x91\xAF'
    BRIDE_WITH_VEIL = b'\xF0\x9F\x91\xB0'
    PERSON_WITH_BLOND_HAIR = b'\xF0\x9F\x91\xB1'
    MAN_WITH_GUA_PI_MAO = b'\xF0\x9F\x91\xB2'
    MAN_WITH_TURBAN = b'\xF0\x9F\x91\xB3'
    OLDER_MAN = b'\xF0\x9F\x91\xB4'
    OLDER_WOMAN = b'\xF0\x9F\x91\xB5'
    BABY = b'\xF0\x9F\x91\xB6'
    CONSTRUCTION_WORKER = b'\xF0\x9F\x91\xB7'
    PRINCESS = b'\xF0\x9F\x91\xB8'
    JAPANESE_OGRE = b'\xF0\x9F\x91\xB9'
    JAPANESE_GOBLIN = b'\xF0\x9F\x91\xBA'
    GHOST = b'\xF0\x9F\x91\xBB'
    BABY_ANGEL = b'\xF0\x9F\x91\xBC'
    EXTRATERRESTRIAL_ALIEN = b'\xF0\x9F\x91\xBD'
    ALIEN_MONSTER = b'\xF0\x9F\x91\xBE'
    IMP = b'\xF0\x9F\x91\xBF'
    SKULL = b'\xF0\x9F\x92\x80'
    INFORMATION_DESK_PERSON = b'\xF0\x9F\x92\x81'
    GUARDSMAN = b'\xF0\x9F\x92\x82'
    DANCER = b'\xF0\x9F\x92\x83'
    LIPSTICK = b'\xF0\x9F\x92\x84'
    NAIL_POLISH = b'\xF0\x9F\x92\x85'
    FACE_MASSAGE = b'\xF0\x9F\x92\x86'
    HAIRCUT = b'\xF0\x9F\x92\x87'
    BARBER_POLE = b'\xF0\x9F\x92\x88'
    SYRINGE = b'\xF0\x9F\x92\x89'
    PILL = b'\xF0\x9F\x92\x8A'
    KISS_MARK = b'\xF0\x9F\x92\x8B'
    LOVE_LETTER = b'\xF0\x9F\x92\x8C'
    RING = b'\xF0\x9F\x92\x8D'
    GEM_STONE = b'\xF0\x9F\x92\x8E'
    KISS = b'\xF0\x9F\x92\x8F'
    BOUQUET = b'\xF0\x9F\x92\x90'
    COUPLE_WITH_HEART = b'\xF0\x9F\x92\x91'
    WEDDING = b'\xF0\x9F\x92\x92'
    BEATING_HEART = b'\xF0\x9F\x92\x93'
    BROKEN_HEART = b'\xF0\x9F\x92\x94'
    TWO_HEARTS = b'\xF0\x9F\x92\x95'
    SPARKLING_HEART = b'\xF0\x9F\x92\x96'
    GROWING_HEART = b'\xF0\x9F\x92\x97'
    HEART_WITH_ARROW = b'\xF0\x9F\x92\x98'
    BLUE_HEART = b'\xF0\x9F\x92\x99'
    GREEN_HEART = b'\xF0\x9F\x92\x9A'
    YELLOW_HEART = b'\xF0\x9F\x92\x9B'
    PURPLE_HEART = b'\xF0\x9F\x92\x9C'
    HEART_WITH_RIBBON = b'\xF0\x9F\x92\x9D'
    REVOLVING_HEARTS = b'\xF0\x9F\x92\x9E'
    HEART_DECORATION = b'\xF0\x9F\x92\x9F'
    DIAMOND_SHAPE_WITH_A_DOT_INSIDE = b'\xF0\x9F\x92\xA0'
    ELECTRIC_LIGHT_BULB = b'\xF0\x9F\x92\xA1'
    ANGER_SYMBOL = b'\xF0\x9F\x92\xA2'
    BOMB = b'\xF0\x9F\x92\xA3'
    SLEEPING_SYMBOL = b'\xF0\x9F\x92\xA4'
    COLLISION_SYMBOL = b'\xF0\x9F\x92\xA5'
    SPLASHING_SWEAT_SYMBOL = b'\xF0\x9F\x92\xA6'
    DROPLET = b'\xF0\x9F\x92\xA7'
    DASH_SYMBOL = b'\xF0\x9F\x92\xA8'
    PILE_OF_POO = b'\xF0\x9F\x92\xA9'
    FLEXED_BICEPS = b'\xF0\x9F\x92\xAA'
    DIZZY_SYMBOL = b'\xF0\x9F\x92\xAB'
    SPEECH_BALLOON = b'\xF0\x9F\x92\xAC'
    WHITE_FLOWER = b'\xF0\x9F\x92\xAE'
    HUNDRED_POINTS_SYMBOL = b'\xF0\x9F\x92\xAF'
    MONEY_BAG = b'\xF0\x9F\x92\xB0'
    CURRENCY_EXCHANGE = b'\xF0\x9F\x92\xB1'
    HEAVY_DOLLAR_SIGN = b'\xF0\x9F\x92\xB2'
    CREDIT_CARD = b'\xF0\x9F\x92\xB3'
    BANKNOTE_WITH_YEN_SIGN = b'\xF0\x9F\x92\xB4'
    BANKNOTE_WITH_DOLLAR_SIGN = b'\xF0\x9F\x92\xB5'
    MONEY_WITH_WINGS = b'\xF0\x9F\x92\xB8'
    CHART_WITH_UPWARDS_TREND_AND_YEN_SIGN = b'\xF0\x9F\x92\xB9'
    SEAT = b'\xF0\x9F\x92\xBA'
    PERSONAL_COMPUTER = b'\xF0\x9F\x92\xBB'
    BRIEFCASE = b'\xF0\x9F\x92\xBC'
    MINIDISC = b'\xF0\x9F\x92\xBD'
    FLOPPY_DISK = b'\xF0\x9F\x92\xBE'
    OPTICAL_DISC = b'\xF0\x9F\x92\xBF'
    DVD = b'\xF0\x9F\x93\x80'
    FILE_FOLDER = b'\xF0\x9F\x93\x81'
    OPEN_FILE_FOLDER = b'\xF0\x9F\x93\x82'
    PAGE_WITH_CURL = b'\xF0\x9F\x93\x83'
    PAGE_FACING_UP = b'\xF0\x9F\x93\x84'
    CALENDAR = b'\xF0\x9F\x93\x85'
    TEAR_OFF_CALENDAR = b'\xF0\x9F\x93\x86'
    CARD_INDEX = b'\xF0\x9F\x93\x87'
    CHART_WITH_UPWARDS_TREND = b'\xF0\x9F\x93\x88'
    CHART_WITH_DOWNWARDS_TREND = b'\xF0\x9F\x93\x89'
    BAR_CHART = b'\xF0\x9F\x93\x8A'
    CLIPBOARD = b'\xF0\x9F\x93\x8B'
    PUSHPIN = b'\xF0\x9F\x93\x8C'
    ROUND_PUSHPIN = b'\xF0\x9F\x93\x8D'
    PAPERCLIP = b'\xF0\x9F\x93\x8E'
    STRAIGHT_RULER = b'\xF0\x9F\x93\x8F'
    TRIANGULAR_RULER = b'\xF0\x9F\x93\x90'
    BOOKMARK_TABS = b'\xF0\x9F\x93\x91'
    LEDGER = b'\xF0\x9F\x93\x92'
    NOTEBOOK = b'\xF0\x9F\x93\x93'
    NOTEBOOK_WITH_DECORATIVE_COVER = b'\xF0\x9F\x93\x94'
    CLOSED_BOOK = b'\xF0\x9F\x93\x95'
    OPEN_BOOK = b'\xF0\x9F\x93\x96'
    GREEN_BOOK = b'\xF0\x9F\x93\x97'
    BLUE_BOOK = b'\xF0\x9F\x93\x98'
    ORANGE_BOOK = b'\xF0\x9F\x93\x99'
    BOOKS = b'\xF0\x9F\x93\x9A'
    NAME_BADGE = b'\xF0\x9F\x93\x9B'
    SCROLL = b'\xF0\x9F\x93\x9C'
    MEMO = b'\xF0\x9F\x93\x9D'
    TELEPHONE_RECEIVER = b'\xF0\x9F\x93\x9E'
    PAGER = b'\xF0\x9F\x93\x9F'
    FAX_MACHINE = b'\xF0\x9F\x93\xA0'
    SATELLITE_ANTENNA = b'\xF0\x9F\x93\xA1'
    PUBLIC_ADDRESS_LOUDSPEAKER = b'\xF0\x9F\x93\xA2'
    CHEERING_MEGAPHONE = b'\xF0\x9F\x93\xA3'
    OUTBOX_TRAY = b'\xF0\x9F\x93\xA4'
    INBOX_TRAY = b'\xF0\x9F\x93\xA5'
    PACKAGE = b'\xF0\x9F\x93\xA6'
    E_MAIL_SYMBOL = b'\xF0\x9F\x93\xA7'
    INCOMING_ENVELOPE = b'\xF0\x9F\x93\xA8'
    ENVELOPE_WITH_DOWNWARDS_ARROW_ABOVE = b'\xF0\x9F\x93\xA9'
    CLOSED_MAILBOX_WITH_LOWERED_FLAG = b'\xF0\x9F\x93\xAA'
    CLOSED_MAILBOX_WITH_RAISED_FLAG = b'\xF0\x9F\x93\xAB'
    POSTBOX = b'\xF0\x9F\x93\xAE'
    NEWSPAPER = b'\xF0\x9F\x93\xB0'
    MOBILE_PHONE = b'\xF0\x9F\x93\xB1'
    MOBILE_PHONE_WITH_RIGHTWARDS_ARROW_AT_LEFT = b'\xF0\x9F\x93\xB2'
    VIBRATION_MODE = b'\xF0\x9F\x93\xB3'
    MOBILE_PHONE_OFF = b'\xF0\x9F\x93\xB4'
    ANTENNA_WITH_BARS = b'\xF0\x9F\x93\xB6'
    CAMERA = b'\xF0\x9F\x93\xB7'
    VIDEO_CAMERA = b'\xF0\x9F\x93\xB9'
    TELEVISION = b'\xF0\x9F\x93\xBA'
    RADIO = b'\xF0\x9F\x93\xBB'
    VIDEOCASSETTE = b'\xF0\x9F\x93\xBC'
    CLOCKWISE_DOWNWARDS_AND_UPWARDS_OPEN_CIRCLE_ARROWS = b'\xF0\x9F\x94\x83'
    SPEAKER_WITH_THREE_SOUND_WAVES = b'\xF0\x9F\x94\x8A'
    BATTERY = b'\xF0\x9F\x94\x8B'
    ELECTRIC_PLUG = b'\xF0\x9F\x94\x8C'
    LEFT_POINTING_MAGNIFYING_GLASS = b'\xF0\x9F\x94\x8D'
    RIGHT_POINTING_MAGNIFYING_GLASS = b'\xF0\x9F\x94\x8E'
    LOCK_WITH_INK_PEN = b'\xF0\x9F\x94\x8F'
    CLOSED_LOCK_WITH_KEY = b'\xF0\x9F\x94\x90'
    KEY = b'\xF0\x9F\x94\x91'
    LOCK = b'\xF0\x9F\x94\x92'
    OPEN_LOCK = b'\xF0\x9F\x94\x93'
    BELL = b'\xF0\x9F\x94\x94'
    BOOKMARK = b'\xF0\x9F\x94\x96'
    LINK_SYMBOL = b'\xF0\x9F\x94\x97'
    RADIO_BUTTON = b'\xF0\x9F\x94\x98'
    BACK_WITH_LEFTWARDS_ARROW_ABOVE = b'\xF0\x9F\x94\x99'
    END_WITH_LEFTWARDS_ARROW_ABOVE = b'\xF0\x9F\x94\x9A'
    ON_WITH_EXCLAMATION_MARK_WITH_LEFT_RIGHT_ARROW_ABOVE = b'\xF0\x9F\x94\x9B'
    SOON_WITH_RIGHTWARDS_ARROW_ABOVE = b'\xF0\x9F\x94\x9C'
    TOP_WITH_UPWARDS_ARROW_ABOVE = b'\xF0\x9F\x94\x9D'
    NO_ONE_UNDER_EIGHTEEN_SYMBOL = b'\xF0\x9F\x94\x9E'
    KEYCAP_TEN = b'\xF0\x9F\x94\x9F'
    INPUT_SYMBOL_FOR_LATIN_CAPITAL_LETTERS = b'\xF0\x9F\x94\xA0'
    INPUT_SYMBOL_FOR_LATIN_SMALL_LETTERS = b'\xF0\x9F\x94\xA1'
    INPUT_SYMBOL_FOR_NUMBERS = b'\xF0\x9F\x94\xA2'
    INPUT_SYMBOL_FOR_SYMBOLS = b'\xF0\x9F\x94\xA3'
    INPUT_SYMBOL_FOR_LATIN_LETTERS = b'\xF0\x9F\x94\xA4'
    FIRE = b'\xF0\x9F\x94\xA5'
    ELECTRIC_TORCH = b'\xF0\x9F\x94\xA6'
    WRENCH = b'\xF0\x9F\x94\xA7'
    HAMMER = b'\xF0\x9F\x94\xA8'
    NUT_AND_BOLT = b'\xF0\x9F\x94\xA9'
    HOCHO = b'\xF0\x9F\x94\xAA'
    PISTOL = b'\xF0\x9F\x94\xAB'
    CRYSTAL_BALL = b'\xF0\x9F\x94\xAE'
    SIX_POINTED_STAR_WITH_MIDDLE_DOT = b'\xF0\x9F\x94\xAF'
    JAPANESE_SYMBOL_FOR_BEGINNER = b'\xF0\x9F\x94\xB0'
    TRIDENT_EMBLEM = b'\xF0\x9F\x94\xB1'
    BLACK_SQUARE_BUTTON = b'\xF0\x9F\x94\xB2'
    WHITE_SQUARE_BUTTON = b'\xF0\x9F\x94\xB3'
    LARGE_RED_CIRCLE = b'\xF0\x9F\x94\xB4'
    LARGE_BLUE_CIRCLE = b'\xF0\x9F\x94\xB5'
    LARGE_ORANGE_DIAMOND = b'\xF0\x9F\x94\xB6'
    LARGE_BLUE_DIAMOND = b'\xF0\x9F\x94\xB7'
    SMALL_ORANGE_DIAMOND = b'\xF0\x9F\x94\xB8'
    SMALL_BLUE_DIAMOND = b'\xF0\x9F\x94\xB9'
    UP_POINTING_RED_TRIANGLE = b'\xF0\x9F\x94\xBA'
    DOWN_POINTING_RED_TRIANGLE = b'\xF0\x9F\x94\xBB'
    UP_POINTING_SMALL_RED_TRIANGLE = b'\xF0\x9F\x94\xBC'
    DOWN_POINTING_SMALL_RED_TRIANGLE = b'\xF0\x9F\x94\xBD'
    CLOCK_FACE_ONE_OCLOCK = b'\xF0\x9F\x95\x90'
    CLOCK_FACE_TWO_OCLOCK = b'\xF0\x9F\x95\x91'
    CLOCK_FACE_THREE_OCLOCK = b'\xF0\x9F\x95\x92'
    CLOCK_FACE_FOUR_OCLOCK = b'\xF0\x9F\x95\x93'
    CLOCK_FACE_FIVE_OCLOCK = b'\xF0\x9F\x95\x94'
    CLOCK_FACE_SIX_OCLOCK = b'\xF0\x9F\x95\x95'
    CLOCK_FACE_SEVEN_OCLOCK = b'\xF0\x9F\x95\x96'
    CLOCK_FACE_EIGHT_OCLOCK = b'\xF0\x9F\x95\x97'
    CLOCK_FACE_NINE_OCLOCK = b'\xF0\x9F\x95\x98'
    CLOCK_FACE_TEN_OCLOCK = b'\xF0\x9F\x95\x99'
    CLOCK_FACE_ELEVEN_OCLOCK = b'\xF0\x9F\x95\x9A'
    CLOCK_FACE_TWELVE_OCLOCK = b'\xF0\x9F\x95\x9B'
    MOUNT_FUJI = b'\xF0\x9F\x97\xBB'
    TOKYO_TOWER = b'\xF0\x9F\x97\xBC'
    STATUE_OF_LIBERTY = b'\xF0\x9F\x97\xBD'
    SILHOUETTE_OF_JAPAN = b'\xF0\x9F\x97\xBE'
    MOYAI = b'\xF0\x9F\x97\xBF'
    GRINNING_FACE = b'\xF0\x9F\x98\x80'
    SMILING_FACE_WITH_HALO = b'\xF0\x9F\x98\x87'
    SMILING_FACE_WITH_HORNS = b'\xF0\x9F\x98\x88'
    SMILING_FACE_WITH_SUNGLASSES = b'\xF0\x9F\x98\x8E'
    NEUTRAL_FACE = b'\xF0\x9F\x98\x90'
    EXPRESSIONLESS_FACE = b'\xF0\x9F\x98\x91'
    CONFUSED_FACE = b'\xF0\x9F\x98\x95'
    KISSING_FACE = b'\xF0\x9F\x98\x97'
    KISSING_FACE_WITH_SMILING_EYES = b'\xF0\x9F\x98\x99'
    FACE_WITH_STUCK_OUT_TONGUE = b'\xF0\x9F\x98\x9B'
    WORRIED_FACE = b'\xF0\x9F\x98\x9F'
    FROWNING_FACE_WITH_OPEN_MOUTH = b'\xF0\x9F\x98\xA6'
    ANGUISHED_FACE = b'\xF0\x9F\x98\xA7'
    GRIMACING_FACE = b'\xF0\x9F\x98\xAC'
    FACE_WITH_OPEN_MOUTH = b'\xF0\x9F\x98\xAE'
    HUSHED_FACE = b'\xF0\x9F\x98\xAF'
    SLEEPING_FACE = b'\xF0\x9F\x98\xB4'
    FACE_WITHOUT_MOUTH = b'\xF0\x9F\x98\xB6'
    HELICOPTER = b'\xF0\x9F\x9A\x81'
    STEAM_LOCOMOTIVE = b'\xF0\x9F\x9A\x82'
    TRAIN = b'\xF0\x9F\x9A\x86'
    LIGHT_RAIL = b'\xF0\x9F\x9A\x88'
    TRAM = b'\xF0\x9F\x9A\x8A'
    ONCOMING_BUS = b'\xF0\x9F\x9A\x8D'
    TROLLEYBUS = b'\xF0\x9F\x9A\x8E'
    MINIBUS = b'\xF0\x9F\x9A\x90'
    ONCOMING_POLICE_CAR = b'\xF0\x9F\x9A\x94'
    ONCOMING_TAXI = b'\xF0\x9F\x9A\x96'
    ONCOMING_AUTOMOBILE = b'\xF0\x9F\x9A\x98'
    ARTICULATED_LORRY = b'\xF0\x9F\x9A\x9B'
    TRACTOR = b'\xF0\x9F\x9A\x9C'
    MONORAIL = b'\xF0\x9F\x9A\x9D'
    MOUNTAIN_RAILWAY = b'\xF0\x9F\x9A\x9E'
    SUSPENSION_RAILWAY = b'\xF0\x9F\x9A\x9F'
    MOUNTAIN_CABLEWAY = b'\xF0\x9F\x9A\xA0'
    AERIAL_TRAMWAY = b'\xF0\x9F\x9A\xA1'
    ROWBOAT = b'\xF0\x9F\x9A\xA3'
    VERTICAL_TRAFFIC_LIGHT = b'\xF0\x9F\x9A\xA6'
    PUT_LITTER_IN_ITS_PLACE_SYMBOL = b'\xF0\x9F\x9A\xAE'
    DO_NOT_LITTER_SYMBOL = b'\xF0\x9F\x9A\xAF'
    POTABLE_WATER_SYMBOL = b'\xF0\x9F\x9A\xB0'
    NON_POTABLE_WATER_SYMBOL = b'\xF0\x9F\x9A\xB1'
    NO_BICYCLES = b'\xF0\x9F\x9A\xB3'
    BICYCLIST = b'\xF0\x9F\x9A\xB4'
    MOUNTAIN_BICYCLIST = b'\xF0\x9F\x9A\xB5'
    NO_PEDESTRIANS = b'\xF0\x9F\x9A\xB7'
    CHILDREN_CROSSING = b'\xF0\x9F\x9A\xB8'
    SHOWER = b'\xF0\x9F\x9A\xBF'
    BATHTUB = b'\xF0\x9F\x9B\x81'
    PASSPORT_CONTROL = b'\xF0\x9F\x9B\x82'
    CUSTOMS = b'\xF0\x9F\x9B\x83'
    BAGGAGE_CLAIM = b'\xF0\x9F\x9B\x84'
    LEFT_LUGGAGE = b'\xF0\x9F\x9B\x85'
    EARTH_GLOBE_EUROPE_AFRICA = b'\xF0\x9F\x8C\x8D'
    EARTH_GLOBE_AMERICAS = b'\xF0\x9F\x8C\x8E'
    GLOBE_WITH_MERIDIANS = b'\xF0\x9F\x8C\x90'
    WAXING_CRESCENT_MOON_SYMBOL = b'\xF0\x9F\x8C\x92'
    WANING_GIBBOUS_MOON_SYMBOL = b'\xF0\x9F\x8C\x96'
    LAST_QUARTER_MOON_SYMBOL = b'\xF0\x9F\x8C\x97'
    WANING_CRESCENT_MOON_SYMBOL = b'\xF0\x9F\x8C\x98'
    NEW_MOON_WITH_FACE = b'\xF0\x9F\x8C\x9A'
    LAST_QUARTER_MOON_WITH_FACE = b'\xF0\x9F\x8C\x9C'
    FULL_MOON_WITH_FACE = b'\xF0\x9F\x8C\x9D'
    SUN_WITH_FACE = b'\xF0\x9F\x8C\x9E'
    EVERGREEN_TREE = b'\xF0\x9F\x8C\xB2'
    DECIDUOUS_TREE = b'\xF0\x9F\x8C\xB3'
    LEMON = b'\xF0\x9F\x8D\x8B'
    PEAR = b'\xF0\x9F\x8D\x90'
    BABY_BOTTLE = b'\xF0\x9F\x8D\xBC'
    HORSE_RACING = b'\xF0\x9F\x8F\x87'
    RUGBY_FOOTBALL = b'\xF0\x9F\x8F\x89'
    EUROPEAN_POST_OFFICE = b'\xF0\x9F\x8F\xA4'
    RAT = b'\xF0\x9F\x90\x80'
    MOUSE = b'\xF0\x9F\x90\x81'
    OX = b'\xF0\x9F\x90\x82'
    WATER_BUFFALO = b'\xF0\x9F\x90\x83'
    COW = b'\xF0\x9F\x90\x84'
    TIGER = b'\xF0\x9F\x90\x85'
    LEOPARD = b'\xF0\x9F\x90\x86'
    RABBIT = b'\xF0\x9F\x90\x87'
    CAT = b'\xF0\x9F\x90\x88'
    DRAGON = b'\xF0\x9F\x90\x89'
    CROCODILE = b'\xF0\x9F\x90\x8A'
    WHALE = b'\xF0\x9F\x90\x8B'
    RAM = b'\xF0\x9F\x90\x8F'
    GOAT = b'\xF0\x9F\x90\x90'
    ROOSTER = b'\xF0\x9F\x90\x93'
    DOG = b'\xF0\x9F\x90\x95'
    PIG = b'\xF0\x9F\x90\x96'
    DROMEDARY_CAMEL = b'\xF0\x9F\x90\xAA'
    BUSTS_IN_SILHOUETTE = b'\xF0\x9F\x91\xA5'
    TWO_MEN_HOLDING_HANDS = b'\xF0\x9F\x91\xAC'
    TWO_WOMEN_HOLDING_HANDS = b'\xF0\x9F\x91\xAD'
    THOUGHT_BALLOON = b'\xF0\x9F\x92\xAD'
    BANKNOTE_WITH_EURO_SIGN = b'\xF0\x9F\x92\xB6'
    BANKNOTE_WITH_POUND_SIGN = b'\xF0\x9F\x92\xB7'
    OPEN_MAILBOX_WITH_RAISED_FLAG = b'\xF0\x9F\x93\xAC'
    OPEN_MAILBOX_WITH_LOWERED_FLAG = b'\xF0\x9F\x93\xAD'
    POSTAL_HORN = b'\xF0\x9F\x93\xAF'
    NO_MOBILE_PHONES = b'\xF0\x9F\x93\xB5'
    TWISTED_RIGHTWARDS_ARROWS = b'\xF0\x9F\x94\x80'
    CLOCKWISE_RIGHTWARDS_AND_LEFTWARDS_OPEN_CIRCLE_ARROWS = b'\xF0\x9F\x94\x81'
    CLOCKWISE_RIGHTWARDS_AND_LEFTWARDS_OPEN_CIRCLE_ARROWS_WITH_CIRCLED_ONE_OVERLAY = b'\xF0\x9F\x94\x82'
    ANTICLOCKWISE_DOWNWARDS_AND_UPWARDS_OPEN_CIRCLE_ARROWS = b'\xF0\x9F\x94\x84'
    LOW_BRIGHTNESS_SYMBOL = b'\xF0\x9F\x94\x85'
    HIGH_BRIGHTNESS_SYMBOL = b'\xF0\x9F\x94\x86'
    SPEAKER_WITH_CANCELLATION_STROKE = b'\xF0\x9F\x94\x87'
    SPEAKER_WITH_ONE_SOUND_WAVE = b'\xF0\x9F\x94\x89'
    BELL_WITH_CANCELLATION_STROKE = b'\xF0\x9F\x94\x95'
    MICROSCOPE = b'\xF0\x9F\x94\xAC'
    TELESCOPE = b'\xF0\x9F\x94\xAD'
    CLOCK_FACE_ONE_THIRTY = b'\xF0\x9F\x95\x9C'
    CLOCK_FACE_TWO_THIRTY = b'\xF0\x9F\x95\x9D'
    CLOCK_FACE_THREE_THIRTY = b'\xF0\x9F\x95\x9E'
    CLOCK_FACE_FOUR_THIRTY = b'\xF0\x9F\x95\x9F'
    CLOCK_FACE_FIVE_THIRTY = b'\xF0\x9F\x95\xA0'
    CLOCK_FACE_SIX_THIRTY = b'\xF0\x9F\x95\xA1'
    CLOCK_FACE_SEVEN_THIRTY = b'\xF0\x9F\x95\xA2'
    CLOCK_FACE_EIGHT_THIRTY = b'\xF0\x9F\x95\xA3'
    CLOCK_FACE_NINE_THIRTY = b'\xF0\x9F\x95\xA4'
    CLOCK_FACE_TEN_THIRTY = b'\xF0\x9F\x95\xA5'
    CLOCK_FACE_ELEVEN_THIRTY = b'\xF0\x9F\x95\xA6'
    CLOCK_FACE_TWELVE_THIRTY = b'\xF0\x9F\x95\xA7'


class Catalog:
    def __init__(self, name):
        self.name = name


class Product:
    def __init__(self, user_id):
        self.user_id = user_id
        self.product = None
        self.section = None
        self.price = None
        self.amount = None
        self.amount_MAX = None
        self.code = None


class AddProduct:
    def __init__(self, section):
        self.section = section
        self.product = None
        self.price = None
        self.info = None


class DownloadProduct:
    def __init__(self, name_section):
        self.name_section = name_section
        self.name_product = None


class GiveBalance:
    def __init__(self, login):
        self.login = login
        self.balance = None
        self.code = None


class send_message_admin:
    def __init__(self, user_id):
        self.user_id = user_id
        self.text = None

def left_right_to_emoji(string):
    y = string
    result = []
   
    if y == "left":
        result.append(Emoji.BLACK_LEFT_POINTING_TRIANGLE)
    elif y == "right":
        result.append(Emoji.BLACK_RIGHT_POINTING_TRIANGLE)
    else:
        result.append(Emoji.DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP)
    
    txt = b' '.join(result)
    return txt.decode('utf-8')

def number_to_emoji(number):
    y = str(number)
    result = []
    for i in range(0, len(y)):
        x = y[i]
        if x == "1":
            result.append(Emoji.DIGIT_ONE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "2":
            result.append(Emoji.DIGIT_TWO_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "3":
            result.append(Emoji.DIGIT_THREE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "4":
            result.append(Emoji.DIGIT_FOUR_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "5":
            result.append(Emoji.DIGIT_FIVE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "6":
            result.append(Emoji.DIGIT_SIX_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "7":
            result.append(Emoji.DIGIT_SEVEN_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "8":
            result.append(Emoji.DIGIT_EIGHT_PLUS_COMBINING_ENCLOSING_KEYCAP)
        elif x == "9":
            result.append(Emoji.DIGIT_NINE_PLUS_COMBINING_ENCLOSING_KEYCAP)
        else:
            result.append(Emoji.DIGIT_ZERO_PLUS_COMBINING_ENCLOSING_KEYCAP)
    
    txt = b' '.join(result)
    return txt.decode('utf-8')

# Menu catalog
def menu_catalog(user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM catalog')
    row = cursor.fetchall()

    catalog_index = 1
    catalog_index = dwn_section_user(user_id)

    menu = types.InlineKeyboardMarkup(row_width=3)

    for i in row:
        menu.add(types.InlineKeyboardButton(text=f'{i[0]}', callback_data=f'{i[1]}'))

    menu.add(types.InlineKeyboardButton(text='??????????', callback_data='exit_menu'))

    cursor.close()
    conn.close()

    return menu

# User Download
def dwn_section_user(user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    cursor.execute(f"SELECT section_index FROM users WHERE user_id = '{user_id}'")
    row = cursor.fetchall()

    cursor.close()
    conn.close()

    return row[0][0]


# User Download
def dwn_lcd_user(user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    cursor.execute(f"SELECT last_call_data FROM users WHERE user_id = '{user_id}'")
    row = cursor.fetchall()

    cursor.close()
    conn.close()

    return row[0][0]


# User Update
def update_user_lsd(user_id, lccd):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    if lccd in list_sections():
        cursor.execute(f"UPDATE users SET 'last_call_data' = '{lccd}' WHERE user_id = '{user_id}'")

    conn.commit()
    cursor.close()
    conn.close()

# User Update
def update_user(user_id, section_index, lcd):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    if lcd in list_sections():
        cursor.execute(f"UPDATE users SET 'section_index' = '{section_index}', 'last_call_data' = '{lcd}' WHERE user_id = '{user_id}'")
    else:
        cursor.execute(f"UPDATE users SET 'section_index' = '{section_index}' WHERE user_id = '{user_id}'")

    conn.commit()
    cursor.close()
    conn.close()

# Menu section
def menu_section(name_section, user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    
    lcd = ""
    section_index = 1
    section_index = dwn_section_user(user_id)
    
    if name_section is None or name_section == "Update":
        name_section = dwn_lcd_user(user_id)
    else:
        lcd = name_section

    cursor.execute(f"SELECT * FROM '{name_section}' ")
    row = cursor.fetchall()

    menu = types.InlineKeyboardMarkup(row_width=3)
    
    for index, i in enumerate(row):
        if index >= ((section_index - 1) * 10) and index < (section_index * 10) and index <= len(row):
            menu.add(types.InlineKeyboardButton(text=f'{i[0]}', callback_data=f'{i[2]}'))
    
    if len(row) >= 10:
        if section_index <= 1:                
            menu.add(
                    types.InlineKeyboardButton(text=number_to_emoji(section_index), callback_data='search_section'),
                    types.InlineKeyboardButton(text=left_right_to_emoji("right"), callback_data='right_section_list')
                )
        elif section_index > 1 and section_index < (len(row) % 10):
            menu.add(
                types.InlineKeyboardButton(text=left_right_to_emoji("left"), callback_data='left_section_list'),
                types.InlineKeyboardButton(text=number_to_emoji(section_index), callback_data='search_section'),
                types.InlineKeyboardButton(text=left_right_to_emoji("right"), callback_data='right_section_list')
            )
        else:
            menu.add(
                types.InlineKeyboardButton(text=left_right_to_emoji("left"), callback_data='left_section_list'),
                types.InlineKeyboardButton(text=number_to_emoji(section_index), callback_data='search_section')
            )

    menu.add(types.InlineKeyboardButton(text='??????????', callback_data='exit_menu'))

    cursor.close()
    conn.close()
    
    update_user(user_id, section_index, lcd)

    return menu


# Menu product
def menu_product(product, dict):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    row = cursor.execute(f'SELECT * FROM section WHERE code = "{product}"').fetchone()
    section = row[1]
    info = row[3]

    amount = len(cursor.execute(f'SELECT * FROM "{product}"').fetchall())

    cursor.execute(f'SELECT * FROM "{section}" WHERE code = "{product}"')
    row = cursor.fetchone()

    dict.section = section
    dict.product = product
    dict.amount_MAX = amount
    dict.price = row[1]

    text = settings.text_purchase.format(
        name=row[0],
        info=info,
        price=row[1],
        amount=amount
    )

    return text, dict

#   Admin menu - add_to_section_to_catalog
def add_section_catalog(name_section):
    # Connection
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    code = random.randint(11111, 99999)
    # Add
    cursor.execute(f"INSERT INTO catalog VALUES ('{name_section}', '{code}')")
    conn.commit()

    # Create table section
    conn.execute(f"CREATE TABLE '{code}' (list text, price text, code text)")

    # Close connection
    cursor.close()
    conn.close()


# Admin menu - delete_section_catalog
def delete_section_catalog(name_section):
    # Connection
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    # Del
    cursor.execute(f"DELETE FROM catalog WHERE code = '{name_section}'")
    conn.commit()

    cursor.execute(f"DROP TABLE '{name_section}'")

    row = cursor.execute(f'SELECT * FROM section WHERE section = "{name_section}"').fetchall()

    for i in range(len(row)):
        cursor.execute(f'DROP TABLE "{row[i][2]}"')

        cursor.execute(f'DELETE FROM section WHERE code = "{row[i][2]}"')
        conn.commit()

    # Close connection
    cursor.close()
    conn.close()


# Admin menu - add_product_section
def add_product_section(name_product, price, name_section, info):
    # Connection
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    code = random.randint(11111, 99999)

    cursor.execute(f"INSERT INTO '{name_section}' VALUES ('{name_product}', '{price}', '{code}')")
    conn.commit()

    cursor.execute(f"INSERT INTO 'section' VALUES ('{name_product}', '{name_section}', '{code}', '{info}')")
    conn.commit()

    # Create table product
    cursor.execute(f"CREATE TABLE '{code}' (list text, code text)")

    # Close connection
    cursor.close()
    conn.close()


# Admin menu - delete_product_section
def delete_product_section(name_product, section):
    # Connection
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    # del
    product = cursor.execute(f'SELECT * FROM "{section}" WHERE list = "{name_product}"').fetchone()

    cursor.execute(f"DELETE FROM '{section}' WHERE list = '{name_product}'")
    conn.commit()

    cursor.execute(f"DROP TABLE '{product[2]}'")

    # Close connection
    cursor.close()
    conn.close()


def product_download(name_file, product):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    file = open(name_file, 'r')

    for i in file:
        cursor.execute(f"INSERT INTO '{product}' VALUES ('{i}', '{random.randint(111111, 999999)}')")

    conn.commit()

    file.close()
    os.remove(name_file)

    cursor.close()
    conn.close()


def basket(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM purchase_information WHERE user_id = "{user_id}"').fetchall()

    text = ''

    for i in row:
        text = text + '???? ' + i[2][:10:] + ' | ' + i[1] + '\n\n'

    return text


def first_join(user_id, name, code):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"').fetchall()

    ref_code = code
    if ref_code == '':
        ref_code = 0
    
    if len(row) == 0:
        cursor.execute(f'INSERT INTO users VALUES ("{user_id}", "{name}", "{datetime.datetime.now()}", "{user_id}", "{ref_code}", "0", "1", "1", "", "user")')
        conn.commit()



def admin_info():
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()
    row = cursor.execute(f'SELECT * FROM users').fetchone()

    current_time = str(datetime.datetime.now())

    amount_user_all = 0
    amount_user_day = 0
    amount_user_hour = 0

    while row is not None:
        amount_user_all += 1
        if row[2][:-15:] == current_time[:-15:]:
            amount_user_day += 1
        if row[2][:-13:] == current_time[:-13:]:
            amount_user_hour += 1

        row = cursor.fetchone()

    msg = '??? ????????????????????:\n\n' \
          f'??? ???? ?????? ?????????? - {amount_user_all}\n' \
          f'??? ???? ???????? - {amount_user_day}\n' \
          f'??? ???? ?????? - {amount_user_hour}'

    return msg

def wait_payment(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()
    try:
        session = requests.Session()
        session.headers['authorization'] = 'Bearer ' + settings.QIWI_TOKEN
        parameters = {'rows': '5'}
        h = session.get(
            'https://edge.qiwi.com/payment-history/v1/persons/{}/payments'.format(settings.QIWI_NUMBER),
            params=parameters)
        req = json.loads(h.text)
        result = cursor.execute(f'SELECT * FROM wait_payment WHERE user_id = {user_id}').fetchone()
        comment = result[1]

        for i in range(len(req['data'])):
            if comment in str(req['data'][i]['comment']):
                balance = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"').fetchone()

                balance = float(balance[5]) + float(req["data"][i]["sum"]["amount"])

                cursor.execute(f'UPDATE users SET balance = {balance} WHERE user_id = "{user_id}"')
                conn.commit()

                cursor.execute(f'DELETE FROM wait_payment WHERE user_id = "{user_id}"')
                conn.commit()

                referral_link(user_id, float(req["data"][i]["sum"]["amount"]))

                return 1, req["data"][i]["sum"]["amount"]
    except Exception as e:
        print(e)

    return 0, 0

def get_pay_code(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'SELECT code FROM wait_payment WHERE user_id = "{user_id}"')
    pcode = cursor.fetchall()

    return pcode[0][0]

def get_pay_url(chat_id):
    return "https://qiwi.com/payment/form/99?extra%5B%27account%27%5D=" + settings.QIWI_NUMBER + "&amountInteger=None&amountFraction=0&extra%5B%27comment%27%5D=" + get_pay_code(chat_id) + "&currency=643&blocked[0]=account&blocked[2]=comment"

def request_code_balance(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    code = random.randint(1111111111, 9999999999)
    
    cursor.execute(f'SELECT * FROM wait_payment WHERE user_id = "{user_id}"')
    row = cursor.fetchall()
    
    if len(row) > 0:
        cursor.execute(f'DELETE FROM wait_payment WHERE user_id = "{user_id}"')
        conn.commit()

    cursor.execute(f'INSERT INTO wait_payment VALUES ("{user_id}", "{code}", "0")')
    conn.commit()

def balance_replenish(user_id):
    msg = settings.balance_replenish.format(
        number=settings.QIWI_NUMBER,
        code=get_pay_code(user_id),
    )

    return msg

def cancel_payment(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM wait_payment WHERE user_id = "{user_id}"')
    conn.commit()

def profile(user_id):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    row = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"').fetchone()

    return row


def buy(dict):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    data = str(datetime.datetime.now())
    list = ''
    cursor.execute(f'SELECT * FROM "{dict.product}"')
    row = cursor.fetchmany(int(dict.amount))

    for i in range(int(dict.amount)):
        list = list + f'???? {data[:19]} | {row[i][0]}\n'


        cursor.execute(f'INSERT INTO purchase_information VALUES ("{dict.user_id}", "{row[i][0]}", "{data}")')
        conn.commit()

        cursor.execute(f'DELETE FROM "{dict.product}" WHERE code = "{row[i][1]}"')
        conn.commit()


    balance = cursor.execute(f'SELECT * FROM users WHERE user_id = "{dict.user_id}"').fetchone()
    balance = float(balance[5]) - (float(dict.price) * float(dict.amount))
    cursor.execute(f'UPDATE users SET balance = "{balance}" WHERE user_id = "{dict.user_id}"')
    conn.commit()

    return list

def give_money(dict):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'UPDATE users SET balance = "{dict.balance}" WHERE user_id = "{dict.login}"')
    conn.commit()

def check_balance(user_id, price):
    conn = sqlite3.connect('bd.sqlite')
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    row = cursor.fetchone()

    if float(row[5]) >= float(price):
        return 1
    else:
        return 0


def list_sections():
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM catalog')
    row = cursor.fetchall()

    sections = []

    for i in row:
        sections.append(i[1])

    return sections


def list_product():
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM section')
    row = cursor.fetchall()

    list_product = []

    for i in row:
        list_product.append(i[2])

    return list_product


def check_referral_code(user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    user = cursor.fetchone()

    if int(user[3]) == 0:
        cursor.execute(f'UPDATE users SET ref_code = {user_id} WHERE user_id = "{user_id}"')
        conn.commit()

    return user_id
        

def referral_link(user_id, deposit_sum):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM users WHERE user_id = "{user_id}"')
    user = cursor.fetchone()

    if user[4] == '0':
        return
    else:
        user2 = cursor.execute(f'SELECT * FROM users WHERE user_id = "{user[4]}"').fetchone()

        profit = (deposit_sum / 100) * float(settings.referrral_percent)

        balance = float(user[5]) + profit

        cursor.execute(f'UPDATE users SET balance = {balance} WHERE user_id = "{user[4]}"')
        conn.commit()

        referral_log(user2[0], profit, user2[1])


def referral_log(user_id, profit, name):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM ref_log WHERE user_id = "{user_id}"')
    user = cursor.fetchall()

    if len(user) == 0:
        cursor.execute(f'INSERT INTO ref_log VALUES ("{user_id}", "{profit}", "{name}")')
        conn.commit()
    else:
        all_profit = user[0][1]

        all_profit = float(all_profit) + float(profit)

        cursor.execute(f'UPDATE ref_log SET all_profit = {all_profit} WHERE user_id = "{user_id}"')
        conn.commit()


def check_all_profit_user(user_id):
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM ref_log WHERE user_id = "{user_id}"')
    user = cursor.fetchall()

    if len(user) == 0:
        return 0
    else:
        return user[0][1]


def admin_top_referral():
    conn = sqlite3.connect("bd.sqlite")
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM ref_log')
    users = cursor.fetchall()

    msg = '<b>?????? ?????? ?????????????????? ???? ?????? ??????????:</b>\n' \

    for i in users:
        msg = msg + f'{i[0]}/{i[2]} - {i[1]} ???\n'

    return msg
