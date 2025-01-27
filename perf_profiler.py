import cProfile
import io
import pstats
import time
from functools import wraps


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        profiler.dump_stats("profile_output.prof")
        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream).sort_stats(
            pstats.SortKey.CUMULATIVE
        )
        stats.print_stats()
        print(stream.getvalue())

        return result

    return wrapper


def async_profile(output_path=""):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            profiler = cProfile.Profile()
            profiler.enable()
            result = await func(*args, **kwargs)
            profiler.disable()
            _output_path = func.__name__ if not output_path else output_path
            profiler.dump_stats(f"{_output_path}.prof")
            stream = io.StringIO()
            stats = pstats.Stats(profiler, stream=stream).sort_stats(
                pstats.SortKey.CUMULATIVE
            )
            stats.print_stats()
            with open(f"{_output_path}.txt", "w") as f:
                f.write(stream.getvalue())

            return result

        return wrapper

    return decorator
