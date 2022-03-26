class ResponseModel:
    def __init__(self, status, coverage, universe, errors, files) -> None:
        self.status = status
        self.coverage = coverage
        self.universe = universe
        self.errors = errors
        self.files = files
    
    def toJson(self):
        return {
            'status': self.status,
            'coverage': self.coverage,
            'universe': self.universe,
            'errors': self.errors,
            'files': self.files
        }