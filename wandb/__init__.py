import os
import json

from aim import Run


_global_run = None


def init(**kwargs):
  global _global_run
  _global_run = Run(repo=os.environ.get('AIM_REPO_DIR', '.'),
                experiment=kwargs['project'])
  _global_run.name = kwargs['name']
  _global_run["config"] = kwargs['config']
  _global_run["env"] =  json.dumps(dict(os.environ))
  return

def log(kwargs):
  global _global_run
  i = kwargs.get('step', None)
  for k, v in kwargs.items():
    _global_run.track(v, name=k, epoch=i)
