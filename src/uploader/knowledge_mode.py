"""
=========================================
Knowledge Base Modes
=========================================
"""

from enum import Enum


class KnowledgeMode(Enum):

    REPLACE = "replace"

    ADD = "add"

    SKIP_DUPLICATES = "skip_duplicates"

    UPDATE_EXISTING = "update_existing"