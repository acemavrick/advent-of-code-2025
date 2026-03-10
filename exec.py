import os
import sys
import time
from pathlib import Path

# ANSI color codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
SWIFT_COLOR = "\033[38;5;208m"   # orange for Swift
JAVA_COLOR = "\033[38;5;160m"    # red for Java
PYTHON_COLOR = "\033[38;5;33m"   # blue for Python

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: swiftx.py {day} {part} [-s] [-sw|-j|-p]")
        sys.exit(1)

    day = int(sys.argv[1])
    part = int(sys.argv[2])
    sample = "-s" in sys.argv

    # determine language
    if "-j" in sys.argv:
        lang = "java"
    elif "-p" in sys.argv:
        lang = "python"
    else:
        lang = "swift"

    # check if input exists
    inputfile = Path(f"input/d{day}{'s' if sample else ''}.in")
    if not inputfile.exists():
        raise FileNotFoundError(f"Input file missing: {inputfile}")

    Path(".build").mkdir(exist_ok=True)

    if lang == "swift":
        src_base = f"day-{day:02}/Shubh_{day:02}_{part}"
        src = f"{src_base}{SWIFT_COLOR}.swift{CYAN}"
        out = f".build/swift_d{day:02}p{part}"
        print(f"{CYAN}building {src}... {RESET}")
        build_start = time.perf_counter()
        code = os.system(f"swiftc -O {src_base}.swift -o {out}")
        build_end = time.perf_counter()

        if code != 0:
            raise RuntimeError("building failed")

        build_elapsed = build_end - build_start
        print(f"{GREEN}build time: {build_elapsed:.4f}s{RESET}")

        print(f"{CYAN}running....{RESET}")
        print(f"{YELLOW}{'='*15}{RESET}")
        print(RESET, end="", flush=True)
        run_start = time.perf_counter()
        os.system(f"{out} < {inputfile.absolute()}")
        run_end = time.perf_counter()
        print(RESET, end="", flush=True)

    elif lang == "java":
        src_base = f"day-{day:02}/Shubh_{day:02}_{part}"
        src = f"{src_base}{JAVA_COLOR}.java{CYAN}"
        classname = f"Shubh_{day:02}_{part}"
        outdir = ".build"
        print(f"{CYAN}building {src}... {RESET}")
        build_start = time.perf_counter()
        code = os.system(f"javac -O -d {outdir} {src_base}.java")
        build_end = time.perf_counter()

        if code != 0:
            raise RuntimeError("building failed")

        build_elapsed = build_end - build_start
        print(f"{GREEN}build time: {build_elapsed:.4f}s{RESET}")

        print(f"{CYAN}running....{RESET}")
        print(f"{YELLOW}{'='*15}{RESET}")
        print(RESET, end="", flush=True)
        run_start = time.perf_counter()
        os.system(f"java -cp {outdir} {classname} < {inputfile.absolute()}")
        run_end = time.perf_counter()
        print(RESET, end="", flush=True)

    elif lang == "python":
        src_base = f"day-{day:02}/Shubh_{day:02}_{part}"
        src = f"{src_base}{PYTHON_COLOR}.py{CYAN}"
        print(f"{CYAN}running {src}....{RESET}")
        print(f"{YELLOW}{'='*15}{RESET}")
        print(RESET, end="", flush=True)
        run_start = time.perf_counter()
        os.system(f"python3 {src_base}.py < {inputfile.absolute()}")
        run_end = time.perf_counter()
        print(RESET, end="", flush=True)

    run_elapsed = run_end - run_start
    print(f"{YELLOW}{'='*15}{RESET}")
    print(f"{GREEN}run time:   {run_elapsed:.4f}s{RESET}")