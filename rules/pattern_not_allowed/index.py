from typing import Any
from models.response_model import ResponseModel
from helpers.file_helpers import get_file_paths, search_pattern_in_file
class PatternNotAllowedRule:
    identifier = 'pattern_not_allowed'
    def __init__(self, base_url: str, coverage: float, data: Any) -> None:
        self.base_url = base_url
        self.coverage = coverage
        self.data = data
    

    def __call__(self) -> ResponseModel:
        universe = 0
        errors = 0
        response = []
        for search in self.data['searches']:
            files = get_file_paths(search['files-to-search-in'], self.base_url)
            universe += len(files)
            patterns = search['searched-patterns']

            for file in files:
                for pattern in patterns:
                    res = search_pattern_in_file(pattern, file)
                    if(len(res) > 0):
                        errors += 1
                        response.append(
                            {
                                'file': file,
                                'errors': res
                            }
                        )
        status = True
        coverage = 1
        if(universe > 0):
            coverage = (1- (errors/universe))
            status = coverage >= self.coverage
        return ResponseModel(
            status,
            coverage,
            universe,
            errors,
            response
        )
