from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
#buildOptions = dict(packages = ["pygame"], excludes = [],include_files = ["game_bar1.png","game_check1.png","game_note1.png","ipaexg.ttf"])



base = None

executables = [
    Executable('title.py', base=base, targetName = 'MEIRO_OOOOH')
]

setup(name='PEANO_TAERU',
      version = '1.0',
      description = '',
      options = {"build_exe": {"include_files": ["img"]}},
      #options = dict(build_exe = buildOptions),
      executables = executables)
