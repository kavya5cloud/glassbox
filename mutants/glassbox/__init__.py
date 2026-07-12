__version__ = "0.2.0"

from .demo import DemoEngine, ScriptedTraceSource

__all__ = ["DemoEngine", "ScriptedTraceSource", "__version__"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
