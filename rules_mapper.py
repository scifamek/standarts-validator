from rules.pattern_not_allowed.index import PatternNotAllowedRule
from rules.allowed_structure_by_folder.index import AllowedStructureByFolder


MAPPER = {
    PatternNotAllowedRule.identifier: PatternNotAllowedRule,
    AllowedStructureByFolder.identifier: AllowedStructureByFolder
}