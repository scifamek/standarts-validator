from typing import Any
import numpy as np
from models.response_model import ResponseModel

from helpers.file_helpers import get_file_paths, search_pattern_in_file


class AllowedStructureByFolder:
    identifier = 'allowed_structure_by_folder'
    def __init__(self, base_url: str, coverage: float, data: Any) -> None:
        self.base_url = base_url
        self.coverage = coverage
        self.data = data


    def __call__(self) -> ResponseModel:
        universe = 0
        errors = 0
        response = []
     
        for search in self.data['folders']:
            folder_pattern = search['folder-pattern'] if 'folder-pattern' in search else None 
            valid_files_pattern = search['valid-files-pattern'] if 'valid-files-pattern' in search else None
            invalid_files_pattern = search['invalid-files-pattern'] if 'invalid-files-pattern' in search else None

            all_files = set(get_file_paths([f'{folder_pattern}/**/*.*'],self.base_url))
            universe += len(all_files)
            valid_files = set([])
            invalid_files = set([])
            if(valid_files_pattern):
                valid_files = set(get_file_paths(map(lambda x : f'{folder_pattern}/{x}',valid_files_pattern), self.base_url))
                diff = all_files.difference(valid_files)
                if(len(diff) > 0):
                    errors += len(diff)
                    response.append(
                        {
                            'folder': folder_pattern,
                            'valid-pattern': valid_files_pattern,
                            'errors': list(diff)
                        }
                    )

            elif(invalid_files_pattern):
                invalid_files = set(get_file_paths(map(lambda x : f'{folder_pattern}/{x}',invalid_files_pattern), self.base_url))
                if(len(invalid_files) > 0):
                    errors += len(invalid_files)

                    response.append(
                        {
                            'folder': folder_pattern,
                            'invalid-pattern': invalid_files_pattern,
                            'errors': list(invalid_files)
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