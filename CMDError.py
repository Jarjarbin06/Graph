## graph ##
## by JARJARBIN'S STUDIO ##
## v1.2 ##

class CMDError(Exception):
    """
        Error class for CMD errors
    """

    def __init__(self: object, cmd: list[str] | None = None, err_pos: int | None = None, msg: str | None = None) -> None:

        """
            create an error object (child = Exception class)

            Parameter :
                - self (object) : CMDError object
                - cmd (list[str] | None) = None : list of every word in command
                - err_pos (int | None) = None : position/index of the error in cmd
                - msg (str | None) = None : message join to the error
        """

        self.cmd = cmd
        self.err_pos = err_pos
        self.msg = msg

    def __str__(self: object) -> str:

        """
            get a string version of CMDError

            Parameter :
                - self (object) : CMDError object

            Return :
                str : CMDError
        """

        s = '\n============================================================\n'
        s += '= \033[31m-------------------- ERROR DETECTED --------------------\033[0m =\n'
        s += '============================================================\n'
        if self.cmd:
            s += '\033[31mCMD ERROR in :\n    " '
            if self.err_pos:
                for n in range(len(self.cmd)):
                    if n == self.err_pos:
                        s += '\033[0m\033[41m' + self.cmd[n] + '\033[0m\033[31m '
                    else:
                        s += self.cmd[n] + ' '
            else:
                s += '\033[0m\033[41m'
                for x in self.cmd:
                    s += x + ' '
                s = s[:-1]
                s += '\033[0m\033[31m '
            s += '"'
        s += '\033[0m\n\n\033[7m'
        if self.msg:
            s += self.msg
        else:
            s += 'Error in command'
        s += '\033[0m\n\n(try "help" to get information about commands)\n'
        s += '============================================================\n'
        return s