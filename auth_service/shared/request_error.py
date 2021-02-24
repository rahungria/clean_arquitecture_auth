class RequestError(Exception):
    def __init__(self, msg: str, status_code: int) -> None:
        self.msg = msg
        self.status_code = status_code
        super().__init__(msg)

    def __str__(self):
        return f"[{self.status_code}]: {self.msg}"