AREA = 4000  # Change USER_THRESHOLD and STEP_SIZE when changing the area
STEP_SIZE = 250
USERS_THRESHOLD = 2
NUM_GENERATIONS = 5
NUM_CHROMOSOMES = 50
NUM_USERS = 1000

THERMAL_NOISE = -112.240257  # (In dbm)
SINR_THRESHOLD = -9
OUTAGE_PROBABILITY = 0.15

COST_WEIGHT = 0.4
MAX_COST = 3000
COVERAGE_WEIGHT = 0.3
MAX_COVERAGE = 90
INTERFERENCE_WEIGHT = 0.3
MAX_INTERFERENCE = 1

NUM_FIXED_MACRO = 15
NUM_MACRO = 15
NUM_MICRO = 30
NUM_PICO = 20
NUM_FEMTO = 20

FIXED_MACRO_RADIUS = 1000
MACRO_RADIUS = 1000
MICRO_RADIUS = 250
PICO_RADIUS = 100
FEMTO_RADIUS = 50

FIXED_MACRO_COST = 0
MACRO_COST = 175
MICRO_COST = 25
PICO_COST = 5
FEMTO_COST = 1

FIXED_MACRO_FREQ = 3.5
MACRO_FREQ = 3.5
SMALL_CELL_FREQ = 28

FIXED_MACRO_MIN_USERS = 0
MACRO_MIN_USERS = 10
MICRO_MIN_USERS = 5
PICO_MIN_USERS = 2
FEMTO_MIN_USERS = 1


FIXED_MACRO_MAX_USERS = 30
MACRO_MAX_USERS = 30
MICRO_MAX_USERS = 20
PICO_MAX_USERS = 15
FEMTO_MAX_USERS = 10

FIXED_MACRO_POWER = 40
MACRO_POWER = 40
MICRO_POWER = 10
PICO_POWER = 10
FEMTO_POWER = 10

SELECTION_METHOD = "sus"
CROSSOVER_METHOD = "whole_arithmetic"
MUTATION_METHOD = "non_uniform"
MUTATION_TYPE = "gaussian"

CROSSOVER_PROBABILTY = 0.6
MUTATION_PROBABILTY = 0.4

ALPHA = 0.4
