import subprocess

from denite import util

from .base import Base


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = "fasd"
        self.kind = "file"

    def gather_candidates(self, context):
        if len(context["args"]) < 1:
            arg = util.input(self.vim, context, "FASD string: ")
        else:
            arg = context["args"][0]

        sub = subprocess.Popen(["fasd", "-f", "-l", "-R", arg], stdout=subprocess.PIPE)
        return [{"word": x, "action__path": x} for x in sub.communicate()[0].decode("utf-8").split()]
