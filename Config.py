"""
    Author: Christian Hahm
    Created: October 9, 2020
    Purpose: Specific configuration settings for NARS
"""
"""
    System Parameters
"""
k = 1 # evidential horizon
t = 0.25 # decision rule (goal decision-making) threshold
MINDFULNESS = 1.0 # between 0-1, how much attention the system allocates to the present moment (overall experience buffer) [1.0] vs. pondering concepts [0.0]

"""
    Bags
"""
BAG_CAPACITY = 60 # how many items can fit in a bag
BAG_NUMBER_OF_BUCKETS = 100 # how many probability buckets are there? e.g. 100 allows 100 probability values in [0%, 100%)
BAG_PRIORITY_DECAY_MULTIPLIER = 0.9 # value in [0,1] multiplied w/ priority during priority decay

"""
    Tables
"""
TABLE_CAPACITY = 30

"""
    Others
"""
TRUTH_EPSILON = 0.01 # minimum size that truth-value can be incremented/
MAX_EVIDENTIAL_BASE_LENGTH = 20000 # maximum IDs to store documenting evidential base

"""
    Default Input Task Values
"""
DEFAULT_CONCEPT_EXPECTATION = 0.6
DEFAULT_CONCEPT_EXPECTATION_GOAL = 0.6

DEFAULT_JUDGMENT_FREQUENCY = 1.0
DEFAULT_JUDGMENT_CONFIDENCE = 0.9
DEFAULT_JUDGMENT_PRIORITY = 0.8
DEFAULT_JUDGMENT_DURABILITY = 0.5

DEFAULT_QUESTION_PRIORITY = 0.9
DEFAULT_QUESTION_DURABILITY = 0.9

DEFAULT_GOAL_CONFIDENCE = 0.9
DEFAULT_GOAL_PRIORITY = 0.9
DEFAULT_GOAL_DURABILITY = 0.9

DEFAULT_QUEST_PRIORITY = 0.9
DEFAULT_QUEST_DURABILITY = 0.9