class RollError(Exception):
    pass


class ExcesiveRollError(RollError):
    pass


class RollLimitError(RollError):
    pass

class GameNotFinished(RollError):
    pass